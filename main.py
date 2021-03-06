#!/usr/bin/env python

import tkinter as tk
import tkinter.font as tkFont

class ZoomText(tk.Text):
    '''font resize Text() Wrapper, with
    keybinding Ctrl + {Scroll,+,-,0}'''

    def __init__(self, parent=None):
        self.container = tk.Frame(parent)
        self.container.pack(fill="both", expand=True)

        tk.Text.__init__(self, self.container)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.grid(row=0, column=0, sticky="nsew")
        self.bind_keys()

    def bind_keys(self):
        self.bind('<Control-Button-4>', lambda e: self.resize(1))
        self.bind('<Control-Key-plus>', lambda e: self.resize(1))
        self.bind('<Control-Button-5>', lambda e: self.resize(-1))
        self.bind('<Control-Key-minus>', lambda e: self.resize(-1))
        self.bind('<Control-0>', lambda e: self.font.config(size=self.size))

    def resize(self, d=1):
        self.container.grid_propagate(False)
        font_names = [ self.tag_cget(t, "font") for t in self.tag_names() ]
        font_names.append(self['font'])
        for name in set(font_names):
            try:
                font = tkFont.nametofont(name)
                s = abs(font["size"]); #print(s)
                font.config(size=max(s+2*d, 8))
            except:
                continue

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Zoom Text")
    root.bind("<Key-Escape>", lambda event: quit())

    t = ZoomText()
    t.insert("end", t.__doc__)
    t.focus_set()

    root.mainloop()
