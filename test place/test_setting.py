import tkinter as tk
from tkinter import ttk

class SettingsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Settings")
        self.root.geometry("400x250")

        # Variables to store hotkeys
        self.execution_hotkey = tk.StringVar()
        self.termination_hotkey = tk.StringVar()
        self.delay_time = tk.StringVar()

        # 실행모드 단축키 설명 라벨 추가
        ttk.Label(root, text="버튼을 눌러 실행모드에 사용할 단축키를 설정하세요.").grid(row=0, column=0, columnspan=3, padx=10, pady=5, sticky='w')
        # 실행모드 단축키 라벨
        ttk.Label(root, text="실행모드 단축키:").grid(row=1, column=0, padx=10, pady=5, sticky='e')
        # 실행모드 단축키 입력 필드
        self.execution_entry = ttk.Entry(root, textvariable=self.execution_hotkey)
        self.execution_entry.grid(row=1, column=1, padx=10, pady=5, sticky='w')
        # 실행모드 단축키 설정 버튼
        ttk.Button(root, text="Set", command=self.set_execution_hotkey, width=6).grid(row=1, column=2, padx=10, pady=5, sticky='w')

        # 실행모드 종료 단축키 설명 라벨 추가
        ttk.Label(root, text="버튼을 눌러 실행모드에 중단할 단축키를 설정하세요.").grid(row=2, column=0, columnspan=3, padx=10, pady=5, sticky='w')
        # 실행모드 종료 단축키 라벨
        ttk.Label(root, text="실행모드 종료 단축키:").grid(row=3, column=0, padx=10, pady=5, sticky='e')
        # 실행모드 종료 단축키 입력 필드
        self.termination_entry = ttk.Entry(root, textvariable=self.termination_hotkey)
        self.termination_entry.grid(row=3, column=1, padx=10, pady=5, sticky='w')
        # 실행모드 종료 단축키 설정 버튼
        ttk.Button(root, text="Set", command=self.set_termination_hotkey, width=6).grid(row=3, column=2, padx=10, pady=5, sticky='w')

        # 딜레이 설정 설명 라벨 추가
        ttk.Label(root, text="숫자를 입력하여 실행 간 딜레이를 설정하세요.").grid(row=4, column=0, columnspan=3, padx=10, pady=5, sticky='w')
        # 딜레이 설정 라벨
        ttk.Label(root, text="딜레이 설정:").grid(row=5, column=0, padx=10, pady=5, sticky='e')
        # 딜레이 설정 입력 필드
        self.delay_entry = ttk.Entry(root, textvariable=self.delay_time)
        self.delay_entry.grid(row=5, column=1, padx=10, pady=5, sticky='w')
        # 딜레이 단위 라벨
        ttk.Label(root, text="초").grid(row=5, column=2, padx=10, pady=5, sticky='w')

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
