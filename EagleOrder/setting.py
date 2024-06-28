import json
from pathlib import Path
import tkinter as tk
from tkinter import StringVar, ttk
import os
from virtual_key import g_vk_list

class MacroSettingGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("키보드/마우스 매크로 설정")
        self.root.geometry("380x300")
        
        self.delay_var = StringVar(root, "0.5")
        self.combobox_run = None
        self.combobox_stop = None
        self.check_run_vars = []
        self.check_stop_vars = []
        self.check_run_buttons = []
        self.check_stop_buttons = []
        
        self.setup_ui()
        self.load_data()
        
    def setup_ui(self):
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        self.setup_delay_section(main_frame)
        self.setup_shortcut_section(main_frame)
        self.setup_buttons(main_frame)

    def setup_delay_section(self, parent):
        delay_frame = ttk.LabelFrame(parent, text="딜레이 설정", padding="10")
        delay_frame.pack(fill=tk.X, expand=True, pady=5)
        
        ttk.Label(delay_frame, text="지연시간:").grid(row=0, column=0, padx=(5,15))
        ttk.Label(delay_frame, text="초").grid(row=0, column=2, padx=5)
        
        delay_time = ttk.Entry(delay_frame, width=10, textvariable=self.delay_var)
        delay_time.grid(row=0, column=1)

    def setup_shortcut_section(self, parent):
        shortcut_frame = ttk.LabelFrame(parent, text="매크로 시작/중지에 단축키 사용", padding="10")
        shortcut_frame.pack(fill=tk.X, expand=True, pady=5)

        self.create_shortcut_ui(shortcut_frame, "시작 단축키:", 0, is_run=True)
        self.create_shortcut_ui(shortcut_frame, "종료 단축키:", 2, is_run=False)

    def create_shortcut_ui(self, parent, label_text, row, is_run):
        ttk.Label(parent, text=label_text).grid(row=row, column=0, sticky='w')

        combo_button_frame = ttk.Frame(parent)
        combo_button_frame.grid(row=row, column=2, columnspan=2, pady=2, sticky='w')

        vk_descs = [info.vk_desc for info in g_vk_list if info.vk_code != -1]
        combobox = ttk.Combobox(combo_button_frame, values=vk_descs, state='readonly')
        combobox.pack(side=tk.LEFT, padx=5)

        if is_run:
            self.combobox_run = combobox
        else:
            self.combobox_stop = combobox

        ttk.Button(combo_button_frame, text="누를 때").pack(side=tk.LEFT, padx=5)

        md_frame = ttk.Frame(parent)
        md_frame.grid(row=row+1, column=1, columnspan=3, pady=2, sticky='w')

        check_vars = []
        check_buttons = []
        for i, text in enumerate(["Modifier Key:", "Ctrl", "Alt", "Shift"]):
            var = tk.BooleanVar()
            check = ttk.Checkbutton(md_frame, text=text, variable=var)
            check.pack(side=tk.LEFT, padx=5)
            check_vars.append(var)
            check_buttons.append(check)
            if i > 0:
                check.state(['disabled'])

        if is_run:
            self.check_run_vars = check_vars
            self.check_run_buttons = check_buttons
        else:
            self.check_stop_vars = check_vars
            self.check_stop_buttons = check_buttons

        check_vars[0].trace('w', lambda *args: self.toggle_checkboxes(check_buttons, check_vars[0]))

    def toggle_checkboxes(self, check_buttons, master_var):
        state = '!disabled' if master_var.get() else 'disabled'
        for check in check_buttons[1:]:
            check.state([state])

    def setup_buttons(self, parent):
        button_frame = ttk.Frame(parent)
        button_frame.pack(fill=tk.X, pady=10)

        ttk.Button(button_frame, text="Cancel", command=self.save_geometry).pack(side=tk.RIGHT, padx=5)
        ttk.Button(button_frame, text="OK", command=self.save_data).pack(side=tk.RIGHT)

    def save_data(self):
        data = {
            "delaytime": self.delay_var.get(),
            "combobox_run": self.combobox_run.get(),
            "combobox_stop": self.combobox_stop.get(),
            "check_run": [var.get() for var in self.check_run_vars],
            "check_stop": [var.get() for var in self.check_stop_vars],
            "window_geometry": self.root.geometry()
        }
        self.save_json(data)
        self.root.destroy()

    def save_geometry(self):
        data = self.load_json() or {}
        data['window_geometry'] = self.root.geometry()
        self.save_json(data)
        self.root.destroy()

    def load_data(self):
        data = self.load_json()
        if data:
            self.delay_var.set(data.get('delaytime', '0.5'))
            self.combobox_run.set(data.get('combobox_run', ''))
            self.combobox_stop.set(data.get('combobox_stop', ''))
            
            for i, value in enumerate(data.get('check_run', [])):
                self.check_run_vars[i].set(value)
            for i, value in enumerate(data.get('check_stop', [])):
                self.check_stop_vars[i].set(value)
            
            self.toggle_checkboxes(self.check_run_buttons, self.check_run_vars[0])
            self.toggle_checkboxes(self.check_stop_buttons, self.check_stop_vars[0])
            
            self.root.geometry(data.get('window_geometry', '380x300'))

    def save_json(self, data):
        json_data = json.dumps(data, indent=4, ensure_ascii=False)
        try:
            with open(self.get_data_path(), 'w', encoding='utf-8') as f:
                f.write(json_data)
        except IOError as e:
            print(f"데이터 저장 중 오류 발생: {e}")

    def load_json(self):
        try:
            with open(self.get_data_path(), 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print("데이터 파일을 찾을 수 없습니다.")
        except json.JSONDecodeError:
            print("잘못된 JSON 형식입니다.")
        return None

    @staticmethod
    def get_data_path():
        if os.name == 'nt':  # Windows
            return Path("C:/myGit/myGit/data_setting_win.json")
        else:  # Mac 또는 기타 OS
            return Path("mac 경로")

if __name__ == "__main__":
    root = tk.Tk()
    app = MacroSettingGUI(root)
    root.mainloop()
