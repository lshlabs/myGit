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
        
        # ComboBox에 0-9 숫자 추가
        for i in range(10):
            self.ui.comboBox.addItem(str(i))
            
        self.data_file = get_data_file_path()
        self.load_settings()
        self.ui.buttonBox.accepted.connect(self.save_settings)
        
    def load_settings(self):
        """저장된 설정값 로드"""
        data = load_json_data(self.data_file)
        if data and 'settings' in data:
            index = self.ui.comboBox.findText(data['settings']['combobox_value'])
            if index >= 0:
                self.ui.comboBox.setCurrentIndex(index)
            self.ui.checkBox.setChecked(data['settings']['checkbox_state'])
            
    def save_settings(self):
        """설정값 저장"""
        data = load_json_data(self.data_file)
        if data:
            data['settings'] = {
                'combobox_value': self.ui.comboBox.currentText(),
                'checkbox_state': self.ui.checkBox.isChecked()
            }
            save_json_data(self.data_file, data)