import tkinter as tk
from tkinter import messagebox

def text_win(d):
    window = tk.Tk()
    def close_window():
        window.destroy()

    custom_font = ("JetBrainsMono NF", 14)
    textbox = tk.Text(window, height=10)
    textbox.grid(row = 1)

    for k in d:
        textbox.insert(tk.END,str(k)+'\n')
    bt = tk.Button(window, text="OK", command=close_window, font=custom_font).grid(row=11, column=6)
    
    tk.mainloop()

def result_prompt(flag=None):

    if flag == 1:
        msg = "\nCommand Executed Successfully.\n"
    elif flag == 0:
        msg = "\nSome Error Occured.\n"
    else:
        msg = "\nRuntime Error\n"

    custom_font = ("JetBrainsMono NF", 14)
    messagebox.showinfo("Result", msg)
