import json
import os
from PySide6.QtWidgets import QDialog
from ui.SettingsDialog_ui import Ui_SettingsDialog
#import resource_rc
from utils import get_data_file_path, load_json_data, save_json_data

class SettingsDialog(QDialog):
    def __init__(self, main_window, parent=None):
        super().__init__(parent)
        self.main_window = main_window
        self.ui = Ui_SettingsDialog()
        self.ui.setupUi(self)
        
        # ComboBox_run에 0-9 숫자 추가
        for i in range(10):
            self.ui.combo_run.addItem(str(i))
        
        # ComboBox_stop에 0-9 숫자 추가
        for i in range(10):
            self.ui.combo_stop.addItem(str(i))
            
        self.data_file = get_data_file_path()
        self.load_settings()
        self.ui.buttonBox.accepted.connect(self.save_settings)
        self.ui.buttonBox.rejected.connect(self.reject)
        
    def load_settings(self):
        """저장된 설정값 로드"""
        data = load_json_data(self.data_file)  # 데이터 파일에서 기존 데이터 로드
        current_menu = self.main_window.get_current_menu()  # 현재 선택된 메뉴 가져오기
        if data and current_menu in data:
            settings = data[current_menu]['settings']  # 현재 메뉴의 설정 가져오기
            
            index = self.ui.combo_run.findText(settings['combo_run_value'])
            if index >= 0:
                self.ui.combo_run.setCurrentIndex(index)
            index = self.ui.combo_stop.findText(settings['combo_stop_value'])
            if index >= 0:
                self.ui.combo_stop.setCurrentIndex(index)
            
            self.ui.check_ctrl1.setChecked(settings['check_ctrl1_state'])
            self.ui.check_alt1.setChecked(settings['check_alt1_state'])
            self.ui.check_shift1.setChecked(settings['check_shift1_state'])
            self.ui.check_ctrl2.setChecked(settings['check_ctrl2_state'])
            self.ui.check_alt2.setChecked(settings['check_alt2_state'])
            self.ui.check_shift2.setChecked(settings['check_shift2_state'])
            
    def save_settings(self):
        """설정값 저장"""
        data = load_json_data(self.data_file)  # 데이터 파일에서 기존 데이터 로드
        current_menu = self.main_window.get_current_menu()  # 현재 선택된 메뉴 가져오기
        if data:
            # 현재 메뉴에 해당하는 설정 저장
            data[current_menu]['settings'] = {
                'combo_run_value': self.ui.combo_run.currentText(),
                'check_ctrl1_state': self.ui.check_ctrl1.isChecked(),
                'check_alt1_state': self.ui.check_alt1.isChecked(),
                'check_shift1_state': self.ui.check_shift1.isChecked(),
                'combo_stop_value': self.ui.combo_stop.currentText(),
                'check_ctrl2_state': self.ui.check_ctrl2.isChecked(),
                'check_alt2_state': self.ui.check_alt2.isChecked(),
                'check_shift2_state': self.ui.check_shift2.isChecked(),
            }
            save_json_data(self.data_file, data)  # 수정된 데이터를 JSON 파일에 저장