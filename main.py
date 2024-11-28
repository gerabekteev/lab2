from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
import pygame as pg

pg.mixer.init()
root = Tk()
l = []
cur_i = 0
cur = ""
cur_path = ""
h = 0


def on_item_click(event):
    # Получить индекс выбранного элемента
    selected_index = listbox.curselection()
    if selected_index:
        # Получить текст выбранного элемента

        selected_item = listbox.get(selected_index)
        global h,cur,cur_i,cur_path
        h = 1
        cur = selected_item
        cur_i = selected_index[0]
        cur_path = l[cur_i]["path"]
        update_text()
        print(cur,cur_path)
        play()


def update_listbox(items):
    listbox.delete(0, END)  # Очистить Listbox
    for item in items:
        listbox.insert(END, item["name"])

def update_text():
    global cur
    text_var.set(cur[:60])


def find_music():
    file_name = fd.askopenfilename()
    if file_name:
        pg.mixer.music.load((file_name))
        global l, h,cur_path,cur_i,cur
        l.append({"name": file_name[file_name.rfind('/') + 1:file_name.rfind('.')], "path": file_name})
        h = 1
        cur = file_name[file_name.rfind('/') + 1:file_name.rfind('.')]
        cur_path = file_name
        cur_i = len(l)-1
        update_listbox(l)
        update_text()


def play():
    global cur_path,h
    if cur_path:
        if h == 1:
            pg.mixer.music.load((cur_path))
            pg.mixer.music.play()
        elif h == 2:
            pg.mixer.music.unpause()
            h = 1
    update_text()

def pause():
    global h
    global l
    pg.mixer.music.pause()
    h = 2

def up():
    global cur,cur_i,l,cur_path,h
    if cur_i!=len(l)-1:
        cur_i += 1
    cur = l[cur_i]["name"]
    cur_path = l[cur_i]["path"]
    h = 1
    play()
    update_text()
def down():
    global cur,cur_i,l,cur_path,h
    if cur_i != 0:
        cur_i -= 1
    cur = l[cur_i]["name"]
    cur_path = l[cur_i]["path"]
    h = 1
    play()
    update_text()

def on_scale_change(value):
    pg.mixer.music.set_volume(int(value)/100)


root["bg"] = "#ffffff"
root.title("mp3 player")
# root.wm_attributes('-alpha',0.7)
root.geometry("800x450")
root.resizable(width=True, height=True)

# нижний прямоугоник
frame = Frame(root, bg="orange")
frame.place(relx=0.05, rely=0.8, relwidth=0.9, relheight=0.15)
# верхний прямоугоник
framelist = Frame(root, bg="orange")
framelist.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.7)

#для текста
text_var = StringVar()
text_var.set("Выбранные файлы окажутся в списке тут")

listbox = Listbox(framelist, font=("Arial", 12), selectmode=SINGLE)
listbox.place(relx=0.01, rely=0.02,relwidth=0.98)
update_listbox(l)
listbox.bind("<<ListboxSelect>>", on_item_click)

name_text = Label(framelist,textvariable=text_var, bg="orange", font=60)
name_text.place(relx=0.02, rely=0.7)

title = Label(frame, text="добавь файл", bg="orange", font=40)
title.place(relx=0.01, rely=0.01)
title = Label(frame, text="звук:", bg="orange", font=40)
title.place(relx=0.4, rely=0.2)
btn = Button(frame, text="файл", bg="white", command=find_music)
btn.place(relx=0.01, rely=0.5)
btn_play = Button(frame, text=">", bg="white", command=play)
btn_play.place(relx=0.11, rely=0.5)
btn_pause = Button(frame, text="||", bg="white", command=pause)
btn_pause.place(relx=0.14, rely=0.5)

btn_play = Button(frame, text=">>", bg="white", command=up)
btn_play.place(relx=0.17, rely=0.5)

# Ползунок
slider = Scale(
    frame,
    from_=0,          # Начальное значение
    to=100,           # Конечное значение
    orient="horizontal",  # Горизонтальный ползунок
    length=300,       # Длина ползунка
    command=on_scale_change  # Функция для обработки изменений
)
slider.set(80)
slider.place(relx=0.5,rely=0.1)

btn_play = Button(frame, text="<<", bg="white", command=down)
btn_play.place(relx=0.07, rely=0.5)
root.mainloop()
