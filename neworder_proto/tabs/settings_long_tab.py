from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtCore import Qt
import os
import sys
from trading_settings import TradingSettings

# 상위 디렉토리 경로를 Python 경로에 추가
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# 그 후 ma_dialog 모듈에서 MASettingDialog 클래스 임포트
from ma_dialog import MASettingDialog
from rsi_dialog import RSISettingDialog
from macd_dialog import MACDSettingDialog
from boll_dialog import BollingerSettingDialog

class SettingsLongTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        # 롱 포지션 설정 객체 생성
        self.settings = TradingSettings(is_short=False)
        self.setup_ui()
        self.setup_connections()
        
        # 프로그램 시작 시 자동으로 저장된 설정 로드
        self.load_settings_from_json()
        print("프로그램 시작 시 롱 포지션 설정 로드 시도")
        
    def setup_ui(self):
        # 코인 선택 그룹박스
        self.Layout_long_coin_selection = self.parent.Layout_long_coin_selection
        self.comboBox_coin_selection_long = self.parent.comboBox_coin_selection_long
        
        # 매수 시그널 설정
        self.buy_signal1_long = self.parent.buy_signal1_long
        self.label_signal1_long = self.parent.label_signal1_long
        self.comboBox_signal1_long = self.parent.comboBox_signal1_long
        self.comboBox_timeframe1_long = self.parent.comboBox_timeframe1_long
        self.btn_detail_signal1_long = self.parent.btn_detail_signal1_long
        
        self.buy_signal2_long = self.parent.buy_signal2_long
        self.label_signal2_long = self.parent.label_signal2_long
        self.comboBox_signal2_long = self.parent.comboBox_signal2_long
        self.comboBox_timeframe2_long = self.parent.comboBox_timeframe2_long
        self.btn_detail_signal2_long = self.parent.btn_detail_signal2_long
        
        # 매수 수량 설정
        self.buy_long_amount = self.parent.buy_long_amount
        self.label_buy_amount_long = self.parent.label_buy_amount_long
        self.spinBox_buy_amount_long = self.parent.spinBox_buy_amount_long
        self.spinBox_additional_long = self.parent.spinBox_additional_long
        self.checkBox_split_buy_long = self.parent.checkBox_split_buy_long
        
        # 분할매수 1 설정
        self.buy_split1_long = self.parent.buy_split1_long
        self.checkBox1_split_long = self.parent.checkBox1_split_long
        self.spinBox1_split1_long = self.parent.spinBox1_split1_long
        self.label1_split1_long = self.parent.label1_split1_long
        self.spinBox2_split1_long = self.parent.spinBox2_split1_long
        self.spinBox3_split1_long = self.parent.spinBox3_split1_long
        self.label2_split1_long = self.parent.label2_split1_long
        
        # 분할매수 2 설정
        self.buy_split2_long = self.parent.buy_split2_long
        self.checkBox2_split_long = self.parent.checkBox2_split_long
        self.spinBox1_split2_long = self.parent.spinBox1_split2_long
        self.label1_split2_long = self.parent.label1_split2_long
        self.spinBox2_split2_long = self.parent.spinBox2_split2_long
        self.spinBox3_split2_long = self.parent.spinBox3_split2_long
        self.label2_split2_long = self.parent.label2_split2_long
        
        # 익절 설정
        self.Layout_long_sell1 = self.parent.Layout_long_sell1
        self.label_profit_cut_long = self.parent.label_profit_cut_long
        self.checkBox_takeprofit1_long = self.parent.checkBox_takeprofit1_long
        self.doubleSpinBox_profit_rate_long = self.parent.doubleSpinBox_profit_rate_long
        self.label_profit_condition_long = self.parent.label_profit_condition_long
        self.checkBox_takeprofit2_long = self.parent.checkBox_takeprofit2_long
        self.spinBox_takeprofit1_long = self.parent.spinBox_takeprofit1_long
        self.label_profit_condition_2_long = self.parent.label_profit_condition_2_long
        
        # 손절 설정
        self.Layout_long_sell2 = self.parent.Layout_long_sell2
        self.label_loss_cut_long = self.parent.label_loss_cut_long
        self.checkBox_stoploss1_long = self.parent.checkBox_stoploss1_long
        self.doubleSpinBox_loss_rate_long = self.parent.doubleSpinBox_loss_rate_long
        self.label_loss_condition_long = self.parent.label_loss_condition_long
        self.checkBox_stoploss2_long = self.parent.checkBox_stoploss2_long
        self.spinBox_stoploss1_long = self.parent.spinBox_stoploss1_long
        self.label_profit_condition_3_long = self.parent.label_profit_condition_3_long
        
    def setup_connections(self):
        # 시그널 상세설정 버튼 연결
        self.btn_detail_signal1_long.clicked.connect(self.show_signal1_detail)
        self.btn_detail_signal2_long.clicked.connect(self.show_signal2_detail)
        
        # 분할매수 체크박스 상태 변경 이벤트 연결
        self.checkBox_split_buy_long.stateChanged.connect(self.on_split_buy_changed)
        self.checkBox1_split_long.stateChanged.connect(self.on_split1_changed)
        self.checkBox2_split_long.stateChanged.connect(self.on_split2_changed)
        
        # 익절 체크박스 상태 변경 이벤트 연결
        self.checkBox_takeprofit1_long.stateChanged.connect(self.on_takeprofit1_changed)
        self.checkBox_takeprofit2_long.stateChanged.connect(self.on_takeprofit2_changed)
        
        # 손절 체크박스 상태 변경 이벤트 연결
        self.checkBox_stoploss1_long.stateChanged.connect(self.on_stoploss1_changed)
        self.checkBox_stoploss2_long.stateChanged.connect(self.on_stoploss2_changed)
        
        # 저장 버튼 연결 (존재할 경우)
        if hasattr(self.parent, 'button_save_long'):
            self.button_save_long = self.parent.button_save_long
            self.button_save_long.clicked.connect(self.save_settings_to_json)
        
        # 로드 버튼 연결 (버튼이 있다면)
        if hasattr(self.parent, 'button_load_long'):
            self.button_load_long = self.parent.button_load_long
            self.button_load_long.clicked.connect(self.load_settings_from_json)
        
    def on_split_buy_changed(self, state):
        # 분할매수 체크박스 상태에 따라 레이아웃 표시/숨김
        is_enabled = state == 2  # Qt.CheckState.Checked는 2와 같음
        
        # buy_split1_long과 buy_split2_long 레이아웃을 포함하는 위젯들을 숨김/표시
        for layout_name in ['buy_split1_long', 'buy_split2_long']:
            layout = getattr(self.parent, layout_name)
            if layout:
                for i in range(layout.count()):
                    widget = layout.itemAt(i).widget()
                    if widget:
                        widget.setVisible(is_enabled)
        
    def on_split1_changed(self, state):
        if state == 2:  # 체크됨
            self.checkBox2_split_long.setChecked(False)  # 다른 체크박스 해제
            # 분할매수 1 위젯들 활성화
            self.spinBox1_split1_long.setEnabled(True)
            self.label1_split1_long.setEnabled(True)
            self.spinBox2_split1_long.setEnabled(True)
            self.spinBox3_split1_long.setEnabled(True)
            self.label2_split1_long.setEnabled(True)
            # 분할매수 2 위젯들 비활성화
            self.spinBox1_split2_long.setEnabled(False)
            self.label1_split2_long.setEnabled(False)
            self.spinBox2_split2_long.setEnabled(False)
            self.spinBox3_split2_long.setEnabled(False)
            self.label2_split2_long.setEnabled(False)
            
    def on_split2_changed(self, state):
        if state == 2:  # 체크됨
            self.checkBox1_split_long.setChecked(False)  # 다른 체크박스 해제
            # 분할매수 1 위젯들 비활성화
            self.spinBox1_split1_long.setEnabled(False)
            self.label1_split1_long.setEnabled(False)
            self.spinBox2_split1_long.setEnabled(False)
            self.spinBox3_split1_long.setEnabled(False)
            self.label2_split1_long.setEnabled(False)
            # 분할매수 2 위젯들 활성화
            self.spinBox1_split2_long.setEnabled(True)
            self.label1_split2_long.setEnabled(True)
            self.spinBox2_split2_long.setEnabled(True)
            self.spinBox3_split2_long.setEnabled(True)
            self.label2_split2_long.setEnabled(True)
        
    def on_takeprofit1_changed(self, state):
        if state == 2:  # 체크됨
            self.checkBox_takeprofit2_long.setChecked(False)  # 다른 체크박스 해제
            # 익절 1 위젯 활성화
            self.doubleSpinBox_profit_rate_long.setEnabled(True)
            self.label_profit_condition_long.setEnabled(True)
            # 익절 2 위젯 비활성화
            self.spinBox_takeprofit1_long.setEnabled(False)
            self.label_profit_condition_2_long.setEnabled(False)
            
    def on_takeprofit2_changed(self, state):
        if state == 2:  # 체크됨
            self.checkBox_takeprofit1_long.setChecked(False)  # 다른 체크박스 해제
            # 익절 1 위젯 비활성화
            self.doubleSpinBox_profit_rate_long.setEnabled(False)
            self.label_profit_condition_long.setEnabled(False)
            # 익절 2 위젯 활성화
            self.spinBox_takeprofit1_long.setEnabled(True)
            self.label_profit_condition_2_long.setEnabled(True)
        
    def on_stoploss1_changed(self, state):
        if state == 2:  # 체크됨
            self.checkBox_stoploss2_long.setChecked(False)  # 다른 체크박스 해제
            # 손절 1 위젯 활성화
            self.doubleSpinBox_loss_rate_long.setEnabled(True)
            self.label_loss_condition_long.setEnabled(True)
            # 손절 2 위젯 비활성화
            self.spinBox_stoploss1_long.setEnabled(False)
            self.label_profit_condition_3_long.setEnabled(False)
            
    def on_stoploss2_changed(self, state):
        if state == 2:  # 체크됨
            self.checkBox_stoploss1_long.setChecked(False)  # 다른 체크박스 해제
            # 손절 1 위젯 비활성화
            self.doubleSpinBox_loss_rate_long.setEnabled(False)
            self.label_loss_condition_long.setEnabled(False)
            # 손절 2 위젯 활성화
            self.spinBox_stoploss1_long.setEnabled(True)
            self.label_profit_condition_3_long.setEnabled(True)
        
    def show_signal1_detail(self):
        # comboBox_signal1_long의 현재 선택값 가져오기
        signal_type = self.comboBox_signal1_long.currentText()
        timeframe = self.comboBox_timeframe1_long.currentText()
        
        # 선택된 시그널 타입에 따라 적절한 다이얼로그 표시
        if signal_type == "이동평균선":
            dialog = MASettingDialog(self)
        elif signal_type == "RSI":
            dialog = RSISettingDialog(self)
        elif signal_type == "MACD":
            dialog = MACDSettingDialog(self)
        elif signal_type == "볼린저밴드":
            dialog = BollingerSettingDialog(self)
        else:
            print(f"시그널 1 상세설정: {signal_type}에 대한 다이얼로그가 없습니다.")
            return
            
        # 다이얼로그 실행 및 결과 처리
        if dialog.exec():
            settings = dialog.get_settings()
            # TradingSettings 객체에 저장
            self.settings.signal1["type"] = signal_type
            self.settings.signal1["timeframe"] = timeframe
            self.settings.signal1["settings"] = settings
            print(f"시그널 1 {signal_type} 설정:", settings)
            
            # 설정 요약 업데이트 (만약 요약 표시 UI가 있다면)
            self.update_settings_summary()
    
    def show_signal2_detail(self):
        # comboBox_signal2_long의 현재 선택값 가져오기
        signal_type = self.comboBox_signal2_long.currentText()
        timeframe = self.comboBox_timeframe2_long.currentText()
        
        # 선택된 시그널 타입에 따라 적절한 다이얼로그 표시
        if signal_type == "이동평균선":
            dialog = MASettingDialog(self)
        elif signal_type == "RSI":
            dialog = RSISettingDialog(self)
        elif signal_type == "MACD":
            dialog = MACDSettingDialog(self)
        elif signal_type == "볼린저밴드":
            dialog = BollingerSettingDialog(self)
        else:
            print(f"시그널 2 상세설정: {signal_type}에 대한 다이얼로그가 없습니다.")
            return
            
        # 다이얼로그 실행 및 결과 처리
        if dialog.exec():
            settings = dialog.get_settings()
            # TradingSettings 객체에 저장
            self.settings.signal2["type"] = signal_type
            self.settings.signal2["timeframe"] = timeframe
            self.settings.signal2["settings"] = settings
            
            # 설정 요약 업데이트
            self.update_settings_summary()
    
    # 설정을 UI에 반영하는 메서드
    def update_settings_summary(self):
        # 여기서 설정 요약을 표시하는 UI 요소가 있다면 업데이트
        if hasattr(self.parent, 'label_settings_summary_long'):
            summary_text = self.settings.to_text()
            self.parent.label_settings_summary_long.setText(summary_text)
    
    def update_settings_from_ui(self):
        """UI 컨트롤의 값을 설정 객체에 업데이트"""
        # 코인 선택
        self.settings.coin_selection = self.comboBox_coin_selection_long.currentText()
        
        # 매수 시그널 설정
        self.settings.signal1["type"] = self.comboBox_signal1_long.currentText()
        self.settings.signal1["timeframe"] = self.comboBox_timeframe1_long.currentText()
        
        self.settings.signal2["type"] = self.comboBox_signal2_long.currentText()
        self.settings.signal2["timeframe"] = self.comboBox_timeframe2_long.currentText()
        
        # 매수 수량 설정 (수정)
        self.settings.buy_amount["base_amount"] = self.spinBox_buy_amount_long.value()  # 매수 수량
        self.settings.buy_amount["leverage"] = self.spinBox_additional_long.value()    # 레버리지
        
        split_checked = self.checkBox_split_buy_long.isChecked()
        self.settings.buy_amount["use_split"] = split_checked
        
        # 분할 매수 설정
        if split_checked:
            if self.checkBox1_split_long.isChecked():
                self.settings.buy_amount["split_criteria"] = "rsi"
                self.settings.buy_amount["rsi_level1"] = self.spinBox1_split1_long.value()
                self.settings.buy_amount["rsi_amount1"] = self.spinBox2_split1_long.value()
                self.settings.buy_amount["rsi_amount2"] = self.spinBox3_split1_long.value()
            elif self.checkBox2_split_long.isChecked():
                self.settings.buy_amount["split_criteria"] = "price"
                self.settings.buy_amount["price_drop1"] = self.spinBox1_split2_long.value()
                self.settings.buy_amount["price_amount1"] = self.spinBox2_split2_long.value()
                self.settings.buy_amount["price_amount2"] = self.spinBox3_split2_long.value()
        
        # 체크박스 상태에 따라 UI 업데이트
        check_state = 2 if split_checked else 0
        self.on_split_buy_changed(check_state)
        
        # 익절 설정
        if self.checkBox_takeprofit1_long.isChecked():
            self.settings.take_profit["type"] = "rate"
            self.settings.take_profit["rate"] = self.doubleSpinBox_profit_rate_long.value()
        elif self.checkBox_takeprofit2_long.isChecked():
            self.settings.take_profit["type"] = "indicator"
            self.settings.take_profit["indicator"] = self.spinBox_takeprofit1_long.value()
        
        # 손절 설정
        if self.checkBox_stoploss1_long.isChecked():
            self.settings.stop_loss["type"] = "rate"
            self.settings.stop_loss["rate"] = self.doubleSpinBox_loss_rate_long.value()
        elif self.checkBox_stoploss2_long.isChecked():
            self.settings.stop_loss["type"] = "indicator"
            self.settings.stop_loss["indicator"] = self.spinBox_stoploss1_long.value()
        
        # 설정 요약 업데이트
        self.update_settings_summary()

    def load_settings_to_ui(self):
        """설정 객체의 값을 UI 컨트롤에 반영"""
        # 코인 선택
        if self.settings.coin_selection:
            index = self.comboBox_coin_selection_long.findText(self.settings.coin_selection)
            if index >= 0:
                self.comboBox_coin_selection_long.setCurrentIndex(index)
        
        # 시그널 1 설정
        if self.settings.signal1["type"]:
            index = self.comboBox_signal1_long.findText(self.settings.signal1["type"])
            if index >= 0:
                self.comboBox_signal1_long.setCurrentIndex(index)
        
        if self.settings.signal1["timeframe"]:
            index = self.comboBox_timeframe1_long.findText(self.settings.signal1["timeframe"])
            if index >= 0:
                self.comboBox_timeframe1_long.setCurrentIndex(index)
        
        # 시그널 2 설정
        if self.settings.signal2["type"]:
            index = self.comboBox_signal2_long.findText(self.settings.signal2["type"])
            if index >= 0:
                self.comboBox_signal2_long.setCurrentIndex(index)
        
        if self.settings.signal2["timeframe"]:
            index = self.comboBox_timeframe2_long.findText(self.settings.signal2["timeframe"])
            if index >= 0:
                self.comboBox_timeframe2_long.setCurrentIndex(index)
        
        # 매수 수량 설정
        self.spinBox_buy_amount_long.setValue(self.settings.buy_amount["base_amount"])
        # 레버리지 설정 추가
        self.settings.buy_amount["leverage"] = self.spinBox_additional_long.value()
        split_checked = self.settings.buy_amount["use_split"]
        self.checkBox_split_buy_long.setChecked(split_checked)
        
        # 분할 매수 설정
        if split_checked:
            if self.settings.buy_amount["split_criteria"] == "rsi":
                self.checkBox1_split_long.setChecked(True)
                self.spinBox1_split1_long.setValue(self.settings.buy_amount.get("rsi_level1", 0))
                self.spinBox2_split1_long.setValue(self.settings.buy_amount.get("rsi_amount1", 0))
                self.spinBox3_split1_long.setValue(self.settings.buy_amount.get("rsi_amount2", 0))
            elif self.settings.buy_amount["split_criteria"] == "price":
                self.checkBox2_split_long.setChecked(True)
                self.spinBox1_split2_long.setValue(self.settings.buy_amount.get("price_drop1", 0))
                self.spinBox2_split2_long.setValue(self.settings.buy_amount.get("price_amount1", 0))
                self.spinBox3_split2_long.setValue(self.settings.buy_amount.get("price_amount2", 0))
        
        # 여기에서 직접 on_split_buy_changed 호출 추가
        check_state = 2 if split_checked else 0
        self.on_split_buy_changed(check_state)
        
        # 익절 설정
        if self.settings.take_profit["type"] == "rate":
            self.checkBox_takeprofit1_long.setChecked(True)
            self.doubleSpinBox_profit_rate_long.setValue(self.settings.take_profit.get("rate", 0.0))
        elif self.settings.take_profit["type"] == "indicator":
            self.checkBox_takeprofit2_long.setChecked(True)
            self.spinBox_takeprofit1_long.setValue(self.settings.take_profit.get("indicator", 0))
        
        # 손절 설정
        if self.settings.stop_loss["type"] == "rate":
            self.checkBox_stoploss1_long.setChecked(True)
            self.doubleSpinBox_loss_rate_long.setValue(self.settings.stop_loss.get("rate", 0.0))
        elif self.settings.stop_loss["type"] == "indicator":
            self.checkBox_stoploss2_long.setChecked(True)
            self.spinBox_stoploss1_long.setValue(self.settings.stop_loss.get("indicator", 0))
        
        # 설정 요약 업데이트
        self.update_settings_summary()

    def save_settings_to_json(self):
        """설정을 data.json 파일에 저장"""
        # UI 값을 설정 객체에 업데이트
        self.update_settings_from_ui()
        
        # data.json 파일에 저장
        self.settings.save_to_file()
        print("롱 포지션 설정이 data.json에 저장되었습니다.")
        
        # 필요시 저장 완료 메시지 표시
        if hasattr(self.parent, 'statusBar'):
            self.parent.statusBar().showMessage("롱 포지션 설정 저장 완료", 3000)
        
        # TradingTab의 설정 표시 업데이트
        if hasattr(self.parent, 'tab_trading'):  # 'trading_tab'이 아닌 'tab_trading'으로 수정
            self.parent.tab_trading.update_settings_display()

    def load_settings_from_json(self):
        """data.json 파일에서 설정 로드"""
        # 파일에서 설정 로드
        if self.settings.load_from_file():
            # UI 업데이트
            self.load_settings_to_ui()
            print("롱 포지션 설정이 data.json에서 로드되었습니다.")
            
            # 필요시 로드 완료 메시지 표시
            if hasattr(self.parent, 'statusBar'):
                self.parent.statusBar().showMessage("롱 포지션 설정 로드 완료", 3000)
        else:
            print("설정 파일 로드 실패")
            # 로드 실패 메시지 표시
            if hasattr(self.parent, 'statusBar'):
                self.parent.statusBar().showMessage("설정 파일 로드 실패", 3000)