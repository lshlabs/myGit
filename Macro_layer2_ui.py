import tkinter as tk
from tkinter import ttk
import os

class App(tk.Tk):
    def __init__(self, master=None):
        super().__init__(master)
        self.geometry('700x500')
        self.resizable(False, False)
        self.title('매크로')
        self.configure(bg='gainsboro', padx=20, pady=20)
        self.load_window_position()
        self.create_menu()
        self.create_content()
        
    def toggle(self):
        if self.button_onoff.config('text')[-1] == 'Off':
            self.button_onoff.config(text='On', bg='lightgreen')
        else:
            self.button_onoff.config(text='Off', bg='lightgrey')

    def load_window_position(self):
        position_file = 'data.txt'
        if os.path.exists(position_file):
            with open(position_file, 'r') as f:
                self.geometry(f.read())

    def create_menu(self):
        menu_frame = tk.Frame(self, width=140, height=460, bd=1, relief='solid', bg='white')
        menu_frame.grid(padx=(0, 10))
        menu_frame.grid_propagate(False)

        # 개별 메뉴 항목 생성 및 배치
        self.menu_item1 = tk.Label(menu_frame, text="배달 플랫폼", bg="purple", fg="white", font=('default', 12), width=20, height=2, anchor='center')
        self.menu_item1.grid(row=0, column=0, sticky='nsew')

        self.menu_item2 = tk.Label(menu_frame, text="배달의 민족", bg="white", fg="black", font=('default', 12), width=20, height=2, anchor='center')
        self.menu_item2.grid(row=1, column=0, sticky='nsew')

        self.menu_item3 = tk.Label(menu_frame, text="요기요", bg="white", fg="black", font=('default', 12), width=20, height=2, anchor='center')
        self.menu_item3.grid(row=2, column=0, sticky='nsew')

        self.menu_item4 = tk.Label(menu_frame, text="+", bg="white", fg="black", font=('default', 13), width=20, height=2, anchor='center')
        self.menu_item4.grid(row=3, column=0, sticky='nsew')

        self.menu_item5 = tk.Label(menu_frame, text="배차 플랫폼", bg="purple", fg="white", font=('default', 12), width=20, height=2, anchor='center')
        self.menu_item5.grid(row=4, column=0, sticky='nsew')

        self.menu_item6 = tk.Label(menu_frame, text="만나", bg="white", fg="black", font=('default', 12), width=20, height=2, anchor='center')
        self.menu_item6.grid(row=5, column=0, sticky='nsew')

        self.menu_item7 = tk.Label(menu_frame, text="+", bg="white", fg="black", font=('default', 12), width=20, height=2, anchor='center')
        self.menu_item7.grid(row=6, column=0, sticky='nsew')

        # 각 행에 대한 가중치 설정
        for i in range(7):
            menu_frame.grid_rowconfigure(i, weight=1)
        menu_frame.grid_columnconfigure(0, weight=1)

    def create_content(self):
        content_frame = tk.Frame(self, bd=1, width=500, height=460, relief='solid', bg='white')
        content_frame.grid(row=0, column=1)
        self.create_widgets()

     # 콘텐츠 프레임에 내용을 채우는 함수입니다.
    def create_widgets(self):
        # 상단 타이틀 부분
        self.frame_title = tk.Frame(self, width=500, height=66, bg='grey', relief='solid', bd=1)
        self.frame_title.place(x=150,y=0)
        self.frame_title.pack_propagate(False)
        
        self.label_title = tk.Label(self.frame_title, text="@platform name", bg='grey', fg='white', font=('default',25))
        self.label_title.pack(padx=15, pady=10, anchor='w')
        
        self.button_onoff = tk.Button(self.frame_title, text='OFF', width=5, height=2, bg='grey')
        self.button_onoff.place(x=400, y=10)
        
        label_tip = tk.Label(text='※ 이미지를 클릭하여 등록해주세요', bg='white')
        label_tip.place(x=170, y=80)
        # 이미지 프레임 생성 및 배치
        self.frame_image1 = tk.Frame(self, width=120, height=120, bg='grey', bd=1)
        self.frame_image2 = tk.Frame(self, width=120, height=120, bg='grey', bd=1)
        self.frame_image3 = tk.Frame(self, width=120, height=120, bg='grey', bd=1)
        #self.frame_image4 = tk.Frame(self, width=120, height=120, bg='grey', bd=1)
        #self.frame_image5 = tk.Frame(self, width=120, height=120, bg='grey', bd=1)
        #self.frame_image6 = tk.Frame(self, width=120, height=120, bg='grey', bd=1)
        self.frame_image1.pack_propagate(False)
        self.frame_image2.pack_propagate(False)
        self.frame_image3.pack_propagate(False)
        #self.frame_image4.pack_propagate(False)
        #self.frame_image5.pack_propagate(False)
        #self.frame_image6.pack_propagate(False)
        self.frame_image1.place(x=180,y=120)
        self.frame_image2.place(x=345,y=120)
        self.frame_image3.place(x=510,y=120)
        #self.frame_image4.place(x=180,y=260)
        #self.frame_image5.place(x=345,y=260)
        #self.frame_image6.place(x=510,y=260)
        
        # 이미지를 프레임 내에 이미지를 보여줄 레이블 생성 및 배치
        self.label_image1 = tk.Label(self.frame_image1)
        self.label_image2 = tk.Label(self.frame_image2)
        self.label_image3 = tk.Label(self.frame_image3)
        #self.label_image4 = tk.Label(self.frame_image4)
        #self.label_image5 = tk.Label(self.frame_image5)
        #self.label_image6 = tk.Label(self.frame_image6)
        self.label_image1.pack(expand=True, fill=tk.BOTH)
        self.label_image2.pack(expand=True, fill=tk.BOTH)
        self.label_image3.pack(expand=True, fill=tk.BOTH)
        #self.label_image4.pack(expand=True, fill=tk.BOTH)
        #self.label_image5.pack(expand=True, fill=tk.BOTH)
        #self.label_image6.pack(expand=True, fill=tk.BOTH)
        
        # 이미지 이름 레이블 생성 및 배치
        title_image1 = tk.Label(text="image 1", bg='white')
        title_image2 = tk.Label(text="image 2", bg='white')
        title_image3 = tk.Label(text="image 3", bg='white')
        #title_image4 = tk.Label(text="image 4", bg='white')
        #title_image5 = tk.Label(text="image 5", bg='white')
        #title_image6 = tk.Label(text="image 6", bg='white')
        title_image1.place(x=180, y=240, width=120)
        title_image2.place(x=345, y=240, width=120)
        title_image3.place(x=510, y=240, width=120)
        #title_image4.place(x=180, y=380, width=120)
        #title_image5.place(x=345, y=380, width=120)
        #title_image6.place(x=510, y=380, width=120)
        
        # 옵션1 위젯 생성 및 배치
        frame_option1 = tk.Frame(self, height=30, bg='white')  # Frame 높이 설정
        frame_option1.place(x=180, y=290)  # Frame을 윈도우에 패딩과 함께 배치
        
        # 기타 옵션 레이블 생성 및 Frame 내에 배치
        label_reception1 = tk.Label(frame_option1, text="배달 기본 접수시간(분)", bg='white', font=('default', 10))
        label_reception1.grid(row=0, column=0, padx=(0, 10), sticky='w')
        
        # StringVar 인스턴스 생성 및 초기값 설정
        self.entry_var1 = tk.StringVar(self, "50")
        
        # '-' 버튼 생성 및 Frame 내에 배치
        self.btn_decrease1 = tk.Button(frame_option1, text='-')
        self.btn_decrease1.grid(row=0, column=1, sticky='ew')
        
        # Entry 위젯 생성 및 Frame 내에 배치, 비활성화 상태로 설정
        self.entry1 = ttk.Entry(frame_option1, justify='center', width=5, textvariable=self.entry_var1)
        self.entry1.grid(row=0, column=2, padx=5, sticky='ew')
        self.entry1.config(state='readonly')  # 사용자의 직접 입력을 방지
        
        # '+' 버튼 생성 및 Frame 내에 배치
        self.btn_increase1 = tk.Button(frame_option1, text='+')
        self.btn_increase1.grid(row=0, column=3, sticky='ew')

        # Grid column 설정
        frame_option1.grid_columnconfigure(2, weight=1)  # Entry 위젯이 있는 열의 너비를 가변적으로 설정

        # 옵션2 위젯 생성 및 배치
        frame_option2 = tk.Frame(self, height=30, bg='white')  # Frame 높이 설정
        frame_option2.place(x=180, y=330)  # Frame을 윈도우에 패딩과 함께 배치
        
        # 기타 옵션 레이블 생성 및 Frame 내에 배치
        label_reception2 = tk.Label(frame_option2, text="포장 기본 접수시간(분)", bg='white', font=('default', 10))
        label_reception2.grid(row=0, column=0, padx=(0, 10), sticky='w')
        
        # StringVar 인스턴스 생성 및 초기값 설정
        self.entry_var2 = tk.StringVar(self, "15")
        
        # '-' 버튼 생성 및 Frame 내에 배치
        self.btn_decrease2 = tk.Button(frame_option2, text='-')
        self.btn_decrease2.grid(row=0, column=1, sticky='ew')
        
        # Entry 위젯 생성 및 Frame 내에 배치, 비활성화 상태로 설정
        self.entry2 = ttk.Entry(frame_option2, justify='center', width=5, textvariable=self.entry_var2)
        self.entry2.grid(row=0, column=2, padx=5, sticky='ew')
        self.entry2.config(state='readonly')  # 사용자의 직접 입력을 방지
        
        # '+' 버튼 생성 및 Frame 내에 배치
        self.btn_increase2 = tk.Button(frame_option2, text='+')
        self.btn_increase2.grid(row=0, column=3, sticky='ew')

        # Grid column 설정
        frame_option2.grid_columnconfigure(2, weight=1)  # Entry 위젯이 있는 열의 너비를 가변적으로 설정

    def save_position(self, event):
        with open('data.txt', 'w') as f: 
            f.write(self.geometry())

if __name__ == "__main__":
    app = App()
    app.mainloop()