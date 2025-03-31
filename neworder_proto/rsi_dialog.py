from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import Qt
import os

class RSISettingDialog(QtWidgets.QDialog):
    def __init__(self, parent=None, is_short=False):
        super(RSISettingDialog, self).__init__(parent)
        
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
        ui_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ui", "rsi_dialog.ui")
        
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
                self.radio_option1.setText("RSI 과매수에서 하락 전환 시 숏 포지션 진입 (역추세)")
            
            # radio_option2 텍스트 변경
            if hasattr(self, 'radio_option2'):
                self.radio_option2.setText("RSI 50 돌파 후 하락하고 있을 때 숏 포지션 진입 (추세추종)")
    
    def reset_values(self):
        """설정값 초기화"""
        # RSI 길이와 과매수/과매도 초기화
        self.rsi_length.setValue(14)
        self.rsi_overbought.setValue(70)
        self.rsi_oversold.setValue(30)
        
        # 라디오 버튼 초기화
        self.radio_option1.setChecked(True)
        self.radio_option2.setChecked(False)
    
    def get_settings(self):
        """현재 설정값 반환"""
        return {
            'rsi_length': self.rsi_length.value(),
            'rsi_overbought': self.rsi_overbought.value(),
            'rsi_oversold': self.rsi_oversold.value(),
            'option': 1 if self.radio_option1.isChecked() else 2,
            'is_short': self.is_short
        } 