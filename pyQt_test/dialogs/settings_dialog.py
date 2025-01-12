import json
import os
from PySide6.QtWidgets import QDialog
from ui.SettingsDialog_ui import Ui_SettingsDialog
#import resource_rc
from utils import get_data_file_path, load_json_data, save_json_data
from utils.virtual_key import get_key_list
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QCursor

class SettingsDialog(QDialog):
    def __init__(self, main_window, parent=None):
        super().__init__(parent)
        self.main_window = main_window
        self.ui = Ui_SettingsDialog()
        self.ui.setupUi(self)
        
        self.setFixedSize(self.width(), self.height())
        
        # ComboBox에 키 리스트 추가 (액티브 모드)
        key_list = get_key_list()
        self.ui.combo_run.addItems(key_list)
        self.ui.combo_stop.addItems(key_list)
        
        # ComboBox에 키 리스트 추가 (패시브 모드)
        self.ui.combo_ps1.addItems(key_list)
        self.ui.combo_ps2.addItems(key_list)
        self.ui.combo_ps3.addItems(key_list)
        self.ui.combo_ps4.addItems(key_list)
        self.ui.combo_ps5.addItems(key_list)
        self.ui.combo_ps6.addItems(key_list)
        
        # ComboBox 최대 표시 항목 수 설정
        for combo in [self.ui.combo_run, self.ui.combo_stop,
                     self.ui.combo_ps1, self.ui.combo_ps2, self.ui.combo_ps3,
                     self.ui.combo_ps4, self.ui.combo_ps5, self.ui.combo_ps6]:
            combo.setMaxVisibleItems(10)
        
        # 현재 메뉴에 따라 UI 요소 표시/숨김 설정
        self.adjust_passive_ui()
        
        self.data_file = get_data_file_path()
        self.load_settings()
        self.ui.buttonBox.accepted.connect(self.save_settings)
        self.ui.buttonBox.rejected.connect(self.reject)
        
        # 좌표 기록 관련 변수 초기화
        self.recording = False
        self.active_button = None
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_coordinates)
        
        # 이벤트 필터 설치
        self.installEventFilter(self)
        
        # 좌표 기록 버튼 연결
        self.connect_record_buttons()
    
    def connect_record_buttons(self):
        """좌표 기록 버튼 이벤트 연결"""
        # 버튼 클릭 이벤트 연결
        self.ui.button_record1.clicked.connect(self.record_coordinate)
        self.ui.button_record2.clicked.connect(self.record_coordinate)
        self.ui.button_record3.clicked.connect(self.record_coordinate)
        self.ui.button_record4.clicked.connect(self.record_coordinate)
        self.ui.button_record5.clicked.connect(self.record_coordinate)
        self.ui.button_record6.clicked.connect(self.record_coordinate)
    
    def record_coordinate(self):
        """좌표기록 버튼 클릭이벤트"""
        sender = self.sender()
        if not self.recording:
            self.recording = True
            # 어떤 버튼이 클릭되었는지 저장
            for i in range(1, 7):
                if sender == getattr(self.ui, f'button_record{i}'):
                    self.active_button = i
                    break
            sender.setText("기록 중...")
            self.timer.start(50)
    
    def update_coordinates(self):
        """좌표 업데이트"""
        if self.recording:
            cursor_pos = QCursor.pos()
            # 활성화된 버튼에 따라 다른 텍스트 에디트 업데이트
            if self.active_button:
                getattr(self.ui, f'textEdit_X{self.active_button}').setText(str(cursor_pos.x()))
                getattr(self.ui, f'textEdit_Y{self.active_button}').setText(str(cursor_pos.y()))
    
    def eventFilter(self, obj, event):
        """이벤트 필터"""
        if self.recording and event.type() == event.Type.KeyPress:
            if event.key() == Qt.Key.Key_F10:
                self.recording = False
                # 활성화된 버튼 텍스트 복원
                if self.active_button:
                    getattr(self.ui, f'button_record{self.active_button}').setText("기록 시작")
                self.timer.stop()
                return True
        return super().eventFilter(obj, event)
    
    def adjust_passive_ui(self):
        """현재 메뉴에 따라 패시브 모드 UI 요소 표시/숨김 설정"""
        current_menu = self.main_window.get_current_menu()
        
        # menu2, menu3일 때는 4-6번째 요소들 숨김
        hide_elements = current_menu in ['menu2', 'menu3']
        
        # 4-6번째 요소들의 위젯 리스트
        widgets_to_hide = [
            # 패시브 모드 설정
            (self.ui.label_img4, self.ui.combo_ps4, 
             self.ui.check_ctrl6, self.ui.check_alt6, self.ui.check_shift6),
            (self.ui.label_img5, self.ui.combo_ps5,
             self.ui.check_ctrl7, self.ui.check_alt7, self.ui.check_shift7),
            (self.ui.label_img6, self.ui.combo_ps6,
             self.ui.check_ctrl8, self.ui.check_alt8, self.ui.check_shift8),
            # 좌표 설정
            (self.ui.label_img4_2, self.ui.label_X4, self.ui.textEdit_X4 
             ,self.ui.label_Y4, self.ui.textEdit_Y4, self.ui.button_record4),
            (self.ui.label_img5_2, self.ui.label_X5, self.ui.textEdit_X5 
             ,self.ui.label_Y5, self.ui.textEdit_Y5, self.ui.button_record5),
            (self.ui.label_img6_2, self.ui.label_X6, self.ui.textEdit_X6 
             ,self.ui.label_Y6, self.ui.textEdit_Y6, self.ui.button_record6)
        ]
        
        # 위젯들의 표시/숨김 설정
        for widgets in widgets_to_hide:
            for widget in widgets:
                widget.setVisible(not hide_elements)
        
        if hide_elements:
            # menu2, menu3일 때
            self.setFixedHeight(440)  # 다이얼로그 전체 높이
            self.ui.tabWidget.setFixedHeight(380)   # 탭위젯 높이
            self.ui.groupBox_passive.setFixedHeight(180)  # 패시브 그룹박스 높이
            self.ui.groupBox_coordinate.setFixedHeight(260)  # 좌표 그룹박스 높이
            self.ui.buttonBox.setGeometry(self.ui.buttonBox.x(), 400,  # 버튼박스 y좌표 수정
                                        self.ui.buttonBox.width(),
                                        self.ui.buttonBox.height())
        else:
            # menu6일 때
            self.setFixedHeight(580)  # 다이얼로그 전체 높이
            self.ui.tabWidget.setFixedHeight(520)  # 탭위젯 높이
            self.ui.groupBox_passive.setFixedHeight(330)  # 패시브 그룹박스 높이
            self.ui.groupBox_coordinate.setFixedHeight(410)  # 좌표 그룹박스 높이    
            self.ui.buttonBox.setGeometry(self.ui.buttonBox.x(), 540,  # 버튼박스 y좌표 수정
                                        self.ui.buttonBox.width(),
                                        self.ui.buttonBox.height())
        
    def load_settings(self):
        """저장된 설정값 로드"""
        data = load_json_data(self.data_file)
        current_menu = self.main_window.get_current_menu()
        if data and current_menu in data:
            # 액티브 모드 설정 로드
            active_settings = data[current_menu]['settings_active']
            
            # 실행/중지 콤보박스 설정
            index = self.ui.combo_run.findText(active_settings['combo_run_value'])
            if index >= 0:
                self.ui.combo_run.setCurrentIndex(index)
            index = self.ui.combo_stop.findText(active_settings['combo_stop_value'])
            if index >= 0:
                self.ui.combo_stop.setCurrentIndex(index)
            
            # 액티브 모드 체크박스 설정
            self.ui.check_ctrl1.setChecked(active_settings['check_ctrl1_state'])
            self.ui.check_alt1.setChecked(active_settings['check_alt1_state'])
            self.ui.check_shift1.setChecked(active_settings['check_shift1_state'])
            self.ui.check_ctrl2.setChecked(active_settings['check_ctrl2_state'])
            self.ui.check_alt2.setChecked(active_settings['check_alt2_state'])
            self.ui.check_shift2.setChecked(active_settings['check_shift2_state'])
            
            # 패시브 모드 설정 로드
            passive_settings = data[current_menu]['settings_passive']
            
            # menu2, menu3는 3개, menu6는 6개의 설정
            max_items = 6 if current_menu == 'menu6' else 3
            
            for i in range(1, max_items + 1):
                combo = getattr(self.ui, f'combo_ps{i}')
                index = combo.findText(passive_settings.get(f'combo_ps{i}_value', '0'))
                if index >= 0:
                    combo.setCurrentIndex(index)
                
                ctrl = getattr(self.ui, f'check_ctrl{i+2}')
                alt = getattr(self.ui, f'check_alt{i+2}')
                shift = getattr(self.ui, f'check_shift{i+2}')
                
                ctrl.setChecked(passive_settings.get(f'check_ctrl{i+2}_state', False))
                alt.setChecked(passive_settings.get(f'check_alt{i+2}_state', False))
                shift.setChecked(passive_settings.get(f'check_shift{i+2}_state', False))

    def save_settings(self):
        """설정값 저장"""
        data = load_json_data(self.data_file)
        current_menu = self.main_window.get_current_menu()
        if data:
            # 액티브 모드 설정 저장
            active_settings = {
                'combo_run_value': self.ui.combo_run.currentText(),
                'check_ctrl1_state': self.ui.check_ctrl1.isChecked(),
                'check_alt1_state': self.ui.check_alt1.isChecked(),
                'check_shift1_state': self.ui.check_shift1.isChecked(),
                'combo_stop_value': self.ui.combo_stop.currentText(),
                'check_ctrl2_state': self.ui.check_ctrl2.isChecked(),
                'check_alt2_state': self.ui.check_alt2.isChecked(),
                'check_shift2_state': self.ui.check_shift2.isChecked(),
            }
            
            # 패시브 모드 설정 저장
            passive_settings = {}
            max_items = 6 if current_menu == 'menu6' else 3
            
            for i in range(1, max_items + 1):
                combo = getattr(self.ui, f'combo_ps{i}')
                ctrl = getattr(self.ui, f'check_ctrl{i+2}')
                alt = getattr(self.ui, f'check_alt{i+2}')
                shift = getattr(self.ui, f'check_shift{i+2}')
                
                passive_settings.update({
                    f'combo_ps{i}_value': combo.currentText(),
                    f'check_ctrl{i+2}_state': ctrl.isChecked(),
                    f'check_alt{i+2}_state': alt.isChecked(),
                    f'check_shift{i+2}_state': shift.isChecked(),
                })
            
            # 패시브 모드 좌표 데이터 저장
            try:
                for i in range(1, max_items + 1):
                    x_coord = getattr(self.ui, f'textEdit_X{i}').toPlainText()
                    y_coord = getattr(self.ui, f'textEdit_Y{i}').toPlainText()
                    
                    if x_coord and y_coord:
                        data[current_menu]['coordinates_passive']['setting_pos'][f'image{i}_x'] = int(x_coord)
                        data[current_menu]['coordinates_passive']['setting_pos'][f'image{i}_y'] = int(y_coord)
                    else:
                        # 좌표가 비어있는 경우 초기화
                        data[current_menu]['coordinates_passive']['setting_pos'][f'image{i}_x'] = 0
                        data[current_menu]['coordinates_passive']['setting_pos'][f'image{i}_y'] = 0
            except ValueError:
                pass  # 숫자로 변환할 수 없는 경우 무시
            
            # 설정 저장
            data[current_menu]['settings_active'] = active_settings
            data[current_menu]['settings_passive'] = passive_settings
            save_json_data(self.data_file, data)