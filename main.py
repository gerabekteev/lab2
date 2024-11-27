from tkinter import *
from tkinter import filedialog as fd
import pygame as pg
pg.mixer.init()
root = Tk()
def find_music():
    file_name = fd.askopenfilename()
    pg.mixer.music.load((file_name))
    pg.mixer.music.play()

root["bg"] = "#ffffff"
root.title("mp3 player")
# root.wm_attributes('-alpha',0.7)
root.geometry("800x450")
root.resizable(width=True, height=True)



frame = Frame(root, bg="orange")
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)

title = Label(frame, text="выбири файл", bg="orange", font=40)
title.pack()
btn = Button(frame,text="файл",bg="white",command = find_music)
btn.pack()
root.mainloop()
