import sys
import json
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel, QDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from MainWindow_ui import Ui_MainWindow
from ImageDialog_ui import Ui_ImageDialog

class ImageDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ImageDialog()
        self.ui.setupUi(self)
        
        # QLabel 클릭 이벤트 연결
        self.ui.preview_label.mousePressEvent = self.select_image
        
        # 버튼 이벤트 연결
        self.ui.apply_button.clicked.connect(self.accept)
        self.ui.cancel_button.clicked.connect(self.reject)
        self.ui.reset_button.clicked.connect(self.reset_image)
        
        self.selected_pixmap = None
        self.selected_file_path = None
        self.reset_requested = False  # reset 요청 여부를 추적하는 플래그
        
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
            
            # 원본 이미지의 비율을 유지하면서 preview_label 크기에 맞게 조절
            label_size = self.ui.preview_label.size()
            scaled_pixmap = original_pixmap.scaled(
                label_size,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
            
            # 미리보기용 이미지는 라벨 크기에 맞게 표시
            self.ui.preview_label.setPixmap(scaled_pixmap)
            
            # 실제 저장/사용될 이미지는 120x120으로 유지
            self.selected_pixmap = original_pixmap.scaled(
                120, 120,
                Qt.IgnoreAspectRatio,
                Qt.SmoothTransformation
            )
    
    def reset_image(self):
        """이미지 초기화"""
        self.selected_pixmap = None
        self.selected_file_path = None
        self.reset_requested = True  # reset 플래그 설정
        self.ui.preview_label.clear()
        self.ui.preview_label.setText("이미지를 선택하세요")  # 기본 텍스트 다시 설정

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # 현재 파일의 디렉토리 경로를 가져와서 데이터 파일 경로 설정
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.data_file = os.path.join(current_dir, 'image_data.json')
        
        # 각 메뉴별 이미지 저장 딕셔너리 초기화
        self.menu_pixmaps = {
            'menu2': {},
            'menu3': {},
            'menu6': {}
        }
        
        # 데이터 파일이 없으면 생성
        if not os.path.exists(self.data_file):
            self.create_data_file()
            
        # 이미지 데이터 로드
        self.load_image_data()
        
        # 초기 화면 설정 (menu2와 동일하게)
        self.show_menu2()
        
        # 메뉴 클릭 이벤트 연결
        self.ui.label_menu2.mousePressEvent = lambda e: self.show_menu2()
        self.ui.label_menu3.mousePressEvent = lambda e: self.show_menu3()
        self.ui.label_menu6.mousePressEvent = lambda e: self.show_menu6()

        # 이미지 프레임 클릭 이벤트 연결
        self.ui.frame_image1.mousePressEvent = lambda e: self.show_image_dialog(self.ui.frame_image1)
        self.ui.frame_image2.mousePressEvent = lambda e: self.show_image_dialog(self.ui.frame_image2)
        self.ui.frame_image3.mousePressEvent = lambda e: self.show_image_dialog(self.ui.frame_image3)
        self.ui.frame_image4.mousePressEvent = lambda e: self.show_image_dialog(self.ui.frame_image4)
        self.ui.frame_image5.mousePressEvent = lambda e: self.show_image_dialog(self.ui.frame_image5)
        self.ui.frame_image6.mousePressEvent = lambda e: self.show_image_dialog(self.ui.frame_image6)

    def create_data_file(self):
        """초기 이미지 데이터 파일 생성"""
        initial_data = {
            'menu2': {
                'frame_image1': None,
                'frame_image2': None,
                'frame_image3': None
            },
            'menu3': {
                'frame_image1': None,
                'frame_image2': None,
                'frame_image3': None
            },
            'menu6': {
                'frame_image1': None,
                'frame_image2': None,
                'frame_image3': None,
                'frame_image4': None,
                'frame_image5': None,
                'frame_image6': None
            }
        }
        
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(initial_data, f, ensure_ascii=False, indent=2)

    def load_image_data(self):
        """이미지 데이터 로드"""
        with open(self.data_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
            # 각 메뉴의 이미지 경로를 QPixmap으로 변환하여 저장
            for menu in ['menu2', 'menu3', 'menu6']:
                for frame_name, image_path in data[menu].items():
                    absolute_path = self.get_absolute_path(image_path)
                    if absolute_path and os.path.exists(absolute_path):
                        pixmap = QPixmap(absolute_path)
                        self.menu_pixmaps[menu][frame_name] = pixmap.scaled(
                            120, 120, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
                    else:
                        self.menu_pixmaps[menu][frame_name] = None

    def get_relative_path(self, absolute_path):
        """절대 경로를 상대 경로로 변환"""
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            relative_path = os.path.relpath(absolute_path, current_dir)
            # Windows에서도 항상 forward slash(/)를 사용하도록 변환
            return relative_path.replace(os.path.sep, '/')
        except ValueError:
            # 다른 드라이브에 있는 경우 등 상대 경로를 만들 수 없는 경우
            return absolute_path

    def get_absolute_path(self, relative_path):
        """상대 경로를 절대 경로로 변환"""
        if not relative_path:
            return None
        # forward slash를 시스템 경로 구분자로 변환
        relative_path = relative_path.replace('/', os.path.sep)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(current_dir, relative_path)

    def show_menu2(self):
        # menu2 화면 설정 - 이미지 프레임 1~3만 표시
        self.ui.Setting_frame.show()
        self.ui.Setting_frame.setGeometry(43, 190, 460, 171)  # 설정 프레임 위치를 위로 이동
        
        # 타이틀 변경 - menu2의 텍스트를 가져와서 설정
        self.ui.label_title.setText(self.ui.label_menu2.text())
        
        # 스크롤 영역과 내용물 크기 조절 및 스크롤바 비활성화
        self.ui.scrollAreaWidgetContents.setFixedHeight(390)  # 3개 이미지용
        
        # menu2의 이미지 표시
        for frame_name in ['frame_image1', 'frame_image2', 'frame_image3']:
            frame = getattr(self.ui, frame_name)
            if self.menu_pixmaps['menu2'][frame_name]:
                frame.setPixmap(self.menu_pixmaps['menu2'][frame_name])
                frame.setStyleSheet("background: transparent; border: 1px solid black;")
            else:
                frame.clear()
                frame.setStyleSheet("background:rgb(206, 208, 208);\nborder:1px solid black;")
            frame.show()
            getattr(self.ui, frame_name.replace('frame_', 'label_')).show()
        
        # 나머지 프레임 숨기기
        for frame_name in ['frame_image4', 'frame_image5', 'frame_image6']:
            getattr(self.ui, frame_name).hide()
            getattr(self.ui, frame_name.replace('frame_', 'label_')).hide()
        
        # 메뉴 스타일 변경
        self.ui.label_menu2.setStyleSheet("background:rgb(206, 208, 208);\ncolor: white;\nborder: none;")
        self.ui.label_menu3.setStyleSheet("background-color:rgb(255, 255, 255);\ncolor: black;\nborder: none;")
        self.ui.label_menu6.setStyleSheet("background-color:rgb(255, 255, 255);\ncolor: black;\nborder: none;")

    def show_menu3(self):
        # menu3 화면 설정 - 이미지 프레임 1~3만 표시
        self.ui.Setting_frame.show()
        self.ui.Setting_frame.setGeometry(43, 190, 460, 171)  # 설정 프레임 위치를 위로 이동
        
        # 타이틀 변경 - menu3의 텍스트를 가져와서 설정
        self.ui.label_title.setText(self.ui.label_menu3.text())
        
        # menu3의 이미지 표시
        for frame_name in ['frame_image1', 'frame_image2', 'frame_image3']:
            frame = getattr(self.ui, frame_name)
            if self.menu_pixmaps['menu3'][frame_name]:
                frame.setPixmap(self.menu_pixmaps['menu3'][frame_name])
                frame.setStyleSheet("background: transparent; border: 1px solid black;")
            else:
                frame.clear()
                frame.setStyleSheet("background:rgb(206, 208, 208);\nborder:1px solid black;")
            frame.show()
            getattr(self.ui, frame_name.replace('frame_', 'label_')).show()
        
        # 나머지 프레임 숨기기
        for frame_name in ['frame_image4', 'frame_image5', 'frame_image6']:
            getattr(self.ui, frame_name).hide()
            getattr(self.ui, frame_name.replace('frame_', 'label_')).hide()
        
        # 메뉴 스타일 변경
        self.ui.label_menu2.setStyleSheet("background-color:rgb(255, 255, 255);\ncolor: black;\nborder: none;")
        self.ui.label_menu3.setStyleSheet("background:rgb(206, 208, 208);\ncolor: white;\nborder: none;")
        self.ui.label_menu6.setStyleSheet("background-color:rgb(255, 255, 255);\ncolor: black;\nborder: none;")

        # 스크롤 영역 내용물 크기 조절
        self.ui.scrollAreaWidgetContents.setFixedHeight(390)  # 3개 이미지용

    def show_menu6(self):
        # menu6 화면 설정 - 모든 이미지 프레임(1~6) 표시
        self.ui.Setting_frame.show()
        self.ui.Setting_frame.setGeometry(43, 350, 460, 171)  # 설정 프레임 원래 위치로 복귀
        
        # 타이틀 변경 - menu6의 텍스트를 가져와서 설정
        self.ui.label_title.setText(self.ui.label_menu6.text())
        
        # menu6의 이미지 표시
        for frame_name in ['frame_image1', 'frame_image2', 'frame_image3',
                          'frame_image4', 'frame_image5', 'frame_image6']:
            frame = getattr(self.ui, frame_name)
            if self.menu_pixmaps['menu6'][frame_name]:
                frame.setPixmap(self.menu_pixmaps['menu6'][frame_name])
                frame.setStyleSheet("background: transparent; border: 1px solid black;")
            else:
                frame.clear()
                frame.setStyleSheet("background:rgb(206, 208, 208);\nborder:1px solid black;")
            frame.show()
            getattr(self.ui, frame_name.replace('frame_', 'label_')).show()
        
        # 메뉴 스타일 변경
        self.ui.label_menu2.setStyleSheet("background-color:rgb(255, 255, 255);\ncolor: black;\nborder: none;")
        self.ui.label_menu3.setStyleSheet("background-color:rgb(255, 255, 255);\ncolor: black;\nborder: none;")
        self.ui.label_menu6.setStyleSheet("background:rgb(206, 208, 208);\ncolor: white;\nborder: none;")

        # 스크롤 영역 내용물 크기 조절
        self.ui.scrollAreaWidgetContents.setFixedHeight(540)  # 6개 이미지용

    def show_image_dialog(self, frame):
        dialog = ImageDialog(self)
        frame_name = frame.objectName()
        
        # 현재 메뉴 확인
        current_menu = 'menu2'
        if self.ui.label_menu3.styleSheet().find("background:rgb(206, 208, 208)") != -1:
            current_menu = 'menu3'
        elif self.ui.label_menu6.styleSheet().find("background:rgb(206, 208, 208)") != -1:
            current_menu = 'menu6'
        
        # 저장된 이미지가 있다면 다이얼로그에 표시
        if self.menu_pixmaps[current_menu][frame_name]:
            dialog.selected_pixmap = self.menu_pixmaps[current_menu][frame_name]
            dialog.ui.preview_label.setPixmap(self.menu_pixmaps[current_menu][frame_name])
        
        if dialog.exec() == QDialog.Accepted:
            if dialog.reset_requested:
                # 리셋 요청이 있는 경우
                frame.clear()
                self.menu_pixmaps[current_menu][frame_name] = None
                frame.setStyleSheet("background:rgb(206, 208, 208);\nborder:1px solid black;")
                
                # JSON 파일에서 이미지 경로 삭제
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                data[current_menu][frame_name] = None
                with open(self.data_file, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
            
            elif dialog.selected_pixmap:
                # 새 이미지가 선택된 경우
                frame.setPixmap(dialog.selected_pixmap)
                self.menu_pixmaps[current_menu][frame_name] = dialog.selected_pixmap
                frame.setStyleSheet("background: transparent; border: 1px solid black;")
                
                # JSON 파일 업데이트
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                data[current_menu][frame_name] = self.get_relative_path(dialog.selected_file_path)
                with open(self.data_file, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())