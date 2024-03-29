import tkinter as tk
from tkinter import messagebox
from Macro_main_ui import App  # Macro_main_ui 모듈에서 App 클래스를 가져옵니다.

def on_menu_click(event):
    # 클릭된 메뉴의 이름을 팝업으로 띄워줍니다.
    menu_name = event.widget.cget("text")
    messagebox.showinfo("메뉴 선택", f"선택된 메뉴: {menu_name}")

def main():
    root = tk.Tk()
    app = App()  # App 인스턴스를 생성하고, tkinter의 메인 윈도우를 master로 설정합니다.

    # 각 메뉴 항목에 클릭 이벤트 바인딩
    app.menu_item1.bind("<Button-1>", on_menu_click)
    app.menu_item2.bind("<Button-1>", on_menu_click)
    app.menu_item3.bind("<Button-1>", on_menu_click)
    app.menu_item4.bind("<Button-1>", on_menu_click)
    app.menu_item5.bind("<Button-1>", on_menu_click)
    app.menu_item6.bind("<Button-1>", on_menu_click)
    app.menu_item7.bind("<Button-1>", on_menu_click)

    root.mainloop()

if __name__ == "__main__":
    main()
