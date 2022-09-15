from tkinter import *
from functools import partial
from calculate import *


# 生成计算器主界面
def buju(root):
    menu = Menu(root)  # 菜单
    submenu1 = Menu(menu, tearoff=0)  # 分窗，0为在原窗，1为点击分为两个窗口
    menu.add_cascade(label='编辑', menu=submenu1)  # 添加子选项（label参数为显示内容）
    submenu1.add_command(label='复制', command=lambda: bianji(entry, 'copy'))  # 添加命令
    submenu1.add_command(label='剪切', command=lambda: bianji(entry, 'cut'))
    submenu1.add_command(label='粘贴', command=lambda: bianji(entry, 'paste'))
    submenu2 = Menu(menu, tearoff=0)
    menu.add_cascade(label='查看', menu=submenu2)
    submenu2.add_command(label='帮助', command=lambda: chakan(entry, 'help'))
    submenu2.add_command(label='作者', command=lambda: chakan(entry, 'author'))
    root.config(menu=menu)  # 重新配置，添加菜单

    label = Label(root, width=29, height=1, bd=5, bg='#FFFACD', anchor='se',
                  textvariable=label_text)  # 标签，可以显示文字或图片
    label.grid(row=0, columnspan=5)  # 布局器，向窗口注册并显示控件； rowspan：设置单元格纵向跨越的列数

    entry = Entry(root, width=23, bd=5, bg='#FFFACD', justify="right", font=('微软雅黑', 12))  # 文本框（单行）
    entry.grid(row=1, column=0, columnspan=5, sticky=N + W + S + E, padx=5, pady=5)  # 设置控件周围x、y方向空白区域保留大小

    myButton = partial(Button, root, width=5, cursor='hand2', activebackground='#90EE90')  # 偏函数：带有固定参数的函数
    button_sin = myButton(text='sin', command=lambda: get_input(entry, 'sin('))  # 按钮
    button_arcsin = myButton(text='arcsin', command=lambda: get_input(entry, 'arcsin('))
    button_exp = myButton(text='e', command=lambda: get_input(entry, 'e'))
    button_ln = myButton(text='ln', command=lambda: get_input(entry, 'ln('))
    button_xy = myButton(text='x^y', command=lambda: get_input(entry, '^'))
    button_sin.grid(row=2, column=0)
    button_arcsin.grid(row=2, column=1)
    button_exp.grid(row=2, column=2)
    button_ln.grid(row=2, column=3)
    button_xy.grid(row=2, column=4)

    button_shanyige = myButton(text='←', command=lambda: backspace(entry))  # command指定按钮消息的回调函数
    button_shanquanbu = myButton(text=' C ', command=lambda: clear(entry))
    button_zuokuohao = myButton(text='(', command=lambda: get_input(entry, '('))
    button_youkuohao = myButton(text=')', command=lambda: get_input(entry, ')'))
    button_genhao = myButton(text='√x', command=lambda: get_input(entry, '√('))
    button_shanyige.grid(row=3, column=0)
    button_shanquanbu.grid(row=3, column=1)
    button_zuokuohao.grid(row=3, column=2)
    button_youkuohao.grid(row=3, column=3)
    button_genhao.grid(row=3, column=4)

    button_7 = myButton(text=' 7 ', command=lambda: get_input(entry, '7'))
    button_8 = myButton(text=' 8 ', command=lambda: get_input(entry, '8'))
    button_9 = myButton(text=' 9 ', command=lambda: get_input(entry, '9'))
    button_chu = myButton(text=' / ', command=lambda: get_input(entry, '/'))
    button_yu = myButton(text='%', command=lambda: get_input(entry, '%'))
    button_7.grid(row=4, column=0)
    button_8.grid(row=4, column=1)
    button_9.grid(row=4, column=2)
    button_chu.grid(row=4, column=3)
    button_yu.grid(row=4, column=4)

    button_4 = myButton(text=' 4 ', command=lambda: get_input(entry, '4'))
    button_5 = myButton(text=' 5 ', command=lambda: get_input(entry, '5'))
    button_6 = myButton(text=' 6 ', command=lambda: get_input(entry, '6'))
    button_cheng = myButton(text=' * ', command=lambda: get_input(entry, '*'))
    button_jiecheng = myButton(text='二进制', command=lambda: jinzhi(entry))
    button_4.grid(row=5, column=0)
    button_5.grid(row=5, column=1)
    button_6.grid(row=5, column=2)
    button_cheng.grid(row=5, column=3)
    button_jiecheng.grid(row=5, column=4)

    button_1 = myButton(text=' 1 ', command=lambda: get_input(entry, '1'))
    button_2 = myButton(text=' 2 ', command=lambda: get_input(entry, '2'))
    button_3 = myButton(text=' 3 ', command=lambda: get_input(entry, '3'))
    button_jian = myButton(text=' - ', command=lambda: get_input(entry, '-'))
    button_dengyu = myButton(text=' \n = \n ', command=lambda: calculator(entry))
    button_1.grid(row=6, column=0)
    button_2.grid(row=6, column=1)
    button_3.grid(row=6, column=2)
    button_jian.grid(row=6, column=3)
    button_dengyu.grid(row=6, column=4, rowspan=2)  # rowspan：设置单元格横向跨越的行数

    button_pai = myButton(text=' π ', command=lambda: get_input(entry, 'π'))
    button_0 = myButton(text=' 0 ', command=lambda: get_input(entry, '0'))
    button_xiaoshudian = myButton(text=' . ', command=lambda: get_input(entry, '.'))
    button_jia = myButton(text=' + ', command=lambda: get_input(entry, '+'))
    button_pai.grid(row=7, column=0)
    button_0.grid(row=7, column=1)
    button_xiaoshudian.grid(row=7, column=2)
    button_jia.grid(row=7, column=3)


# 对文本框中的算式或答案进行复制、剪切或粘贴
def bianji(entry, argu):
    """
    :param entry: 文本框
    :param argu: 按钮对应的值
    """
    if argu == 'copy':
        entry.event_generate("<<Copy>>")
    elif argu == 'cut':
        entry.event_generate("<<Cut>>")
        clear(entry)
    elif argu == 'paste':
        entry.event_generate("<<Paste>>")


# 查看使用帮助和作者信息
def chakan(entry, argu):
    root = Tk()
    root.resizable(0, 0)
    text = Text(root, width=20, height=2, bd=5, bg='#FFFACD', font=('微软雅黑', 12))
    text.grid(padx=5, pady=5)
    if argu == 'help':
        root.title('帮助')
        text.insert(INSERT, '这是高级计算器\n')
        text.insert(INSERT, '请自行查阅资料')
    elif argu == 'author':
        root.title('作者')
        text.insert(INSERT, 'Author：小树\n')
        text.insert(INSERT, 'Time：2019-07-08')


# 删除最后一次输入内容
def backspace(entry):
    entry.delete(len(entry.get()) - 1)  # 删除文本框的最后一个输入值


# 删除所有输入内容和显示内容
def clear(entry):
    entry.delete(0, END)  # 删除文本框的所有内容
    label_text.set('')


# 点击计算器输入按钮后向文本框中添加内容
def get_input(entry, argu):
    formula = entry.get()
    for char in formula:
        if '\u4e00' <= char <= '\u9fa5':
            clear(entry)  # 删除文本框中的汉字显示，减少手动删除操作
    entry.insert(INSERT, argu)  # 使用END时，键盘敲入和按键输入组合操作会出错


# 十进制整数转换为二进制整数
def jinzhi(entry):
    try:
        formula = entry.get()
        if re.match('\d+$', formula):
            number = int(formula)
            cunchu = []  # 放置每次除以2后的余数
            result = ''
            while number:
                cunchu.append(number % 2)
                number //= 2  # 整数除法,返回商
            while cunchu:
                result += str(cunchu.pop())  # 将所有余数倒置得到结果
            clear(entry)
            entry.insert(END, result)
            label_text.set(''.join(formula + '='))
        else:
            clear(entry)
            entry.insert(END, '请输入十进制整数')
    except:
        clear(entry)
        entry.insert(END, '出错')


# 点击“=”后进行计算
def calculator(entry):
    try:
        formula = entry.get()
        # 输入内容只是数字或π或e时，仍显示该内容
        if re.match('-?[\d+,π,e]\.?\d*$', formula):
            label_text.set(''.join(formula + '='))
            return
        # 输入内容是算式时，显示其计算结果
        result = final_calc(formula_format(formula))
        clear(entry)
        entry.insert(END, result)  # 将结果输出到文本框中
        label_text.set(''.join(formula + '='))
    except:
        clear(entry)
        entry.insert(END, '出错')


if __name__ == '__main__':
    root = Tk()  # 生成窗口
    root.title('理正计算器')  # 窗口的名字
    root.resizable(0, 0)  # 窗口大小可调性，分别表示x，y方向的可变性
    global label_text  # 定义全局变量
    label_text = StringVar()
    buju(root)
    root.mainloop()  # 进入消息循环（必需组件），否则生成的窗口一闪而过

