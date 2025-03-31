from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtCore import QUrl
#from PyQt6.QtWebEngineWidgets import QWebEngineView

class WebViewTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setup_ui()
        self.load_tradingview()
        
    def setup_ui(self):
        # 웹 엔진 뷰 참조
        self.webview = self.parent.webEngineView
        
        # JavaScript 활성화 
        self.webview.settings().setAttribute(
            self.webview.settings().WebAttribute.JavascriptEnabled, True
        )
        
    def load_tradingview(self):
        """트레이딩뷰 차트 로드"""
        # 트레이딩뷰 URL 설정
        tradingview_url = "https://kr.tradingview.com/chart/Fozj1uf6/?symbol=BINANCE%3ABTCUSDT"
        self.webview.load(QUrl(tradingview_url))
        
        # 개발자 도구 활성화 (디버깅용)
        self.webview.settings().setAttribute(
            self.webview.settings().WebAttribute.DeveloperExtrasEnabled, True
        )
        
    def refresh_chart(self):
        """차트 새로고침"""
        self.webview.reload()
