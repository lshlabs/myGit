import encodings
import json
from pathlib import Path
import tkinter as tk
from tkinter import StringVar, ttk
from virtual_key import g_vk_list

root = tk.Tk()
root.title("키보드/마우스 매크로 설정")
root.geometry("380x300")
        
main_frame = ttk.Frame(root, padding="10")
main_frame.pack(fill=tk.BOTH, expand=True)

# 딜레이 설정 섹션
delay_frame = ttk.LabelFrame(main_frame, text="딜레이 설정", padding="10")
delay_frame.pack(fill=tk.X, expand=True, pady=5)
        
ttk.Label(delay_frame, text="지연시간:").grid(row=0, column=0, padx=(5,15))
ttk.Label(delay_frame, text="초").grid(row=0, column=2, padx=5)
        
delay_var = StringVar(root, "0.5")
delay_time = ttk.Entry(delay_frame, width=10, textvariable=delay_var)
# delay_time.insert(0, "0.5")
delay_time.grid(row=0, column=1)

# 매크로 시작/중지에 단축키 사용 섹션
shortcut_frame = ttk.LabelFrame(main_frame, text="매크로 시작/중지에 단축키 사용", padding="10")
shortcut_frame.pack(fill=tk.X, expand=True, pady=5)
    
# 체크박스 생성 및 체크박수 변수 생성
label_run = ttk.Label(shortcut_frame, text="시작 단축키:")
label_run.grid(row=0, column=0, sticky='w')

label_stop = ttk.Label(shortcut_frame, text="종료 단축키:")
label_stop.grid(row=2, column=0, sticky='w')

# 콤보박스와 버튼 프레임 생성
combo_button_frame1 = ttk.Frame(shortcut_frame)
combo_button_frame1.grid(row=0, column=2, columnspan=2, pady=2, sticky='w')

combo_button_frame2 = ttk.Frame(shortcut_frame)
combo_button_frame2.grid(row=2, column=2, columnspan=2, pady=2, sticky='w')

# 가상 키 설명을 가져와서 콤보박스에 설정
vk_descs = [info.vk_desc for info in g_vk_list if info.vk_code != -1]

# 콤보박스
combobox_run = ttk.Combobox(combo_button_frame1, values=vk_descs, state='readonly')
combobox_run.pack(side=tk.LEFT, padx=5)

combobox_stop = ttk.Combobox(combo_button_frame2, values=vk_descs, state='readonly')
combobox_stop.pack(side=tk.LEFT, padx=5)

# # 키 이벤트 바인딩
# root.bind("<Key>", on_key_press)

# 버튼
button_run = ttk.Button(combo_button_frame1, text="누를 때")
button_run.pack(side=tk.LEFT, padx=5)
button_stop = ttk.Button(combo_button_frame2, text="누를 때")
button_stop.pack(side=tk.LEFT, padx=5)

# modifier 체크박스 프레임 생성
md_frame1 = ttk.Frame(shortcut_frame)
md_frame1.grid(row=1, column=1, columnspan=3, pady=2, sticky='w')

md_frame2 = ttk.Frame(shortcut_frame)
md_frame2.grid(row=3, column=1, columnspan=3, pady=2, sticky='w')

# 체크박스 상태변수 생성
v_check_run1 = tk.BooleanVar()
v_check_run2 = tk.BooleanVar()
v_check_run3 = tk.BooleanVar()
v_check_run4 = tk.BooleanVar()
v_check_stop1 = tk.BooleanVar()
v_check_stop2 = tk.BooleanVar()
v_check_stop3 = tk.BooleanVar()
v_check_stop4 = tk.BooleanVar()

# 체크박스 활성화/비활성화
def toggle_ckrun():
    if check_run1.instate(['selected']):
        check_run2.state(['!disabled'])
        check_run3.state(['!disabled'])
        check_run4.state(['!disabled'])
    else:
        check_run2.state(['disabled'])
        check_run3.state(['disabled'])
        check_run4.state(['disabled'])

def toggle_ckstop():
    if check_stop1.instate(['selected']):
        check_stop2.state(['!disabled'])
        check_stop3.state(['!disabled'])
        check_stop4.state(['!disabled'])
    else:
        check_stop2.state(['disabled'])
        check_stop3.state(['disabled'])
        check_stop4.state(['disabled'])

# 체크박스 생성
check_run1 = ttk.Checkbutton(md_frame1, text="Modifier Key:", variable=v_check_run1, command=toggle_ckrun)
check_run2 = ttk.Checkbutton(md_frame1, text="Ctrl", variable=v_check_run2, state='disabled')
check_run3 = ttk.Checkbutton(md_frame1, text="Alt", variable=v_check_run3, state='disabled')
check_run4 = ttk.Checkbutton(md_frame1, text="Shift", variable=v_check_run4, state='disabled')
check_stop1 = ttk.Checkbutton(md_frame2, text="Modifier Key:", variable=v_check_stop1, command=toggle_ckstop)
check_stop2 = ttk.Checkbutton(md_frame2, text="Ctrl", variable=v_check_stop2, state='disabled')
check_stop3 = ttk.Checkbutton(md_frame2, text="Alt", variable=v_check_stop3, state='disabled')
check_stop4 = ttk.Checkbutton(md_frame2, text="Shift", variable=v_check_stop4, state='disabled')

# 체크박스 배치
check_run1.pack(side=tk.LEFT, padx=5)
check_run2.pack(side=tk.LEFT, padx=5)
check_run3.pack(side=tk.LEFT, padx=5)
check_run4.pack(side=tk.LEFT, padx=5)
check_stop1.pack(side=tk.LEFT, padx=5)
check_stop2.pack(side=tk.LEFT, padx=5)
check_stop3.pack(side=tk.LEFT, padx=5)
check_stop4.pack(side=tk.LEFT, padx=5)

# 세이브데이터 경로
data_path_win = Path("C:\myGit\myGit\data_setting_win.json")
data_path_mac = Path("mac 경로")

# 데이터 저장 함수
def save_data():
    data = {
        "delaytime": delay_var.get(),
        "combobox_run": combobox_run['values'][combobox_run.current()],
        "combobox_stop": combobox_stop['values'][combobox_stop.current()],
        "check_run1": v_check_run1.get(),
        "check_run2": v_check_run2.get(),
        "check_run3": v_check_run3.get(),
        "check_run4": v_check_run4.get(),
        "check_stop1": v_check_stop1.get(),
        "check_stop2": v_check_stop2.get(),
        "check_stop3": v_check_stop3.get(),
        "check_stop4": v_check_stop4.get(),
        "window_geometry": root.geometry()
    }
    json_data = json.dumps(data, indent=4, ensure_ascii=False)
    with open(data_path_win, 'w', encoding='utf-8') as f:
        f.write(json_data)
        
    root.destroy()

# 데이터 로드 함수
def load_data():
    if not data_path_win.exists():
        print("found no data")
        return
    with open(data_path_win, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
    delay_var.set(data.get('delaytime', '0.5'))
    combobox_run.set(data['combobox_run'])
    combobox_stop.set(data['combobox_stop'])
    value_r1 = data.get("check_run1")
    value_r2 = data.get("check_run2")
    value_r3 = data.get("check_run3")
    value_r4 = data.get("check_run4")
    value_s1 = data.get("check_stop1")
    value_s2 = data.get("check_stop2")
    value_s3 = data.get("check_stop3")
    value_s4 = data.get("check_stop4")
    
    v_check_run1.set(value_r1)
    v_check_run2.set(value_r2)
    v_check_run3.set(value_r3)
    v_check_run4.set(value_r4)
    v_check_stop1.set(value_s1)
    v_check_stop2.set(value_s2)
    v_check_stop3.set(value_s3)
    v_check_stop4.set(value_s4)
    
    toggle_ckrun()
    toggle_ckstop()
    
    root.geometry(data['window_geometry'])
    # print("Data loading succesfull")
    
def save_data_geometry():
    with open(data_path_win, 'r', encoding='utf-8') as f:
            data = json.load(f)
    
    data['window_geometry'] = root.geometry()
    
    json_data = json.dumps(data, indent=4, ensure_ascii=False)
    with open(data_path_win, 'w', encoding='utf-8') as f:
        f.write(json_data)
    
    root.destroy()
    
# 확인 및 취소 버튼
button_frame = ttk.Frame(main_frame)
button_frame.pack(fill=tk.X, pady=10)

button_cancel = ttk.Button(button_frame, text="Cancel", command=save_data_geometry)
button_cancel.pack(side=tk.RIGHT, padx=5)
button_ok = ttk.Button(button_frame, text="OK", command=save_data)
button_ok.pack(side=tk.RIGHT)

load_data()
root.mainloop()