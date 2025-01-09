import sys
import os
import resource_rc
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from ui.MainWindow_ui import Ui_MainWindow
from dialogs.image_dialog import ImageDialog
from dialogs.settings_dialog import SettingsDialog
from macro.macro_controller import MacroController
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
        
        # 데이터 파일이 없으면 생성
        if not os.path.exists(self.data_file):
            self.create_data_file()  # 데이터 파일 생성
        
        # MacroController 인스턴스 생성
        self.macro_controller = MacroController(self.data_file, self)  # MainWindow 인스턴스 전달
        
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
            self.ui.entry1.setText(str(data['menu2']['other_values']['entry1']))
            self.ui.entry2.setText(str(data['menu2']['other_values']['entry2']))

       

    def create_data_file(self):
        """초기 데이터 파일 생성"""
        initial_data = {
            'menu2': {
                'settings': {
                    'combo_run_value': '0',
                    'check_ctrl1_state': False,
                    'check_alt1_state': False,
                    'check_shift1_state': False,
                    'combo_stop_value': '0',
                    'check_ctrl2_state': False,
                    'check_alt2_state': False,
                    'check_shift2_state': False,
                },
                'other_values': {
                    'frame_image1': None,
                    'frame_image2': None,
                    'frame_image3': None,
                    'entry1': 50,
                    'entry2': 15,
                    'button_state': 'off',
                    'frame_color': "#CED0D0"  # RGB(206, 208, 208) -> HEX
                }
            },
            'menu3': {
                'settings': {
                    'combo_run_value': '0',
                    'check_ctrl1_state': False,
                    'check_alt1_state': False,
                    'check_shift1_state': False,
                    'combo_stop_value': '0',
                    'check_ctrl2_state': False,
                    'check_alt2_state': False,
                    'check_shift2_state': False,
                },
                'other_values': {
                    'frame_image1': None,
                    'frame_image2': None,
                    'frame_image3': None,
                    'entry1': 50,
                    'entry2': 15,
                    'button_state': 'off',
                    'frame_color': "#CED0D0"  # RGB(206, 208, 208) -> HEX
                }
            },
            'menu6': {
                'settings': {
                    'combo_run_value': '0',
                    'check_ctrl1_state': False,
                    'check_alt1_state': False,
                    'check_shift1_state': False,
                    'combo_stop_value': '0',
                    'check_ctrl2_state': False,
                    'check_alt2_state': False,
                    'check_shift2_state': False,
                },
                'other_values': {
                    'frame_image1': None,
                    'frame_image2': None,
                    'frame_image3': None,
                    'frame_image4': None,
                    'frame_image5': None,
                    'frame_image6': None,
                    'entry2': 15,
                    'button_state': 'off',
                    'frame_color': "#CED0D0"  # RGB(206, 208, 208) -> HEX
                }
            }
        }
        save_json_data(self.data_file, initial_data)

    def load_image_data(self):
        """이미지 데이터 로드"""
        data = load_json_data(self.data_file)
        if data:
            for menu in ['menu2', 'menu3', 'menu6']:
                self.menu_pixmaps[menu] = {}  # 각 메뉴에 대한 초기화
                for frame_name in data[menu]['other_values']:  # 'other_values'에서 프레임 이름 가져오기
                    if frame_name.startswith('frame_'):
                        image_path = data[menu]['other_values'][frame_name]
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
            'menu2': {'frames': ['frame_image1', 'frame_image2', 'frame_image3'], 'y_pos': 190, 'height': 390},
            'menu3': {'frames': ['frame_image1', 'frame_image2', 'frame_image3'], 'y_pos': 190, 'height': 390},
            'menu6': {'frames': ['frame_image1', 'frame_image2', 'frame_image3',
                               'frame_image4', 'frame_image5', 'frame_image6'], 'y_pos': 355, 'height': 540}
        }[menu_name]
        
        # scrollAreaWidgetContents 높이 조절
        self.ui.scrollAreaWidgetContents.setMinimumHeight(settings['height'])
        self.ui.scrollAreaWidgetContents.setMaximumHeight(settings['height'])
        
        # UI 업데이트
        self.update_menu_display(menu_name, settings)

    def update_menu_display(self, menu_name, settings):
        """메뉴 화면 업데이트"""
        # Setting 프레임 설정
        self.ui.Setting_frame.show()
        self.ui.Setting_frame.setGeometry(43, settings['y_pos'], 460, 171)
        
        # 타이틀 변경
        self.ui.label_title.setText(getattr(self.ui, f'label_{menu_name}').text())
        
        # menu6일 때 entry1 숨기기
        if menu_name == 'menu6':
            self.ui.frame_timeset1.hide()
            self.ui.label_timeset2.setText("배차 요청시간(분)")
            self.ui.Setting_frame.setMinimumHeight(120)
            self.ui.Setting_frame.setMaximumHeight(120)
            self.ui.frame_timeset2.setGeometry(5, 10, 453, 50)
            self.ui.frame_timeset3.setGeometry(5, 65, 453, 50)
            self.ui.scrollAreaWidgetContents.setMinimumHeight((settings['height']-40))
            self.ui.scrollAreaWidgetContents.setMaximumHeight((settings['height']-40))
        else:
            self.ui.frame_timeset1.show()
            self.ui.label_timeset2.setText("포장 기본 접수시간(분)")
            self.ui.Setting_frame.setMinimumHeight(171)
            self.ui.Setting_frame.setMaximumHeight(171)
            self.ui.frame_timeset2.setGeometry(5, 65, 453, 50)
            self.ui.frame_timeset3.setGeometry(5, 120, 453, 50)
            self.ui.scrollAreaWidgetContents.setMinimumHeight(settings['height'])
            self.ui.scrollAreaWidgetContents.setMaximumHeight(settings['height'])
        
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
                    frame.setStyleSheet("background:#CED0D0;\nborder:1px solid black;")
                frame.show()
                label.show()
            else:
                frame.hide()
                label.hide()
        
        # 메뉴 스타일 변경
        for m in ['menu2', 'menu3', 'menu6']:
            style = "background:#CED0D0;\ncolor: white;\nborder: none;" if m == menu_name else \
                   "background-color:rgb(255, 255, 255);\ncolor: black;\nborder: none;"
            getattr(self.ui, f'label_{m}').setStyleSheet(style)

        # entry 값과 버튼 상태 로드
        data = load_json_data(self.data_file)
        if data:
            # menu6가 아닐 때만 entry1 값 설정
            if menu_name != 'menu6':
                self.ui.entry1.setText(str(data[menu_name]['other_values']['entry1']))
            self.ui.entry2.setText(str(data[menu_name]['other_values']['entry2']))
        self.load_button_state(menu_name)

    def update_entry_value(self, entry_number, increment=True):
        """entry 값 업데이트 통합 메서드"""
        entry = getattr(self.ui, f'entry{entry_number}')
        current_value = int(entry.text())
        
        # 최솟값과 최댓값 설정
        min_value = 0  # 최솟값
        max_value = 180  # 최댓값
        
        new_value = current_value + (5 if increment else -5)
        
        # 최솟값과 최댓값을 초과하지 않도록 조정
        if new_value < min_value:
            new_value = min_value
        elif new_value > max_value:
            new_value = max_value
        
        entry.setText(str(new_value))
        
        current_menu = self.get_current_menu()
        data = load_json_data(self.data_file)
        if data:
            data[current_menu]['other_values'][f'entry{entry_number}'] = new_value
            save_json_data(self.data_file, data)

    def get_current_menu(self):
        """현재 선택된 메뉴 반환"""
        if self.ui.label_menu3.styleSheet().find("background:#CED0D0") != -1:
            return 'menu3'
        elif self.ui.label_menu6.styleSheet().find("background:#CED0D0") != -1:
            return 'menu6'
        return 'menu2'

    def save_button_state(self, current_menu, state, color):
        """버튼 상태와 프레임 색상 저장"""
        data = load_json_data(self.data_file)
        if data:
            # button_state와 frame_color를 other_values에 저장
            data[current_menu]['other_values']['button_state'] = state
            data[current_menu]['other_values']['frame_color'] = color
            
            # label_title 색상 저장
            if state == 'off':
                data[current_menu]['other_values']['label_title_color'] = "#000000"  # OFF 상태일 때 검은색
            else:
                data[current_menu]['other_values']['label_title_color'] = "#FFFFFF"  # ON 상태일 때 흰색
            
            save_json_data(self.data_file, data)

    def load_button_state(self, menu):
        """버튼 상태와 프레임 색상 로드"""
        data = load_json_data(self.data_file)
        if not data:
            return
            
        state = data[menu]['other_values']['button_state']
        
        # label_title 색상 로드
        label_title_color = data[menu]['other_values'].get('label_title_color', "#000000")  # 기본값은 검은색
        self.ui.label_title.setStyleSheet(f"color: {label_title_color};")
        
        if state == 'off':  # OFF 상태
            self.ui.button_off.show()
            self.ui.button_on.hide()
            self.ui.frame_title.setStyleSheet("background:#CED0D0")  # RGB(206, 208, 208) -> HEX
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
        color = "background:#CED0D0"  # RGB(206, 208, 208) -> HEX
        self.ui.frame_title.setStyleSheet(color)
        self.save_button_state(current_menu, 'off', color)
        
        # label_title 색상 변경
        self.ui.label_title.setStyleSheet("color: #000000;")  # ON 상태일 때 검은색

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
        
        # label_title 색상 변경
        self.ui.label_title.setStyleSheet("color: #FFFFFF;")  # OFF 상태일 때 흰색

    def show_image_dialog(self, frame):
        """이미지 선택 다이얼로그 표시"""
        dialog = ImageDialog(self)
        current_menu = self.get_current_menu()
        frame_name = frame.objectName()
        
        if frame.pixmap() and not frame.pixmap().isNull():
            dialog.set_preview_image(frame.pixmap())
            data = load_json_data(self.data_file)
            if data:
                current_path = data[current_menu]['other_values'][frame_name]
                if current_path:
                    dialog.selected_file_path = get_absolute_path(current_path)
        
        if dialog.exec() == QDialog.Accepted:
            if dialog.reset_requested:
                # 이미지 초기화
                frame.clear()
                frame.setStyleSheet("background:#CED0D0;\nborder:1px solid black;")  # RGB(206, 208, 208) -> HEX
                self.menu_pixmaps[current_menu][frame_name] = None
                
                # JSON 파일 업데이트
                data = load_json_data(self.data_file)
                if data:
                    data[current_menu]['other_values'][frame_name] = None
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
                    data[current_menu]['other_values'][frame_name] = relative_path
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