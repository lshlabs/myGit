from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from pathlib import Path
import sys
import shutil
sys.path.append(str(Path(__file__).parents[1]))
from dialog.action_dialog import ActionDialog
from dialog.wizard_step2_dialog import WizardStep2Dialog
from dialog.wizard_step3_dialog import WizardStep3Dialog
from utils.temp_manager import TempManager
from utils.data_manager import DataManager

class ActionWizardDialog(QtWidgets.QDialog):
    def __init__(self, parent=None, title_text=""):
        super().__init__(parent)
        uic.loadUi('deeporder/ui/ActionWizardWindow.ui', self)
        self.setFixedSize(500, 470)
        self.title_text = title_text  # 전달받은 텍스트 저장
        self.init_ui()
        self.connect_signals()
        
    def init_ui(self):
        """UI 요소 초기화"""
        # 라벨들
        self.label_title1 = self.findChild(QtWidgets.QLabel, 'label_title1')
        self.label_title2 = self.findChild(QtWidgets.QLabel, 'label_title2')
        self.label_title3 = self.findChild(QtWidgets.QLabel, 'label_title3')
        
        # 라벨들에 텍스트 설정
        self.label_title1.setText(self.title_text)
        self.label_title2.setText(self.title_text)
        self.label_title3.setText(self.title_text)
        
        # === Page 1 요소들 ===
        self.init_page1_ui()
        
        # === Page 2 요소들 ===
        self.init_page2_ui()
        
        # === Page 3 요소들 ===
        self.init_page3_ui()
        
        # button 초기 비활성화
        self.button_next1.setEnabled(False)
        self.button_next2.setEnabled(False)
        self.button_save.setEnabled(False)
        
    def init_page1_ui(self):
        """Page 1 UI 요소 초기화"""
        # 프레임
        self.frame1 = self.findChild(QtWidgets.QFrame, 'frame1')
        # 라벨들
        self.label_step1 = self.findChild(QtWidgets.QLabel, 'label_step1')
        self.label_step1_text = self.findChild(QtWidgets.QLabel, 'label_step1_text')
        self.label_preview1 = self.findChild(QtWidgets.QLabel, 'label_preview1')
        # 버튼들
        self.button_next1 = self.findChild(QtWidgets.QPushButton, 'button_next1')
        self.button_cancel = self.findChild(QtWidgets.QPushButton, 'button_cancel')
        
    def init_page2_ui(self):
        """Page 2 UI 요소 초기화"""
        # 프레임
        self.frame2 = self.findChild(QtWidgets.QFrame, 'frame2')
        # 라벨들
        self.label_step2 = self.findChild(QtWidgets.QLabel, 'label_step2')
        self.label_step2_text = self.findChild(QtWidgets.QLabel, 'label_step2_text')
        self.label_preview2 = self.findChild(QtWidgets.QLabel, 'label_preview2')
        self.label_tip1 = self.findChild(QtWidgets.QLabel, 'label_tip1')
        # 버튼들
        self.button_next2 = self.findChild(QtWidgets.QPushButton, 'button_next2')
        self.button_prev1 = self.findChild(QtWidgets.QPushButton, 'button_prev1')
        
    def init_page3_ui(self):
        """Page 3 UI 요소 초기화"""
        # 프레임
        self.frame3 = self.findChild(QtWidgets.QFrame, 'frame3')
        # 라벨들
        self.label_step3 = self.findChild(QtWidgets.QLabel, 'label_step3')
        self.label_step3_text = self.findChild(QtWidgets.QLabel, 'label_step3_text')
        self.label_preview3 = self.findChild(QtWidgets.QLabel, 'label_preview3')
        self.label_tip2 = self.findChild(QtWidgets.QLabel, 'label_tip2')
        # 버튼들
        self.button_save = self.findChild(QtWidgets.QPushButton, 'button_save')
        self.button_prev2 = self.findChild(QtWidgets.QPushButton, 'button_prev2')
    
    def connect_signals(self):
        """시그널 연결"""
        # Page 1 버튼
        self.button_next1.clicked.connect(lambda: self.change_page(1))  # 0 -> 1
        self.button_cancel.clicked.connect(self.close)
        
        # Page 2 버튼
        self.button_next2.clicked.connect(lambda: self.change_page(2))  # 1 -> 2
        self.button_prev1.clicked.connect(lambda: self.change_page(0))  # 1 -> 0
        
        # Page 3 버튼
        self.button_save.clicked.connect(self.save_action)
        self.button_prev2.clicked.connect(lambda: self.change_page(1))  # 2 -> 1
        
        self.label_preview1.mousePressEvent = self.label_preview1_clicked
        self.label_preview2.mousePressEvent = self.label_preview2_clicked
        self.label_preview3.mousePressEvent = self.label_preview3_clicked
    
    def change_page(self, index: int):
        """페이지 전환
        Args:
            index (int): 이동할 페이지 인덱스 (0, 1, 2)
        """
        current_index = self.stackedWidget.currentIndex()
        
        # 현재 페이지가 0이고 다음 페이지로 이동하려는 경우
        if current_index == 0 and index == 1:
            # label_preview1에 이미지가 없으면 이동 불가
            if self.label_preview1.pixmap() is None:
                return
        
        self.stackedWidget.setCurrentIndex(index)
    
    def save_action(self):
        """저장 버튼 클릭 시 tempdata의 정보를 data로 옮기고 창을 닫습니다"""
        # DataManager 인스턴스 가져오기
        data_manager = DataManager.get_instance()
        temp_manager = TempManager.get_instance()
        
        # 새로운 매크로 키 생성 (M0, M1, ...)
        macro_key = f"M{len(data_manager._data['macro_list'])}"
        
        # 매크로 기본 정보 생성
        data_manager._data['macro_list'][macro_key] = {
            'name': self.title_text,
        }
        
        # 기본 액션 생성 (이미지 파일 복사 포함)
        data_manager.create_default_actions(macro_key)
        
        # 크롭된 이미지들을 매크로 폴더로 복사
        area_files = {
            'minus': 'A0.png',
            'plus': 'A1.png',
            'time': 'A2.png',
            'reject': 'A3.png',
            'accept': 'A4.png'
        }
        
        macro_folder = data_manager.img_path / self.title_text
        for label, filename in area_files.items():
            temp_image_path = temp_manager.get_cropped_image(label)
            if temp_image_path:
                shutil.copy2(temp_image_path, macro_folder / filename)
        
        # 임시 데이터 정리
        temp_manager.clear_temp_data()
        
        # 창 닫기
        self.accept()
        
        # ActionDialog 열기 (macro_key 전달)
        dialog = ActionDialog(self.parent(), macro_key=macro_key)
        dialog.show()
        
    def label_preview1_clicked(self, event):
        """이미지 선택 및 미리보기"""
        file_dialog = QtWidgets.QFileDialog(self)
        file_dialog.setWindowTitle("이미지 선택")
        file_dialog.setFileMode(QtWidgets.QFileDialog.FileMode.ExistingFile)
        file_dialog.setNameFilter("Images (*.png *.xpm *.jpg *.jpeg *.bmp)")
        
        if file_dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
            file_path = file_dialog.selectedFiles()[0]
            pixmap = QPixmap(file_path)
            
            # 각 label에 이미지 설정
            for label in [self.label_preview1, self.label_preview2, self.label_preview3]:
                scaled_pixmap = pixmap.scaled(
                    label.size(),
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation
                )
                label.setPixmap(scaled_pixmap)
            
            # 버튼 활성화 및 스타일시트 변경
            self.button_next1.setEnabled(True)
            next_style = self.button_next1.styleSheet().replace('darkgray', '#f0f0f0')
            self.button_next1.setStyleSheet(next_style)

    def label_preview2_clicked(self, event):
        """Step2 다이얼로그 열기"""
        if self.label_preview2.pixmap():
            dialog = WizardStep2Dialog(self)
            # 원본 이미지 설정 (label_preview1의 pixmap 사용)
            dialog.original_pixmap = self.label_preview1.pixmap().copy()
            dialog.display_pixmap = dialog.original_pixmap.copy()
            dialog.label_preview.setPixmap(dialog.display_pixmap)
            dialog.update_preview()  # 저장된 드래그 영역 표시
            dialog.show()

    def label_preview3_clicked(self, event):
        """Step3 다이얼로그 열기"""
        if self.label_preview3.pixmap():
            dialog = WizardStep3Dialog(self)
            # 원본 이미지 설정 (label_preview1의 pixmap 사용)
            dialog.original_pixmap = self.label_preview1.pixmap().copy()
            dialog.display_pixmap = dialog.original_pixmap.copy()
            dialog.label_preview.setPixmap(dialog.display_pixmap)
            dialog.update_preview()  # 저장된 드래그 영역 표시
            dialog.show()

    def closeEvent(self, event):
        """다이얼로그가 닫힐 때 임시 데이터 삭제"""
        TempManager.get_instance().clear_temp_data()
        super().closeEvent(event)
