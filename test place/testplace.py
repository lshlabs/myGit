import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import json

class ImageFrameApp:
    def __init__(self, root):
        self.root = root
        self.images = [None, None, None]  # 이미지 경로를 저장할 리스트
        self.image_labels = []  # 이미지 라벨 위젯을 저장할 리스트
        self.load_data()  # 이전 상태 불러오기

        for i in range(3):
            frame = tk.Frame(root, width=200, height=200, borderwidth=2, relief='groove')
            frame.pack(side='left', padx=10, pady=10)
            frame.propagate(False)  # 프레임 크기 고정
            
            # 이미지 레이블 추가, 레이블 크기를 프레임과 동일하게 설정
            label = tk.Label(frame, width=200, height=200)
            label.pack(expand=True, fill='both')
            label.bind('<Button-1>', lambda event, index=i: self.select_image(index))
            self.image_labels.append(label)
            
            # 저장된 이미지가 있으면 표시
            if self.images[i]:
                self.display_image(i, self.images[i])
        
        # 종료 이벤트 처리
        root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def select_image(self, index):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.images[index] = file_path
            self.display_image(index, file_path)

    def display_image(self, index, file_path):
        image = Image.open(file_path)
        image = image.resize((200, 200), Image.Resampling.LANCZOS)  # 이미지를 레이블 크기에 맞게 조절
        photo = ImageTk.PhotoImage(image)
        
        label = self.image_labels[index]
        label.configure(image=photo)
        label.image = photo  # 참조를 유지, 이 부분이 중요합니다!

    def on_closing(self):
        self.save_data()
        self.root.destroy()

    def save_data(self):
        with open('image_data.json', 'w') as f:
            json.dump(self.images, f)

    def load_data(self):
        try:
            with open('image_data.json', 'r') as f:
                self.images = json.load(f)
        except FileNotFoundError:
            self.images = [None, None, None]

if __name__ == '__main__':
    root = tk.Tk()
    root.title("이미지 액자 앱")
    root.geometry("660x220")  # 창의 초기 크기 설정
    root.resizable(True, True)  # 창의 크기 조절 가능

    app = ImageFrameApp(root)
    root.mainloop()
