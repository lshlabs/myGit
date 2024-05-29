# test.py
import tkinter as tk
import json, os
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
from numpy import save
from test_ui import setup_ui
from test_setting import open_sub_window

baemin = {"text": "배달의 민족", "color": "#45D3D3"}
yogiyo = {"text": "요기요", "color": "#FA0150"}
manna = {"text": "만나", "color": "#ff6b00"}

# 이미지 경로를 저장할 딕셔너리
image_paths = {i: None for i in range(12)}

def update_layout(bind_scroll=True):
    scrollbar.pack_forget() if not bind_scroll else scrollbar.pack(side="right", fill='both')
    content_canvas.yview_moveto(0.0)  # 스크롤을 최상단으로 이동
    if bind_scroll:
        scrollable_frame.bind("<MouseWheel>", on_mousewheel)
    else:
        scrollable_frame.unbind("<MouseWheel>")

def update_value(entry_var, change):
    # 현재 엔트리의 값 가져오기
    current_value = int(entry_var.get())
    # 새로운 값 계산
    new_value = max(0, current_value + change)  # 0 미만으로 내려가지 않도록 처리
    # 새로운 값으로 StringVar 업데이트
    entry_var.set(str(new_value))
    save_data()  # 엔트리 값이 변경될 때마다 저장

# 이미지 선택 함수
def select_image(event, label):
    file_path = filedialog.askopenfilename()
    # 'label_image'를 제거하여 순수 숫자 부분만 추출
    index_str = label.name.replace('label_image', '')  # 'label_image' 문자열을 제거
    if index_str.isdigit():  # 추출된 부분이 숫자인지 확인
        index = int(index_str) - 1  # 숫자로 변환
        image_paths[index] = file_path # 파일 경로 저장
        display_image(label, image_paths[index]) # 올바른 파일 경로를 전달
    else:
        return  # 숫자가 아니면 함수 종료

    if file_path:
        image_paths[index] = file_path  # 인덱스를 사용하여 image_paths 딕셔너리에 경로 저장
        display_image(label, file_path)
    else:
        # 경로가 없는 경우, label을 변경하지 않음
        print(f"No image path for label {index}, leaving it unchanged.")

# 이미지 디스플레이 함수
def display_image(frame, file_path):
    try:
        image = Image.open(file_path)
        image = image.resize((120, 120), Image.Resampling.LANCZOS)     
        photo = ImageTk.PhotoImage(image)
        frame.configure(image=photo)
        frame.image = photo  # 참조를 유지
        print("Attempting to open image at:", file_path)  # 경로 로그 출력
    except Exception as e:
        print(f"Failed to open image: {e}")

# 데이터 저장 함수
def save_data():
    program_id = title_label.cget("text")
    data = {}
    # 각 프로그램 ID에 따라 다르게 저장할 데이터 설정
    if program_id == "배달의 민족":
        data[program_id] = {
            "image_paths": image_paths,
            "entry_var1": entry_var1.get(),
            "entry_var2": entry_var2.get()
        }
    elif program_id == "요기요":
        data[program_id] = {
            "image_paths": image_paths,
            "entry_var1": entry_var1.get(),
            "entry_var2": entry_var2.get()
        }
    elif program_id == "만나":
        data[program_id] = {
            "image_paths": image_paths,
            "entry_var2": entry_var2.get()
        }
    # 윈도우 위치 저장
    data_window_position = {
        "window_geometry": root.geometry()
    }
    # 전체 데이터를 불러오기
    try:
        with open('data2_win.json', 'r', encoding='utf-8') as f:
            try:
                all_data = json.load(f)
            except json.JSONDecodeError:
                all_data = {}
    except FileNotFoundError:
        all_data = {}

    # 현재 프로그램의 데이터를 업데이트
    all_data.update(data)
    # window_geometry 데이터 업데이트
    all_data.update(data_window_position)

    # 데이터 저장
    with open('data2_win.json', 'w', encoding='utf-8') as f:
        json.dump(all_data, f, indent=4, ensure_ascii=False)

    print(f"Data saved for {program_id}")

def load_data(menu_name=None, load_window_geometry=True):
    global image_paths
    # program_id 대신 menu_name을 사용하여 데이터 로드
    program_id = menu_name if menu_name else title_label.cget("text")
    try:
        with open('data2_win.json', 'r', encoding='utf-8') as f:
            all_data = json.load(f)
            data = all_data.get(program_id, {})

            loaded_paths = data.get("image_paths", {str(i): None for i in range(12)})
            image_paths = {int(k): v for k, v in loaded_paths.items() if v is not None}

            if menu_name == manna["text"]:
                entry_var1.set(data.get("entry_var1", "15"))
            else:
                entry_var1.set(data.get("entry_var1", "50"))
                entry_var2.set(data.get("entry_var2", "15"))

            if load_window_geometry:
                root.geometry(all_data.get("window_geometry", ""))
    except FileNotFoundError:
        print("data2_win.json 파일을 찾을 수 없습니다. 기본값을 사용합니다.")
        image_paths = {i: None for i in range(12)}
    except json.JSONDecodeError:
        print("JSON 파일을 해석하는 데 오류가 발생했습니다. 기본값을 사용합니다.")
        image_paths = {i: None for i in range(12)}
    except Exception as e:
        print(f"예상치 못한 오류가 발생했습니다: {e}")
        image_paths = {i: None for i in range(12)}

    # 로드된 이미지 경로를 사용하여 이미지 표시
    for i, path in image_paths.items():
        label = ilabels[i]
        if path:
            display_image(label, str(path))
        else:
            # 경로가 없는 경우, label을 변경하지 않음
            print(f"No image path for label {i}, leaving it unchanged.")

# menu 클릭이벤트 함수
def on_menu_click(event):
    save_data()
    # 클릭된 메뉴의 이름을 `configure_title()` 함수로 전달하여 타이틀 변경
    menu_name = event.widget.cget("text")
    configure_title(menu_name)
    # window_geometry 로딩을 건너뜀
    # 메뉴 아이템 클릭 시 해당 데이터 로드
    load_data(menu_name, load_window_geometry=False)
    # 로드된 이미지 경로를 사용하여 이미지 표시
    # for i, path in image_paths.items():  # items()로 키와 값을 함께 가져옵니다
    #      if path:
    #         label = ilabels[i]
    #         display_image(label, path)

def configure_title(menu_name=None):
    if menu_name == baemin["text"]:
        manage_frames_visibility(0, 3, True)  # Displaying iframes 0-2
        oframes[0].grid(row=5)
        oframes[1].grid(row=6)
        oframes[2].grid(row=7)
        title_frame.config(bg=baemin["color"])
        title_label.config(text=baemin["text"], bg=baemin["color"])
        menu_item2.config(bg="gainsboro")
        menu_item3.config(bg="white")
        menu_item6.config(bg="white")
    elif menu_name == yogiyo["text"]:
        manage_frames_visibility(3, 6, True)  # Displaying iframes 3-5
        oframes[0].grid(row=5)
        oframes[1].grid(row=6)
        oframes[2].grid(row=7)
        title_frame.config(bg=yogiyo["color"])
        title_label.config(text=yogiyo["text"], bg=yogiyo["color"])
        menu_item2.config(bg="white")
        menu_item3.config(bg="gainsboro")
        menu_item6.config(bg="white")
    elif menu_name == manna["text"]:
        manage_frames_visibility(6, 12, True)  # Displaying iframes 6-11
        oframes[1].grid_remove()
        oframes[0].grid(row=10)
        oframes[2].grid(row=11)
        title_frame.config(bg=manna["color"])
        title_label.config(text=manna["text"], bg=manna["color"])
        menu_item2.config(bg="white")
        menu_item3.config(bg="white")
        menu_item6.config(bg="gainsboro")
    update_layout(menu_name == manna["text"])

def manage_frames_visibility(start, end, visible):
    # 모든 프레임을 숨김
    for i in range(len(iframes)):
        iframes[i].grid_remove()
        inames[i].grid_remove()
        ilabels[i].pack_forget()

    # 지정된 범위의 프레임만 표시
    for i in range(start, end):
        iframes[i].grid()
        inames[i].grid()
        ilabels[i].pack()

def on_mousewheel(event):
    content_canvas.yview_scroll(int(-1*(event.delta/120)), "units")

# 프로그램 종료 시 실행할 함수
def on_closing():
    save_data()
    root.destroy()
    
# 프로그램 시작 시 실행할 함수
def on_opening(app):
    load_data(load_window_geometry=True)
    # 로드된 이미지 경로를 사용하여 이미지 표시
    for i, path in image_paths.items():  # items()로 키와 값을 함께 가져옵니다
        if path:
            label = ilabels[i]
            display_image(label, path)
        else:
            # 경로가 없는 경우, label을 변경하지 않음
            print(f"No image path for label {i}, leaving it unchanged.")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("700x500")
    root.resizable(False, False)
    root.title('매크로')
    
    (title_label, content_canvas, iframes, ilabels, inames, menu_frame, uni_frame, scrollbar, title_frame, title_label, scrollable_frame, btn_setting,
    menu_item2, menu_item3, menu_item4, menu_item6, menu_item7, setting_icon_photo, entry_var1, entry_var2, oframes, obtn_m1, obtn_m2, obtn_p1, obtn_p2) = setup_ui(root)

    configure_title(baemin["text"])
    on_opening(root)

    menu_item2.bind("<Button-1>", on_menu_click)
    menu_item3.bind("<Button-1>", on_menu_click)
    menu_item6.bind("<Button-1>", on_menu_click)
    
    # 각 이미지 프레임 및 라벨에 이벤트 바인딩
    for i in range(12):
        ilabels[i].name = f"label_image{i+1}"
        iframes[i].bind("<Button-1>", lambda event, idx=i: select_image(event, ilabels[idx]))
        ilabels[i].bind("<Button-1>", lambda event, idx=i: select_image(event, ilabels[idx]))

    obtn_p1.config(command=lambda: update_value(entry_var1, +5))
    obtn_m1.config(command=lambda: update_value(entry_var1, -5))
    obtn_p2.config(command=lambda: update_value(entry_var2, +5))
    obtn_m2.config(command=lambda: update_value(entry_var2, -5))
    
    btn_setting.config(command=lambda: open_sub_window(root))

    # 종료 이벤트 처리
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()
