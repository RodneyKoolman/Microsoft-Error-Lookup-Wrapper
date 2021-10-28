import sys
import os
import subprocess
import tkinter as tk
from tkinter import ttk, Text, Scrollbar
from tkinter.constants import BOTH, BOTTOM, TOP, RIGHT, X, Y

root = tk.Tk()
root.title("Microsoft Error Lookup Wrapper")
root.geometry("1000x500")
root.resizable(True, True)

frame = ttk.Frame(root)
frame.pack(padx=10, pady=10, fill=BOTH, expand=True)

input = "input\Err_6.4.5.exe"
message = "Usage:\n\
1. Search decorated hex (0x54f)\n\
2. Search implicit hex (54f)\n\
3. Search ambiguous (1359)\n\
4. Search exact string (=ERROR_INTERNAL_ERROR)\n\
5. Search substring (:INTERNAL_ERROR)\n\
6. Use show all to output all known error codes\n\
7. Use clear all to clear all input and output fields\n\n\
There are currently 25259 return codes registered from 173 sources."


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def search(query):
    if query == "":
        return
    text_box.delete("1.0", "end")

    with subprocess.Popen(
        [resource_path(input), query],
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
        bufsize=1,
        universal_newlines=True,
    ) as p:
        for line in p.stdout:
            text_box.insert(tk.END, line)


def clear():
    text_box.delete("1.0", "end")
    query_entry.delete(0, "end")
    text_box.insert("end", message)


query_var = tk.StringVar()
query_entry = tk.Entry(frame, textvariable=query_var, font="sans 14 bold")
query_entry.pack(side=TOP, fill=X, pady=5)
query_entry.focus()

search_button = tk.Button(
    frame, text="search", font="sans 14 bold", command=lambda: search(query_var.get())
)
search_button.pack(fill=X)

showall_button = tk.Button(
    frame, text="show all", font="sans 14 bold", command=lambda: search("/:outputtoCSV")
)
showall_button.pack(fill=X)

clear_button = tk.Button(frame, text="clear all", font="sans 14 bold", command=clear)
clear_button.pack(fill=X)

scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)

text_box = Text(
    frame,
    height=13,
    width=40,
    wrap="word",
    yscrollcommand=scrollbar.set,
    relief="sunken",
)
text_box.pack(side=BOTTOM, pady=10, fill=BOTH, expand=True)
text_box.insert("end", message)

scrollbar.config(command=text_box.yview)

root.mainloop()
