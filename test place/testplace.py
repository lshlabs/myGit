# from cgitb import text
import tkinter as tk
from tkinter import ttk
from tkinter import IntVar

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
        
        # 체크박스 생성 및 체크박수 변수 생성
        #checkVar_run = tk.IntVar(value=1)
        check_run = ttk.Checkbutton(shortcut_frame, text="시작 단축키:")
        check_run.grid(row=0, column=0, sticky='w')
        check_run.state(['!alternate'])
        
        #checkVar_stop = tk.IntVar(value=1)
        check_stop = ttk.Checkbutton(shortcut_frame, text="종료 단축키:")
        check_stop.grid(row=2, column=0, sticky='w')
        check_stop.state(['!alternate'])
        
        # 콤보박스와 버튼 프레임 생성
        combo_button_frame1 = ttk.Frame(shortcut_frame)
        combo_button_frame1.grid(row=0, column=2, columnspan=2, pady=2, sticky='w')
        
        combo_button_frame2 = ttk.Frame(shortcut_frame)
        combo_button_frame2.grid(row=2, column=2, columnspan=2, pady=2, sticky='w')
        
        # 콤보박스
        combobox_run = ttk.Combobox(combo_button_frame1, values=["F2 key", "F3 key"])
        combobox_run.pack(side=tk.LEFT, padx=5)
        combobox_stop = ttk.Combobox(combo_button_frame2, values=["F2 key", "F3 key"])
        combobox_stop.pack(side=tk.LEFT, padx=5)
        
        # 버튼
        button_run = ttk.Button(combo_button_frame1, text="누를 때")
        button_run.pack(side=tk.LEFT, padx=5)
        button_stop = ttk.Button(combo_button_frame2, text="누를 때")
        button_stop.pack(side=tk.LEFT, padx=5)
        
        # Modifier Key 체크박스 (아래로 이동)
        modifier_frame1 = ttk.Frame(shortcut_frame)
        modifier_frame1.grid(row=1, column=2, columnspan=3, pady=2, sticky='w')
        
        modifier_frame2 = ttk.Frame(shortcut_frame)
        modifier_frame2.grid(row=3, column=2, columnspan=3, pady=2, sticky='w')

        check_mod1 = ttk.Checkbutton(modifier_frame1, text="Modifier Key:")
        check_mod1_option1 = ttk.Checkbutton(modifier_frame1, text="Ctrl", state='disabled')
        check_mod1_option2 = ttk.Checkbutton(modifier_frame1, text="Alt", state='disabled')
        check_mod1_option3 = ttk.Checkbutton(modifier_frame1, text="Shift", state='disabled')
        
        check_mod1.pack(side=tk.LEFT, padx=5)
        check_mod1_option1.pack(side=tk.LEFT, padx=5)
        check_mod1_option2.pack(side=tk.LEFT, padx=5)
        check_mod1_option3.pack(side=tk.LEFT, padx=5)
        
        check_mod1.state(['!alternate'])
        check_mod1_option1.state(['!alternate'])
        check_mod1_option2.state(['!alternate'])
        check_mod1_option3.state(['!alternate'])
        
        check_mod2 = ttk.Checkbutton(modifier_frame2, text="Modifier Key:")
        check_mod2_option1 = ttk.Checkbutton(modifier_frame2, text="Ctrl", state='disabled')
        check_mod2_option2 = ttk.Checkbutton(modifier_frame2, text="Alt", state='disabled')
        check_mod2_option3 = ttk.Checkbutton(modifier_frame2, text="Shift", state='disabled')
        
        check_mod2.pack(side=tk.LEFT, padx=5)
        check_mod2_option1.pack(side=tk.LEFT, padx=5)
        check_mod2_option2.pack(side=tk.LEFT, padx=5)
        check_mod2_option3.pack(side=tk.LEFT, padx=5)
        
        check_mod2.state(['!alternate'])
        check_mod2_option1.state(['!alternate'])
        check_mod2_option2.state(['!alternate'])
        check_mod2_option3.state(['!alternate'])

        # 확인 및 취소 버튼
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(button_frame, text="Cancel", command=root.destroy).pack(side=tk.RIGHT, padx=5)
        ttk.Button(button_frame, text="OK").pack(side=tk.RIGHT)

if __name__ == "__main__":
    root = tk.Tk()
    app = MacroSettingsApp(root)
    root.mainloop()
