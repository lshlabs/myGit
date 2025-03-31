from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic
import sys
import os

from tabs.trading_tab import TradingTab
from tabs.settings_long_tab import SettingsLongTab
from tabs.settings_short_tab import SettingsShortTab
from tabs.profits_tab import ProfitsTab
from tabs.auth_tab import AuthTab
from tabs.coordin_tab import CoordinTab
#from tabs.webview_tab import WebViewTab

UI_PATH = os.path.join(os.path.dirname(__file__), "ui", "main.ui")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # UI 파일 로드
        uic.loadUi(UI_PATH, self)
        
        # 탭 위젯의 각 페이지를 커스텀 클래스로 교체
        self.tab_trading = TradingTab(self)
        self.tab_settings_long = SettingsLongTab(self)
        self.tab_settings_short = SettingsShortTab(self)
        self.tab_profits = ProfitsTab(self)
        self.tab_auth = AuthTab(self)
        self.coordin_tab = CoordinTab(self)
        #self.webview_tab = WebViewTab(self)
        
        # 현재 탭 설정
        self.tabWidget.setCurrentWidget(self.tab_trading)
        
        # 버튼 연결
        self.btn_all_coins.clicked.connect(self.liquidate_all_positions)
        
    def liquidate_all_positions(self):
        print("모든 포지션 청산")
        self.status_label.setText("포지션 청산 중...")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
