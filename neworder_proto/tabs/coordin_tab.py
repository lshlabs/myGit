import os
import json
import time
import pyautogui
from PyQt6.QtCore import Qt, QThread, pyqtSignal, QTimer
from PyQt6.QtWidgets import QWidget, QMessageBox

class RecordThread(QThread):
    """좌표 녹화를 위한 스레드"""
    coordinates_captured = pyqtSignal(int, int)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.running = True
        
    def run(self):
        # 5초 카운트다운 후 좌표 캡처 (F2 키 감지 대신)
        print("5초 후 현재 마우스 위치를 캡처합니다...")
        for i in range(5, 0, -1):
            print(f"{i}...")
            time.sleep(1)
            if not self.running:
                return
        
        # 카운트다운 후 현재 좌표 캡처
        try:
            x, y = pyautogui.position()
            self.coordinates_captured.emit(x, y)
        except Exception as e:
            print(f"좌표 캡처 중 오류 발생: {str(e)}")
        
        self.running = False
                
    def stop(self):
        self.running = False


class CoordinTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setup_ui()
        self.setup_connections()
        self.record_thread = None
        self.active_button = None
        self.active_x_field = None
        self.active_y_field = None
        self.active_coordinate_name = None
        
        # 좌표 데이터 로드 또는 초기화
        self.coordinates_data = self.load_coordinates() or {}
        
        # 저장된 좌표 값이 있으면 UI에 표시
        self.load_coordinates_to_ui()
        
    def setup_ui(self):
        # UI 요소 참조
        self.lineEdit_limit_x = self.parent.lineEdit_limit_x
        self.lineEdit_limit_y = self.parent.lineEdit_limit_y
        self.button_record1 = self.parent.button_record1
        
        self.lineEdit_market_x = self.parent.lineEdit_market_x
        self.lineEdit_market_y = self.parent.lineEdit_market_y
        self.button_record2 = self.parent.button_record2
        
        self.lineEdit_buy_x = self.parent.lineEdit_buy_x
        self.lineEdit_buy_y = self.parent.lineEdit_buy_y
        self.button_record3 = self.parent.button_record3
        
        self.lineEdit_sell_x = self.parent.lineEdit_sell_x
        self.lineEdit_sell_y = self.parent.lineEdit_sell_y
        self.button_record4 = self.parent.button_record4
        
        self.lineEdit_buyprice_x = self.parent.lineEdit_buyprice_x
        self.lineEdit_buyprice_y = self.parent.lineEdit_buyprice_y
        self.button_record5 = self.parent.button_record5
        
        self.lineEdit_nowprice_x = self.parent.lineEdit_nowprice_x
        self.lineEdit_nowprice_y = self.parent.lineEdit_nowprice_y
        self.button_record6 = self.parent.button_record6
        
        self.lineEdit_quantity_x = self.parent.lineEdit_quantity_x
        self.lineEdit_quantity_y = self.parent.lineEdit_quantity_y
        self.button_record7 = self.parent.button_record7
        
        self.lineEdit_leverage_x = self.parent.lineEdit_leverage_x
        self.lineEdit_leverage_y = self.parent.lineEdit_leverage_y
        self.button_record8 = self.parent.button_record8
        
        self.lineEdit_position_x = self.parent.lineEdit_position_x
        self.lineEdit_position_y = self.parent.lineEdit_position_y
        self.button_record9 = self.parent.button_record9
        
        self.lineEdit_oi_x = self.parent.lineEdit_oi_x
        self.lineEdit_oi_y = self.parent.lineEdit_oi_y
        self.button_record10 = self.parent.button_record10
        
        self.lineEdit_details_x = self.parent.lineEdit_details_x
        self.lineEdit_details_y = self.parent.lineEdit_details_y
        self.button_record11 = self.parent.button_record11
        
        self.lineEdit_pnl_x = self.parent.lineEdit_pnl_x
        self.lineEdit_pnl_y = self.parent.lineEdit_pnl_y
        self.button_record12 = self.parent.button_record12
        
        self.lineEdit_allsell_x = self.parent.lineEdit_allsell_x
        self.lineEdit_allsell_y = self.parent.lineEdit_allsell_y
        self.button_record13 = self.parent.button_record13
        
        self.lineEdit_allcancel_x = self.parent.lineEdit_allcancel_x
        self.lineEdit_allcancel_y = self.parent.lineEdit_allcancel_y
        self.button_record14 = self.parent.button_record14
        
    def setup_connections(self):
        # 녹화 버튼 연결
        self.button_record1.clicked.connect(lambda: self.start_recording(self.lineEdit_limit_x, self.lineEdit_limit_y, self.button_record1, "limit"))
        self.button_record2.clicked.connect(lambda: self.start_recording(self.lineEdit_market_x, self.lineEdit_market_y, self.button_record2, "market"))
        self.button_record3.clicked.connect(lambda: self.start_recording(self.lineEdit_buy_x, self.lineEdit_buy_y, self.button_record3, "buy"))
        self.button_record4.clicked.connect(lambda: self.start_recording(self.lineEdit_sell_x, self.lineEdit_sell_y, self.button_record4, "sell"))
        self.button_record5.clicked.connect(lambda: self.start_recording(self.lineEdit_buyprice_x, self.lineEdit_buyprice_y, self.button_record5, "buyprice"))
        self.button_record6.clicked.connect(lambda: self.start_recording(self.lineEdit_nowprice_x, self.lineEdit_nowprice_y, self.button_record6, "nowprice"))
        self.button_record7.clicked.connect(lambda: self.start_recording(self.lineEdit_quantity_x, self.lineEdit_quantity_y, self.button_record7, "quantity"))
        self.button_record8.clicked.connect(lambda: self.start_recording(self.lineEdit_leverage_x, self.lineEdit_leverage_y, self.button_record8, "leverage"))
        self.button_record9.clicked.connect(lambda: self.start_recording(self.lineEdit_position_x, self.lineEdit_position_y, self.button_record9, "position"))
        self.button_record10.clicked.connect(lambda: self.start_recording(self.lineEdit_oi_x, self.lineEdit_oi_y, self.button_record10, "oi"))
        self.button_record11.clicked.connect(lambda: self.start_recording(self.lineEdit_details_x, self.lineEdit_details_y, self.button_record11, "details"))
        self.button_record12.clicked.connect(lambda: self.start_recording(self.lineEdit_pnl_x, self.lineEdit_pnl_y, self.button_record12, "pnl"))
        self.button_record13.clicked.connect(lambda: self.start_recording(self.lineEdit_allsell_x, self.lineEdit_allsell_y, self.button_record13, "allsell"))
        self.button_record14.clicked.connect(lambda: self.start_recording(self.lineEdit_allcancel_x, self.lineEdit_allcancel_y, self.button_record14, "allcancel"))
        
    def start_recording(self, x_field, y_field, button, coordinate_name):
        """좌표 녹화 시작"""
        if self.record_thread and self.record_thread.isRunning():
            self.record_thread.stop()
            self.record_thread.wait()
            button.setText("녹화 시작")
            return
            
        # 녹화 시작
        self.active_x_field = x_field
        self.active_y_field = y_field
        self.active_button = button
        self.active_coordinate_name = coordinate_name
        
        button.setText("녹화 중...")
        
        # 스레드 생성 및 시작
        self.record_thread = RecordThread(self)
        self.record_thread.coordinates_captured.connect(self.on_coordinates_captured)
        self.record_thread.finished.connect(self.on_recording_finished)
        self.record_thread.start()
        
        # 안전장치: 10초 후 자동 종료 타이머
        QTimer.singleShot(10000, self.check_recording_status)
        
    def check_recording_status(self):
        """녹화 상태 확인 및 필요시 종료"""
        if self.record_thread and self.record_thread.isRunning():
            self.record_thread.stop()
            if self.active_button:
                self.active_button.setText("녹화 시작")
    
    def on_coordinates_captured(self, x, y):
        """좌표가 캡처되었을 때"""
        if self.active_x_field and self.active_y_field:
            self.active_x_field.setText(str(x))
            self.active_y_field.setText(str(y))
            
            # 좌표 데이터 저장
            if self.active_coordinate_name:
                self.coordinates_data[self.active_coordinate_name] = {'x': x, 'y': y}
                self.save_coordinates()
    
    def on_recording_finished(self):
        """녹화가 종료되었을 때"""
        if self.active_button:
            self.active_button.setText("녹화 시작")
            
    def load_coordinates(self):
        """저장된 좌표 데이터 로드"""
        try:
            coordinates_file = os.path.join("neworder_proto", "data", "coordinates.json")
            if os.path.exists(coordinates_file):
                with open(coordinates_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except Exception as e:
            print(f"좌표 데이터 로드 중 오류: {str(e)}")
        return {}
    
    def save_coordinates(self):
        """좌표 데이터 저장"""
        try:
            # 디렉토리 생성 (존재하지 않는 경우)
            os.makedirs(os.path.join("neworder_proto", "data"), exist_ok=True)
            
            coordinates_file = os.path.join("neworder_proto", "data", "coordinates.json")
            with open(coordinates_file, 'w', encoding='utf-8') as f:
                json.dump(self.coordinates_data, f, ensure_ascii=False, indent=2)
            print("좌표가 저장되었습니다.")
        except Exception as e:
            print(f"좌표 데이터 저장 중 오류: {str(e)}")
    
    def load_coordinates_to_ui(self):
        """저장된 좌표 값을 UI에 표시"""
        if not self.coordinates_data:
            return
            
        coord_map = {
            "limit": (self.lineEdit_limit_x, self.lineEdit_limit_y),
            "market": (self.lineEdit_market_x, self.lineEdit_market_y),
            "buy": (self.lineEdit_buy_x, self.lineEdit_buy_y),
            "sell": (self.lineEdit_sell_x, self.lineEdit_sell_y),
            "buyprice": (self.lineEdit_buyprice_x, self.lineEdit_buyprice_y),
            "nowprice": (self.lineEdit_nowprice_x, self.lineEdit_nowprice_y),
            "quantity": (self.lineEdit_quantity_x, self.lineEdit_quantity_y),
            "leverage": (self.lineEdit_leverage_x, self.lineEdit_leverage_y),
            "position": (self.lineEdit_position_x, self.lineEdit_position_y),
            "oi": (self.lineEdit_oi_x, self.lineEdit_oi_y),
            "details": (self.lineEdit_details_x, self.lineEdit_details_y),
            "pnl": (self.lineEdit_pnl_x, self.lineEdit_pnl_y),
            "allsell": (self.lineEdit_allsell_x, self.lineEdit_allsell_y),
            "allcancel": (self.lineEdit_allcancel_x, self.lineEdit_allcancel_y)
        }
        
        for name, (x_field, y_field) in coord_map.items():
            if name in self.coordinates_data:
                coord = self.coordinates_data[name]
                x_field.setText(str(coord.get('x', '')))
                y_field.setText(str(coord.get('y', '')))
