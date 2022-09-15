# import tkinter
from tkinter import *
from webbrowser import *
import webbrowser
import os
from os import *

aaa = '初始值，后面数字防止与初始值碰撞：121212173875264376274657364725685767346587236487632978263457637467657634765723436254363756874675637467564875673465736485638765783467836521212123454657887654321 '
ChooseP =False
ChooseC =False

def funChooseP():
    with open
# def funChooseC():
def setting():
    global radioBtnA,radioBtnB
    window = Tk()
    v = IntVar()
    radioBtnA = Radiobutton(window, text="启用 规避重复搜索功能", variable=v, value=1, command=funChooseP)
    radioBtnA.pack()
    radioBtnB = Radiobutton(window, text="弃用 规避重复搜索功能", variable=v, value=2, command=funChooseC)
    radioBtnB.pack()
    lab = Label(window, text="")
    lab.pack()
    window.title('一键搜歌-设置')
    window.geometry('380x300')
    window.resizable(width=False, height=False)
    window.iconbitmap(r"D:\my_work\Python\一键搜歌\一键搜歌图标.ico")
    window.mainloop()
def func():
    global w,b,aaa
    if entry.get() == '':
        w['text'] = "请输入文本!"
        w['fg'] = "red"
    elif entry.get() == aaa:
        w['text'] = "重复的搜索内容!"
        w['fg'] = "red"
    else:
        w['text'] = "成功✓"
        w['fg'] = "green"
        aaa = entry.get()
        b = 'https://tonzhon.com/search?keyword=' + entry.get()
        webbrowser.open_new(b)


win = Tk()
win.title('一键搜歌')
win.geometry('380x300')
win.resizable(width=False, height=False)
win.iconbitmap(r"D:\my_work\Python\一键搜歌\一键搜歌图标.ico")


label = Label(win, text="欢迎使用一键搜歌！", font=("仿宋", 12), fg="black")
label.grid()

entry = Entry(win, font=("仿宋", 15), fg="black")
entry.grid(row=2, column=0)

app = Label(win, text="引擎by铜钟", font=("仿宋", 12), fg="black")
app.grid(row=3, column=0)

app1 = Label(win, text="界面by tkinter", font=("仿宋", 12), fg="black")
app1.grid(row=5, column=1)

button = Button(win, text="开始搜索", font=("微软雅黑", 10), fg="blue", command=func)
button.grid(row=2, column=1)

w = Label(win, text="请输入文本…", font=("微软雅黑", 10), fg="black")
w.grid(row=1, column=1)

photo = PhotoImage(file=r"铜钟.png")
imageLabel = Label(win, image=photo)
imageLabel.grid(row=4, column=0)

photo1 = PhotoImage(file=r"D:\my_work\Python\一键搜歌\tkinter.png")
imageLabel1 = Label(win, image=photo1)
imageLabel1.grid(row=6, column=1)

win.mainloop()
