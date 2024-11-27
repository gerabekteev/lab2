from tkinter import *
from tkinter import filedialog as fd
import pygame as pg
pg.mixer.init()
root = Tk()
l = []
cur_i = 0
cur = ""
h = 0
def find_music():
    file_name = fd.askopenfilename()
    if file_name:
        pg.mixer.music.load((file_name))
        global l,h
        l.append({"name": file_name[file_name.rfind('/')+1:file_name.rfind('.')], "path": file_name})
        h = 1
def play():
    global h
    if h==1:
        pg.mixer.music.play()
    elif h==2:
        pg.mixer.music.unpause()
        h = 2
def pause():
    global h
    global l
    for i in l:
        print(i["name"],"|",i["path"])
    pg.mixer.music.pause()
    h = 2

root["bg"] = "#ffffff"
root.title("mp3 player")
# root.wm_attributes('-alpha',0.7)
root.geometry("800x450")
root.resizable(width=True, height=True)



frame = Frame(root, bg="orange")
frame.place(relx=0.05, rely=0.8, relwidth=0.9, relheight=0.15)

framelist = Frame(root, bg="orange")
framelist.place(relx=0.05,rely=0.05,relwidth=0.9,relheight=0.7)

title = Label(frame, text="добавь файл", bg="orange", font=40)
title.place(relx=0.01,rely=0.01)
btn = Button(frame,text="файл",bg="white",command = find_music)
btn.place(relx=0.01,rely=0.5)
btn_play = Button(frame,text=">",bg="white",command = play)
btn_play.place(relx=0.07,rely=0.5)
btn_pause = Button(frame,text="||",bg="white",command = pause)
btn_pause.place(relx=0.10,rely=0.5)
root.mainloop()
