import tkinter as tk
from test_ui import setup_ui

def on_configure(event):
    content_canvas.configure(scrollregion=content_canvas.bbox("all"))

def show_frames():
    for frame in frames[3:]:
        frame.grid()

def hide_frames():
    for frame in frames[3:]:
        frame.grid_remove()
        
def on_mousewheel(event):
    # MacOS에서는 event.delta 값이 다를 수 있으니 주의
    # Linux에서는 '<Button-4>'와 '<Button-5>' 사용
    try:
        # Windows와 MacOS
        scroll = int(-1*(event.delta/120))
    except AttributeError:
        # Linux에서는 event.delta가 없으므로 event.num을 사용하여 스크롤 방향 결정
        if event.num == 4:
            scroll = -1
        else:
            scroll = 1
    content_canvas.yview_scroll(scroll, "units")

def bind_mousewheel(widget):
    widget.bind("<MouseWheel>", on_mousewheel)  # Windows와 MacOS
    widget.bind("<Button-4>", on_mousewheel)  # Linux
    widget.bind("<Button-5>", on_mousewheel)  # Linux
   
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x400")
    root.title('테스트 예제')

    content_canvas, frames, menu_frame = setup_ui(root)
    
    # 모든 플랫폼에서 마우스 휠 바인딩
    bind_mousewheel(content_canvas)

    inner_frame = content_canvas.winfo_children()[0]
    inner_frame.bind("<Configure>", on_configure)
    # inner_frame에도 바인딩 추가, 스크롤 영역 확장을 위해
    bind_mousewheel(inner_frame)

    # 버튼 추가 및 기능 연결
    button1 = tk.Button(menu_frame, text="메뉴 1", bg='lightgrey', command=hide_frames)
    button1.pack(padx=10, pady=5, fill=tk.X)

    button2 = tk.Button(menu_frame, text="메뉴 2", bg='lightgrey', command=show_frames)
    button2.pack(padx=10, pady=5, fill=tk.X)

    # 프로그램 시작 시 스크롤바 숨기기
    hide_frames()

    root.mainloop()