import tkinter as tk
from pynput import mouse

class CoordinateRecorder:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("좌표 녹화")
        self.root.geometry("300x200")
        
        # 창을 항상 최상위로 설정
        self.root.attributes('-topmost', True)
        
        # 좌표 표시 레이블
        self.start_label = tk.Label(self.root, text="시작 좌표: 없음 (S키로 녹화)")
        self.start_label.pack(pady=10)
        
        self.end_label = tk.Label(self.root, text="끝 좌표: 없음 (E키로 녹화)")
        self.end_label.pack(pady=10)
        
        # 녹화 버튼
        self.record_button = tk.Button(self.root, text="녹화 시작", command=self.start_recording)
        self.record_button.pack(pady=20)
        
        # 좌표 저장용 변수
        self.start_pos = None
        self.end_pos = None
        self.recording = False
        self.current_pos = (0, 0)
        
    def start_recording(self):
        if not self.recording:
            self.record_button.config(text="녹화 중... (ESC 취소)")
            self.recording = True
            
            # 마우스 위치 추적
            self.mouse_listener = mouse.Listener(on_move=self.on_move)
            self.mouse_listener.start()
            
            # 키 바인딩
            self.root.bind('<s>', self.on_s_press)
            self.root.bind('<e>', self.on_e_press)
            self.root.bind('<S>', self.on_s_press)  # 대문자도 처리
            self.root.bind('<E>', self.on_e_press)  # 대문자도 처리
            self.root.bind('<Escape>', self.stop_recording)
            
    def stop_recording(self, event=None):
        if self.recording:
            self.recording = False
            self.mouse_listener.stop()
            self.record_button.config(text="녹화 시작")
            # 키 바인딩 제거
            self.root.unbind('<s>')
            self.root.unbind('<e>')
            self.root.unbind('<S>')
            self.root.unbind('<E>')
            self.root.unbind('<Escape>')
            
    def on_move(self, x, y):
        self.current_pos = (x, y)
            
    def on_s_press(self, event):
        if self.recording:
            self.start_pos = self.current_pos
            self.start_label.config(text=f"시작 좌표: ({self.start_pos[0]}, {self.start_pos[1]})")
            
    def on_e_press(self, event):
        if self.recording:
            self.end_pos = self.current_pos
            self.end_label.config(text=f"끝 좌표: ({self.end_pos[0]}, {self.end_pos[1]})")
            self.stop_recording()
                
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = CoordinateRecorder()
    app.run()