import tkinter as tk

def open_sub_window(main_window):
    sub_window = tk.Toplevel(main_window)
    sub_window.title("Sub Window")
    sub_window.geometry("400x480")  # Sub window sizesss

    # Get the position of the main window
    main_x = main_window.winfo_x()
    main_y = main_window.winfo_y()
    main_width = main_window.winfo_width()
    main_height = main_window.winfo_height()

    # Calculate the position to center the sub window in the main window
    sub_width = 400
    sub_height = 480
    x = main_x + (main_width // 2) - (sub_width // 2)
    y = main_y + (main_height // 2) - (sub_height // 2)

    sub_window.geometry(f"{sub_width}x{sub_height}+{x}+{y}")

    label = tk.Label(sub_window, text="This is the sub window")
    label.pack(pady=20)

    button_close = tk.Button(sub_window, text="Close", command=sub_window.destroy)
    button_close.pack(pady=10)
