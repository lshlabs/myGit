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
    content_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
   

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x400")
    root.title('테스트 예제')

    content_canvas, frames, menu_frame = setup_ui(root)
    
    # Windows와 MacOS에서는 '<MouseWheel>' 사용
    content_canvas.bind('<MouseWheel>', on_mousewheel)

    inner_frame = content_canvas.winfo_children()[0]
    inner_frame.bind("<Configure>", on_configure)

    # 버튼 추가 및 기능 연결
    button1 = tk.Button(menu_frame, text="메뉴 1", bg='lightgrey', command=hide_frames)
    button1.pack(padx=10, pady=5, fill=tk.X)

    button2 = tk.Button(menu_frame, text="메뉴 2", bg='lightgrey', command=show_frames)
    button2.pack(padx=10, pady=5, fill=tk.X)

    # 프로그램 시작 시 스크롤바 숨기기
    hide_frames()

    root.mainloop()
