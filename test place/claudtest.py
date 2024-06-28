# test.py
import tkinter as tk
import json, os
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
from test_ui import setup_ui
import subprocess

MENU_CONFIG = {
    "배달의 민족": {"color": "#45D3D3", "frame_range": (0, 3), "entry_vars": 2},
    "요기요": {"color": "#FA0150", "frame_range": (3, 6), "entry_vars": 2},
    "만나": {"color": "#ff6b00", "frame_range": (6, 12), "entry_vars": 1}
}

class DeliveryMacro:
    def __init__(self, root):
        self.root = root
        self.root.geometry("700x500")
        self.root.resizable(False, False)
        self.root.title('매크로')

        self.image_paths = {i: None for i in range(12)}
        self.setup_ui()
        self.load_data(load_window_geometry=True)
        self.bind_events()

    def setup_ui(self):
        ui_elements = setup_ui(self.root)
        (
            self.title_label, self.content_canvas, self.iframes, self.ilabels, 
            self.inames, self.menu_frame, self.uni_frame, self.scrollbar, 
            self.title_frame, self.title_label, self.scrollable_frame, self.btn_setting,
            self.menu_item2, self.menu_item3, self.menu_item4, self.menu_item6, 
            self.menu_item7, self.setting_icon_photo, self.entry_var1, self.entry_var2, 
            self.oframes, self.obtn_m1, self.obtn_m2, self.obtn_p1, self.obtn_p2
        ) = ui_elements
        
        self.configure_title("배달의 민족")
        self.update_layout(False)

    def bind_events(self):
        self.menu_item2.bind("<Button-1>", self.on_menu_click)
        self.menu_item3.bind("<Button-1>", self.on_menu_click)
        self.menu_item6.bind("<Button-1>", self.on_menu_click)

        for i in range(12):
            self.ilabels[i].name = f"label_image{i+1}"
            self.iframes[i].bind("<Button-1>", lambda event, idx=i: self.select_image(event, self.ilabels[idx]))
            self.ilabels[i].bind("<Button-1>", lambda event, idx=i: self.select_image(event, self.ilabels[idx]))

        self.obtn_p1.config(command=lambda: self.update_value(self.entry_var1, +5))
        self.obtn_m1.config(command=lambda: self.update_value(self.entry_var1, -5))
        self.obtn_p2.config(command=lambda: self.update_value(self.entry_var2, +5))
        self.obtn_m2.config(command=lambda: self.update_value(self.entry_var2, -5))
        
        self.btn_setting.config(command=self.run_testplace)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def update_layout(self, bind_scroll=True):
        if bind_scroll:
            self.scrollbar.pack(side="right", fill='both')
            self.scrollable_frame.bind("<MouseWheel>", self.on_mousewheel)
        else:
            self.scrollbar.pack_forget()
            self.scrollable_frame.unbind("<MouseWheel>")
        self.content_canvas.yview_moveto(0.0)

    def update_value(self, entry_var, change):
        current_value = int(entry_var.get())
        new_value = max(0, current_value + change)
        entry_var.set(str(new_value))
        self.save_data()

    def select_image(self, event, label):
        file_path = filedialog.askopenfilename()
        index_str = label.name.replace('label_image', '')
        if index_str.isdigit():
            index = int(index_str) - 1
            self.image_paths[index] = file_path
            self.display_image(label, file_path)

    def display_image(self, frame, file_path):
        try:
            image = Image.open(file_path)
            image = image.resize((120, 120), Image.Resampling.LANCZOS)     
            photo = ImageTk.PhotoImage(image)
            frame.configure(image=photo)
            frame.image = photo
        except Exception as e:
            print(f"Failed to open image: {e}")

    def save_data(self):
        program_id = self.title_label.cget("text")
        data = {
            program_id: {
                "image_paths": self.image_paths,
                "entry_var1": self.entry_var1.get() if self.entry_var1.get() else None,
                "entry_var2": self.entry_var2.get() if hasattr(self, 'entry_var2') and self.entry_var2.get() else None
            },
            "window_geometry_main": self.root.geometry()
        }

        self.save_to_json(data)

    def load_data(self, menu_name=None, load_window_geometry=True):
        program_id = menu_name if menu_name else self.title_label.cget("text")
        data = self.load_from_json()
        
        if program_id in data:
            self.image_paths = {int(k): v for k, v in data[program_id].get("image_paths", {}).items() if v is not None}
            self.entry_var1.set(data[program_id].get("entry_var1", "50"))
            if hasattr(self, 'entry_var2'):
                self.entry_var2.set(data[program_id].get("entry_var2", "15"))

        if load_window_geometry and "window_geometry_main" in data:
            self.root.geometry(data["window_geometry_main"])

        for i, path in self.image_paths.items():
            if path:
                self.display_image(self.ilabels[i], path)

    def on_menu_click(self, event):
        self.save_data()
        menu_name = event.widget.cget("text")
        self.configure_title(menu_name)
        self.load_data(menu_name, load_window_geometry=False)

    def configure_title(self, menu_name):
        config = MENU_CONFIG[menu_name]
        start, end = config["frame_range"]
        self.manage_frames_visibility(start, end)
        
        self.title_frame.config(bg=config["color"])
        self.title_label.config(text=menu_name, bg=config["color"])
        
        self.menu_item2.config(bg="gainsboro" if menu_name == "배달의 민족" else "white")
        self.menu_item3.config(bg="gainsboro" if menu_name == "요기요" else "white")
        self.menu_item6.config(bg="gainsboro" if menu_name == "만나" else "white")

        if menu_name == "만나":
            self.oframes[1].grid_remove()
            self.oframes[0].grid(row=10)
            self.oframes[2].grid(row=11)
        else:
            self.oframes[0].grid(row=5)
            self.oframes[1].grid(row=6)
            self.oframes[2].grid(row=7)

        self.update_layout(menu_name == "만나")

    def manage_frames_visibility(self, start, end):
        for i in range(len(self.iframes)):
            if start <= i < end:
                self.iframes[i].grid()
                self.inames[i].grid()
                self.ilabels[i].pack()
            else:
                self.iframes[i].grid_remove()
                self.inames[i].grid_remove()
                self.ilabels[i].pack_forget()

    def on_mousewheel(self, event):
        self.content_canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def on_closing(self):
        self.save_data()
        self.root.destroy()

    def run_testplace(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        script_path = os.path.join(script_dir, "testplace.py")
        subprocess.run(["python", script_path])

    def save_to_json(self, data):
        try:
            with open('data.json', 'r+', encoding='utf-8') as f:
                all_data = json.load(f)
                all_data.update(data)
                f.seek(0)
                json.dump(all_data, f, indent=4, ensure_ascii=False)
                f.truncate()
        except FileNotFoundError:
            with open('data.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)

    def load_from_json(self):
        try:
            with open('data.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            print("JSON 파일을 해석하는 데 오류가 발생했습니다. 기본값을 사용합니다.")
            return {}

if __name__ == "__main__":
    root = tk.Tk()
    app = DeliveryMacro(root)
    root.mainloop()