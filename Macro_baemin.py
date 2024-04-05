import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter import messagebox
from Macro_layer1_ui import App  # Macro_main_ui 모듈에서 App 클래스를 가져옵니다.

app = App()  # App 인스턴스를 생성하고, tkinter의 메인 윈도우를 master로 설정합니다.
color_baemin = "#45D3D3"

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
        
def on_image_frame_click(event, label_widget):
    # 파일 선택 다이얼로그 열기
    file_path = filedialog.askopenfilename(
        title='이미지 선택',
        filetypes=(('PNG 이미지', '*.png'), ('JPEG 이미지', '*.jpg;*.jpeg'), ('모든 파일', '*.*'))
    )
    
    if file_path:  # 파일이 선택되었다면
        # 이미지를 표시할 라벨 위젯에 접근
        display_thumbnail(file_path, label_widget)

def display_thumbnail(file_path, image_label):
    # 이미지 로드
    image = Image.open(file_path)
    # 이미지를 120x120 크기로 리사이징
    resized_image = image.resize((120, 120), Image.Resampling.LANCZOS)
    # Tkinter와 호환되는 이미지로 변환
    photo = ImageTk.PhotoImage(resized_image)
    # 이미지 라벨에 이미지 표시
    image_label.config(image=photo)
    # 중요: 이미지 라벨 위젯에 이미지 객체에 대한 참조를 저장하여 유지
    image_label.image = photo

def main():
    configure_title()
    
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
    app.frame_image1.bind("<Button-1>", lambda event: on_image_frame_click(event, app.label_image1))
    app.frame_image2.bind("<Button-1>", lambda event: on_image_frame_click(event, app.label_image2))
    app.frame_image3.bind("<Button-1>", lambda event: on_image_frame_click(event, app.label_image3))
    #app.frame_image4.bind("<Button-1>", lambda event: on_image_frame_click(event, app.label_image4))
    #app.frame_image5.bind("<Button-1>", lambda event: on_image_frame_click(event, app.label_image5))
    #app.frame_image6.bind("<Button-1>", lambda event: on_image_frame_click(event, app.label_image6))
    
    app.label_image1.bind("<Button-1>", lambda event: on_image_frame_click(event, app.label_image1))
    app.label_image2.bind("<Button-1>", lambda event: on_image_frame_click(event, app.label_image2))
    app.label_image3.bind("<Button-1>", lambda event: on_image_frame_click(event, app.label_image3))
    #app.label_image4.bind("<Button-1>", lambda event: on_image_frame_click(event, app.label_image4))
    #app.label_image5.bind("<Button-1>", lambda event: on_image_frame_click(event, app.label_image5))
    #app.label_image6.bind("<Button-1>", lambda event: on_image_frame_click(event, app.label_image6))

    app.mainloop()

if __name__ == "__main__":
    main()
