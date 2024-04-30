import tkinter as tk

root = tk.Tk()

# 외부 Canvas (스크롤되는 영역)
outer_canvas = tk.Canvas(root, width=500, height=450)
outer_canvas.pack()

# 스크롤바 생성 및 연동
scroll_y = tk.Scrollbar(root, orient="vertical", command=outer_canvas.yview)
scroll_y.pack(side="right", fill="y")
outer_canvas.config(yscrollcommand=scroll_y.set)

# 내부 Frame (실제 콘텐츠를 포함하는 부분, 500x500)
frame = tk.Frame(outer_canvas)
frame_id = outer_canvas.create_window((0, 0), window=frame, anchor='nw')

# 예시 콘텐츠 배치 (500x500 크기 설정 가능)
for i in range(25):
    tk.Label(frame, text=f"Item {i+1}").pack()

# 내부 컨텐츠 사이즈 업데이트를 위한 함수
def update_scrollregion(event):
    outer_canvas.configure(scrollregion=outer_canvas.bbox('all'))

# 콘텐츠 사이즈에 따라 스크롤 영역 업데이트
frame.bind("<Configure>", update_scrollregion)

root.mainloop()
