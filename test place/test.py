import tkinter as tk
from test_ui import setup_ui

def menu1():
    global labels
    for frame in frames[3:]:
        frame.grid_remove()
    for label in labels[18:]:
        label.grid_remove()
    scrollbar.pack_forget()
    title_frame.config(bg="#45D3D3")
    title_label.config(text="배달의 민족", bg="#45D3D3")
    content_canvas.yview_moveto(0.0)    # 스크롤을 최상단으로 이동
    scrollable_frame.unbind("<MouseWheel>")  # 마우스 휠 이벤트 바인딩 제거
    
def menu2():
    global labels
    for frame in frames[3:]:
        frame.grid_remove()
    for label in labels[18:]:
        label.grid_remove()
    scrollbar.pack_forget()
    title_frame.config(bg="#FA0150")
    title_label.config(text="요기요", bg="#FA0150")
    content_canvas.yview_moveto(0.0)    # 스크롤을 최상단으로 이동
    scrollable_frame.unbind("<MouseWheel>")  # 마우스 휠 이벤트 바인딩 제거

def menu3():
    global labels
    for frame in frames[3:]:
        frame.grid()
    for label in labels[18:]:
        label.grid()
    scrollbar.pack(side="right", fill='both')
    title_frame.config(bg="#ff6b00")
    title_label.config(text="만나", bg="#ff6b00")
    content_canvas.yview_moveto(0.0)    # 스크롤을 최상단으로 이동
    scrollable_frame.bind("<MouseWheel>", on_mousewheel)  # 마우스 휠 이벤트 바인딩
    
def on_mousewheel(event):
    # Windows 사용 시
    content_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
   
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x400")
    root.resizable(False, False)
    root.title('테스트 예제')

    content_canvas, frames, menu_frame, uni_frame, scrollbar, title_frame, title_label, scrollable_frame, labels = setup_ui(root)
    
    # 버튼 추가 및 기능 연결
    button1 = tk.Button(menu_frame, text="배민", command=menu1)
    button1.pack(padx=10, pady=5, fill=tk.X)

    button2 = tk.Button(menu_frame, text="요기요", command=menu2)
    button2.pack(padx=10, pady=5, fill=tk.X)
    
    button3 = tk.Button(menu_frame, text="만나", command=menu3)
    button3.pack(padx=10, pady=5, fill=tk.X)


    menu1()

    root.mainloop()