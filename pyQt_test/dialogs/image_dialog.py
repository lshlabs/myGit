import os
from PySide6.QtWidgets import QDialog, QFileDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from ui.ImageDialog_ui import Ui_ImageDialog
import resource_rc

# 상수 정의
THUMBNAIL_SIZE = (120, 120)  # 썸네일 이미지 크기

class ImageDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ImageDialog()
        self.ui.setupUi(self)
        
        # tooltips 아이콘 설정
        tooltips_icon = QPixmap(":/img/tooltips.png")
        self.ui.tool_tip.setPixmap(tooltips_icon)
        self.ui.tool_tip.setScaledContents(True)
        self.ui.tool_tip.setCursor(Qt.PointingHandCursor)
        tooltip_text = """
            <html>
            <h3>좌표 녹화 도움말</h3>
            <p>1. 녹화 버튼을 클릭하세요</p>
            <p>2. 해당 이미지가 있는 실제 화면상의 위치에 마우스를 올려주세요</p>
            <p>3. ESC 버튼을 누르면 좌표가 자동으로 채워집니다</p>
            </html>
        """
        self.ui.tool_tip.setToolTip(tooltip_text)
        
        # QLabel 클릭 이벤트 연결
        self.ui.preview_label.mousePressEvent = self.select_image
        
        # 버튼 이벤트 연결
        self.ui.apply_button.clicked.connect(self.accept)
        self.ui.cancel_button.clicked.connect(self.reject)
        self.ui.reset_button.clicked.connect(self.reset_image)
        
        self.selected_pixmap = None
        self.selected_file_path = None
        self.reset_requested = False
        
        # preview_label이 이미지를 자동으로 크기에 맞추도록 설정
        self.ui.preview_label.setScaledContents(True)
        
    def select_image(self, event):
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "이미지 선택",
            "",
            "Images (*.png *.xpm *.jpg *.bmp)"
        )
        
        if file_name:
            self.selected_file_path = file_name
            original_pixmap = QPixmap(file_name)
            
            label_size = self.ui.preview_label.size()
            scaled_pixmap = original_pixmap.scaled(
                label_size,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
            
            self.ui.preview_label.setPixmap(scaled_pixmap)
            
            self.selected_pixmap = original_pixmap.scaled(
                THUMBNAIL_SIZE[0], THUMBNAIL_SIZE[1],
                Qt.IgnoreAspectRatio,
                Qt.SmoothTransformation
            )
    
    def reset_image(self):
        """이미지 초기화"""
        self.selected_pixmap = None
        self.selected_file_path = None
        self.reset_requested = True
        self.ui.preview_label.clear()
        self.ui.preview_label.setText("이미지를 선택하세요")
    
    def set_preview_image(self, pixmap):
        """기존 이미지 미리보기 설정"""
        if pixmap:
            scaled_pixmap = pixmap.scaled(
                self.ui.preview_label.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
            self.ui.preview_label.setPixmap(scaled_pixmap)
            self.selected_pixmap = pixmap