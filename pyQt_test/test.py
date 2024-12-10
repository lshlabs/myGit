from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("첫 번째 Qt 앱")
        button = QPushButton("클릭하세요!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self):
        print("버튼이 클릭되었습니다!")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
