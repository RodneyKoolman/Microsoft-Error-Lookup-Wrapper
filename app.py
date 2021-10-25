import tkinter as tk
from tkinter import ttk, Text
from tkinter.constants import BOTH, BOTTOM, TOP, X
import subprocess

# Main window
root = tk.Tk()
root.title('Microsoft Error Lookup Tool - Wrapper')
root.geometry('1000x500')
root.resizable(True, True)

# Frame
frame = ttk.Frame(root)
frame.pack(padx=10, pady=10, fill=BOTH, expand=True)

# Settings
tool = 'input\Err_6.4.5.exe'
message = 'You can search Microsoft errors in hexadecimal 0x0 or decimal 0'

def search(query):
    text_box.delete("1.0", "end")

    with subprocess.Popen([tool, query], shell=True, stdout=subprocess.PIPE, bufsize=1, universal_newlines=True) as p:
        for line in p.stdout:
            text_box.insert(tk.END, line)

def clear():
    text_box.delete("1.0","end")
    query_entry.delete(0, 'end')
    text_box.insert('end', message)

query_var = tk.StringVar()
query_entry = tk.Entry(frame, textvariable=query_var, font='sans 14 bold')
query_entry.pack(side=TOP, fill=X, pady=5)
query_entry.focus()

search_button = tk.Button(frame, text="search", font='sans 14 bold', command=lambda:search(query_var.get()))
search_button.pack(fill=X)

clear_button = tk.Button(frame, text="clear all", font='sans 14 bold', command=clear)
clear_button.pack(fill=X)

text_box = Text(frame, height=13, width=40, wrap='word')
text_box.pack(side=BOTTOM, pady=10, fill=BOTH, expand=True)
text_box.insert('end', message)

root.mainloop()
