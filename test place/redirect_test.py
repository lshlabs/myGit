import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Real-time Console Output to Text Widget")

        # Text 위젯 생성
        self.text_widget = tk.Text(root, wrap='word')
        self.text_widget.pack(expand=True, fill='both')

        # 버튼 생성
        self.button = tk.Button(root, text="Print Message", command=self.on_button_click)
        self.button.pack()

    def on_button_click(self):
        """버튼 클릭 시 호출되는 메서드"""
        message = "버튼이 눌렸습니다.\n"
        print(message)  # 콘솔에 메시지 출력
        self.text_widget.insert(tk.END, message)  # Text 위젯에 메시지 추가
        self.text_widget.see(tk.END)  # 항상 마지막으로 스크롤

def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()