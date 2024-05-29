# test_ui.py
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def setup_ui(root):
    
    main_frame = tk.Frame(root, bg='white', padx=5, pady=5)
    main_frame.pack(fill='both', expand=True)
    # 메인프레임 요소 가중치 설정
    main_frame.rowconfigure(0, weight=1)
    main_frame.columnconfigure(0, weight=1)
    main_frame.columnconfigure(1, weight=6)
    
    # 메뉴 프레임 생성 및 배치
    menu_frame = tk.Frame(main_frame, bd=1, relief='solid')
    menu_frame.grid(row=0, column=0, padx=5, pady=5, sticky='nesw')
    
    # 메뉴항목 추가 및 기능 연결
    menu_item1 = tk.Label(menu_frame, text="배달 플랫폼", bg="purple", fg="white", font=('default', 12), anchor='center')
    menu_item1.grid(row=0, column=0, sticky='nsew')

    menu_item2 = tk.Label(menu_frame, text="배달의 민족", bg="white", fg="black", font=('default', 12), anchor='center')
    menu_item2.grid(row=1, column=0, sticky='nsew')

    menu_item3 = tk.Label(menu_frame, text="요기요", bg="white", fg="black", font=('default', 12), anchor='center')
    menu_item3.grid(row=2, column=0, sticky='nsew')

    menu_item4 = tk.Label(menu_frame, text="+", bg="white", fg="black", font=('default', 13), anchor='center')
    menu_item4.grid(row=3, column=0, sticky='nsew')

    menu_item5 = tk.Label(menu_frame, text="배차 플랫폼", bg="purple", fg="white", font=('default', 12), anchor='center')
    menu_item5.grid(row=4, column=0, sticky='nsew')

    menu_item6 = tk.Label(menu_frame, text="만나", bg="white", fg="black", font=('default', 12), anchor='center')
    menu_item6.grid(row=5, column=0, sticky='nsew')

    menu_item7 = tk.Label(menu_frame, text="+", bg="white", fg="black", font=('default', 12), anchor='center')
    menu_item7.grid(row=6, column=0, sticky='nsew') 
    
    # 각 행에 대한 가중치 설정
    for i in range(7):
        menu_frame.grid_rowconfigure(i, weight=1)
    menu_frame.grid_columnconfigure(0, weight=1)

    dummy_frame = tk.Frame(main_frame, bg='white')
    dummy_frame.grid(row=0, column=1, padx=(0,5), pady=5, sticky='nesw')
    
    # 타이틀 프레임 생성 및 배치
    title_frame = tk.Frame(dummy_frame, bg='#45D3D3', bd=1, relief='solid')
    title_frame.place(relwidth=1, relheight=0.144)
    
    # 타이틀 라벨 생성 및 배치
    title_label = tk.Label(title_frame, text="flatform name", bg='#45D3D3', font=("default", 20, "bold"), fg='white')
    title_label.pack(pady=20, anchor='center')
    
    # 캔버스와 스크롤바를 품은 프레임
    uni_frame = tk.Frame(dummy_frame, bd=1, relief='solid', bg='white')
    uni_frame.place(relwidth=1, relheight=0.860, rely=0.141)
    
    # 캔버스 생성 및 배치
    content_canvas = tk.Canvas(uni_frame, bg='white')
    content_canvas.pack(side="left", fill='both', expand=True)
    
    scrollbar = tk.Scrollbar(uni_frame, orient='vertical', command=content_canvas.yview, bg='white')
    scrollbar.pack(side="right", fill='both')
    scrollable_frame = tk.Frame(content_canvas, bg='white')
    scrollable_frame.pack(side='right', fill='both')
    
    scrollable_frame.bind(
        "<Configure>",
        lambda e: content_canvas.configure(
            scrollregion=content_canvas.bbox("all")
        )
    )
    content_canvas.create_window((0,0), window=scrollable_frame, anchor="nw")
    content_canvas.configure(yscrollcommand=scrollbar.set)
    
    dummy_frame2 = tk.Frame(scrollable_frame, height=30, bg='white', pady=15)
    dummy_frame2.grid(row=0, columnspan=3, sticky='w')
    
    label_tip = tk.Label(dummy_frame2, text='※ 이미지를 클릭하여 등록해주세요', bg='white', fg='black', padx=27)
    label_tip.grid(row=0, column=0)
        
    iframes = []
    inames = []
    for i in range(12):
        # 각 이미지 프레임 생성 및 위치 설정
        iframe = tk.Frame(scrollable_frame, width=120, height=120, bd=1, relief='solid')
        iframe.grid(row=((i//3)*2)+1, column=i%3, padx=23, pady=5)  # row 값을 2*i로 설정하여 각 프레임 사이에 공간을 남깁니다.
        iframe.pack_propagate(False)
        iframes.append(iframe)
    
        # 각 이미지 이름 레이블 생성 및 이미지 프레임 바로 아래 위치 설정
        iname = tk.Label(scrollable_frame, text="이미지 " + str(i+1), bg='white')
        iname.grid(row=((i//3)*2)+2, column=i%3, padx=27, pady=(0,15))  # row 값을 2*i + 1로 설정하여 각 프레임 바로 아래에 레이블을 위치시킵니다.
        inames.append(iname)
        
    # 프레임 내에 이미지를 보여줄 레이블 생성 및 배치
    ilabels = []
    for i, iframe in enumerate(iframes):
        # 이미지 레이블에 고유 번호를 부여하여 텍스트 설정
        ilabel = tk.Label(iframe)
        ilabel.pack(expand=True, fill=tk.BOTH)
        ilabels.append(ilabel)

    
    dummy_frame3 = tk.Frame(scrollable_frame, height=30, bg='white', pady=10)
    dummy_frame3.grid(row=5)
    
    oframes = []
    for i in range(3):
        oframe = tk.Frame(scrollable_frame, bg='white')
        oframe.grid(row=(5+i), column=0, pady=10, columnspan=3, sticky='w')
        oframe.grid_columnconfigure(2, weight=1)
        oframes.append(oframe)
        
    olabel1 = tk.Label(oframes[0], text="배달 기본 접수시간(분)", bg='white', fg='black', font=('default', 12))
    olabel1.grid(row=0, column=0, padx=27, sticky='w')
    
    obtn_m1 = tk.Button(oframes[0], text='-', bg='gainsboro', relief='solid', bd=1, width=2, height=1)
    obtn_m1.grid(row=0, column=1, sticky='ew')
    
    obtn_p1 = tk.Button(oframes[0], text='+', bg='gainsboro', relief='solid', bd=1, width=2, height=1)
    obtn_p1.grid(row=0, column=3, sticky='ew')
    
    entry_var1 = tk.StringVar(root, "50")

    oentry1 = ttk.Entry(oframes[0], justify='center', width=5, textvariable=entry_var1, state='readonly')
    oentry1.grid(row=0, column=2, padx=5, sticky='ew', ipady=1)
    
    olabel2 = tk.Label(oframes[1], text="포장 기본 접수시간(분)", bg='white', fg='black', font=('default', 12))
    olabel2.grid(row=0, column=0, padx=27, sticky='w')
    
    obtn_m2 = tk.Button(oframes[1], text='-', bg='gainsboro', relief='solid', bd=1, width=2, height=1)
    obtn_m2.grid(row=0, column=1, sticky='ew')
    
    obtn_p2 = tk.Button(oframes[1], text='+', bg='gainsboro', relief='solid', bd=1, width=2, height=1)
    obtn_p2.grid(row=0, column=3, sticky='ew')
    
    entry_var2 = tk.StringVar(root, "15")

    oentry2 = ttk.Entry(oframes[1], justify='center', width=5, textvariable=entry_var2, state='readonly')
    oentry2.grid(row=0, column=2, padx=5, sticky='ew', ipady=1)
    
    olabel3 = tk.Label(oframes[2], text="매크로 동작 설정", bg='white', fg='black', font=('default', 12))
    olabel3.grid(row=0, column=0, padx=(27,10), sticky='w')
    
    setting_icon = Image.open("C:\myGit\myGit\imagefiles\settings.png")
    setting_icon = setting_icon.resize((25, 25), Image.Resampling.LANCZOS)
    setting_icon_photo = ImageTk.PhotoImage(setting_icon)
    
    btn_setting = tk.Button(oframes[2], image=setting_icon_photo, borderwidth=0, bg='white')
    btn_setting.grid(row=0, column=1, sticky='ew')
    
    return (title_label, content_canvas, iframes, ilabels, inames, menu_frame, uni_frame, scrollbar, title_frame, title_label, scrollable_frame, btn_setting,
            menu_item2, menu_item3, menu_item4, menu_item6, menu_item7, setting_icon_photo, entry_var1, entry_var2, oframes, obtn_m1, obtn_m2, obtn_p1, obtn_p2)