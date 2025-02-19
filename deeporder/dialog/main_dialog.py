from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import Qt
from pathlib import Path
import sys
import shutil
sys.path.append(str(Path(__file__).parents[1]))
from dialog.action_wizard_dialog import ActionWizardDialog
from dialog.action_dialog import ActionDialog
from dialog.main_setting_dialog import MainSettingDialog
from utils.data_manager import DataManager

class MainDialog(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('deeporder/ui/MainWindow.ui', self)
        self.setFixedSize(500, 570)
        self.init_ui()
        self.connect_signals()
        self.load_macro_list()  # 데이터 로딩 추가

    def init_ui(self):
        """UI 요소 초기화"""
        # 라벨들
        self.label_title = self.findChild(QtWidgets.QLabel, 'label_title')
        self.label_run = self.findChild(QtWidgets.QLabel, 'label_run')
        self.label_stop = self.findChild(QtWidgets.QLabel, 'label_stop')
        
        # 리스트 위젯과 라인 에딧
        self.listWidget = self.findChild(QtWidgets.QListWidget, 'listWidget')
        self.lineEdit = self.findChild(QtWidgets.QLineEdit, 'lineEdit')
        
        # 버튼들
        self.button_add = self.findChild(QtWidgets.QPushButton, 'button_add')
        self.button_delete = self.findChild(QtWidgets.QPushButton, 'button_delete')
        self.button_edit = self.findChild(QtWidgets.QPushButton, 'button_edit')
        self.button_copy = self.findChild(QtWidgets.QPushButton, 'button_copy')
        self.button_setting = self.findChild(QtWidgets.QPushButton, 'button_setting')

    def connect_signals(self):
        """시그널 연결"""
        self.button_add.clicked.connect(self.btn_add)
        self.button_delete.clicked.connect(self.btn_delete)
        self.button_edit.clicked.connect(self.btn_edit)
        self.button_copy.clicked.connect(self.btn_copy)
        self.button_setting.clicked.connect(self.btn_setting)
        self.label_run.mousePressEvent = self.label_run_clicked
        self.label_stop.mousePressEvent = self.label_stop_clicked
        self.listWidget.itemClicked.connect(self.listWidget_item_clicked)

    def btn_add(self):
        """추가 버튼 클릭 시 실행"""
        if not self.validate_lineEdit():
            return
        
        dialog = ActionWizardDialog(self, title_text=self.lineEdit.text().strip())
        if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:  # save 버튼으로 닫힌 경우
            self.manage_listWidget('add')

    def btn_delete(self):
        """삭제 버튼 클릭 시 실행"""
        current_item = self.listWidget.currentItem()
        if current_item:
            # 데이터에서 해당 매크로 찾기
            data_manager = DataManager.get_instance()
            macro_list = data_manager._data['macro_list']
            
            # 매크로 이름으로 매크로 키 찾기
            macro_key = None
            for key, macro in macro_list.items():
                if macro['name'] == current_item.text():
                    macro_key = key
                    break
            
            if macro_key:
                # 이미지 폴더 삭제
                macro_folder = data_manager.img_path / current_item.text()
                if macro_folder.exists():
                    shutil.rmtree(macro_folder)
                
                # 데이터에서 매크로 삭제
                del macro_list[macro_key]
                data_manager.save_data()
            
            # listWidget에서 아이템 삭제
            self.listWidget.takeItem(self.listWidget.currentRow())

    def btn_edit(self):
        """편집 버튼 클릭 시 실행"""
        self.manage_listWidget('edit')

    def btn_copy(self):
        """복제 버튼 클릭 시 실행"""
        self.manage_listWidget('copy')

    def btn_setting(self):
        dialog = MainSettingDialog(self)
        dialog.show()
        
    def label_run_clicked(self, event):
        """실행 라벨 클릭 시 실행"""
        # 리스트가 비어있는 경우
        if self.listWidget.count() == 0:
            QtWidgets.QMessageBox.warning(
                self,
                "실행 오류",
                "실행 할 동작이 없습니다."
            )
            return
        
        current_item = self.listWidget.currentItem()
        if current_item:
            # 현재 선택된 아이템의 텍스트가 ' (실행 중)'으로 끝나지 않는 경우에만 추가
            if not current_item.text().endswith(' (실행 중)'):
                current_item.setText(f"{current_item.text()} (실행 중)")
            
            # 라벨들의 스타일시트 변경 (run 상태)
            run_style = self.label_run.styleSheet().replace('darkgray', 'deepskyblue')
            stop_style = self.label_stop.styleSheet().replace('deepskyblue', 'darkgray')
            
            self.label_run.setStyleSheet(run_style)
            self.label_stop.setStyleSheet(stop_style)
            
            # label_title은 실행 중인 아이템이 하나라도 있으면 run 상태 유지
            title_style = self.label_title.styleSheet().replace('darkgray', 'deepskyblue')
            self.label_title.setStyleSheet(title_style)

    def label_stop_clicked(self, event):
        """중지 라벨 클릭 시 실행"""
        current_item = self.listWidget.currentItem()
        if current_item and current_item.text().endswith(' (실행 중)'):
            current_item.setText(current_item.text().replace(' (실행 중)', ''))
        
        # 라벨들의 스타일시트 변경 (stop 상태)
        run_style = self.label_run.styleSheet().replace('deepskyblue', 'darkgray')
        stop_style = self.label_stop.styleSheet().replace('darkgray', 'deepskyblue')
        
        self.label_run.setStyleSheet(run_style)
        self.label_stop.setStyleSheet(stop_style)
        
        # 실행 중인 아이템이 하나라도 있는지 확인
        has_running_item = False
        for i in range(self.listWidget.count()):
            if self.listWidget.item(i).text().endswith(' (실행 중)'):
                has_running_item = True
                break
        
        # 실행 중인 아이템 유무에 따라 label_title 상태 변경
        if has_running_item:
            title_style = self.label_title.styleSheet().replace('darkgray', 'deepskyblue')
        else:
            title_style = self.label_title.styleSheet().replace('deepskyblue', 'darkgray')
        self.label_title.setStyleSheet(title_style)

    def listWidget_item_clicked(self, item):
        """리스트 위젯 아이템 클릭 시 실행"""
        # 클릭된 아이템이 '실행 중' 상태인 경우 run 상태로, 아닌 경우 stop 상태로 변경
        if item.text().endswith(' (실행 중)'):
            # run 상태로 변경
            run_style = self.label_run.styleSheet().replace('darkgray', 'deepskyblue')
            stop_style = self.label_stop.styleSheet().replace('deepskyblue', 'darkgray')
        else:
            # stop 상태로 변경
            run_style = self.label_run.styleSheet().replace('deepskyblue', 'darkgray')
            stop_style = self.label_stop.styleSheet().replace('darkgray', 'deepskyblue')
        
        self.label_run.setStyleSheet(run_style)
        self.label_stop.setStyleSheet(stop_style)

    def manage_listWidget(self, action: str):
        """ListWidget 항목 관리
        
        Args:
            action (str): 수행할 동작 ('add', 'delete', 'copy', 'edit')
        """
        if action == 'add':
            text = self.lineEdit.text().strip()
            self.listWidget.addItem(text)
            self.lineEdit.clear()
            # 추가된 항목 선택
            self.listWidget.setCurrentRow(self.listWidget.count() - 1)
            
        elif action == 'delete':
            current_item = self.listWidget.currentItem()
            if current_item:
                # 실행 중인 아이템 삭제 시도 시 경고
                if current_item.text().endswith(' (실행 중)'):
                    QtWidgets.QMessageBox.warning(
                        self,
                        "삭제 오류",
                        "실행중인 동작은 삭제할 수 없습니다."
                    )
                    return
                
                reply = QtWidgets.QMessageBox.question(
                    self,
                    '삭제 확인',
                    '정말 삭제하시겠습니까?',
                    QtWidgets.QMessageBox.StandardButton.Yes | 
                    QtWidgets.QMessageBox.StandardButton.No
                )
                if reply == QtWidgets.QMessageBox.StandardButton.Yes:
                    self.listWidget.takeItem(self.listWidget.currentRow())
                
        elif action == 'copy':
            current_item = self.listWidget.currentItem()
            if current_item:
                # 실행 중인 아이템 복제 시도 시 경고
                if current_item.text().endswith(' (실행 중)'):
                    QtWidgets.QMessageBox.warning(
                        self,
                        "복제 오류",
                        "실행중인 동작은 복제할 수 없습니다."
                    )
                    return
                
                base_text = current_item.text()
                # 복제 번호 확인
                import re
                copy_num = 1
                while True:
                    new_text = f"{base_text} ({copy_num})"
                    # 같은 번호가 있는지 확인
                    exists = False
                    for i in range(self.listWidget.count()):
                        if self.listWidget.item(i).text() == new_text:
                            exists = True
                            break
                    if not exists:
                        break
                    copy_num += 1
                # 새 항목 추가
                self.listWidget.addItem(new_text)
                # 원본 항목 선택 유지
                self.listWidget.setCurrentItem(current_item)

        elif action == 'edit':
            current_item = self.listWidget.currentItem()
            if current_item:
                # 실행 중인 아이템 수정 시도 시 경고
                if current_item.text().endswith(' (실행 중)'):
                    QtWidgets.QMessageBox.warning(
                        self,
                        "수정 오류",
                        "실행중인 동작은 수정할 수 없습니다."
                    )
                    return
                
                # 매크로 이름으로 매크로 키 찾기
                data_manager = DataManager.get_instance()
                macro_list = data_manager._data['macro_list']
                macro_key = None
                for key, macro in macro_list.items():
                    if macro['name'] == current_item.text():
                        macro_key = key
                        break
                
                if macro_key:
                    dialog = ActionDialog(self, macro_key=macro_key)
                    dialog.show()

    def validate_lineEdit(self) -> bool:
        """LineEdit 텍스트 유효성 검사
        
        Returns:
            bool: 유효성 검사 통과 여부
        """
        text = self.lineEdit.text().strip()
        
        # 빈 텍스트 검사
        if not text:
            QtWidgets.QMessageBox.warning(
                self,
                "입력 오류",
                "이름을 입력해주세요."
            )
            return False
        
        # 특수문자 검사 (알파벳, 숫자, 한글, 공백만 허용)
        import re
        if not re.match(r'^[a-zA-Z0-9가-힣\s]+$', text):
            QtWidgets.QMessageBox.warning(
                self,
                "입력 오류",
                "특수문자는 사용할 수 없습니다."
            )
            return False
        
        # 중복 항목 검사
        for i in range(self.listWidget.count()):
            if self.listWidget.item(i).text() == text:
                QtWidgets.QMessageBox.warning(
                    self,
                    "중복 오류",
                    "이미 존재하는 이름입니다."
                )
                return False
        
        return True

    def load_macro_list(self):
        """데이터에서 매크로 리스트 로드"""
        data_manager = DataManager.get_instance()
        macro_list = data_manager._data['macro_list']
        
        # listWidget 초기화
        self.listWidget.clear()
        
        # 매크로 이름들을 listWidget에 추가
        for macro in macro_list.values():
            self.listWidget.addItem(macro['name'])

def main():
    app = QtWidgets.QApplication([])
    window = MainDialog()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
