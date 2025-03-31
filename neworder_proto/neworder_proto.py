import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QColor, QBrush
from ma_dialog import MASettingDialog

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        # UI 파일 로드
        uic.loadUi('neworder_proto/main_ui.ui', self)
        
        # 탭 위젯 연결
        self.tabWidget.currentChanged.connect(self.on_tab_changed)
        
        # 롱 탭 - 분할매수 체크박스 연결
        self.checkBox_split_buy_long.stateChanged.connect(self.toggle_split_buy_options_long)
        
        # 롱 탭 - 하위 체크박스 연결 (RSI, 가격)
        if hasattr(self, 'checkBox_split_buy_1_long'):
            self.checkBox_split_buy_1_long.setChecked(False)  # 초기 상태 체크 해제
            self.checkBox_split_buy_1_long.stateChanged.connect(self.toggle_split_option1_long)
            
        if hasattr(self, 'checkBox_split_buy_2_long'):
            self.checkBox_split_buy_2_long.setChecked(False)  # 초기 상태 체크 해제
            self.checkBox_split_buy_2_long.stateChanged.connect(self.toggle_split_option2_long)
        
        # 롱 탭 - 익절/손절 체크박스 연결 및 초기 상태 설정
        if hasattr(self, 'checkBox_takeprofit1_long'):
            self.checkBox_takeprofit1_long.setChecked(True)  # 수익률 기준 익절 - 초기 상태 체크 
            self.checkBox_takeprofit1_long.stateChanged.connect(self.toggle_profit_option1_long)
        
        if hasattr(self, 'checkBox_takeprofit2_long'):
            self.checkBox_takeprofit2_long.setChecked(False)  # 현재가 대비 기준 익절 - 초기 상태 체크 해제
            self.checkBox_takeprofit2_long.stateChanged.connect(self.toggle_profit_option2_long)
        
        if hasattr(self, 'checkBox_stoploss1_long'):
            self.checkBox_stoploss1_long.setChecked(True)  # 수익률 기준 손절 - 초기 상태 체크
            self.checkBox_stoploss1_long.stateChanged.connect(self.toggle_loss_option1_long)
        
        if hasattr(self, 'checkBox_stoploss2_long'):
            self.checkBox_stoploss2_long.setChecked(False)  # 현재가 대비 기준 손절 - 초기 상태 체크 해제
            self.checkBox_stoploss2_long.stateChanged.connect(self.toggle_loss_option2_long)
        
        # 롱 탭 - 익절/손절 위젯 초기 상태 명시적 설정
        if hasattr(self, 'spinBox_takeprofit1_long'):
            self.spinBox_takeprofit1_long.setEnabled(False)  # 현재가 대비 익절 스핀박스 비활성화
        
        if hasattr(self, 'label_profit_condition_2_long'):
            self.label_profit_condition_2_long.setEnabled(False)  # 현재가 대비 익절 라벨 비활성화
        
        if hasattr(self, 'doubleSpinBox_profit_rate_long'):
            self.doubleSpinBox_profit_rate_long.setEnabled(True)  # 수익률 기준 익절 스핀박스 활성화
        
        if hasattr(self, 'label_profit_condition_long'):
            self.label_profit_condition_long.setEnabled(True)  # 수익률 기준 익절 라벨 활성화
        
        if hasattr(self, 'spinBox_stoploss1_long'):
            self.spinBox_stoploss1_long.setEnabled(False)  # 현재가 대비 손절 스핀박스 비활성화
        
        if hasattr(self, 'label_profit_condition_3_long'):
            self.label_profit_condition_3_long.setEnabled(False)  # 현재가 대비 손절 라벨 비활성화
        
        if hasattr(self, 'doubleSpinBox_loss_rate_long'):
            self.doubleSpinBox_loss_rate_long.setEnabled(True)  # 수익률 기준 손절 스핀박스 활성화
        
        if hasattr(self, 'label_loss_condition_long'):
            self.label_loss_condition_long.setEnabled(True)  # 수익률 기준 손절 라벨 활성화
        
        # 롱 탭 - 하위 레이아웃의 각 위젯 숨김 (초기 상태)
        self.set_layout_widgets_visible(self.horizontalLayout_buy_split1_long, False)
        self.set_layout_widgets_visible(self.horizontalLayout_buy_split2_long, False)
        
        # 롱 탭 - 레이아웃 내 요소들 비활성화 (초기 상태) - 체크박스 제외
        self.set_layout_widgets_enabled(
            self.horizontalLayout_buy_split1_long, 
            False, 
            self.checkBox_split_buy_1_long
        )
        self.set_layout_widgets_enabled(
            self.horizontalLayout_buy_split2_long, 
            False, 
            self.checkBox_split_buy_2_long
        )
        
        # 숏 탭 - 분할매수 체크박스 연결
        if hasattr(self, 'checkBox_split_buy'):
            self.checkBox_split_buy.stateChanged.connect(self.toggle_split_buy_options_short)
        
        # 숏 탭 - 하위 체크박스 연결 (RSI, 가격)
        if hasattr(self, 'checkBox_split_buy_1'):
            self.checkBox_split_buy_1.setChecked(False)  # 초기 상태 체크 해제
            self.checkBox_split_buy_1.stateChanged.connect(self.toggle_split_option1_short)
            
        if hasattr(self, 'checkBox_split_buy_2'):
            self.checkBox_split_buy_2.setChecked(False)  # 초기 상태 체크 해제
            self.checkBox_split_buy_2.stateChanged.connect(self.toggle_split_option2_short)
        
        # 숏 탭 - 익절/손절 체크박스 연결 (UI에 해당 위젯 있는 경우)
        if hasattr(self, 'checkBox_takeprofit1'):
            self.checkBox_takeprofit1.setChecked(True)  # 수익률 기준 익절 - 초기 상태 체크
            self.checkBox_takeprofit1.stateChanged.connect(self.toggle_profit_option1_short)
        
        if hasattr(self, 'checkBox_takeprofit2'):
            self.checkBox_takeprofit2.setChecked(False)  # 현재가 대비 기준 익절 - 초기 상태 체크 해제
            self.checkBox_takeprofit2.stateChanged.connect(self.toggle_profit_option2_short)
        
        if hasattr(self, 'checkBox_stoploss1'):
            self.checkBox_stoploss1.setChecked(True)  # 수익률 기준 손절 - 초기 상태 체크
            self.checkBox_stoploss1.stateChanged.connect(self.toggle_loss_option1_short)
        
        if hasattr(self, 'checkBox_stoploss2'):
            self.checkBox_stoploss2.setChecked(False)  # 현재가 대비 기준 손절 - 초기 상태 체크 해제
            self.checkBox_stoploss2.stateChanged.connect(self.toggle_loss_option2_short)
        
        # 숏 탭 - 익절/손절 위젯 초기 상태 명시적 설정
        if hasattr(self, 'spinBox_takeprofit1'):
            self.spinBox_takeprofit1.setEnabled(False)  # 현재가 대비 익절 스핀박스 비활성화
        
        if hasattr(self, 'label_profit_condition_2'):
            self.label_profit_condition_2.setEnabled(False)  # 현재가 대비 익절 라벨 비활성화
        
        if hasattr(self, 'doubleSpinBox_profit_rate'):
            self.doubleSpinBox_profit_rate.setEnabled(True)  # 수익률 기준 익절 스핀박스 활성화
        
        if hasattr(self, 'label_profit_condition'):
            self.label_profit_condition.setEnabled(True)  # 수익률 기준 익절 라벨 활성화
        
        if hasattr(self, 'spinBox_stoploss1'):
            self.spinBox_stoploss1.setEnabled(False)  # 현재가 대비 손절 스핀박스 비활성화
        
        if hasattr(self, 'label_profit_condition_3'):
            self.label_profit_condition_3.setEnabled(False)  # 현재가 대비 손절 라벨 비활성화
        
        if hasattr(self, 'doubleSpinBox_loss_rate'):
            self.doubleSpinBox_loss_rate.setEnabled(True)  # 수익률 기준 손절 스핀박스 활성화
        
        if hasattr(self, 'label_loss_condition'):
            self.label_loss_condition.setEnabled(True)  # 수익률 기준 손절 라벨 활성화
        
        # 숏 탭 - 하위 레이아웃의 각 위젯 숨김 (초기 상태)
        self.set_layout_widgets_visible(self.horizontalLayout_buy_split1, False)
        self.set_layout_widgets_visible(self.horizontalLayout_buy_split2, False)
        
        # 숏 탭 - 레이아웃 내 요소들 비활성화 (초기 상태) - 체크박스 제외
        self.set_layout_widgets_enabled(
            self.horizontalLayout_buy_split1, 
            False, 
            self.checkBox_split_buy_1
        )
        self.set_layout_widgets_enabled(
            self.horizontalLayout_buy_split2, 
            False, 
            self.checkBox_split_buy_2
        )
        
        # 트레이딩 패널 버튼 연결
        self.start_button.clicked.connect(self.start_trading)
        self.stop_button.clicked.connect(self.stop_trading)
        self.log_clear.clicked.connect(self.clear_log)
        
        # 코인 테이블 초기화
        self.setup_coin_table()
        
        # 수익 테이블 초기화
        self.setup_profit_table()
        
        # 롱 매매설정 탭 요소 연결
        self.btn_detail_signal2_long.clicked.connect(self.open_signal_detail_long)
        self.btn_detail_signal1_long.clicked.connect(self.open_signal_detail1_long)
        self.comboBox_signal2_long.currentIndexChanged.connect(self.on_signal_changed_long)
        self.comboBox_timeframe2_long.currentIndexChanged.connect(self.on_timeframe_changed_long)
        
        # 숏 매매설정 탭 요소 연결
        self.btn_detail_signal2_short.clicked.connect(self.open_signal_detail_short)
        self.btn_detail_signal1_short.clicked.connect(self.open_signal_detail1_short)
        self.comboBox_signal2_short.currentIndexChanged.connect(self.on_signal_changed_short)
        self.comboBox_timeframe2_short.currentIndexChanged.connect(self.on_timeframe_changed_short)
        
        # 수익 탭 요소 연결
        self.period_combo.currentIndexChanged.connect(self.on_period_changed)
        self.excel_download_btn.clicked.connect(self.download_excel)
        
        # 보유포지션 청산 버튼 연결
        self.btn_all_coins.clicked.connect(self.clear_all_positions)
        
        # 상태 메시지 설정
        self.status_label.setText("프로그램 준비 완료")
        
    def setup_coin_table(self):
        """코인 테이블 초기화"""
        # 헤더 설정
        self.coin_table.setColumnCount(5)
        self.coin_table.setHorizontalHeaderLabels(["코인명", "회차", "평가손익(USDT)", "손익률(%)", "보유수량"])
        
        # 컬럼 너비 직접 설정
        self.coin_table.setColumnWidth(0, 40)  # 코인명
        self.coin_table.setColumnWidth(1, 30)  # 회차
        self.coin_table.setColumnWidth(2, 85) # 평가손익(USDT)
        self.coin_table.setColumnWidth(3, 60)  # 손익률(%)
        self.coin_table.setColumnWidth(4, 60)  # 보유수량
        
        # 테이블 행 수 설정 (샘플 데이터)
        self.coin_table.setRowCount(10)
        
        # 샘플 데이터로 테이블 채우기
        sample_data = [
            ("BTC", "32", "62,000", "+10.2", "3,210"),
            ("ETH", "21", "3,500", "-3.5", "2,143"),
        ]
        
        for row, (coin, round_num, profit, percent, amount) in enumerate(sample_data):
            self.coin_table.setItem(row, 0, QtWidgets.QTableWidgetItem(coin))
            self.coin_table.setItem(row, 1, QtWidgets.QTableWidgetItem(round_num))
            
            # 평가손익에 색상 적용
            profit_item = QtWidgets.QTableWidgetItem(profit)
            if profit.startswith("+"):
                profit_item.setForeground(QBrush(QColor("green")))
            elif profit.startswith("-"):
                profit_item.setForeground(QBrush(QColor("red")))
            self.coin_table.setItem(row, 2, profit_item)
            
            # 손익률에 색상 적용
            percent_item = QtWidgets.QTableWidgetItem(percent)
            if percent.startswith("+"):
                percent_item.setForeground(QBrush(QColor("green")))
            elif percent.startswith("-"):
                percent_item.setForeground(QBrush(QColor("red")))
            self.coin_table.setItem(row, 3, percent_item)
            
            self.coin_table.setItem(row, 4, QtWidgets.QTableWidgetItem(amount))
        
        # 테이블 헤더 설정
        header = self.coin_table.horizontalHeader()
        header.setStretchLastSection(True)  # 마지막 열을 남은 공간에 맞게 늘림
    
    def setup_profit_table(self):
        """수익 테이블 초기화"""
        # 테이블 행 수 설정 (샘플 데이터)
        self.profit_table.setRowCount(5)
        
        # 샘플 데이터로 테이블 채우기
        sample_data = [
            ("2023-05-10 14:30", "MACD", "BTC", "0.01", "62,100,000", "62,600,000", "+48,000", "+0.8%"),
            ("2023-05-09 11:15", "이평선", "ETH", "0.5", "3,250,000", "3,300,000", "+24,000", "+1.5%"),
            ("2023-05-08 16:45", "MACD", "SOL", "5", "142,000", "145,000", "+14,500", "+2.1%"),
            ("2023-05-07 09:20", "이평선", "XRP", "1000", "750", "730", "-20,000", "-2.7%"),
            ("2023-05-06 13:55", "MACD", "AVAX", "2", "35,000", "36,200", "+2,300", "+3.4%"),
        ]
        
        for row, (date, signal, symbol, amount, buy_price, sell_price, profit, percent) in enumerate(sample_data):
            self.profit_table.setItem(row, 0, QtWidgets.QTableWidgetItem(""))  # 첫 번째 열은 비워둠
            self.profit_table.setItem(row, 1, QtWidgets.QTableWidgetItem(date))
            self.profit_table.setItem(row, 2, QtWidgets.QTableWidgetItem(signal))
            self.profit_table.setItem(row, 3, QtWidgets.QTableWidgetItem(symbol))
            self.profit_table.setItem(row, 4, QtWidgets.QTableWidgetItem(amount))
            self.profit_table.setItem(row, 5, QtWidgets.QTableWidgetItem(buy_price))
            self.profit_table.setItem(row, 6, QtWidgets.QTableWidgetItem(sell_price))
            
            # 수익과 수익률에 색상 적용
            profit_item = QtWidgets.QTableWidgetItem(profit)
            percent_item = QtWidgets.QTableWidgetItem(percent)
            
            if profit.startswith("+"):
                profit_item.setForeground(QBrush(QColor("green")))
                percent_item.setForeground(QBrush(QColor("green")))
            elif profit.startswith("-"):
                profit_item.setForeground(QBrush(QColor("red")))
                percent_item.setForeground(QBrush(QColor("red")))
                
            self.profit_table.setItem(row, 7, profit_item)
            self.profit_table.setItem(row, 8, percent_item)

    def set_layout_widgets_visible(self, layout, visible):
        """레이아웃 내 모든 위젯의 표시 상태 설정"""
        for i in range(layout.count()):
            widget = layout.itemAt(i).widget()
            if widget:
                widget.setVisible(visible)
    
    def set_layout_widgets_enabled(self, layout, enabled, exclude_widget=None):
        """레이아웃 내 모든 위젯의 활성화 상태 설정 (특정 위젯 제외 가능)"""
        for i in range(layout.count()):
            widget = layout.itemAt(i).widget()
            if widget and widget != exclude_widget:
                widget.setEnabled(enabled)
    
    def toggle_split_buy_options_long(self, state):
        """롱 - 분할매수 체크박스 상태에 따라 추가 옵션 표시/숨김"""
        checked = state == Qt.CheckState.Checked.value
        
        # 레이아웃 내 각 위젯 표시/숨김
        self.set_layout_widgets_visible(self.horizontalLayout_buy_split1_long, checked)
        self.set_layout_widgets_visible(self.horizontalLayout_buy_split2_long, checked)
        
        # 체크 해제 시 하위 체크박스도 초기화
        if not checked:
            if hasattr(self, 'checkBox_split_buy_1_long'):
                self.checkBox_split_buy_1_long.setChecked(False)
            if hasattr(self, 'checkBox_split_buy_2_long'):
                self.checkBox_split_buy_2_long.setChecked(False)
        
        status = "활성화" if checked else "비활성화"
        self.status_label.setText(f"롱 - 분할매수 옵션이 {status}되었습니다.")
    
    def toggle_split_option1_long(self, state):
        """롱 - 첫 번째 분할매수 옵션(RSI) 체크박스 상태에 따른 처리"""
        checked = state == Qt.CheckState.Checked.value
        
        # 체크박스를 제외한 나머지 위젯 활성화/비활성화
        self.set_layout_widgets_enabled(
            self.horizontalLayout_buy_split1_long, 
            checked, 
            self.checkBox_split_buy_1_long
        )
        
        # 첫 번째 체크박스가 체크되면 두 번째 체크박스 체크 해제
        if checked and hasattr(self, 'checkBox_split_buy_2_long'):
            self.checkBox_split_buy_2_long.setChecked(False)
        
    def toggle_split_option2_long(self, state):
        """롱 - 두 번째 분할매수 옵션(가격) 체크박스 상태에 따른 처리"""
        checked = state == Qt.CheckState.Checked.value
        
        # 체크박스를 제외한 나머지 위젯 활성화/비활성화
        self.set_layout_widgets_enabled(
            self.horizontalLayout_buy_split2_long, 
            checked, 
            self.checkBox_split_buy_2_long
        )
        
        # 두 번째 체크박스가 체크되면 첫 번째 체크박스 체크 해제
        if checked and hasattr(self, 'checkBox_split_buy_1_long'):
            self.checkBox_split_buy_1_long.setChecked(False)
    
    def on_tab_changed(self, index):
        """탭 변경 시 호출되는 함수"""
        tab_names = ["트레이딩", "매매설정(롱)", "매매설정(숏)", "수익기록", "인증설정"]
        if 0 <= index < len(tab_names):
            self.status_label.setText(f"{tab_names[index]} 탭으로 이동했습니다.")
    
    def start_trading(self):
        """매매 시작 버튼 클릭 시 호출"""
        self.status_label.setText("매매를 시작합니다...")
        # 여기에 매매 시작 관련 로직 추가
    
    def stop_trading(self):
        """매매 중지 버튼 클릭 시 호출"""
        self.status_label.setText("매매를 중지합니다...")
        # 여기에 매매 중지 관련 로직 추가
    
    def clear_log(self):
        """로그 삭제 버튼 클릭 시 호출"""
        self.status_label.setText("트레이딩 로그를 삭제했습니다.")
        # 로그 위젯 내용 삭제 로직 추가
    
    def open_signal_detail_long(self):
        """롱 - 시그널 상세 설정 버튼 클릭 시 호출"""
        signal_type = self.comboBox_signal2_long.currentText()
        self.status_label.setText(f"롱 - {signal_type} 상세 설정을 엽니다.")
        # 시그널 상세 설정 다이얼로그 표시 로직 추가
    
    def open_signal_detail1_long(self):
        """롱 - 시그널1 상세 설정 버튼 클릭 시 호출"""
        signal_type = self.comboBox_signal1_long.currentText()
        if signal_type == "이동평균선":
            self.status_label.setText(f"롱 - {signal_type} 상세 설정을 엽니다.")
            # MA 다이얼로그 생성 및 표시
            self.ma_dialog = MASettingDialog(self)
            self.ma_dialog.exec()
        else:
            self.status_label.setText(f"롱 - {signal_type}은(는) 상세 설정이 지원되지 않습니다.")
    
    def on_signal_changed_long(self, index):
        """롱 - 시그널 콤보박스 변경 시 호출"""
        signal_type = self.comboBox_signal2_long.currentText()
        self.status_label.setText(f"롱 - 시그널 유형이 {signal_type}(으)로 변경되었습니다.")
    
    def on_timeframe_changed_long(self, index):
        """롱 - 타임프레임 콤보박스 변경 시 호출"""
        timeframe = self.comboBox_timeframe2_long.currentText()
        self.status_label.setText(f"롱 - 타임프레임이 {timeframe}(으)로 변경되었습니다.")
    
    def on_period_changed(self, index):
        """기간 콤보박스 변경 시 호출"""
        period = self.period_combo.currentText()
        self.status_label.setText(f"조회 기간이 {period}(으)로 변경되었습니다.")
        # 기간에 따른 수익 테이블 갱신 로직 추가
    
    def download_excel(self):
        """엑셀 다운로드 버튼 클릭 시 호출"""
        self.status_label.setText("엑셀 파일 다운로드 중...")
        # 엑셀 다운로드 로직 추가
    
    def clear_all_positions(self):
        """보유포지션 청산 버튼 클릭 시 호출"""
        self.status_label.setText("모든 보유 포지션을 청산합니다...")
        # 포지션 청산 로직 추가

    def open_signal_detail_short(self):
        """숏 시그널 상세 설정 버튼 클릭 시 호출"""
        signal_type = self.comboBox_signal2_short.currentText()
        self.status_label.setText(f"숏 - {signal_type} 상세 설정을 엽니다.")
        # 시그널 상세 설정 다이얼로그 표시 로직 추가
    
    def open_signal_detail1_short(self):
        """숏 시그널1 상세 설정 버튼 클릭 시 호출"""
        signal_type = self.comboBox_signal1_short.currentText()
        if signal_type == "이동평균선":
            self.status_label.setText(f"숏 - {signal_type} 상세 설정을 엽니다.")
            # MA 다이얼로그 생성 및 표시
            self.ma_dialog = MASettingDialog(self)
            self.ma_dialog.exec()
        else:
            self.status_label.setText(f"숏 - {signal_type}은(는) 상세 설정이 지원되지 않습니다.")
    
    def on_signal_changed_short(self, index):
        """숏 시그널 콤보박스 변경 시 호출"""
        signal_type = self.comboBox_signal2_short.currentText()
        self.status_label.setText(f"숏 - 시그널 유형이 {signal_type}(으)로 변경되었습니다.")
    
    def on_timeframe_changed_short(self, index):
        """숏 타임프레임 콤보박스 변경 시 호출"""
        timeframe = self.comboBox_timeframe2_short.currentText()
        self.status_label.setText(f"숏 - 타임프레임이 {timeframe}(으)로 변경되었습니다.")

    def toggle_split_buy_options_short(self, state):
        """숏 - 분할매수 체크박스 상태에 따라 추가 옵션 표시/숨김"""
        checked = state == Qt.CheckState.Checked.value
        
        # 레이아웃 내 각 위젯 표시/숨김
        self.set_layout_widgets_visible(self.horizontalLayout_buy_split1, checked)
        self.set_layout_widgets_visible(self.horizontalLayout_buy_split2, checked)
        
        # 체크 해제 시 하위 체크박스도 초기화
        if not checked:
            if hasattr(self, 'checkBox_split_buy_1'):
                self.checkBox_split_buy_1.setChecked(False)
            if hasattr(self, 'checkBox_split_buy_2'):
                self.checkBox_split_buy_2.setChecked(False)
        
        status = "활성화" if checked else "비활성화"
        self.status_label.setText(f"숏 - 분할매수 옵션이 {status}되었습니다.")

    def toggle_split_option1_short(self, state):
        """숏 - 첫 번째 분할매수 옵션(RSI) 체크박스 상태에 따른 처리"""
        checked = state == Qt.CheckState.Checked.value
        
        # 체크박스를 제외한 나머지 위젯 활성화/비활성화
        if hasattr(self, 'horizontalLayout_buy_split1') and hasattr(self, 'checkBox_split_buy_1'):
            self.set_layout_widgets_enabled(
                self.horizontalLayout_buy_split1, 
                checked, 
                self.checkBox_split_buy_1
            )
        
        # 첫 번째 체크박스가 체크되면 두 번째 체크박스 체크 해제
        if checked and hasattr(self, 'checkBox_split_buy_2'):
            self.checkBox_split_buy_2.setChecked(False)

    def toggle_split_option2_short(self, state):
        """숏 - 두 번째 분할매수 옵션(가격) 체크박스 상태에 따른 처리"""
        checked = state == Qt.CheckState.Checked.value
        
        # 체크박스를 제외한 나머지 위젯 활성화/비활성화
        if hasattr(self, 'horizontalLayout_buy_split2') and hasattr(self, 'checkBox_split_buy_2'):
            self.set_layout_widgets_enabled(
                self.horizontalLayout_buy_split2, 
                checked, 
                self.checkBox_split_buy_2
            )
        
        # 두 번째 체크박스가 체크되면 첫 번째 체크박스 체크 해제
        if checked and hasattr(self, 'checkBox_split_buy_1'):
            self.checkBox_split_buy_1.setChecked(False)

    def toggle_profit_option1_short(self, state):
        """숏 - 익절 옵션1(수익률 기준) 체크박스 상태에 따른 처리"""
        checked = state == Qt.CheckState.Checked.value
        
        # 체크되면 다른 옵션 체크박스 해제
        if checked and hasattr(self, 'checkBox_takeprofit2'):
            self.checkBox_takeprofit2.setChecked(False)
        
        # 수익률 기준 익절 관련 위젯 활성화/비활성화
        if hasattr(self, 'doubleSpinBox_profit_rate'):
            self.doubleSpinBox_profit_rate.setEnabled(checked)
        
        if hasattr(self, 'label_profit_condition'):
            self.label_profit_condition.setEnabled(checked)
        
        # 현재가 대비 익절 관련 위젯 비활성화/활성화
        if hasattr(self, 'spinBox_takeprofit1'):
            self.spinBox_takeprofit1.setEnabled(not checked)
        
        if hasattr(self, 'label_profit_condition_2'):
            self.label_profit_condition_2.setEnabled(not checked)

    def toggle_profit_option2_short(self, state):
        """숏 - 익절 옵션2(현재가 대비) 체크박스 상태에 따른 처리"""
        checked = state == Qt.CheckState.Checked.value
        
        # 체크되면 다른 옵션 체크박스 해제
        if checked and hasattr(self, 'checkBox_takeprofit1'):
            self.checkBox_takeprofit1.setChecked(False)
        
        # 현재가 대비 익절 관련 위젯 활성화/비활성화
        if hasattr(self, 'spinBox_takeprofit1'):
            self.spinBox_takeprofit1.setEnabled(checked)
        
        if hasattr(self, 'label_profit_condition_2'):
            self.label_profit_condition_2.setEnabled(checked)
        
        # 수익률 기준 익절 관련 위젯 비활성화/활성화
        if hasattr(self, 'doubleSpinBox_profit_rate'):
            self.doubleSpinBox_profit_rate.setEnabled(not checked)
        
        if hasattr(self, 'label_profit_condition'):
            self.label_profit_condition.setEnabled(not checked)

    def toggle_loss_option1_short(self, state):
        """숏 - 손절 옵션1(수익률 기준) 체크박스 상태에 따른 처리"""
        checked = state == Qt.CheckState.Checked.value
        
        # 체크되면 다른 옵션 체크박스 해제
        if checked and hasattr(self, 'checkBox_stoploss2'):
            self.checkBox_stoploss2.setChecked(False)
        
        # 수익률 기준 손절 관련 위젯 활성화/비활성화
        if hasattr(self, 'doubleSpinBox_loss_rate'):
            self.doubleSpinBox_loss_rate.setEnabled(checked)
        
        if hasattr(self, 'label_loss_condition'):
            self.label_loss_condition.setEnabled(checked)
        
        # 현재가 대비 손절 관련 위젯 비활성화/활성화
        if hasattr(self, 'spinBox_stoploss1'):
            self.spinBox_stoploss1.setEnabled(not checked)
        
        if hasattr(self, 'label_profit_condition_3'):
            self.label_profit_condition_3.setEnabled(not checked)

    def toggle_loss_option2_short(self, state):
        """숏 - 손절 옵션2(현재가 대비) 체크박스 상태에 따른 처리"""
        checked = state == Qt.CheckState.Checked.value
        
        # 체크되면 다른 옵션 체크박스 해제
        if checked and hasattr(self, 'checkBox_stoploss1'):
            self.checkBox_stoploss1.setChecked(False)
        
        # 현재가 대비 손절 관련 위젯 활성화/비활성화
        if hasattr(self, 'spinBox_stoploss1'):
            self.spinBox_stoploss1.setEnabled(checked)
        
        if hasattr(self, 'label_profit_condition_3'):
            self.label_profit_condition_3.setEnabled(checked)
        
        # 수익률 기준 손절 관련 위젯 비활성화/활성화
        if hasattr(self, 'doubleSpinBox_loss_rate'):
            self.doubleSpinBox_loss_rate.setEnabled(not checked)
        
        if hasattr(self, 'label_loss_condition'):
            self.label_loss_condition.setEnabled(not checked)

    def toggle_profit_option1_long(self, state):
        """롱 - 익절 옵션1(수익률 기준) 체크박스 상태에 따른 처리"""
        checked = state == Qt.CheckState.Checked.value
        
        # 체크되면 다른 옵션 체크박스 해제
        if checked and hasattr(self, 'checkBox_takeprofit2_long'):
            self.checkBox_takeprofit2_long.setChecked(False)
        
        # 수익률 기준 익절 관련 위젯 활성화/비활성화
        if hasattr(self, 'doubleSpinBox_profit_rate_long'):
            self.doubleSpinBox_profit_rate_long.setEnabled(checked)
        
        if hasattr(self, 'label_profit_condition_long'):
            self.label_profit_condition_long.setEnabled(checked)
        
        # 현재가 대비 익절 관련 위젯 비활성화/활성화
        if hasattr(self, 'spinBox_takeprofit1_long'):
            self.spinBox_takeprofit1_long.setEnabled(not checked)
        
        if hasattr(self, 'label_profit_condition_2_long'):
            self.label_profit_condition_2_long.setEnabled(not checked)

    def toggle_profit_option2_long(self, state):
        """롱 - 익절 옵션2(현재가 대비) 체크박스 상태에 따른 처리"""
        checked = state == Qt.CheckState.Checked.value
        
        # 체크되면 다른 옵션 체크박스 해제
        if checked and hasattr(self, 'checkBox_takeprofit1_long'):
            self.checkBox_takeprofit1_long.setChecked(False)
        
        # 현재가 대비 익절 관련 위젯 활성화/비활성화
        if hasattr(self, 'spinBox_takeprofit1_long'):
            self.spinBox_takeprofit1_long.setEnabled(checked)
        
        if hasattr(self, 'label_profit_condition_2_long'):
            self.label_profit_condition_2_long.setEnabled(checked)
        
        # 수익률 기준 익절 관련 위젯 비활성화/활성화
        if hasattr(self, 'doubleSpinBox_profit_rate_long'):
            self.doubleSpinBox_profit_rate_long.setEnabled(not checked)
        
        if hasattr(self, 'label_profit_condition_long'):
            self.label_profit_condition_long.setEnabled(not checked)

    def toggle_loss_option1_long(self, state):
        """롱 - 손절 옵션1(수익률 기준) 체크박스 상태에 따른 처리"""
        checked = state == Qt.CheckState.Checked.value
        
        # 체크되면 다른 옵션 체크박스 해제
        if checked and hasattr(self, 'checkBox_stoploss2_long'):
            self.checkBox_stoploss2_long.setChecked(False)
        
        # 수익률 기준 손절 관련 위젯 활성화/비활성화
        if hasattr(self, 'doubleSpinBox_loss_rate_long'):
            self.doubleSpinBox_loss_rate_long.setEnabled(checked)
        
        if hasattr(self, 'label_loss_condition_long'):
            self.label_loss_condition_long.setEnabled(checked)
        
        # 현재가 대비 손절 관련 위젯 비활성화/활성화
        if hasattr(self, 'spinBox_stoploss1_long'):
            self.spinBox_stoploss1_long.setEnabled(not checked)
        
        if hasattr(self, 'label_profit_condition_3_long'):
            self.label_profit_condition_3_long.setEnabled(not checked)

    def toggle_loss_option2_long(self, state):
        """롱 - 손절 옵션2(현재가 대비) 체크박스 상태에 따른 처리"""
        checked = state == Qt.CheckState.Checked.value
        
        # 체크되면 다른 옵션 체크박스 해제
        if checked and hasattr(self, 'checkBox_stoploss1_long'):
            self.checkBox_stoploss1_long.setChecked(False)
        
        # 현재가 대비 손절 관련 위젯 활성화/비활성화
        if hasattr(self, 'spinBox_stoploss1_long'):
            self.spinBox_stoploss1_long.setEnabled(checked)
        
        if hasattr(self, 'label_profit_condition_3_long'):
            self.label_profit_condition_3_long.setEnabled(checked)
        
        # 수익률 기준 손절 관련 위젯 비활성화/활성화
        if hasattr(self, 'doubleSpinBox_loss_rate_long'):
            self.doubleSpinBox_loss_rate_long.setEnabled(not checked)
        
        if hasattr(self, 'label_loss_condition_long'):
            self.label_loss_condition_long.setEnabled(not checked)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())