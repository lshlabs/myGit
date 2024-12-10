import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from MainWindow_ui import Ui_MainWindow  # 파일 이름과 일치하도록 수정

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # 여기에 버튼 클릭 등의 이벤트 핸들러를 추가할 수 있습니다
        # 예: self.ui.Button_plus1.clicked.connect(self.button_clicked)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())