import tkinter as tk

def setup_ui(root):
    
    main_frame = tk.Frame(root, bg='white')
    main_frame.pack(fill='both', expand=True)
    
    # 메인 프레임의 레이아웃 조정을 위한 설정
    # root.rowconfigure(0, weight=1)  # 루트 윈도우의 첫 번째 행 확장 가능하게 설정
    # root.columnconfigure(0, weight=1)  # 루트 윈도우의 첫 번째 열 확장 가능하게 설정
    
    # 메뉴 프레임 생성 및 배치
    menu_frame = tk.Frame(main_frame, bd=1, relief='solid')
    menu_frame.grid(row=0, column=0, padx=5, pady=5, sticky='nesw')
    main_frame.rowconfigure(0, weight=1)  # main_frame의 두 번째 행이 확장 가능하게 설정
    main_frame.columnconfigure(1, weight=1)  # main_frame의 두 번째 열이 확장 가능하게 설정

    dummy_frame = tk.Frame(main_frame)
    dummy_frame.grid(row=0, column=1, padx=(0,5), pady=5, sticky='nesw')
    
    # 타이틀 프레임 생성 및 배치
    title_frame = tk.Frame(dummy_frame, bg='#45D3D3', bd=1, relief='solid')
    title_frame.place(relwidth=1, relheight=0.2)
    
    # 타이틀 라벨 생성 및 배치
    title_label = tk.Label(title_frame, text="flatform name", bg='#45D3D3', font=("default", 20, "bold"), fg='white')
    title_label.pack(pady=25, anchor='center')
    
    # 캔버스와 스크롤바를 품은 프레임
    uni_frame = tk.Frame(dummy_frame, bd=1, relief='solid')
    uni_frame.place(relwidth=1, relheight=0.804, rely=0.196)
    
    # 캔버스 생성 및 배치
    content_canvas = tk.Canvas(uni_frame)
    content_canvas.pack(side="left", fill='both', expand=True)
    
    scrollbar = tk.Scrollbar(uni_frame, orient='vertical', command=content_canvas.yview, highlightbackground='#d9d9d9')
    scrollbar.pack(side="right", fill='both')
    scrollable_frame = tk.Frame(content_canvas, padx=10, pady=10)
    scrollable_frame.pack(side='right', fill='both')
    
    scrollable_frame.bind(
        "<Configure>",
        lambda e: content_canvas.configure(
            scrollregion=content_canvas.bbox("all")
        )
    )
    content_canvas.create_window((0,0), window=scrollable_frame, anchor="nw")
    content_canvas.configure(yscrollcommand=scrollbar.set)
    
    # 파란색 프레임 추가
    frames = []
    for i in range(6):
        frame = tk.Frame(scrollable_frame, bg='grey', width=100, height=100, bd=1, relief='solid')
        frame.grid(row=i//3, column=i%3, padx=30, pady=15)
        frame.grid_propagate(True)
        frames.append(frame)    # 생성된 프레임을 리스트에 추가

    # 라벨 추가
    labels = []
    for i in range(51):
        label_row = 2 + i//3
        label_column = i%3
        label = tk.Label(scrollable_frame, text="라벨 " + str(i))
        label.grid(row=label_row, column=label_column, pady=3)
        labels.append(label)  # 생성된 라벨을 리스트에 추가

    return content_canvas, frames, menu_frame, uni_frame, scrollbar, title_frame, title_label, scrollable_frame, labels