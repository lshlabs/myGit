import tkinter as tk
from tkinter import ttk

class MacroSettingsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("키보드/마우스 매크로 설정")
        self.root.geometry("450x600")
        
        main_frame = ttk.Frame(root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # 프로그램 실행과 관련된 설정
        program_frame = ttk.LabelFrame(main_frame, text="프로그램 실행과 관련된 설정", padding="10")
        program_frame.pack(fill=tk.X, expand=True, pady=5)
        
        ttk.Label(program_frame, text="매크로 프로그램 이름 변경:").pack(anchor='w', pady=2)
        ttk.Combobox(program_frame, values=["키보드/마우스 매크로 V2"]).pack(fill=tk.X, pady=2)

        ttk.Checkbutton(program_frame, text="다른 윈도우보다 항상 위에 두기").pack(anchor='w', pady=2)
        ttk.Checkbutton(program_frame, text="프로그램 시작시 시스템 트레이로 최소화").pack(anchor='w', pady=2)

        ttk.Label(program_frame, text="윈도우즈 IME 입력기 설정:").pack(anchor='w', pady=2)
        ttk.Combobox(program_frame, values=["두벌식 자판"]).pack(fill=tk.X, pady=2)
        
        # 매크로 실행과 관련된 설정
        execution_frame = ttk.LabelFrame(main_frame, text="매크로 실행과 관련된 설정", padding="10")
        execution_frame.pack(fill=tk.X, expand=True, pady=5)
        
        ttk.Label(execution_frame, text="매크로 실행/중단 키:").pack(anchor='w', pady=2)
        ttk.Combobox(execution_frame, values=["F12 key"]).pack(fill=tk.X, pady=2)

        ttk.Checkbutton(execution_frame, text='"매크로 실행 가능" 선택시 시스템 트레이에 선택된 매크로 실행').pack(anchor='w', pady=2)
        ttk.Checkbutton(execution_frame, text="매크로 실행/중단 시 아이콘 깜박임 및 팝업창 알림").pack(anchor='w', pady=2)

        ttk.Label(execution_frame, text="매크로 주기(빠를수록 숫자 작게):").pack(anchor='w', pady=2)
        ttk.Entry(execution_frame).pack(fill=tk.X, pady=2)
        
        ttk.Label(execution_frame, text="매크로 이벤트 실행 주기:").pack(anchor='w', pady=2)
        ttk.Entry(execution_frame).pack(fill=tk.X, pady=2)
        
        ttk.Checkbutton(execution_frame, text="매크로 실행시 IME의 한/영 전환 상태 유지").pack(anchor='w', pady=2)

        # 매크로 키로 사용하는 키 설정
        key_frame = ttk.LabelFrame(main_frame, text="매크로 키로 사용하는 키 설정", padding="10")
        key_frame.pack(fill=tk.X, expand=True, pady=5)
        
        ttk.Label(key_frame, text="매크로 키를 사용하는 키:").pack(anchor='w', pady=2)
        ttk.Combobox(key_frame, values=["F11 key"]).pack(fill=tk.X, pady=2)
        
        ttk.Label(key_frame, text="마우스 위치 현재 키:").pack(anchor='w', pady=2)
        ttk.Combobox(key_frame, values=["F10 key"]).pack(fill=tk.X, pady=2)

        # 매크로 시작/종료 조건 설정에 사용하는 키 설정
        start_end_frame = ttk.LabelFrame(main_frame, text="매크로 시작/종료 조건 설정에 사용하는 키 설정", padding="10")
        start_end_frame.pack(fill=tk.X, expand=True, pady=5)
        
        ttk.Label(start_end_frame, text="시작 시, 화면이동 키:").pack(anchor='w', pady=2)
        ttk.Combobox(start_end_frame, values=["F9 key"]).pack(fill=tk.X, pady=2)
        
        ttk.Label(start_end_frame, text="종료 시, 화면이동 키:").pack(anchor='w', pady=2)
        ttk.Combobox(start_end_frame, values=["F8 key"]).pack(fill=tk.X, pady=2)
        
        ttk.Checkbutton(start_end_frame, text="매크로가 종료 시 작동(종료/파랑) 및 인식 확인 표시").pack(anchor='w', pady=2)
        ttk.Checkbutton(start_end_frame, text="매크로 실행시 모든 노트 보기/버튼 대기").pack(anchor='w', pady=2)

        # 확인 및 취소 버튼
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(button_frame, text="OK").pack(side=tk.RIGHT, padx=5)
        ttk.Button(button_frame, text="Cancel").pack(side=tk.RIGHT)

if __name__ == "__main__":
    root = tk.Tk()
    app = MacroSettingsApp(root)
    root.mainloop()
