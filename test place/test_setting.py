import tkinter as tk
from tkinter import ttk

class SettingsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Settings")
        self.root.geometry("500x250")

        # Variables to store hotkeys
        self.execution_hotkey = tk.StringVar()
        self.termination_hotkey = tk.StringVar()
        self.delay_time = tk.StringVar()

        left_padding = 20

        # 실행모드 단축키 설명 라벨
        ttk.Label(root, text="실행모드 단축키 설명:").pack(anchor='w', padx=left_padding, pady=5)

        # 실행모드 단축키 설정을 위한 프레임
        execution_frame = ttk.Frame(root)
        execution_frame.pack(anchor='w', padx=30, pady=(5,20), fill='x')

        # 실행모드 단축키 라벨
        ttk.Label(execution_frame, text="실행모드 단축키:").pack(side='left', padx=5)
        # 실행모드 단축키 입력 필드
        self.execution_entry = ttk.Entry(execution_frame, textvariable=self.execution_hotkey, width=15)
        self.execution_entry.pack(side='left', padx=(30,5))
        # 실행모드 단축키 설정 버튼
        ttk.Button(execution_frame, text="Set", command=self.set_execution_hotkey).pack(side='left', padx=5)

        # 실행모드 종료 단축키 설명 라벨
        ttk.Label(root, text="실행모드 종료 단축키 설명:").pack(anchor='w', padx=left_padding, pady=5)
        
        # 실행모드 종료 단축키 설정을 위한 프레임
        termination_frame = ttk.Frame(root)
        termination_frame.pack(anchor='w', padx=30, pady=(5,20), fill='x')

        # 실행모드 종료 단축키 라벨
        ttk.Label(termination_frame, text="실행모드 종료 단축키:").pack(side='left', padx=5)
        # 실행모드 종료 단축키 입력 필드
        self.termination_entry = ttk.Entry(termination_frame, textvariable=self.termination_hotkey, width=15)
        self.termination_entry.pack(side='left', padx=5)
        # 실행모드 종료 단축키 설정 버튼
        ttk.Button(termination_frame, text="기록", width=3, command=self.set_termination_hotkey).pack(side='left', padx=5)
        # 실행모드 종료 단축키 설정 버튼
        ttk.Button(termination_frame, text="설정", width=3).pack(side='left', padx=5)

        # 딜레이 설정 설명 라벨
        ttk.Label(root, text="딜레이 설정 설명:").pack(anchor='w', padx=left_padding, pady=5)
        
        # 딜레이 설정을 위한 프레임
        delay_frame = ttk.Frame(root)
        delay_frame.pack(anchor='w', padx=30, pady=(5,20), fill='x')

        # 딜레이 설정 라벨
        ttk.Label(delay_frame, text="딜레이 설정:").pack(side='left', padx=5)
        # 딜레이 설정 입력 필드
        self.delay_entry = ttk.Entry(delay_frame, textvariable=self.delay_time)
        self.delay_entry.pack(side='left', padx=5)
        # 딜레이 단위 라벨
        ttk.Label(delay_frame, text="초").pack(side='left', padx=5)

        self.current_hotkey = []
        self.setting_execution_hotkey = False
        self.setting_termination_hotkey = False

        self.root.bind('<Key>', self.key_press_event)
        self.root.bind('<KeyRelease>', self.key_release_event)

    def set_execution_hotkey(self):
        self.setting_execution_hotkey = not self.setting_execution_hotkey
        self.setting_termination_hotkey = False
        self.current_hotkey = []
        if self.setting_execution_hotkey:
            self.execution_entry.delete(0, tk.END)
            self.execution_entry.insert(0, "Press keys...")
        else:
            self.execution_hotkey.set(" + ".join(self.current_hotkey))

    def set_termination_hotkey(self):
        self.setting_termination_hotkey = not self.setting_termination_hotkey
        self.setting_execution_hotkey = False
        self.current_hotkey = []
        if self.setting_termination_hotkey:
            self.termination_entry.delete(0, tk.END)
            self.termination_entry.insert(0, "Press keys...")
        else:
            self.termination_hotkey.set(" + ".join(self.current_hotkey))

    def key_press_event(self, event):
        if self.setting_execution_hotkey or self.setting_termination_hotkey:
            key = event.keysym
            if key not in self.current_hotkey:
                self.current_hotkey.append(key)
            current_hotkey_str = " + ".join(self.current_hotkey)
            if self.setting_execution_hotkey:
                self.execution_entry.delete(0, tk.END)
                self.execution_entry.insert(0, current_hotkey_str)
            elif self.setting_termination_hotkey:
                self.termination_entry.delete(0, tk.END)
                self.termination_entry.insert(0, current_hotkey_str)

    def key_release_event(self, event):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = SettingsApp(root)
    root.mainloop()
