import tkinter as tk
from tkinter import messagebox
from Macro_main_ui import App  # Macro_main_ui 모듈에서 App 클래스를 가져옵니다.

app = App()  # App 인스턴스를 생성하고, tkinter의 메인 윈도우를 master로 설정합니다.

def on_menu_click(event):
    # 클릭된 메뉴의 이름을 팝업으로 띄워줍니다.
    menu_name = event.widget.cget("text")
    messagebox.showinfo("메뉴 선택", f"선택된 메뉴: {menu_name}")
    
def decrease_value():
    # 현재 엔트리의 값 가져오기
    current_value = int(app.entry.get())
    # 값 감소
    new_value = max(0, current_value - 5)  # 0 미만으로 내려가지 않도록 처리
    # 새로운 값으로 엔트리 업데이트
    app.entry.delete(0, tk.END)
    app.entry.insert(0, str(new_value))

def increase_value():
    # 현재 엔트리의 값 가져오기
    current_value = int(app.entry.get())
    # 값 증가
    new_value = current_value + 5
    # 새로운 값으로 엔트리 업데이트
    app.entry.delete(0, tk.END)
    app.entry.insert(0, str(new_value))


def main():

    # 각 메뉴 항목에 클릭 이벤트 바인딩
    app.menu_item1.bind("<Button-1>", on_menu_click)
    app.menu_item2.bind("<Button-1>", on_menu_click)
    app.menu_item3.bind("<Button-1>", on_menu_click)
    app.menu_item4.bind("<Button-1>", on_menu_click)
    app.menu_item5.bind("<Button-1>", on_menu_click)
    app.menu_item6.bind("<Button-1>", on_menu_click)
    app.menu_item7.bind("<Button-1>", on_menu_click)
    
    # 버튼 클릭 이벤트에 함수 연결
    app.btn_decrease.config(command=decrease_value)
    app.btn_increase.config(command=increase_value)

    app.mainloop()

if __name__ == "__main__":
    main()
