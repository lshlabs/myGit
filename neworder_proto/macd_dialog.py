from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import Qt
import os

class MACDSettingDialog(QtWidgets.QDialog):
    def __init__(self, parent=None, is_short=False):
        super(MACDSettingDialog, self).__init__(parent)
        
        # 숏 전략인지 확인 (부모 위젯 이름으로 확인)
        if parent and hasattr(parent, 'objectName'):
            # 명시적 전달값 우선
            self.is_short = is_short
            # 부모 버튼 이름으로 숏인지 확인
            if not is_short and parent.objectName() in ['btn_detail_signal1_short', 'btn_detail_signal2_short']:
                self.is_short = True
        else:
            self.is_short = is_short
        
        # UI 파일 경로
        ui_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ui", "macd_dialog.ui")
        
        # UI 파일 로드
        uic.loadUi(ui_path, self)
        
        # 버튼 연결
        self.reset_btn.clicked.connect(self.reset_values)
        self.save_btn.clicked.connect(self.accept)
        self.radio_option1.setChecked(True)
        self.radio_option2.setChecked(False)
        
        # 숏 전략일 경우 텍스트 변경
        if self.is_short:
            # radio_option1 텍스트 변경
            if hasattr(self, 'radio_option1'):
                self.radio_option1.setText("MACD선이 0선을 하향 돌파할 때 숏 포지션 진입")
            
            # radio_option2 텍스트 변경
            if hasattr(self, 'radio_option2'):
                self.radio_option2.setText("MACD선이 시그널선을 하향 돌파할 때 숏 포지션 진입")
    
    def reset_values(self):
        """설정값 초기화"""
        # MACD 설정값 초기화
        self.macd_fast.setValue(12)
        self.macd_slow.setValue(26)
        self.macd_signal.setValue(9)
        
        # 라디오 버튼 초기화
        self.radio_option1.setChecked(True)
        self.radio_option2.setChecked(False)
    
    def get_settings(self):
        """현재 설정값 반환"""
        return {
            'macd_fast': self.macd_fast.value(),
            'macd_slow': self.macd_slow.value(),
            'macd_signal': self.macd_signal.value(),
            'option': 1 if self.radio_option1.isChecked() else 2,
            'is_short': self.is_short
        } 