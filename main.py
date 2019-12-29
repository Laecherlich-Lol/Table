import tkinter as t
from tkinter import filedialog


window = t.Tk()
window.title("Kassenbericht")
window.geometry("500x300")
event = t.StringVar()
on_hit = False


def click_button():
    get_files()


def get_files():
    window.filename = filedialog.askopenfilename(
        initialdir="/",
        title="Select file",
        filetypes=(("excel files", "*.xlsx"), ("all files", "*.*")),
    )
    print(window.filename)


def input_new_dir():
    name = t.Entry(window, font=("Arial", 14)).place()
    name.pack()


select_file_button = t.Button(
    window,
    text="选择文件",
    font=("Arial", 12),
    width=25,
    height=1,
    command=click_button,
)
create_new_file = t.Button(
    window,
    text="新的文件",
    font=("Arial", 12),
    width=25,
    height=1,
    command=input_new_dir,
)
select_file_button.pack()
create_new_file.pack()
window.mainloop()
