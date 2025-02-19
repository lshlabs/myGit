from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import Qt
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))
from dialog.image_dialog import ImageDialog
from dialog.action_delay_dialog import ActionDelayDialog
from dialog.action_setting_dialog import ActionSettingDialog
from utils.data_manager import DataManager
import subprocess  # macOS용 프로세스 리스트 가져오기

class ActionDialog(QtWidgets.QDialog):
    def __init__(self, parent=None, macro_key=""):
        super().__init__(parent)
        uic.loadUi('deeporder/ui/ActionWindow.ui', self)
        self.setFixedSize(500, 570)
        self.macro_key = macro_key
        
        # data에서 매크로 정보 가져오기
        data_manager = DataManager.get_instance()
        self.macro_data = data_manager._data['macro_list'][self.macro_key]
        
        # 메모리에 원본 데이터 백업
        self.original_actions = {key: value.copy() for key, value in self.macro_data['actions'].items()}
        self.original_program = self.macro_data.get('program')
        
        self.title_text = self.macro_data['name']
        
        self.init_ui()
        self.connect_signals()
        self.load_actions()  # 액션 데이터 로드
        
    def init_ui(self):
        """UI 요소 초기화"""
        # 테이블 위젯 설정
        self.table_widget = self.findChild(QtWidgets.QTableWidget, 'tableWidget')
        self.table_widget.setColumnCount(2)
        self.table_widget.setHorizontalHeaderLabels(['번호', '이름'])
        self.table_widget.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.table_widget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_widget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)  # 편집 비활성화
        
        # 번호 열 너비 설정
        header = self.table_widget.horizontalHeader()
        header.resizeSection(0, header.sectionSize(0) // 2)
        
        # 스크롤 화살표 버튼 초기 숨김
        self.button_arrowup.hide()
        self.button_arrowdown.hide()
        
        # 스크롤바 이벤트 연결
        scrollbar = self.table_widget.verticalScrollBar()
        scrollbar.valueChanged.connect(self.update_arrow_buttons)
        scrollbar.rangeChanged.connect(self.update_arrow_buttons)
        
        # 콤보박스
        self.combo_window = self.findChild(QtWidgets.QComboBox, 'comboBox_window')
        self.update_window_list()  # 프로그램 목록 업데이트
        
        # 현재 저장된 프로그램이 있다면 선택
        current_program = self.macro_data.get('program')
        if current_program:
            index = self.combo_window.findText(current_program)
            if index >= 0:
                self.combo_window.setCurrentIndex(index)
        
        # 버튼들
        self.button_add = self.findChild(QtWidgets.QPushButton, 'button_add')
        self.button_delay = self.findChild(QtWidgets.QPushButton, 'button_delay')
        self.button_priority = self.findChild(QtWidgets.QPushButton, 'button_priority')
        self.button_edit = self.findChild(QtWidgets.QPushButton, 'button_edit')
        self.button_delete = self.findChild(QtWidgets.QPushButton, 'button_delete')
        self.button_setting = self.findChild(QtWidgets.QPushButton, 'button_setting')
        self.button_save = self.findChild(QtWidgets.QPushButton, 'button_save')
        self.button_cancel = self.findChild(QtWidgets.QPushButton, 'button_cancel')
        self.button_up = self.findChild(QtWidgets.QPushButton, 'button_up')
        self.button_down = self.findChild(QtWidgets.QPushButton, 'button_down')
        self.button_arrowup = self.findChild(QtWidgets.QPushButton, 'button_arrowup')
        self.button_arrowdown = self.findChild(QtWidgets.QPushButton, 'button_arrowdown')
        
        # 라벨들
        self.label_title = self.findChild(QtWidgets.QLabel, 'label_title')
        self.label_title.setText(self.title_text)  # 텍스트 설정
        
    def connect_signals(self):
        """시그널 연결"""
        self.button_add.clicked.connect(self.btn_add)
        self.button_delay.clicked.connect(self.btn_delay)
        self.button_priority.clicked.connect(self.btn_priority)
        self.button_edit.clicked.connect(self.btn_edit)
        self.button_delete.clicked.connect(self.btn_delete)
        self.button_setting.clicked.connect(self.btn_setting)
        self.button_save.clicked.connect(self.btn_save)
        self.button_cancel.clicked.connect(self.btn_cancel)
        self.button_up.clicked.connect(self.btn_move_up)
        self.button_down.clicked.connect(self.btn_move_down)
        self.button_arrowup.clicked.connect(self.btn_arrow_up)
        self.button_arrowdown.clicked.connect(self.btn_arrow_down)
        self.combo_window.currentTextChanged.connect(self.on_combo_changed)
        
    def on_combo_changed(self, text):
        """콤보박스 선택 변경 시 실행"""
        if text == "선택 안 함":
            self.macro_data['program'] = None
        else:
            self.macro_data['program'] = text
        
    def btn_add(self):
        """추가 버튼 클릭 시 실행"""
        dialog = ImageDialog(self, macro_key=self.macro_key)
        dialog.show()
        
    def btn_delay(self):
        """딜레이 버튼 클릭 시 실행"""
        dialog = ActionDelayDialog(self)
        if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
            delay_time = dialog.lineEdit_delay.text()
            
            # 딜레이 액션 생성
            DataManager.get_instance().create_delay_action(self.macro_key, delay_time)
            
            # 테이블 데이터 갱신
            self.load_actions()
        
    def btn_priority(self):
        """우선순위 버튼 클릭 시 실행"""
        current_row = self.table_widget.currentRow()
        if current_row >= 0:  # 선택된 행이 있는 경우
            # number를 기준으로 정렬된 액션 리스트 가져오기
            sorted_actions = sorted(
                self.macro_data['actions'].items(),
                key=lambda x: x[1]['number']
            )
            
            # 현재 선택된 행의 action_key와 데이터 가져오기
            action_key = sorted_actions[current_row][0]
            action_data = self.macro_data['actions'][action_key]
            
            # priority 상태 토글
            action_data['priority'] = not action_data['priority']
            
            # 테이블 아이템 텍스트 업데이트
            name_item = self.table_widget.item(current_row, 1)
            if action_data['priority']:
                if not name_item.text().endswith(' (우선순위 지정됨)'):
                    name_item.setText(name_item.text() + ' (우선순위 지정됨)')
            else:
                if name_item.text().endswith(' (우선순위 지정됨)'):
                    name_item.setText(name_item.text().replace(' (우선순위 지정됨)', ''))
            
            # 데이터 저장
            DataManager.get_instance().save_data()
        
    def btn_edit(self):
        """수정 버튼 클릭 시 실행"""
        current_row = self.table_widget.currentRow()
        if current_row >= 0:  # 선택된 행이 있는 경우
            # number를 기준으로 정렬된 액션 리스트 가져오기
            sorted_actions = sorted(
                self.macro_data['actions'].items(),
                key=lambda x: x[1]['number']
            )
            
            # 현재 선택된 행의 action_key와 action_data 가져오기
            action_key = sorted_actions[current_row][0]
            action_data = self.macro_data['actions'][action_key]
            
            # action type에 따라 다른 다이얼로그 열기
            if action_data['type'] == 'delay':
                dialog = ActionDelayDialog(self)
                # 기존 딜레이 값 설정
                dialog.lineEdit_delay.setText(str(action_data['value']))
                if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
                    # 딜레이 값 업데이트
                    delay_time = float(dialog.lineEdit_delay.text())
                    action_data['value'] = delay_time
                    action_data['name'] = f"딜레이: {delay_time}초"
                    # 테이블 데이터 갱신
                    self.load_actions()
            else:  # type == 'image'
                dialog = ImageDialog(self, macro_key=self.macro_key, action_key=action_key)
                if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
                    self.load_actions()
        
    def btn_delete(self):
        """삭제 버튼 클릭 시 실행"""
        current_row = self.table_widget.currentRow()
        if current_row >= 0:  # 선택된 행이 있는 경우
            # 삭제 확인 메시지
            reply = QtWidgets.QMessageBox.question(
                self,
                '삭제 확인',
                '정말 삭제하시겠습니까?',
                QtWidgets.QMessageBox.StandardButton.Yes | 
                QtWidgets.QMessageBox.StandardButton.No
            )
            
            if reply == QtWidgets.QMessageBox.StandardButton.Yes:
                # number를 기준으로 정렬된 액션 리스트 가져오기
                sorted_actions = sorted(
                    self.macro_data['actions'].items(),
                    key=lambda x: x[1]['number']
                )
                
                # 현재 선택된 행의 action_key 가져오기
                action_key = sorted_actions[current_row][0]
                
                # 데이터에서 액션 삭제
                del self.macro_data['actions'][action_key]
                
                # 남은 액션들의 number 재정렬
                for i, (key, action) in enumerate(sorted(
                    self.macro_data['actions'].items(),
                    key=lambda x: x[1]['number']
                )):
                    action['number'] = i + 1
                
                # 데이터 저장
                DataManager.get_instance().save_data()
                
                # 테이블 데이터 갱신
                self.load_actions()
        
    def btn_setting(self):
        dialog = ActionSettingDialog(self)
        dialog.show()
        
    def btn_save(self):
        """저장 버튼 클릭 시 실행"""
        # 선택된 프로그램 저장
        selected_program = self.combo_window.currentText()
        if selected_program == "선택 안 함":
            self.macro_data['program'] = None
        else:
            self.macro_data['program'] = selected_program
        
        # 메모리의 데이터 업데이트
        DataManager.get_instance()._data['macro_list'][self.macro_key] = self.macro_data
        # 파일에 저장
        DataManager.get_instance().save_data()
        
        self.accept()  # 다이얼로그 수락

    def btn_cancel(self):
        """취소 버튼 클릭 시 실행"""
        # 변경사항 확인
        current_program = self.macro_data.get('program')
        if current_program == "선택 안 함":
            current_program = None
        
        has_changes = (
            self.original_actions != self.macro_data['actions'] or
            self.original_program != current_program  # 프로그램 변경 확인
        )
        
        if has_changes:
            reply = QtWidgets.QMessageBox.question(
                self,
                '저장되지 않은 변경사항',
                '수정사항이 있습니다.\n저장하지 않고 종료하시겠습니까?',
                QtWidgets.QMessageBox.StandardButton.Yes | 
                QtWidgets.QMessageBox.StandardButton.No
            )
            
            if reply == QtWidgets.QMessageBox.StandardButton.No:
                return
        
        # 메모리에서 원본 데이터로 복원
        self.macro_data['actions'] = {key: value.copy() for key, value in self.original_actions.items()}
        self.macro_data['program'] = self.original_program
        DataManager.get_instance().save_data()
        self.reject()
        
    def btn_move_up(self):
        """위로 이동 버튼 클릭 시 실행"""
        current_row = self.table_widget.currentRow()
        if current_row > 0:  # 첫 행이 아닌 경우에만 실행
            # number를 기준으로 정렬된 액션 리스트 가져오기
            sorted_actions = sorted(
                self.macro_data['actions'].items(),
                key=lambda x: x[1]['number']
            )
            
            # 현재 선택된 행과 위 행의 action_key 가져오기
            current_key = sorted_actions[current_row][0]
            upper_key = sorted_actions[current_row - 1][0]
            
            # number 교체
            current_number = self.macro_data['actions'][current_key]['number']
            upper_number = self.macro_data['actions'][upper_key]['number']
            self.macro_data['actions'][current_key]['number'] = upper_number
            self.macro_data['actions'][upper_key]['number'] = current_number
            
            # 데이터 저장
            DataManager.get_instance().save_data()
            
            # 테이블 데이터 갱신
            self.load_actions()
            
            # 선택 행 이동
            self.table_widget.setCurrentCell(current_row - 1, 1)

    def btn_move_down(self):
        """아래로 이동 버튼 클릭 시 실행"""
        current_row = self.table_widget.currentRow()
        if current_row < self.table_widget.rowCount() - 1:  # 마지막 행이 아닌 경우에만 실행
            # number를 기준으로 정렬된 액션 리스트 가져오기
            sorted_actions = sorted(
                self.macro_data['actions'].items(),
                key=lambda x: x[1]['number']
            )
            
            # 현재 선택된 행과 아래 행의 action_key 가져오기
            current_key = sorted_actions[current_row][0]
            lower_key = sorted_actions[current_row + 1][0]
            
            # number 교체
            current_number = self.macro_data['actions'][current_key]['number']
            lower_number = self.macro_data['actions'][lower_key]['number']
            self.macro_data['actions'][current_key]['number'] = lower_number
            self.macro_data['actions'][lower_key]['number'] = current_number
            
            # 데이터 저장
            DataManager.get_instance().save_data()
            
            # 테이블 데이터 갱신
            self.load_actions()
            
            # 선택 행 이동
            self.table_widget.setCurrentCell(current_row + 1, 1)

    def btn_arrow_up(self):
        pass
        
    def btn_arrow_down(self):
        pass

    def load_actions(self):
        """액션 데이터를 테이블에 로드"""
        actions = self.macro_data['actions']
        
        # number를 기준으로 정렬된 액션 리스트 생성
        sorted_actions = sorted(
            actions.items(),
            key=lambda x: x[1]['number']
        )
        
        # 테이블 행 수 설정
        self.table_widget.setRowCount(len(sorted_actions))
        
        # 테이블에 데이터 채우기
        for row, (action_key, action_data) in enumerate(sorted_actions):
            # 번호 열
            number_item = QtWidgets.QTableWidgetItem(str(action_data['number']))
            number_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.table_widget.setItem(row, 0, number_item)
            
            # 이름 열
            name = action_data['name']
            if action_data['priority']:  # priority가 true인 경우
                name += ' (우선순위 지정됨)'
            name_item = QtWidgets.QTableWidgetItem(name)
            name_item.setTextAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
            self.table_widget.setItem(row, 1, name_item)
        
        # 첫 번째 행이 있다면 선택
        if self.table_widget.rowCount() > 0:
            self.table_widget.setCurrentCell(0, 1)  # 첫 번째 행의 이름 열 선택

    def update_arrow_buttons(self):
        """스크롤바 상태에 따라 화살표 버튼 표시/숨김"""
        scrollbar = self.table_widget.verticalScrollBar()
        
        # 스크롤이 필요한지 확인
        if scrollbar.maximum() == 0:
            # 스크롤이 필요없는 경우
            self.button_arrowup.hide()
            self.button_arrowdown.hide()
            return
        
        # 현재 스크롤 위치
        current_pos = scrollbar.value()
        max_pos = scrollbar.maximum()
        
        # 최상단인 경우 (위로 스크롤할 내용이 없음)
        if current_pos == 0:
            self.button_arrowup.hide()
            self.button_arrowdown.show()
        # 최하단인 경우 (아래로 스크롤할 내용이 없음)
        elif current_pos == max_pos:
            self.button_arrowup.show()
            self.button_arrowdown.hide()
        # 중간인 경우 (위아래로 스크롤할 내용이 있음)
        else:
            self.button_arrowup.show()
            self.button_arrowdown.show()

    def update_window_list(self):
        """실행 중인 프로그램 목록 업데이트"""
        try:
            from AppKit import NSWorkspace
            
            # 시스템 프로세스 제외 목록
            exclude_list = {
                'Finder', 'Dock', 'Spotlight', 'NotificationCenter', 'ControlCenter',
                'SystemUIServer', 'loginwindow', 'WindowServer'
            }
            
            # 실행 중인 앱 목록 가져오기
            workspace = NSWorkspace.sharedWorkspace()
            running_apps = workspace.runningApplications()
            
            filtered_programs = set()
            for app in running_apps:
                # GUI 앱만 필터링 (activationPolicy == 0)
                if app.activationPolicy() == 0:  # NSApplicationActivationPolicyRegular
                    name = app.localizedName()
                    if (
                        name and
                        not name.startswith('.') and
                        name not in exclude_list
                    ):
                        filtered_programs.add(name)
            
            # 정렬
            filtered_programs = sorted(filtered_programs)
            
            # 콤보박스 아이템 설정
            self.combo_window.clear()
            self.combo_window.addItem("선택 안 함")
            self.combo_window.addItems(filtered_programs)
            
            # 현재 저장된 프로그램이 있다면 선택
            current_program = self.macro_data.get('program')
            if current_program:
                index = self.combo_window.findText(current_program)
                if index >= 0:
                    self.combo_window.setCurrentIndex(index)
                    
        except Exception as e:
            print(f"프로그램 목록 가져오기 실패: {e}")
            self.combo_window.clear()
            self.combo_window.addItem("선택 안 함")