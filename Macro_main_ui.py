import tkinter as tk
import os

root = tk.Tk()
root.geometry('700x500')  # 창의 크기를 너비 700픽셀, 높이 500픽셀로 설정
root.resizable(False, False)  # 창의 가로 및 세로 크기 조정을 비활성화
root.title('매크로')  # 창의 제목을 '매크로'로 설정
root.configure(bg='white', padx=20, pady=20)  # 창의 배경색을 흰색으로 설정, 내부 여백을 20픽셀로 설정

position_file = 'window_position.txt'
if os.path.exists(position_file):
    with open(position_file, 'r') as f:
        position = f.read()
    root.geometry(position)

# 셀 생성
cells = {i: tk.Label(root, text="", bg='white', font=("Helvetica", 15)) for i in range(7)}
merged_cell = tk.Label(root, text="합병된 셀", bg='white', font=("Helvetica", 15))

# 셀 배치
for i in range(7):
    cells[i].grid(row=i, column=0, sticky="nsew", pady=(0, 1))  # 각 셀은 2의 배수 행에 배치
merged_cell.grid(row=0, column=1, rowspan=7, sticky="nsew")  # 합병된 셀은 모든 행에 걸쳐 배치

# 셀 속성 설정
cells[0].config(text="배달 플랫폼", bg='purple', fg='white')  # 배달 플랫폼 셀
cells[1].config(text="배달의 민족",fg='black')
cells[2].config(text="요기요", fg='black')
cells[3].config(text="+", fg='black')
cells[4].config(text="배차 플랫폼", bg='purple', fg='white')  # 배차 플랫폼 셀
cells[5].config(text="만나", fg='black')
cells[6].config(text="+", fg='black')

root.grid_columnconfigure(0, weight=2)
root.grid_columnconfigure(1, weight=8)
for i in range(7):
    root.grid_rowconfigure(i, weight=1)

def save_position(event):
    with open(position_file, 'w') as f:
        f.write(root.geometry())

root.bind('<Destroy>', save_position)

def highlight_cell(event):
    for i in [1, 2, 5]:
        cells[i].config(bg='white')
    event.widget.config(bg='lightgray')

for i in [1, 2, 5]:
    cells[i].bind('<Button-1>', highlight_cell)

root.mainloop()
