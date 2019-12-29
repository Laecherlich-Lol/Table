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
        filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")),
    )
    print(window.filename)


select_file_button = t.Button(
    window,
    text="choose the directory",
    font=("Arial", 12),
    width=10,
    height=1,
    command=click_button,
)
select_file_button.pack()
window.mainloop()
