import tkinter as tk

def setup_ui(root):
    # 메인 프레임 생성
    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=1, padx=5, pady=10)

    # 메뉴 프레임 생성 및 배치
    menu_frame = tk.Frame(main_frame, bg='white', bd=1, relief='solid')
    menu_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(10,0))


    # 캔버스 생성 및 배치
    content_canvas = tk.Canvas(main_frame, bg='white')
    content_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1, padx=10)

    # 타이틀 프레임 생성 및 배치
    title_frame = tk.Frame(content_canvas, bg='grey', bd=1, relief='solid')
    title_frame.place(relx=0, rely=0, relheight=0.13, relwidth=1, anchor='nw')

    # 타이틀 라벨 생성 및 배치
    title_label = tk.Label(title_frame, text="스크롤 가능한 영역 예제", bg='grey')
    title_label.pack(pady=10)
    
    # 캔버스 안에 스크롤 가능한 프레임 생성
    inner_frame = tk.Frame(content_canvas, bg='white', bd=1, relief='solid')
    inner_frame.place(relx=0, rely=1, relheight=0.88, relwidth=1, anchor='sw')
    
    # 파란색 프레임 추가
    frames = []
    for i in range(6):
        frame = tk.Frame(inner_frame, bg='blue', width=100, height=100)
        frame.grid(row=i//3, column=i%3, padx=27, pady=15)
        frame.grid_propagate(False)
        frames.append(frame)

    # 라벨 추가
    for i in range(50):
        label_row = 2 + i//3
        label_column = i%3
        tk.Label(inner_frame, text="라벨 " + str(i), bg='white').grid(row=label_row, column=label_column, pady=3)

    return content_canvas, frames, menu_frame
