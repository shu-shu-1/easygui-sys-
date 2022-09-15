from tkinter import *
root=Tk() #设置窗口对象
root.title('计算器')
root.geometry("440x550")
root.iconbitmap("Python\计算器\程序组\icon.ico")
root['bg']='yellow2'
frame = LabelFrame(root, width=350, height=50)
frame.pack()
frame.place(x=0,y=0)
  #显示框
label = Label(frame, text="",  font=('黑体', 20),height=3, width=31,fg='blue',bg='Pink3')
label.pack() 
global s
s=""

#键.
def figure_dot():
  global s
  s=s+"."
  label.config(text=s)
#键0
def figure_0():
  global s
  s=s+"0"
  label.config(text=s)
#键1
def figure_1():
  global s
  s=s+"1"
  label.config(text=s)
 
#键2
def figure_2():
  global s
  s=s+"2"
  label.config(text=s)
 
#键3
def figure_3():
  global s
  s=s+"3"
  label.config(text=s)
#键4
def figure_4():
  global s
  s=s+"4"
  label.config(text=s)
#键5
def figure_5():
  global s
  s=s+"5"
  label.config(text=s)
#键6
def figure_6():
  global s
  s=s+"6"
  label.config(text=s)
#键7
def figure_7():
  global s
  s=s+"7"
  label.config(text=s)
#键8
def figure_8():
  global s
  s=s+"8"
  label.config(text=s)
#键9
def figure_9():
  global s
  s=s+"9"
  label.config(text=s)
#加法键
def figure_addition():
  global s
  s=s+"+"
  label.config(text=s)
#减法键
def figure_subtraction():
  global s
  s=s+"-"
  label.config(text=s)
#乘法键
def figure_multiplication():
  global s
  s = s+"*"
  label.config(text=s)
#除法键
def figure_division():
  global s
  s = s+"/"
  label.config(text=s)
 
#清空键
def figure_clear():
  global s
  s = ""
  label.config(text=s)
#百分键（python中%为求余数，此处从百分之几改为乘0.01，数值和百分之几相等）
def figure_percent():
  global s
  global s
  s = s+"*0.01"
  label.config(text=s)
  
#退格键
def figure_back():
  global s
  b = list(s)
  b.pop()
  s=("".join(b))
  label.config(text=s)

#等于键
def figure_vablue():
  global s
  x=eval(s)
  s=str(x)
  label.config(text=s)
btn0 = Button(root, text=".", font=('黑体', 15), width=6, height=2, command=figure_dot, bg='Skyblue', bd=5)
btn0.place(x=20, y=440)
 
btn0 = Button(root, text="0", font=('黑体', 15), width=6, height=2, command=figure_0, bg='Skyblue', bd=5)
btn0.place(x=110, y=440)  
 
btn1 = Button(root, text="1", font=('黑体', 15), width=6,height=2, command=figure_1, bg='Skyblue', bd=5)
btn1.place(x=20, y=360)  
 
btn2 = Button(root, text="2", font=('黑体', 15), width=6,  height=2, command=figure_2, bg='Skyblue', bd=5)
btn2.place(x=110, y=360)  
 
btn3 = Button(root, text="3", font=('黑体', 15), width=6, height=2, command=figure_3, bg='Skyblue', bd=5)
btn3.place(x=200, y=360)  
 
btn4 = Button(root, text="4", font=('黑体', 15), width=6,height=2, command=figure_4, bg='Skyblue', bd=5)
btn4.place(x=20, y=280) 
 
btn5 = Button(root, text="5", font=('黑体', 15), width=6,height=2, command=figure_5, bg='Skyblue', bd=5)
btn5.place(x=110, y=280) 
 
btn6 = Button(root, text="6", font=('黑体', 15), width=6,height=2, command=figure_6, bg='Skyblue', bd=5)
btn6.place(x=200, y=280) 
 
btn7 = Button(root, text="7", font=('黑体', 15), width=6,height=2, command=figure_7, bg='Skyblue', bd=5)
btn7.place(x=20, y=200) 
 
btn8 = Button(root, text="8", font=('黑体', 15), width=6,height=2, command=figure_8, bg='Skyblue', bd=5)
btn8.place(x=110, y=200)  
 
btn9 = Button(root, text="9", font=('黑体', 15), width=6, height=2, command=figure_9, bg='Skyblue', bd=5)
btn9.place(x=200, y=200)  
 
btn_add = Button(root, text="+", font=('黑体', 15), width=6,height=2, command=figure_addition, bg='Pink', bd=5)
btn_add.place(x=290, y=280)  
 
btn_sub = Button(root, text="-", font=('黑体', 15), width=6,height=2, command=figure_subtraction, bg='Pink', bd=5)
btn_sub.place(x=290, y=200)  
 
btn_multi = Button(root, text="×", font=('黑体', 15), width=6, height=2, command=figure_multiplication, bg='Pink', bd=5)
btn_multi.place(x=200, y=120) 
 
btn_divi = Button(root, text="÷", font=('黑体', 15), width=6, height=2,command=figure_division, bg='Pink', bd=5)
btn_divi.place(x=110, y=120) 
 
btn_clear = Button(root, text="C",  font=('黑体', 15), width=6, height=2,command=figure_clear, bg='Pink',bd=5)
btn_clear.place(x=20, y=120)
 
btn_back = Button(root, text="←", font=('黑体', 15), width=6,height=2, command=figure_back, bg='Pink', bd=5)
btn_back.place(x=290, y=120)
 
btn_back = Button(root, text="%", font=('黑体', 15), width=6,height=2, command=figure_percent, bg='Skyblue', bd=5)
btn_back.place(x=200, y=440)
 
btn_vablue = Button(root, text="=", font=('黑体', 15), width=6,height=6, command=figure_vablue, bg='white', bd=5)
btn_vablue.place(x=290, y=360)
root.mainloop()