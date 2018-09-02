#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
import os


def test(text):
    command = 'xterm -fa "Monospace" -fs 14 -e '+text+' &'
    print command
    os.popen(command)


## Main window
root = Tk()
root.title("Buttons!")
## Grid sizing behavior in window
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
## Canvas
cnv = Canvas(root)
cnv.grid(row=0, column=0, sticky='nswe')
## Scrollbars for canvas
hScroll = Scrollbar(root, orient=HORIZONTAL, command=cnv.xview)
hScroll.grid(row=1, column=0, sticky='we')
vScroll = Scrollbar(root, orient=VERTICAL, command=cnv.yview)
vScroll.grid(row=0, column=1, sticky='ns')
cnv.configure(xscrollcommand=hScroll.set, yscrollcommand=vScroll.set)
## Frame in canvas
frm = Frame(cnv)
## This puts the frame in the canvas's scrollable zone
cnv.create_window(0, 0, window=frm, anchor='nw')

button = Button(frm,text="QUIT", fg="red",
                    command=cnv.quit)
button.pack(side=BOTTOM)


commandsFile = open('commands.txt',"r")

for line in commandsFile:
    b = Button(frm, text=line.rstrip(),
                         command=lambda text=line.rstrip(): test(text),width=60)
    b.pack(side=TOP, padx=2, pady=2)

## Update display to get correct dimensions
frm.update_idletasks()
## Configure size of canvas's scrollable zone
cnv.configure(scrollregion=(0, 0, frm.winfo_width(), frm.winfo_height()))
## Go!
img = PhotoImage(file='icon.gif')
root.tk.call('wm', 'iconphoto', root._w, img)
root.geometry("500x1200")
root.mainloop()
