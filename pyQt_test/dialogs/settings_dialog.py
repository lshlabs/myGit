import json
import os
from PySide6.QtWidgets import QDialog
from ui.SettingsDialog_ui import Ui_SettingsDialog
#import resource_rc
from utils import get_data_file_path, load_json_data, save_json_data

class SettingsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
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
        
    def load_settings(self):
        """저장된 설정값 로드"""
        data = load_json_data(self.data_file)
        if data and 'settings' in data:
            index = self.ui.combo_run.findText(data['settings']['combo_run_value'])
            if index >= 0:
                self.ui.combo_run.setCurrentIndex(index)
            index = self.ui.combo_stop.findText(data['settings']['combo_stop_value'])
            if index >= 0:
                self.ui.combo_stop.setCurrentIndex(index)
            self.ui.check_ctrl1.setChecked(data['settings']['check_ctrl1_state'])
            self.ui.check_alt1.setChecked(data['settings']['check_alt1_state'])
            self.ui.check_shift1.setChecked(data['settings']['check_shift1_state'])
            self.ui.check_ctrl2.setChecked(data['settings']['check_ctrl2_state'])
            self.ui.check_alt2.setChecked(data['settings']['check_alt2_state'])
            self.ui.check_shift2.setChecked(data['settings']['check_shift2_state'])
            
    def save_settings(self):
        """설정값 저장"""
        data = load_json_data(self.data_file)
        if data:
            data['settings'] = {
                'combo_run_value': self.ui.combo_run.currentText(),
                'check_ctrl1_state': self.ui.check_ctrl1.isChecked(),
                'check_alt1_state': self.ui.check_alt1.isChecked(),
                'check_shift1_state': self.ui.check_shift1.isChecked(),
                'combo_stop_value': self.ui.combo_stop.currentText(),
                'check_ctrl2_state': self.ui.check_ctrl2.isChecked(),
                'check_alt2_state': self.ui.check_alt2.isChecked(),
                'check_shift2_state': self.ui.check_shift2.isChecked(),
            }
            save_json_data(self.data_file, data)