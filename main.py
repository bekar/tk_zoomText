#!/usr/bin/env python

import tkinter as tk
import tkinter.font as tkFont

def zoom(side):
    name = t['font']
    # name = "TkTextFont"
    # name = "TextFont"
    # name = "TkDefaultFont"
    f = tkFont.nametofont(name)
    print(name)
    print(f.config())
    print(f["size"])
    print(f.actual())
    s = abs(f["size"])
    ns = s - 2 * side
    f.config(size=ns)
    # t.config(font=f)


if __name__ == '__main__':
    root = tk.Tk()
    t = tk.Text(root)
    t.pack(expand=1, fill="both")
    t.insert("end", open("main.py").read())

    t.bind('<Control-Button-4>', lambda e: zoom(-1))
    t.bind('<Control-Button-5>', lambda e: zoom(1))

    root.bind("<Key-Escape>", lambda event: quit())
    root.mainloop()
