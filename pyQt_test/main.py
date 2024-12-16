import sys
import os
import resource_rc
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from ui.MainWindow_ui import Ui_MainWindow
from dialogs.image_dialog import ImageDialog
from dialogs.settings_dialog import SettingsDialog
from utils import (get_data_file_path, load_json_data, save_json_data, 
                  get_relative_path, get_absolute_path)

# 배달앱 정보
baemin = {"text": "배달의 민족", "color": "#45D3D3"}
yogiyo = {"text": "요기요", "color": "#FA0150"}
manna = {"text": "만나", "color": "#ff6b00"}

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.data_file = get_data_file_path()
        
        # settings 아이콘 설정
        settings_icon = QPixmap(":/img/settings.png")
        self.ui.label_settings_icon.setPixmap(settings_icon)
        self.ui.label_settings_icon.setScaledContents(True)
        self.ui.label_settings_icon.mousePressEvent = self.show_settings_dialog
        self.ui.label_settings_icon.setCursor(Qt.PointingHandCursor)

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
        
        # 초기 화면 설정
        self.show_menu('menu2')
        
        # 메뉴 클릭 이벤트 연결
        self.ui.label_menu2.mousePressEvent = lambda e: self.show_menu('menu2')
        self.ui.label_menu3.mousePressEvent = lambda e: self.show_menu('menu3')
        self.ui.label_menu6.mousePressEvent = lambda e: self.show_menu('menu6')

        # 이미지 프레임 클릭 이벤트 연결
        for i in range(1, 7):
            frame = getattr(self.ui, f'frame_image{i}')
            frame.mousePressEvent = lambda e, f=frame: self.show_image_dialog(f)

        # 버튼 클릭 이벤트 연결
        self.ui.button_plus1.clicked.connect(lambda: self.update_entry_value(1, True))
        self.ui.button_minus1.clicked.connect(lambda: self.update_entry_value(1, False))
        self.ui.button_plus2.clicked.connect(lambda: self.update_entry_value(2, True))
        self.ui.button_minus2.clicked.connect(lambda: self.update_entry_value(2, False))
        self.ui.button_on.clicked.connect(self.on_button_on_clicked)
        self.ui.button_off.clicked.connect(self.on_button_off_clicked)

        # entry 초기값 설정
        data = load_json_data(self.data_file)
        if data:
            self.ui.entry1.setText(str(data['menu2']['entry1']))
            self.ui.entry2.setText(str(data['menu2']['entry2']))

    def create_data_file(self):
        """초기 이미지 데이터 파일 생성"""
        initial_data = {
            'settings': {
                'combobox_value': '0',
                'checkbox_state': False
            },
            'menu2': {
                'frame_image1': None,
                'frame_image2': None,
                'frame_image3': None,
                'entry1': 50,
                'entry2': 15,
                'button_state': 'off',
                'frame_color': "background:rgb(206, 208, 208)"
            },
            'menu3': {
                'frame_image1': None,
                'frame_image2': None,
                'frame_image3': None,
                'entry1': 50,
                'entry2': 15,
                'button_state': 'off',
                'frame_color': "background:rgb(206, 208, 208)"
            },
            'menu6': {
                'frame_image1': None,
                'frame_image2': None,
                'frame_image3': None,
                'frame_image4': None,
                'frame_image5': None,
                'frame_image6': None,
                'entry1': 50,
                'entry2': 15,
                'button_state': 'off',
                'frame_color': "background:rgb(206, 208, 208)"
            }
        }
        save_json_data(self.data_file, initial_data)

    def load_image_data(self):
        """이미지 데이터 로드"""
        data = load_json_data(self.data_file)
        if data:
            for menu in ['menu2', 'menu3', 'menu6']:
                for frame_name in data[menu]:
                    if frame_name.startswith('frame_'):
                        image_path = data[menu][frame_name]
                        absolute_path = get_absolute_path(image_path)
                        if absolute_path and os.path.exists(absolute_path):
                            pixmap = QPixmap(absolute_path)
                            self.menu_pixmaps[menu][frame_name] = pixmap.scaled(
                                120, 120, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
                        else:
                            self.menu_pixmaps[menu][frame_name] = None

    def show_menu(self, menu_name):
        """메뉴 표시 통합 메서드"""
        current_menu = self.get_current_menu()
        if current_menu != menu_name:
            current_state = 'on' if self.ui.button_on.isVisible() else 'off'
            self.save_button_state(current_menu, current_state, self.ui.frame_title.styleSheet())
        
        # 메뉴별 설정
        settings = {
            'menu2': {'frames': ['frame_image1', 'frame_image2', 'frame_image3'], 'y_pos': 190},
            'menu3': {'frames': ['frame_image1', 'frame_image2', 'frame_image3'], 'y_pos': 190},
            'menu6': {'frames': ['frame_image1', 'frame_image2', 'frame_image3',
                               'frame_image4', 'frame_image5', 'frame_image6'], 'y_pos': 350}
        }[menu_name]
        
        # UI 업데이트
        self.update_menu_display(menu_name, settings)

    def update_menu_display(self, menu_name, settings):
        """메뉴 화면 업데이트"""
        # Setting 프레임 설정
        self.ui.Setting_frame.show()
        self.ui.Setting_frame.setGeometry(43, settings['y_pos'], 460, 171)
        
        # 타이틀 변경
        self.ui.label_title.setText(getattr(self.ui, f'label_{menu_name}').text())
        
        # 이미지 프레임 표시/숨기기
        all_frames = [f'frame_image{i}' for i in range(1, 7)]
        for frame_name in all_frames:
            frame = getattr(self.ui, frame_name)
            label = getattr(self.ui, frame_name.replace('frame_', 'label_'))
            
            if frame_name in settings['frames']:
                if self.menu_pixmaps[menu_name][frame_name]:
                    frame.setPixmap(self.menu_pixmaps[menu_name][frame_name])
                    frame.setStyleSheet("background: transparent; border: 1px solid black;")
                else:
                    frame.clear()
                    frame.setStyleSheet("background:rgb(206, 208, 208);\nborder:1px solid black;")
                frame.show()
                label.show()
            else:
                frame.hide()
                label.hide()
        
        # 메뉴 스타일 변경
        for m in ['menu2', 'menu3', 'menu6']:
            style = "background:rgb(206, 208, 208);\ncolor: white;\nborder: none;" if m == menu_name else \
                   "background-color:rgb(255, 255, 255);\ncolor: black;\nborder: none;"
            getattr(self.ui, f'label_{m}').setStyleSheet(style)

        # entry 값과 버튼 상태 로드
        data = load_json_data(self.data_file)
        if data:
            self.ui.entry1.setText(str(data[menu_name]['entry1']))
            self.ui.entry2.setText(str(data[menu_name]['entry2']))
        self.load_button_state(menu_name)

    def update_entry_value(self, entry_number, increment=True):
        """entry 값 업데이트 통합 메서드"""
        entry = getattr(self.ui, f'entry{entry_number}')
        current_value = int(entry.text())
        new_value = current_value + (5 if increment else -5)
        entry.setText(str(new_value))
        
        current_menu = self.get_current_menu()
        data = load_json_data(self.data_file)
        if data:
            data[current_menu][f'entry{entry_number}'] = new_value
            save_json_data(self.data_file, data)


    def get_current_menu(self):
        """현재 선택된 메뉴 반환"""
        if self.ui.label_menu3.styleSheet().find("background:rgb(206, 208, 208)") != -1:
            return 'menu3'
        elif self.ui.label_menu6.styleSheet().find("background:rgb(206, 208, 208)") != -1:
            return 'menu6'
        return 'menu2'

    def save_button_state(self, current_menu, state, color):
        """버튼 상태와 프레임 색상 저장"""
        data = load_json_data(self.data_file)
        if data:
            data[current_menu]['button_state'] = state
            data[current_menu]['frame_color'] = color
            save_json_data(self.data_file, data)

    def load_button_state(self, menu):
        """버튼 상태와 프레임 색상 로드"""
        data = load_json_data(self.data_file)
        if not data:
            return
            
        state = data[menu]['button_state']
        
        if state == 'off':  # OFF 상태
            self.ui.button_off.show()
            self.ui.button_on.hide()
            self.ui.frame_title.setStyleSheet("background:rgb(206, 208, 208)")
        else:  # ON 상태
            self.ui.button_on.show()
            self.ui.button_off.hide()
            # 메뉴별 색상 적용
            colors = {
                'menu2': baemin['color'],
                'menu3': yogiyo['color'],
                'menu6': manna['color']
            }
            self.ui.frame_title.setStyleSheet(f"background:{colors[menu]}")

    def on_button_on_clicked(self):
        """ON 버튼 클릭 (ON -> OFF)"""
        current_menu = self.get_current_menu()
        self.ui.button_off.show()
        self.ui.button_on.hide()
        color = "background:rgb(206, 208, 208)"
        self.ui.frame_title.setStyleSheet(color)
        self.save_button_state(current_menu, 'off', color)

    def on_button_off_clicked(self):
        """OFF 버튼 클릭 (OFF -> ON)"""
        current_menu = self.get_current_menu()
        self.ui.button_on.show()
        self.ui.button_off.hide()
        
        colors = {
            'menu2': baemin['color'],
            'menu3': yogiyo['color'],
            'menu6': manna['color']
        }
        color = f"background:{colors[current_menu]}"
        self.ui.frame_title.setStyleSheet(color)
        self.save_button_state(current_menu, 'on', color)

    def show_image_dialog(self, frame):
        """이미지 선택 다이얼로그 표시"""
        dialog = ImageDialog(self)
        current_menu = self.get_current_menu()
        frame_name = frame.objectName()
        
        if frame.pixmap() and not frame.pixmap().isNull():
            dialog.set_preview_image(frame.pixmap())
            data = load_json_data(self.data_file)
            if data:
                current_path = data[current_menu][frame_name]
                if current_path:
                    dialog.selected_file_path = get_absolute_path(current_path)
        
        if dialog.exec() == QDialog.Accepted:
            if dialog.reset_requested:
                # 이미지 초기화
                frame.clear()
                frame.setStyleSheet("background:rgb(206, 208, 208);\nborder:1px solid black;")
                self.menu_pixmaps[current_menu][frame_name] = None
                
                # JSON 파일 업데이트
                data = load_json_data(self.data_file)
                if data:
                    data[current_menu][frame_name] = None
                    save_json_data(self.data_file, data)
            
            elif dialog.selected_pixmap:
                # 새 이미지 설정
                frame.setPixmap(dialog.selected_pixmap)
                frame.setStyleSheet("background: transparent;\nborder:1px solid black;")
                self.menu_pixmaps[current_menu][frame_name] = dialog.selected_pixmap
                
                # JSON 파일 업데이트
                relative_path = get_relative_path(dialog.selected_file_path)
                data = load_json_data(self.data_file)
                if data:
                    data[current_menu][frame_name] = relative_path
                    save_json_data(self.data_file, data)

    def show_settings_dialog(self, event):
        """설정 다이얼로그 표시"""
        dialog = SettingsDialog(self)
        dialog.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())