# -*- coding: utf-8 -*-
# @Time    : 2022-09-10 19:32
# @Author  : young wang
# @FileName: app.py
# @Software: PyCharm

from tkinter import *
from PIL import ImageTk, Image

if __name__ == "__main__":
    # Calling the Tk (The initial constructor of tkinter)
    root = Tk()

    mylabel = Label(root, text ='hellow world')
    mylabel.pack()
    root.mainloop()
    #
    # # We will make the title of our app as Image Viewer
    # root.title("Image Viewer")
    #
    # # The geometry of the box which will be displayed
    # # on the screen
    # root.geometry("700x700")