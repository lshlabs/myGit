from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHeaderView, QTableWidgetItem, QTextEdit
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QColor, QBrush
import os
import sys
import json
import requests

class TradingTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        # 이전 가격 정보 저장용 딕셔너리 추가
        self.previous_prices = {}
        self.setup_ui()
        self.setup_connections()
        # 초기화 시 설정 정보 로드
        self.load_settings_overview()
        
    def setup_ui(self):
        # UI 요소들 참조
        self.coin_table = self.parent.coin_table
        self.scrollArea_log = self.parent.scrollArea_log
        self.scrollArea_setting = self.parent.scrollArea_setting
        self.log_clear = self.parent.log_clear
        self.start_button = self.parent.start_button
        self.stop_button = self.parent.stop_button
        
        # 설정 정보를 표시할 텍스트 에디트 위젯 생성 및 스크롤 영역에 추가
        self.setting_text = QTextEdit()
        self.setting_text.setReadOnly(True)  # 읽기 전용으로 설정
        
        # 스크롤 영역에 위젯 추가
        if hasattr(self.scrollArea_setting, 'setWidget'):
            self.scrollArea_setting.setWidget(self.setting_text)
        
        # 테이블 열 너비 설정
        self.setup_table_columns()
        
        # 가격 업데이트 타이머 설정
        self.price_timer = QTimer(self)
        self.price_timer.timeout.connect(self.update_price_data)
        self.price_timer.start(1000)  # 1초마다 업데이트
        
        # 초기 가격 업데이트
        self.update_price_data()
        
    def setup_table_columns(self):
        # 테이블 헤더 가져오기
        header = self.coin_table.horizontalHeader()
        
        # 모든 열을 내용에 맞게 자동 조정
        for i in range(self.coin_table.columnCount() - 1):
            header.setSectionResizeMode(i, QHeaderView.ResizeMode.ResizeToContents)
        
        # 마지막 열은 남은 공간을 채우도록 설정 (선택사항)
        header.setSectionResizeMode(self.coin_table.columnCount() - 1, QHeaderView.ResizeMode.Stretch)
        
        # 헤더 텍스트 중앙 정렬
        self.coin_table.horizontalHeader().setDefaultAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # 기존 셀 아이템들의 정렬 설정
        self.align_all_items()
        
        # 데이터 변경 시 다시 정렬 설정 (필요한 경우)
        self.coin_table.itemChanged.connect(self.on_item_changed)
        
        # 헤더 클릭으로 정렬 가능하도록 설정
        self.coin_table.setSortingEnabled(True)
    
    def align_all_items(self):
        """테이블의 모든 셀 아이템을 중앙 정렬"""
        for row in range(self.coin_table.rowCount()):
            for col in range(self.coin_table.columnCount()):
                item = self.coin_table.item(row, col)
                if item:
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
    
    def on_item_changed(self, item):
        """데이터 변경 시 셀 아이템 중앙 정렬"""
        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        
    def setup_connections(self):
        self.log_clear.clicked.connect(self.clear_log)
        self.start_button.clicked.connect(self.start_trading)
        self.stop_button.clicked.connect(self.stop_trading)
        
    def clear_log(self):
        print("로그 삭제")
        
    def get_signal_option_text(self, signal_type, option, settings=None, is_short=False):
        """시그널 타입과 옵션 번호에 따른 옵션 텍스트 반환"""
        if signal_type == "RSI":
            if not is_short:  # 롱 포지션
                if option == 1:
                    return "RSI 과매도에서 상승 전환 시 롱 포지션 진입 (역추세)"
                elif option == 2:
                    return "RSI 과매수에서 하락 전환 시 롱 포지션 진입 (추세추종)"
            else:  # 숏 포지션
                if option == 1:
                    return "RSI 과매수에서 하락 전환 시 숏 포지션 진입 (역추세)"
                elif option == 2:
                    return "RSI 과매도에서 상승 전환 시 숏 포지션 진입 (추세추종)"
        elif signal_type == "볼린저밴드":
            if not is_short:  # 롱 포지션
                if option == 1:
                    return "하단밴드 터치 후 반등 시 롱 포지션 진입 (역추세)"
                elif option == 2:
                    return "상단밴드 돌파 후 미들밴드로 조정 시 롱 포지션 진입 (추세추종)"
            else:  # 숏 포지션
                if option == 1:
                    return "상단밴드 터치 후 반락 시 숏 포지션 진입 (역추세)"
                elif option == 2:
                    return "하단밴드 돌파 후 미들밴드로 조정 시 숏 포지션 진입 (추세추종)"
        elif signal_type == "MACD":
            if not is_short:  # 롱 포지션
                if option == 1:
                    return "MACD 골든크로스 시 롱 포지션 진입"
                elif option == 2:
                    return "MACD 시그널 > 0 이상 상승 시 롱 포지션 진입"
            else:  # 숏 포지션
                if option == 1:
                    return "MACD 데드크로스 시 숏 포지션 진입"
                elif option == 2:
                    return "MACD 시그널 < 0 이하 하락 시 숏 포지션 진입"
        elif signal_type == "이동평균선":
            if not settings:
                return "옵션 설명 없음"
            
            if option == 1:
                combo1 = settings.get('combo1', '')
                combo2 = settings.get('combo2', '')
                ma1_value = settings.get(f"{combo1.lower()}_ma", 0)
                ma2_value = settings.get(f"{combo2.lower()}_ma", 0)
                cross_type = "골든크로스" if not is_short else "데드크로스"
                return f"{combo1}: {ma1_value}, {combo2}: {ma2_value} {cross_type} 시"
            elif option == 2:
                if is_short:
                    return "단기, 중기, 장기 역배열 완성 시"
                else:
                    return "단기, 중기, 장기 정배열 완성 시"
        return "옵션 설명 없음"

    def load_settings_overview(self):
        """data.json 파일에서 설정 정보를 로드하여 표시"""
        try:
            # 설정 파일 경로
            settings_file = "neworder_proto/data/data.json"
            
            if not os.path.exists(settings_file):
                self.setting_text.setText("설정 파일이 존재하지 않습니다.")
                return
                
            # 설정 파일 읽기
            with open(settings_file, 'r', encoding='utf-8') as f:
                settings_data = json.load(f)
                
            # HTML 형식으로 설정 정보 구성
            settings_text = "<html><body style='font-family: Arial;'>"
            settings_text += "<h3>=== 매매 설정 정보 ===</h3>"
            
            # 롱 포지션 설정 정보
            if "long_settings" in settings_data:
                long_settings = settings_data["long_settings"]
                settings_text += "<h4>▶ 롱 포지션 설정</h4>"
                settings_text += f"코인: {long_settings.get('coin_selection', '설정 없음')}<br><br>"
                
                # 시그널1 정보
                signal1 = long_settings.get('signal1', {})
                settings_text += "<span style='font-size: 18px; font-weight: bold;'>진입 시그널1: </span>"
                settings_text += f"<span style='color: red; font-size: 18px; font-weight: bold;'>{signal1.get('type', '없음')}</span><br>"
                settings_text += f"봉 타입: {signal1.get('timeframe', '없음')}<br>"
                signal1_option = signal1.get('settings', {}).get('option', 1)
                settings_text += f"옵션 {signal1_option}: {self.get_signal_option_text(signal1.get('type', ''), signal1_option, signal1.get('settings', {}), is_short=False)}<br><br>"
                
                # 시그널2 정보
                signal2 = long_settings.get('signal2', {})
                settings_text += "<span style='font-size: 18px; font-weight: bold;'>진입 시그널2: </span>"
                settings_text += f"<span style='color: red; font-size: 18px; font-weight: bold;'>{signal2.get('type', '없음')}</span><br>"
                settings_text += f"봉 타입: {signal2.get('timeframe', '없음')}<br>"
                signal2_option = signal2.get('settings', {}).get('option', 1)
                settings_text += f"옵션 {signal2_option}: {self.get_signal_option_text(signal2.get('type', ''), signal2_option, signal2.get('settings', {}), is_short=False)}<br><br>"
                
                # 매수 전략
                settings_text += "<span style='font-size: 18px; font-weight: bold;'>매수 전략</span><br>"
                buy_amount = long_settings.get('buy_amount', {})
                settings_text += f"진입수량: {buy_amount.get('base_amount', 0)}개<br>"
                settings_text += f"레버리지: {buy_amount.get('leverage', 1)}x<br>"
                
                if buy_amount.get('use_split', False):
                    settings_text += "분할매수: 사용함<br>"
                    if buy_amount.get('split_criteria') == 'rsi':
                        settings_text += f"&nbsp;&nbsp;기준: RSI 기준 (레벨: {buy_amount.get('rsi_level1', 0)})<br>"
                        settings_text += f"&nbsp;&nbsp;방식: {buy_amount.get('rsi_amount1', 0)}개 / {buy_amount.get('rsi_amount2', 0)}번 진입<br>"
                    elif buy_amount.get('split_criteria') == 'price':
                        settings_text += f"&nbsp;&nbsp;기준: 가격 기준 (변동금액: {buy_amount.get('price_drop1', 0)}USDT)<br>"
                        settings_text += f"&nbsp;&nbsp;방식: {buy_amount.get('price_amount1', 0)}개 / {buy_amount.get('price_amount2', 0)}번 진입<br>"
                else:
                    settings_text += "분할매수: 사용안함<br>"
                
                settings_text += "<br>"
                
                # 매도 전략
                settings_text += "<span style='font-size: 18px; font-weight: bold;'>매도 전략</span><br>"
                take_profit = long_settings.get('take_profit', {})
                if take_profit.get('type') == 'rate':
                    settings_text += f"익절: {take_profit.get('rate', 0.0)}% 이익 시<br>"
                elif take_profit.get('type') == 'indicator':
                    settings_text += f"익절: 포지션 대비 {take_profit.get('indicator', 0)} USDT 상승 시<br>"
                    
                stop_loss = long_settings.get('stop_loss', {})
                if stop_loss.get('type') == 'rate':
                    settings_text += f"손절: {stop_loss.get('rate', 0.0)}% 손실 시<br>"
                elif stop_loss.get('type') == 'indicator':
                    settings_text += f"손절: 포지션 대비 {stop_loss.get('indicator', 0)} USDT 하락 시<br>"
                
                settings_text += "<br>"
            
            # 숏 포지션 설정 정보 (동일한 형식으로 구성)
            if "short_settings" in settings_data:
                short_settings = settings_data["short_settings"]
                settings_text += "<h4>▶ 숏 포지션 설정</h4>"
                settings_text += f"코인: {short_settings.get('coin_selection', '설정 없음')}<br><br>"
                
                # 시그널1 정보
                signal1 = short_settings.get('signal1', {})
                settings_text += "<span style='font-size: 18px; font-weight: bold;'>진입 시그널1: </span>"
                settings_text += f"<span style='color: red; font-size: 18px; font-weight: bold;'>{signal1.get('type', '없음')}</span><br>"
                settings_text += f"봉 타입: {signal1.get('timeframe', '없음')}<br>"
                signal1_option = signal1.get('settings', {}).get('option', 1)
                settings_text += f"옵션 {signal1_option}: {self.get_signal_option_text(signal1.get('type', ''), signal1_option, signal1.get('settings', {}), is_short=True)}<br><br>"
                
                # 시그널2 정보
                signal2 = short_settings.get('signal2', {})
                settings_text += "<span style='font-size: 18px; font-weight: bold;'>진입 시그널2: </span>"
                settings_text += f"<span style='color: red; font-size: 18px; font-weight: bold;'>{signal2.get('type', '없음')}</span><br>"
                settings_text += f"봉 타입: {signal2.get('timeframe', '없음')}<br>"
                signal2_option = signal2.get('settings', {}).get('option', 1)
                settings_text += f"옵션 {signal2_option}: {self.get_signal_option_text(signal2.get('type', ''), signal2_option, signal2.get('settings', {}), is_short=True)}<br><br>"
                
                # 매수 전략
                settings_text += "<span style='font-size: 18px; font-weight: bold;'>매수 전략</span><br>"
                buy_amount = short_settings.get('buy_amount', {})
                settings_text += f"진입수량: {buy_amount.get('base_amount', 0)}개<br>"
                settings_text += f"레버리지: {buy_amount.get('leverage', 1)}x<br>"
                
                if buy_amount.get('use_split', False):
                    settings_text += "분할매수: 사용함<br>"
                    if buy_amount.get('split_criteria') == 'rsi':
                        settings_text += f"&nbsp;&nbsp;기준: RSI 기준 (레벨: {buy_amount.get('rsi_level1', 0)})<br>"
                        settings_text += f"&nbsp;&nbsp;방식: {buy_amount.get('rsi_amount1', 0)}개 / {buy_amount.get('rsi_amount2', 0)}번 진입<br>"
                    elif buy_amount.get('split_criteria') == 'price':
                        settings_text += f"&nbsp;&nbsp;기준: 가격 기준 (변동금액: {buy_amount.get('price_drop1', 0)}USDT)<br>"
                        settings_text += f"&nbsp;&nbsp;방식: {buy_amount.get('price_amount1', 0)}개 / {buy_amount.get('price_amount2', 0)}번 진입<br>"
                else:
                    settings_text += "분할매수: 사용안함<br>"
                
                settings_text += "<br>"
                
                # 매도 전략
                settings_text += "<span style='font-size: 18px; font-weight: bold;'>매도 전략</span><br>"
                take_profit = short_settings.get('take_profit', {})
                if take_profit.get('type') == 'rate':
                    settings_text += f"익절: {take_profit.get('rate', 0.0)}% 이익 시<br>"
                elif take_profit.get('type') == 'indicator':
                    settings_text += f"익절: 포지션 대비 {take_profit.get('indicator', 0)} USDT 상승 시<br>"
                    
                stop_loss = short_settings.get('stop_loss', {})
                if stop_loss.get('type') == 'rate':
                    settings_text += f"손절: {stop_loss.get('rate', 0.0)}% 손실 시<br>"
                elif stop_loss.get('type') == 'indicator':
                    settings_text += f"손절: 포지션 대비 {stop_loss.get('indicator', 0)} USDT 하락 시<br>"
                
                settings_text += "<br>"
            
            settings_text += "</body></html>"
            
            # HTML 텍스트를 QTextEdit에 설정
            self.setting_text.setHtml(settings_text)
            
        except Exception as e:
            self.setting_text.setText(f"설정 정보 로드 중 오류 발생: {str(e)}")
            
    def start_trading(self):
        """매매 시작"""
        # 메인 윈도우에서 현재 활성화된 설정 탭 확인 (롱/숏)
        if hasattr(self.parent, 'tabWidget_main'):
            current_tab_index = self.parent.tabWidget_main.currentIndex()
            
            # 0:롱, 1:숏 (UI 구조에 따라 조정 필요)
            if current_tab_index == 0 and hasattr(self.parent, 'settings_long_tab'):
                # 롱 포지션 설정 사용
                settings = self.parent.settings_long_tab.settings
                
                # 최신 UI 값으로 설정 객체 업데이트
                self.parent.settings_long_tab.update_settings_from_ui()
                
                # 시작 전 설정 정보 업데이트
                self.load_settings_overview()
                
                print("롱 포지션 매매를 시작합니다.")
                print(settings.to_text())
                
            elif current_tab_index == 1 and hasattr(self.parent, 'settings_short_tab'):
                # 숏 포지션 설정 사용
                settings = self.parent.settings_short_tab.settings
                
                # 최신 UI 값으로 설정 객체 업데이트
                self.parent.settings_short_tab.update_settings_from_ui()
                
                # 시작 전 설정 정보 업데이트
                self.load_settings_overview()
                
                print("숏 포지션 매매를 시작합니다.")
                print(settings.to_text())
                
            else:
                print("활성화된 설정 탭을 찾을 수 없습니다.")
        else:
            print("매매 시작")
        
        # 가격 업데이트 시작
        if not self.price_timer.isActive():
            self.price_timer.start(5000)
        
    def stop_trading(self):
        print("매매 중지")
        # 가격 업데이트 중지 (선택사항)
        # self.price_timer.stop()

    def update_settings_display(self):
        """설정 정보를 다시 로드하여 표시 업데이트"""
        self.load_settings_overview()

    def update_price_data(self):
        """Bybit API에서 BTC 및 ETH 선물 가격 정보를 가져와 테이블 업데이트"""
        try:
            # 코인별 정보를 저장할 딕셔너리
            coin_prices = {}
            
            # 가져올 코인 심볼 리스트
            symbols = ["BTCUSDT", "ETHUSDT"]
            
            for symbol in symbols:
                # Bybit API 엔드포인트
                url = "https://api.bybit.com/v5/market/tickers"
                params = {"category": "linear", "symbol": symbol}
                
                # API 요청
                response = requests.get(url, params=params)
                data = response.json()
                
                if data["retCode"] == 0 and data["result"]["list"]:
                    ticker_data = data["result"]["list"][0]
                    # 소수점 1자리까지만 표시
                    price = f"{float(ticker_data['lastPrice']):.1f}"
                    coin = symbol.replace("USDT", "")  # "BTC" 또는 "ETH"
                    coin_prices[coin] = price
            
            # 테이블에 가격 업데이트
            # BTC는 1행(인덱스 0), ETH는 2행(인덱스 1)에 표시
            row_map = {"BTC": 0, "ETH": 1}
            
            for coin, price in coin_prices.items():
                if coin in row_map:
                    row = row_map[coin]
                    
                    # 코인명이 없으면 추가
                    if not self.coin_table.item(row, 0):
                        coin_item = QTableWidgetItem(coin)
                        coin_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                        self.coin_table.setItem(row, 0, coin_item)
                    
                    # 가격 업데이트 (4열 = 인덱스 3)
                    price_item = QTableWidgetItem(price)
                    price_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    
                    # 가격 변동에 따른 색상 처리
                    if coin in self.previous_prices:
                        prev_price = float(self.previous_prices[coin])
                        current_price = float(price)
                        
                        if current_price > prev_price:
                            # 가격 상승 - 녹색
                            price_item.setForeground(QBrush(QColor("green")))
                        elif current_price < prev_price:
                            # 가격 하락 - 빨간색
                            price_item.setForeground(QBrush(QColor("red")))
                    
                    self.coin_table.setItem(row, 4, price_item)
                    
                    # 현재 가격을 이전 가격으로 저장
                    self.previous_prices[coin] = price
                    
        except Exception as e:
            print(f"가격 데이터 업데이트 중 오류: {str(e)}")
