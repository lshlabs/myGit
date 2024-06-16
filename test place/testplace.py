from cgitb import text
import tkinter as tk
from tkinter import ttk

from torch import normal

class MacroSettingsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("키보드/마우스 매크로 설정")
        self.root.geometry("410x300")
        
        main_frame = ttk.Frame(root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # 딜레이 설정 섹션
        delay_frame = ttk.LabelFrame(main_frame, text="딜레이 설정", padding="10")
        delay_frame.pack(fill=tk.X, expand=True, pady=5)
        
        ttk.Label(delay_frame, text="지연시간:").grid(row=0, column=0, padx=(5,15))
        ttk.Label(delay_frame, text="초").grid(row=0, column=2, padx=20)
        
        delay_time = ttk.Entry(delay_frame, width=10)
        delay_time.insert(0, "0.5")
        delay_time.grid(row=0, column=1)
        
        

        # 매크로 시작/중지에 단축키 사용 섹션
        shortcut_frame = ttk.LabelFrame(main_frame, text="매크로 시작/중지에 단축키 사용", padding="10")
        shortcut_frame.pack(fill=tk.X, expand=True, pady=5)
        
        self.add_shortcut_option(shortcut_frame, "시작 단축키:", 0)
        self.add_shortcut_option(shortcut_frame, "중지 단축키:", 2)

        # 확인 및 취소 버튼
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(button_frame, text="Cancel").pack(side=tk.RIGHT, padx=5)
        ttk.Button(button_frame, text="OK").pack(side=tk.RIGHT)

    def add_shortcut_option(self, frame, label_text, row):
        # 체크박스
        ttk.Checkbutton(frame).grid(row=row, column=0, sticky='w')
        
        # 레이블
        ttk.Label(frame, text=label_text).grid(row=row, column=1, padx=5, pady=2, sticky='w')
        
        # 콤보박스와 버튼 프레임 생성
        combo_button_frame = ttk.Frame(frame)
        combo_button_frame.grid(row=row, column=2, columnspan=2, pady=2, sticky='w')
        
        # 콤보박스
        ttk.Combobox(combo_button_frame, values=["F2 key", "F3 key"]).pack(side=tk.LEFT, padx=5)
        
        # 버튼
        ttk.Button(combo_button_frame, text="누를 때").pack(side=tk.LEFT, padx=5)
        
        # Modifier Key 체크박스 (아래로 이동)
        modifier_frame = ttk.Frame(frame)
        modifier_frame.grid(row=row+1, column=2, columnspan=3, pady=2, sticky='w')

        ttk.Checkbutton(modifier_frame, text="Modifier Key:").pack(side=tk.LEFT, padx=5)
        ttk.Checkbutton(modifier_frame, text="Ctrl").pack(side=tk.LEFT, padx=5)
        ttk.Checkbutton(modifier_frame, text="Alt").pack(side=tk.LEFT, padx=5)
        ttk.Checkbutton(modifier_frame, text="Shift").pack(side=tk.LEFT, padx=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = MacroSettingsApp(root)
    root.mainloop()
