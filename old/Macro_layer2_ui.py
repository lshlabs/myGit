import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

def setup_ui(root):
    # 메인 프레임 생성
    main_frame = tk.Frame(root, bg='white')
    main_frame.pack(fill=tk.BOTH, expand=1, padx=10, pady=10)

    # 메뉴 프레임 생성 및 배치
    menu_frame = tk.Frame(main_frame, bg='gainsboro')
    menu_frame.pack(side=tk.LEFT, fill=tk.Y)

    # 타이틀 프레임 생성 및 배치
    title_frame = tk.Frame(main_frame, bg='grey')
    title_frame.pack(side=tk.TOP, fill=tk.X, padx=10)

    # 타이틀 라벨 생성 및 배치
    title_label = tk.Label(title_frame, text="스크롤 가능한 영역 예제", bg='grey')
    title_label.pack(pady=10)

    # 캔버스 생성 및 배치
    content_canvas = tk.Canvas(main_frame)
    content_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, padx=10)

    # 스크롤바 생성 및 캔버스에 연결
    scrollbar = tk.Scrollbar(content_canvas, orient="vertical", command=content_canvas.yview)
    content_canvas.configure(yscrollcommand=scrollbar.set)

    # 캔버스 안에 스크롤 가능한 프레임 생성
    inner_frame = tk.Frame(content_canvas)
    content_canvas.create_window((0, 0), window=inner_frame, anchor="nw")

    # 파란색 프레임 추가
    frames = []
    for i in range(6):
        frame = tk.Frame(inner_frame, bg='blue', width=100, height=100)
        frame.grid(row=i//3, column=i%3, padx=29, pady=15)
        frame.grid_propagate(False)
        frames.append(frame)

    # 라벨 추가
    for i in range(50):
        label_row = 2 + i//3
        label_column = i%3
        tk.Label(inner_frame, text="라벨 " + str(i)).grid(row=label_row, column=label_column, pady=2)

    return content_canvas, scrollbar, frames, menu_frame