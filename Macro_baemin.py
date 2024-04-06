import tkinter as tk
import json
from PIL import Image, ImageTk
from tkinter import filedialog, messagebox
from Macro_layer1_ui import App  # Macro_main_ui 모듈에서 App 클래스를 가져옵니다.

color_baemin = "#45D3D3"
app = App()  # App 인스턴스 생성

# 이미지 경로를 저장할 리스트
image_paths = [None, None, None]

# 이미지 선택 함수
def select_image(event, label):
    index = int(label.name[-1]) - 1  # label.name 예시: 'label_image1'
    file_path = filedialog.askopenfilename()
    if file_path:
        image_paths[index] = file_path
        display_image(label, file_path)

# 이미지 디스플레이 함수
def display_image(label, file_path):
    image = Image.open(file_path)
    image = image.resize((200, 200), Image.Resampling.LANCZOS)  # 이미지를 라벨 크기에 맞게 조절
    photo = ImageTk.PhotoImage(image)
    label.configure(image=photo)
    label.image = photo  # 참조를 유지

# 데이터 저장 함수
def save_data():
    with open('data.json', 'w') as f:
        json.dump(image_paths, f)

# 데이터 로딩 함수
def load_data():
    global image_paths
    try:
        with open('data.json', 'r') as f:
            image_paths = json.load(f)
    except FileNotFoundError:
        image_paths = [None, None, None]

# 프로그램 종료 시 실행할 함수
def on_closing():
    save_data()
    app.destroy()
    
# 프로그램 시작 시 실행할 함수
def on_opening(app):
    load_data()
    # 로드된 이미지 경로를 사용하여 이미지 표시
    for i, path in enumerate(image_paths):
        if path:
            label = getattr(app, f'label_image{i+1}')
            display_image(label, path)
    
def on_menu_click(event):
    # 클릭된 메뉴의 이름을 팝업으로 띄워줍니다.
    menu_name = event.widget.cget("text")
    messagebox.showinfo("메뉴 선택", f"선택된 메뉴: {menu_name}")
    
def configure_title():
    app.frame_title.config(bg=color_baemin)
    app.label_title.config(text="배달의 민족", bg=color_baemin)
    
def update_value(entry_var, change):
    # 현재 엔트리의 값 가져오기
    current_value = int(entry_var.get())
    # 새로운 값 계산
    new_value = max(0, current_value + change)  # 0 미만으로 내려가지 않도록 처리
    # 새로운 값으로 StringVar 업데이트
    entry_var.set(str(new_value))
    
def toggle():
    if app.button_onoff.config('text')[-1] == 'OFF':
        app.button_onoff.config(text='ON', bg='lightgrey')
    else:
        app.button_onoff.config(text='OFF', bg='lightgrey')

def main():
    # 프로그램 시작 시 데이터 로딩
    on_opening(app)
    configure_title()
    
    app.label_image1.name = "label_image1"
    app.label_image2.name = "label_image2"
    app.label_image3.name = "label_image3"

    # 각 메뉴 항목에 클릭 이벤트 바인딩
    app.menu_item2.bind("<Button-1>", on_menu_click)
    app.menu_item3.bind("<Button-1>", on_menu_click)
    app.menu_item4.bind("<Button-1>", on_menu_click)
    app.menu_item6.bind("<Button-1>", on_menu_click)
    app.menu_item7.bind("<Button-1>", on_menu_click)
    
     # On/Off 버튼 클릭 이벤트에 함수 연결
    app.button_onoff.config(command=toggle)
    
    # 버튼 클릭 이벤트에 함수 연결, 증가와 감소를 위해 change 인자에 각각 +5, -5 전달
    app.btn_decrease1.config(command=lambda: update_value(app.entry_var1, -5))
    app.btn_increase1.config(command=lambda: update_value(app.entry_var1, +5))
    app.btn_decrease2.config(command=lambda: update_value(app.entry_var2, -5))
    app.btn_increase2.config(command=lambda: update_value(app.entry_var2, +5))
    
    # 이미지 프레임과 이미지 라벨에 클릭 이벤트 바인딩
    app.frame_image1.bind("<Button-1>", lambda event: select_image(event, app.label_image1))
    app.frame_image2.bind("<Button-1>", lambda event: select_image(event, app.label_image2))
    app.frame_image3.bind("<Button-1>", lambda event: select_image(event, app.label_image3))
    
    app.label_image1.bind("<Button-1>", lambda event: select_image(event, app.label_image1))
    app.label_image2.bind("<Button-1>", lambda event: select_image(event, app.label_image2))
    app.label_image3.bind("<Button-1>", lambda event: select_image(event, app.label_image3))
    
    # 종료 이벤트 처리
    app.protocol("WM_DELETE_WINDOW", on_closing)
    app.mainloop()

if __name__ == "__main__":
    main()