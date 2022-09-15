import math
from tkinter import *
def add_word(c):
    if c == '=': txt.replace('0.0', 'end', eval(txt.get('0.0', 'end')))  # 填充计算结果
    else: txt.insert('end', c)  # 添加按钮输入内容
def handler(fun, c):
    return lambda fun=fun, c=c: fun(c)
root = Tk()
root.title("计算器")
root.iconbitmap("Python\计算器\程序组\icon.ico")
text_arr=['1','2','3','+','4','5','6','-','7','8','9','*','.','0','=','/']
ncol,bw,bh,padding,space,th = 4,50,30,20,10,100  # 按钮列数、按钮宽度、高度、页面边距、按钮间边距、文本框高度
nrow = math.ceil(len(text_arr)*1.0/ncol)  # 按钮行数
root.geometry(f"{bw * ncol + padding * 2 + space * (ncol - 1)}x{th + bh * nrow + padding * 3 + space * (nrow - 1)}")

txt = Text(root)
txt.place(x=padding,y=padding,width=bw*ncol+space*(ncol-1),height=th)
for index in range(len(text_arr)):
    row_index, col_index = (index%ncol), (index//ncol)  # 行序号、列序号
    btn = Button(root, text=text_arr[index], command=handler(add_word, text_arr[index]))
    btn.place(x=padding+row_index*(bw+space), y=(th+padding*2)+col_index*(bh+space), width=bw, height=bh)
root.mainloop()