import tkinter as tk
import json, os
from PIL import Image, ImageTk
from tkinter import filedialog, messagebox
from Macro_layer1_ui import App  # Macro_main_ui 모듈에서 App 클래스를 가져옵니다.

baemin = {"text": "배달의 민족", "color": "#45D3D3"}
yogiyo = {"text": "요기요", "color": "#FA0150"}
manna = {"text": "만나", "color": "#ff6b00"}
app = App()  # App 인스턴스 생성
img_visible = False  # 가시성을 추적하는 전역 변수

# 이미지 경로를 저장할 리스트
image_paths = [None, None, None]

def fold_imageframes():
    global img_visible
    if img_visible:
        app.frame_image4.place_forget()
        app.frame_image5.place_forget()
        app.frame_image6.place_forget()
        app.label_image4.place_forget()
        app.label_image5.place_forget()
        app.label_image6.place_forget()
        app.title_image4.place_forget()
        app.title_image5.place_forget()
        app.title_image6.place_forget()
        app.frame_option3.place(x=180, y=390)
        img_visible = False
    else:
        app.frame_image4.place(x=180,y=260)
        app.frame_image5.place(x=345,y=260)
        app.frame_image6.place(x=510,y=260)
        app.label_image4.pack(expand=True, fill=tk.BOTH)
        app.label_image5.pack(expand=True, fill=tk.BOTH)
        app.label_image6.pack(expand=True, fill=tk.BOTH)
        app.title_image4.place(x=180, y=380)
        app.title_image5.place(x=345, y=380)
        app.title_image6.place(x=510, y=380)
        img_visible = True

# 이미지 선택 함수
def select_image(event, label):
    index = int(label.name[-1]) - 1  # label.name 예시: 'label_image1'
    file_path = filedialog.askopenfilename()
    if file_path:
        image_paths[index] = file_path
        display_image(label, file_path)

# 이미지 디스플레이 함수
def display_image(frame, file_path):
    image = Image.open(file_path)
    # 이미지를 라벨 크기에 맞게 조절
    image = image.resize((120, 120), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    frame.configure(image=photo)
    frame.image = photo  # 참조를 유지

# 데이터 저장 함수
def save_data():
    # 현재 실행 중인 파일의 이름을 기반으로 프로그램 식별자 생성
    program_id = app.label_title.cget("text")
    data = {
        program_id: {  # label_title 을 키로 사용
            "image_paths": image_paths,
            "button_state": app.button_onoff.cget('text'),
            "entry_var1": app.entry_var1.get(),
            "entry_var2": app.entry_var2.get(),
        }
    }
    data_window_position = {
        "window_geometry": app.geometry()
    }
    # 전체 데이터를 불러오기
    try:
        with open('data.json', 'r') as f:
            all_data = json.load(f)
    except FileNotFoundError:
        all_data = {}
        
    # 현재 프로그램의 데이터를 업데이트
    all_data.update(data)
    # window_geometry 데이터 업데이트
    all_data.update(data_window_position)
    
    # 데이터 저장
    with open('data.json', 'w', encoding='utf-8') as f:  # encoding 명시적으로 추가
        json.dump(all_data, f, indent=4, ensure_ascii=False)


# 데이터 로딩 함수
def load_data(menu_name=None, load_window_geometry=True):
    global image_paths
    # program_id 대신 menu_name을 사용하여 데이터 로드
    program_id = menu_name if menu_name else app.label_title.cget("text")
    try:
        with open('data.json', 'r') as f:
            all_data = json.load(f)
            # menu_name을 키로 사용하여 데이터 가져오기
            data = all_data.get(program_id, {})
            
            image_paths = data.get("image_paths", [None, None, None])
            app.button_onoff.config(text=data.get("button_state", "OFF"))
            app.entry_var1.set(data.get("entry_var1", "0"))
            app.entry_var2.set(data.get("entry_var2", "0"))
             # load_window_geometry가 True일 경우에만 window_geometry 정보 로드
            if load_window_geometry:
                app.geometry(all_data.get("window_geometry", ""))
    except (FileNotFoundError, ValueError) as e:
        print(e)
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

# menu 클릭이벤트 함수
def on_menu_click(event):
    # 클릭된 메뉴의 이름을 `configure_title()` 함수로 전달하여 타이틀 변경
    menu_name = event.widget.cget("text")
    configure_title(menu_name)
    # window_geometry 로딩을 건너뜀
    # 메뉴 아이템 클릭 시 해당 데이터 로드
    load_data(menu_name, load_window_geometry=False)
    # 로드된 이미지 경로를 사용하여 이미지 표시
    for i, path in enumerate(image_paths):
        if path:
            label = getattr(app, f'label_image{i+1}')
            display_image(label, path)

# title 수정 함수
def configure_title(menu_name=None):
    # `menu_name`이 주어지면 타이틀 변경, 아니면 기본값 사용
    if menu_name is None or menu_name == baemin["text"]:
        app.frame_title.config(bg=baemin["color"])
        app.label_title.config(text=baemin["text"], bg=baemin["color"])
        app.menu_item2.config(bg="gainsboro")
        app.menu_item3.config(bg="white")
        app.menu_item6.config(bg="white")
    elif menu_name == yogiyo["text"]:
        app.frame_title.config(bg=yogiyo["color"])
        app.label_title.config(text=yogiyo["text"], bg=yogiyo["color"])
        app.menu_item2.config(bg="white")
        app.menu_item3.config(bg="gainsboro")
        app.menu_item6.config(bg="white")
    elif menu_name == manna["text"]:
        app.frame_title.config(bg=manna["color"])
        app.label_title.config(text=manna["text"])
        app.menu_item2.config(bg="white")
        app.menu_item3.config(bg="white")
        app.menu_item6.config(bg="gainsboro")
        
        
def update_value(entry_var, change):
    # 현재 엔트리의 값 가져오기
    current_value = int(entry_var.get())
    # 새로운 값 계산
    new_value = max(0, current_value + change)  # 0 미만으로 내려가지 않도록 처리
    # 새로운 값으로 StringVar 업데이트
    entry_var.set(str(new_value))
    save_data()  # 엔트리 값이 변경될 때마다 저장
    
def toggle():
    if app.button_onoff.config('text')[-1] == 'OFF':
        app.button_onoff.config(text='ON', bg='lightgrey')
    else:
        app.button_onoff.config(text='OFF', bg='lightgrey')
    save_data()  # 버튼 상태가 변경될 때마다 저장
    
def show_message(event):
    messagebox.showinfo("공지", "기능 준비 중입니다.")

def main():
    configure_title()
    # 프로그램 시작 시 데이터 로딩
    on_opening(app)
    
    app.label_image1.name = "label_image1"
    app.label_image2.name = "label_image2"
    app.label_image3.name = "label_image3"

    # 각 메뉴 항목에 클릭 이벤트 바인딩
    app.menu_item2.bind("<Button-1>", on_menu_click)
    app.menu_item3.bind("<Button-1>", on_menu_click)
    app.menu_item4.bind("<Button-1>", show_message)
    #app.menu_item6.bind("<Button-1>", on_menu_click)
    app.menu_item7.bind("<Button-1>", show_message)
    
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