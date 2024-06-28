# test_ui.py
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import json

# 상수 정의
BACKGROUND_COLOR = 'white'
MENU_TITLE_COLOR = 'purple'
TITLE_COLOR = '#45D3D3'
FONT_SIZE = 12

# 설정 파일 로드
with open('config.json', 'r') as f:
    config = json.load(f)

def create_menu_item(parent, text, bg_color, fg_color, row):
    item = tk.Label(parent, text=text, bg=bg_color, fg=fg_color, font=('default', FONT_SIZE), anchor='center')
    item.grid(row=row, column=0, sticky='nsew')
    return item

def create_image_frame(parent, row, col):
    frame = tk.Frame(parent, width=120, height=120, bd=1, relief='solid')
    frame.grid(row=row, column=col, padx=23, pady=5)
    frame.pack_propagate(False)
    
    label = tk.Label(frame)
    label.pack(expand=True, fill=tk.BOTH)
    
    name_label = tk.Label(parent, text=f"이미지 {row*3 + col + 1}", bg=BACKGROUND_COLOR)
    name_label.grid(row=row+1, column=col, padx=27, pady=(0,15))
    
    return frame, label, name_label

def setup_ui(root):
    main_frame = tk.Frame(root, bg=BACKGROUND_COLOR, padx=5, pady=5)
    main_frame.pack(fill='both', expand=True)
    main_frame.rowconfigure(0, weight=1)
    main_frame.columnconfigure(0, weight=1)
    main_frame.columnconfigure(1, weight=6)
    
    menu_frame = tk.Frame(main_frame, bd=1, relief='solid')
    menu_frame.grid(row=0, column=0, padx=5, pady=5, sticky='nesw')
    
    menu_items = [
        ("배달 플랫폼", MENU_TITLE_COLOR, "white"),
        ("배달의 민족", BACKGROUND_COLOR, "black"),
        ("요기요", BACKGROUND_COLOR, "black"),
        ("+", BACKGROUND_COLOR, "black"),
        ("배차 플랫폼", MENU_TITLE_COLOR, "white"),
        ("만나", BACKGROUND_COLOR, "black"),
        ("+", BACKGROUND_COLOR, "black")
    ]
    
    menu_labels = [create_menu_item(menu_frame, *item, i) for i, item in enumerate(menu_items)]
    
    for i in range(len(menu_items)):
        menu_frame.grid_rowconfigure(i, weight=1)
    menu_frame.grid_columnconfigure(0, weight=1)

    dummy_frame = tk.Frame(main_frame, bg=BACKGROUND_COLOR)
    dummy_frame.grid(row=0, column=1, padx=(0,5), pady=5, sticky='nesw')
    
    title_frame = tk.Frame(dummy_frame, bg=TITLE_COLOR, bd=1, relief='solid')
    title_frame.place(relwidth=1, relheight=0.144)
    
    title_label = tk.Label(title_frame, text="flatform name", bg=TITLE_COLOR, font=("default", 20, "bold"), fg='white')
    title_label.pack(pady=20, anchor='center')
    
    uni_frame = tk.Frame(dummy_frame, bd=1, relief='solid', bg=BACKGROUND_COLOR)
    uni_frame.place(relwidth=1, relheight=0.860, rely=0.141)
    
    content_canvas = tk.Canvas(uni_frame, bg=BACKGROUND_COLOR)
    content_canvas.pack(side="left", fill='both', expand=True)
    
    scrollbar = tk.Scrollbar(uni_frame, orient='vertical', command=content_canvas.yview, bg=BACKGROUND_COLOR)
    scrollbar.pack(side="right", fill='both')
    
    scrollable_frame = tk.Frame(content_canvas, bg=BACKGROUND_COLOR)
    scrollable_frame.pack(side='right', fill='both')
    
    scrollable_frame.bind("<Configure>", lambda e: content_canvas.configure(scrollregion=content_canvas.bbox("all")))
    content_canvas.create_window((0,0), window=scrollable_frame, anchor="nw")
    content_canvas.configure(yscrollcommand=scrollbar.set)
    
    tk.Label(scrollable_frame, text='※ 이미지를 클릭하여 등록해주세요', bg=BACKGROUND_COLOR, fg='black', padx=27).grid(row=0, columnspan=3, sticky='w', pady=15)
    
    iframes, ilabels, inames = zip(*[create_image_frame(scrollable_frame, i//3*2+1, i%3) for i in range(12)])
    
    oframes = [tk.Frame(scrollable_frame, bg=BACKGROUND_COLOR) for _ in range(3)]
    for i, frame in enumerate(oframes):
        frame.grid(row=5+i, column=0, pady=10, columnspan=3, sticky='w')
        frame.grid_columnconfigure(2, weight=1)
    
    entry_vars = [tk.StringVar(root, value) for value in config['default_values']]
    
    for i, (label_text, var) in enumerate(zip(["배달 기본 접수시간(분)", "포장 기본 접수시간(분)"], entry_vars)):
        tk.Label(oframes[i], text=label_text, bg=BACKGROUND_COLOR, fg='black', font=('default', FONT_SIZE)).grid(row=0, column=0, padx=27, sticky='w')
        tk.Button(oframes[i], text='-', bg='gainsboro', relief='solid', bd=1, width=2, height=1).grid(row=0, column=1, sticky='ew')
        tk.Button(oframes[i], text='+', bg='gainsboro', relief='solid', bd=1, width=2, height=1).grid(row=0, column=3, sticky='ew')
        ttk.Entry(oframes[i], justify='center', width=5, textvariable=var, state='readonly').grid(row=0, column=2, padx=5, sticky='ew', ipady=1)
    
    tk.Label(oframes[2], text="매크로 동작 설정", bg=BACKGROUND_COLOR, fg='black', font=('default', FONT_SIZE)).grid(row=0, column=0, padx=(27,10), sticky='w')
    
    setting_icon = Image.open(config['setting_icon_path'])
    setting_icon = setting_icon.resize((25, 25), Image.Resampling.LANCZOS)
    setting_icon_photo = ImageTk.PhotoImage(setting_icon)
    
    btn_setting = tk.Button(oframes[2], image=setting_icon_photo, borderwidth=0, bg=BACKGROUND_COLOR)
    btn_setting.grid(row=0, column=1, sticky='ew')
    
    return (title_label, content_canvas, iframes, ilabels, inames, menu_frame, uni_frame, scrollbar, title_frame, title_label, scrollable_frame, btn_setting,
            menu_labels[1], menu_labels[2], menu_labels[3], menu_labels[5], menu_labels[6], setting_icon_photo, *entry_vars, oframes, *[child for frame in oframes[:2] for child in frame.winfo_children() if isinstance(child, tk.Button)])