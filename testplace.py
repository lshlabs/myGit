import tkinter as tk

def change_frame_and_text_color(frame, text_widget, frame_color, text_color):
    """
    Frame의 배경색과 내부 Text 위젯의 텍스트 색상을 변경하는 함수입니다.
    
    :param frame: 색상을 변경할 Frame 객체입니다.
    :param text_widget: 색상을 변경할 Text 위젯 객체입니다.
    :param frame_color: Frame의 새 배경색입니다.
    :param text_color: Text 위젯의 새 텍스트 색상입니다.
    """
    # Frame의 배경색 변경
    frame.config(bg=frame_color)
    # Text 위젯의 텍스트 색상 변경
    text_widget.config(fg=text_color)

# Tkinter 창 생성
root = tk.Tk()
root.title("Frame과 Text 색상 변경 예제")

# Frame 생성 및 배치
frame = tk.Frame(root, width=200, height=100)
frame.pack(padx=10, pady=10)

# Label 생성 및 Frame 내에 배치
label = tk.Label(frame, text="안녕하세요!", font=('Arial', 16))
label.pack(pady=10)

# 색상 변경 버튼 생성 및 클릭 이벤트 연결
color_change_btn = tk.Button(root, text="색상 변경", command=lambda: change_frame_and_text_color(frame, label, "blue", "white"))
color_change_btn.pack(pady=10)

root.mainloop()
