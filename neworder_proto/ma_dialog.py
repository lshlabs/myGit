from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import Qt
import os

class MASettingDialog(QtWidgets.QDialog):
    def __init__(self, parent=None, is_short=False):
        super(MASettingDialog, self).__init__(parent)
        
        # 숏 전략인지 확인 (부모 위젯 이름으로 확인)
        if parent and hasattr(parent, 'objectName'):
            # 명시적 전달값 우선
            self.is_short = is_short
            # 부모 버튼 이름으로 숏인지 확인
            if not is_short and parent.objectName() in ['btn_detail_signal1_short', 'btn_detail_signal2_short']:
                self.is_short = True
        else:
            self.is_short = is_short
        
        # UI 파일 경로 수정 - ui 폴더 추가
        ui_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ui", "ma_dialog.ui")
        
        # UI 파일 로드
        uic.loadUi(ui_path, self)
        
        # 콤보박스 초기화
        self.setup_combos()
        
        # 버튼 연결
        self.reset_btn.clicked.connect(self.reset_values)
        self.save_btn.clicked.connect(self.accept)
        self.radio_option1.setChecked(True)
        self.radio_option2.setChecked(False)
        
        # 숏 전략일 경우 텍스트 변경
        if self.is_short:
            # label5 텍스트 변경
            if hasattr(self, 'label5'):  # UI에 label5가 있는지 확인
                self.label5.setText("데드 크로스 발생 시")
            
            # radio_option2 텍스트 변경
            if hasattr(self, 'radio_option2'):
                self.radio_option2.setText("단기, 중기, 장기 역배열 완성 시")
    
    def setup_combos(self):
        """콤보박스 선택지 설정"""
        # 첫 번째 콤보박스
        self.combo1.clear()
        self.combo1.addItems(["단기", "중기", "장기"])
        self.combo1.setCurrentText("단기")
        
        # 두 번째 콤보박스
        self.combo2.clear()
        self.combo2.addItems(["단기", "중기", "장기"])
        self.combo2.setCurrentText("중기")
    
    def reset_values(self):
        """설정값 초기화"""
        # 이동평균선 기간 초기화
        self.short_ma.setValue(20)
        self.mid_ma.setValue(60)
        self.long_ma.setValue(120)
        
        # 라디오 버튼 초기화
        self.radio_option1.setChecked(True)
        self.radio_option2.setChecked(False)
        
        # 콤보박스 초기화
        self.combo1.setCurrentText("단기")
        self.combo2.setCurrentText("중기")
    
    def get_settings(self):
        """현재 설정값 반환"""
        return {
            'short_ma': self.short_ma.value(),
            'mid_ma': self.mid_ma.value(),
            'long_ma': self.long_ma.value(),
            'option': 1 if self.radio_option1.isChecked() else 2,
            'cross_first': self.combo1.currentText(),
            'cross_second': self.combo2.currentText(),
            'is_short': self.is_short
        }
        
        