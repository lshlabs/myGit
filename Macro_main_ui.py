import tkinter as tk
import os

# App 클래스는 tk.Tk를 상속하여 만든 메인 애플리케이션 클래스입니다.
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # 창 크기, 리사이즈 가능 여부, 타이틀 설정
        self.geometry('700x500')
        self.resizable(False, False)
        self.title('매크로')
        self.configure(bg='gainsboro', padx=20, pady=20)
        
        # 창 위치를 불러오고, 메뉴와 콘텐츠 영역을 생성합니다.
        self.load_window_position()
        self.create_menu()
        self.create_content_area()
        
    # 창 위치를 불러오는 함수입니다. 파일이 존재하면 그 위치에 창을 배치합니다.
    def load_window_position(self):
        position_file = 'window_position.txt'
        if os.path.exists(position_file):
            with open(position_file, 'r') as f:
                position = f.read()
            self.geometry(position)
    
    # 메뉴를 생성하는 함수입니다.
    def create_menu(self):
        menu_frame = tk.Frame(self, width=140, height=460, bd=1, relief='solid', bg='white')
        menu_frame.grid(padx=(0, 10))
        menu_frame.grid_propagate(False)  # 프레임 크기 고정

        # 메뉴 아이템과 색상, 그리고 폰트 크기 설정
        menu_items = [
            ("배달 플랫폼", "purple", "white", 12),
            ("배달의 민족", "white", "black", 12),
            ("요기요", "white", "black", 12),
            ("+", "white", "black", 13),
            ("배차 플랫폼", "purple", "white", 12),
            ("만나", "white", "black", 12),
            ("+", "white", "black", 12)
            ]

        # 메뉴 아이템 생성
        for i, (text, bg, fg, font_size) in enumerate(menu_items):
            label = tk.Label(menu_frame, text=text, bg=bg, fg=fg, 
                      font=('default',font_size),  # 폰트 크기 설정
                      width=20, height=2, anchor='center')
            label.grid(row=i, column=0, sticky='nsew')  # sticky 옵션으로 상하좌우 여백 없이 꽉 채움

        # 프레임 내부의 모든 행과 열에 대해 동일한 공간 배분
        for i in range(len(menu_items)):
            menu_frame.grid_rowconfigure(i, weight=1)
        menu_frame.grid_columnconfigure(0, weight=1)

            
    # 콘텐츠 영역을 생성하는 함수입니다.
    def create_content_area(self):
        content_frame = tk.Frame(self, bd=1, width=500, height=460, relief='solid', bg='white')
        content_frame.grid(row=0, column=1)
        
        # 콘텐츠 프레임을 채웁니다.
        self.create_widgets()
        
    # 콘텐츠 프레임에 내용을 채우는 함수입니다.
    def create_widgets(self):
        label_tip = tk.Label(text='※ 이미지를 클릭하여 등록해주세요', bg='white')
        label_tip.place(x=170, y=8)
        # 이미지 프레임 생성 및 배치
        frame1 = tk.Frame(self, width=120, height=120, bg='grey', bd=1)
        frame2 = tk.Frame(self, width=120, height=120, bg='grey', bd=1)
        frame3 = tk.Frame(self, width=120, height=120, bg='grey', bd=1)
        frame4 = tk.Frame(self, width=120, height=120, bg='grey', bd=1)
        frame5 = tk.Frame(self, width=120, height=120, bg='grey', bd=1)
        frame6 = tk.Frame(self, width=120, height=120, bg='grey', bd=1)
        frame1.place(x=180,y=40)
        frame2.place(x=345,y=40)
        frame3.place(x=510,y=40)
        frame4.place(x=180,y=200)
        frame5.place(x=345,y=200)
        frame6.place(x=510,y=200)
        
        # 이미지 레이블 생성 및 배치
        label_image1 = tk.Label(text="image 1")
        label_image2 = tk.Label(text="image 2")
        label_image3 = tk.Label(text="image 3")
        label_image4 = tk.Label(text="image 4")
        label_image5 = tk.Label(text="image 5")
        label_image6 = tk.Label(text="image 6")
        label_image1.place(x=180, y=150, width=120)
        label_image2.place(x=345, y=150, width=120)
        label_image3.place(x=510, y=150, width=120)
        label_image4.place(x=180, y=310, width=120)
        label_image5.place(x=345, y=310, width=120)
        label_image6.place(x=510, y=310, width=120)
        
        # Frame 위젯 생성 및 배치
        frame_option1 = tk.Frame(self, height=30, bg='white')  # Frame 높이 설정
        frame_option1.place(x=180, y=350)  # Frame을 윈도우에 패딩과 함께 배치
        
        # 기타 옵션 레이블 생성 및 Frame 내에 배치
        label_reception = tk.Label(frame_option1, text="기본 접수시간(분)", bg='white', font=('default', 10))
        label_reception.grid(row=0, column=0, padx=(0, 10), sticky='w')
        
        # '-' 버튼 생성 및 Frame 내에 배치
        btn_decrease = tk.Button(frame_option1, text='-')
        btn_decrease.grid(row=0, column=1, sticky='ew')
        
        # Entry 위젯 생성 및 Frame 내에 배치, 비활성화 상태로 설정
        entry = tk.Entry(frame_option1, justify='center', width=5)
        entry.grid(row=0, column=2, padx=5, sticky='ew')
        entry.insert(0, "50")
        entry.config(state=tk.DISABLED)  # 사용자의 직접 입력을 방지
        
        # '+' 버튼 생성 및 Frame 내에 배치
        btn_increase = tk.Button(frame_option1, text='+')
        btn_increase.grid(row=0, column=3, sticky='ew')

        # Grid column 설정
        frame_option1.grid_columnconfigure(2, weight=1)  # Entry 위젯이 있는 열의 너비를 가변적으로 설정
        
        

    # 창이 닫힐 때 현재 창 위치를 저장하는 함수입니다.
    def save_position(self, event):
        position_file = 'window_position.txt'
        with open(position_file, 'w') as f: 
            f.write(self.geometry())

if __name__ == "__main__":
    app = App()
    app.mainloop()
