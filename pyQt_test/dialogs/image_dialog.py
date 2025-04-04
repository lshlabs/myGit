import os
from PySide6.QtWidgets import QDialog, QFileDialog, QLineEdit
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPixmap, QKeyEvent, QCursor
from PySide6.QtWidgets import QApplication
from ui.ImageDialog_ui import Ui_ImageDialog
from pynput import mouse
import resource_rc
from utils import load_json_data, save_json_data, get_data_file_path

# 상수 정의
THUMBNAIL_SIZE = (120, 120)  # 썸네일 이미지 크기

class ImageDialog(QDialog):
    def __init__(self, parent=None, menu_name=None, image_number=None):
        super().__init__(parent)
        self.ui = Ui_ImageDialog()
        self.ui.setupUi(self)
        
        self.setFixedSize(self.width(), self.height())
        
        # 메뉴 이름과 이미지 번호 저장
        self.menu_name = menu_name
        self.image_number = image_number
        
        # 저장된 이미지 이름 불러오기
        data = load_json_data(get_data_file_path())
        if data and menu_name:
            saved_name = data[menu_name]['other_values'].get(f'frame_image{image_number}_name', '')
            self.ui.textEdit_img_name.setText(saved_name)
        
        self.ui.textEdit_img_name.setPlaceholderText("이미지 이름을 입력하세요")
        
        # tooltips설정
        self.ui.tooltip_1.setCursor(Qt.PointingHandCursor)
        tooltip_text = """
            <html style="font-family: Nanum Gothic; font-size: 12px;">
            <p></p>
            <h3 align="center">툴팁입니다</h3>
            <p> 1. 툴팁툴팁 </p>
            <p> 2. 툴팁툴팁툴팁툴팁툴팁툴팁툴팁툴팁툴팁툴팁툴팁툴팁 </p>
            <p> 3. 툴팁툴팁툴팁툴팁툴팁툴팁 </p>
            <p></p>
            </html>
        """
        self.ui.tooltip_1.setToolTip(tooltip_text)
        
        self.ui.tooltip_2.setCursor(Qt.PointingHandCursor)
        tooltip_text = """
            <html style="font-family: Nanum Gothic; font-size: 12px;">
            <p></p>
            <h3 align="center">툴팁입니다</h3>
            <p> 1. 툴팁툴팁 </p>
            <p> 2. 툴팁툴팁툴팁툴팁툴팁툴팁툴팁툴팁툴팁툴팁툴팁툴팁 </p>
            <p> 3. 툴팁툴팁툴팁툴팁툴팁툴팁 </p>
            <p></p>
            </html>
        """
        self.ui.tooltip_2.setToolTip(tooltip_text)
        
        # QLabel 클릭 이벤트 연결
        self.ui.preview_label.mousePressEvent = self.select_image
        
        # 버튼 이벤트 연결
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)
        self.ui.reset_button.clicked.connect(self.reset_image)
        
        # 좌표 기록 버튼
        self.ui.button_record1.clicked.connect(self.record_coordinate)
        self.ui.button_record2.clicked.connect(self.record_coordinate)
        
        self.selected_pixmap = None
        self.selected_file_path = None
        self.reset_requested = False
        
        # preview_label이 이미지를 자동으로 크기에 맞추도록 설정
        self.ui.preview_label.setScaledContents(True)
        
        self.recording = False
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_coordinates)
        
        # 모든 LineEdit에 이벤트 필터 설치
        self.ui.textEdit_img_name.installEventFilter(self)
        self.ui.textEdit_X1.installEventFilter(self)
        self.ui.textEdit_Y1.installEventFilter(self)
        self.ui.textEdit_X2.installEventFilter(self)
        self.ui.textEdit_Y2.installEventFilter(self)
        
        # 메인 윈도우에 이벤트 필터 설치 추가
        self.installEventFilter(self)
        
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
        self.ui.preview_label.setText("이곳을 클릭하여\n이미지를 선택하세요")
    
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
            
    def record_coordinate(self):
        """좌표기록 버튼 클릭이벤트"""
        sender = self.sender()
        current_button = 1 if sender == self.ui.button_record1 else 2
        
        # 이미 기록 중이고 같은 버튼을 눌렀다면 기록 취소
        if self.recording and self.active_button == current_button:
            self.recording = False
            sender.setText("기록 시작")
            self.timer.stop()
            return
        
        # 새로운 기록 시작
        self.recording = True
        self.active_button = current_button
        sender.setText("기록 중...")
        self.timer.start(50)
        
    def update_coordinates(self):
        """좌표 업데이트"""
        if self.recording:
            cursor_pos = QCursor.pos()
            # 활성화된 버튼에 따라 다른 텍스트 에디트 업데이트
            if self.active_button == 1:
                self.ui.textEdit_X1.setText(str(cursor_pos.x()))
                self.ui.textEdit_Y1.setText(str(cursor_pos.y()))
            else:
                self.ui.textEdit_X2.setText(str(cursor_pos.x()))
                self.ui.textEdit_Y2.setText(str(cursor_pos.y()))
    
    def eventFilter(self, obj, event):
        """이벤트 필터"""
        # 좌표 기록 중 F10 키 처리
        if self.recording and event.type() == event.Type.KeyPress:
            if event.key() == Qt.Key.Key_F10:
                self.recording = False
                # 활성화된 버튼 텍스트 복원
                if self.active_button:
                    getattr(self.ui, f'button_record{self.active_button}').setText("기록 시작")
                self.timer.stop()
                return True
            
        # LineEdit에서 엔터키 처리
        if isinstance(obj, QLineEdit) and event.type() == event.Type.KeyPress:
            if event.key() in [Qt.Key.Key_Return, Qt.Key.Key_Enter]:
                return True  # 엔터키 이벤트 무시
            
        return super().eventFilter(obj, event)
        
    def accept(self):
        """OK 버튼 클릭 시 호출되는 메서드"""
        if self.menu_name and self.image_number:
            data_file = get_data_file_path()
            data = load_json_data(data_file)
            
            if data:
                # 이미지 이름 저장
                img_name = self.ui.textEdit_img_name.text()
                
                # 첫 번째 좌표 저장
                x_coord1 = self.ui.textEdit_X1.text()
                y_coord1 = self.ui.textEdit_Y1.text()
                # 두 번째 좌표 저장
                x_coord2 = self.ui.textEdit_X2.text()
                y_coord2 = self.ui.textEdit_Y2.text()
                
                try:
                    # 이미지 이름 저장
                    if img_name:
                        data[self.menu_name]['other_values'][f'frame_image{self.image_number}_name'] = img_name
                    
                    # 첫 번째 좌표가 있는 경우 저장
                    if x_coord1 and y_coord1:
                        data[self.menu_name]['coordinates_active']['start_pos'][f'image{self.image_number}_x'] = int(x_coord1)
                        data[self.menu_name]['coordinates_active']['start_pos'][f'image{self.image_number}_y'] = int(y_coord1)
                    
                    # 두 번째 좌표가 있는 경우 저장
                    if x_coord2 and y_coord2:
                        data[self.menu_name]['coordinates_active']['end_pos'][f'image{self.image_number}_x'] = int(x_coord2)
                        data[self.menu_name]['coordinates_active']['end_pos'][f'image{self.image_number}_y'] = int(y_coord2)
                    
                    # 이미지가 없고 좌표가 모두 비어있는 경우 초기화
                    if not self.selected_pixmap and not (x_coord1 or y_coord1 or x_coord2 or y_coord2):
                        data[self.menu_name]['coordinates_active']['start_pos'][f'image{self.image_number}_x'] = 0
                        data[self.menu_name]['coordinates_active']['start_pos'][f'image{self.image_number}_y'] = 0
                        data[self.menu_name]['coordinates_active']['end_pos'][f'image{self.image_number}_x'] = 0
                        data[self.menu_name]['coordinates_active']['end_pos'][f'image{self.image_number}_y'] = 0
                    
                    save_json_data(data_file, data)
                except ValueError:
                    pass  # 숫자로 변환할 수 없는 경우 무시
        
        super().accept()
        