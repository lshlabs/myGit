import tkinter as tk

def toggle():
    if button.config('text')[-1] == 'Off':
        button.config(text='On', bg='lightgreen')
    else:
        button.config(text='Off', bg='lightgrey')

root = tk.Tk()
root.title("간단한 On/Off 토글 스위치")

# 토글 스위치 역할을 할 Button 위젯 생성 및 배치
button = tk.Button(root, text='Off', width=10, command=toggle, bg='lightgrey')
button.pack(pady=20)

root.mainloop()
