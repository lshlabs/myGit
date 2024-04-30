import tkinter as tk
from test_ui import setup_ui

def show_frames():
    for frame in frames[3:]:
        frame.grid()
    scrollbar.pack(side="right", fill='both')
    title_frame.config(bg="#FA0150")
    title_label.config(text="요기요", bg="#FA0150")

def hide_frames():
    for frame in frames[3:]:
        frame.grid_forget()   
    scrollbar.pack_forget()
    title_frame.config(bg="#45D3D3")
    title_label.config(text="배달의 민족", bg="#45D3D3")
   
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x400")
    root.title('테스트 예제')

    content_canvas, frames, menu_frame, uni_frame, scrollbar, title_frame, title_label = setup_ui(root)
    
    # 버튼 추가 및 기능 연결
    button1 = tk.Button(menu_frame, text="메뉴 1", command=hide_frames)
    button1.pack(padx=10, pady=5, fill=tk.X)

    button2 = tk.Button(menu_frame, text="메뉴 2", command=show_frames)
    button2.pack(padx=10, pady=5, fill=tk.X)

    hide_frames()

    root.mainloop()