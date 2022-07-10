from ast import While
import easygui as gui
from tkinter import *
import os as cmd
from turtle import *
from datetime import *


def Skip(step):               #建立表的外框
    penup()
    forward(step)
    pendown()

def mkHand(name,length):      #注册turtle形状，建立表针turtle
    reset()
    Skip(-length*0.1)
    begin_poly()
    forward(length*1.1)
    end_poly()
    handForm = get_poly()
    register_shape(name,handForm)

def Init():
    global secHand,minHand,hurHand,printer
    mode("logo")             #重置turtle指向北

    mkHand("secHand",125)    #建立三个表针并初始化
    mkHand("minHand",130)
    mkHand("hurHand",90)

    secHand = Turtle()
    secHand.shape("secHand")
    minHand = Turtle()
    minHand.shape("minHand")
    hurHand = Turtle()
    hurHand.shape("hurHand")

    for hand in secHand,minHand,hurHand:
        hand.shapesize(1,1,3)
        hand.speed(0)

    printer = Turtle()        #建立输出文字turtle
    printer.hideturtle()
    printer.penup()

def SetupClock(radius):      #建立表外框
    reset()
    pensize(7)
    for i in range(60):
        Skip(radius)
        if i % 5 == 0:
            forward(20)
            Skip(-radius-20)
        else:
            dot(5)
            Skip(-radius)
        right(6)

def Week(t):
    week = ["Mon", "Tues", "Wed","Thur", "Fri", "Sat", "Sun"]
    return week[t.weekday()]

def Date(t):
    y = t.year
    m = t.month
    d = t.day
    return "%s %d %d" % (y, m, d)
def Tick():
    t = datetime.today()
    second = t.second + t.microsecond * 0.000001
    minute = t.minute + second/60.0
    hour = t.hour + minute/60.0
    secHand.setheading(6*second)
    minHand.setheading(6*minute)
    hurHand.setheading(30*hour)
    tracer(False)
    printer.forward(65)
    printer.write(Week(t),align="center",font=("微软雅黑",14,"bold"))
    printer.back(130)
    printer.write(Date(t),align="center",font=("微软雅黑",14,"bold"))
    printer.home()
    tracer(True)
    ontimer(Tick,100)                #100ms后继续调用tick

def main():
    tracer(False)
    Init()
    SetupClock(160)
    tracer(True)
    Tick()
    mainloop()


def is_contains_chinese(strs):
    for _char in strs:
        if '\u4e00' <= _char <= '\u9fa5':
            return True
    return False

def get_all_file_in_dir(dir_path):
    '''
    获取目录下的所有文件
    :return:
    '''
    file_name_list = []
    for root, dirs, files in cmd.walk(dir_path):
        if files:
            for name in files:
            
				# 此处可以增加文件名称过滤条件， 比如 -----
				# 跳过所有 ~$ 开头的文件
                # if name.startswith(('~$',)):
                #     continue
                # ---------------------------------------

                file_name = '{0}/{1}'.format(root, name).replace('\\', '/')
                file_name_list.append(file_name)
    return file_name_list


with open(r'D:\my_work\Python\sys\user_name.txt', 'r') as k:
    kk = k.read()
if kk == '' or kk is None:
    gui.msgbox(msg="您还没有注册账号", ok_button='确定')
    new_user = gui.enterbox(msg='请输入您的账户名+密码（使用空格分隔）：', title='账户注册')
    # new_user=input('请输入您的账户名+密码（使用空格分隔）：')
    new_user1 = str.split(new_user, ' ')
    if new_user1[1].isdigit():
        gui.msgbox(msg='密码不能全是数字！', title='账户注册-错误', ok_button='退出')
        quit()
    with open(r'D:\my_work\Python\sys\user_name.txt', 'r+') as y:
        y.write(new_user1[0])
    with open(r'D:\my_work\Python\sys\pwd.txt', 'r+') as y1:
        y1.write(new_user1[1])
    gui.msgbox(msg='设置完毕，请重启')
    quit()

i = 0  # 统计循环执行的次数
while i < 5:  # 0,1,2 ,当i=3时 3<3False，循环执行结束
    user_input = str.split(gui.enterbox(msg='请输入您的用户名+密码（使用空格分隔）：', title='登录'), ' ')
    user_name = user_input[0]
    pwd = user_input[1]
    # 判断
    with open(r'D:\my_work\Python\sys\pwd.txt', 'r') as y2:
        yy = y2.read()
    if user_name == kk and pwd == yy:
        gui.msgbox(msg='系统正在登录，请稍后', title='登录', ok_button='确定')
        # 改变循环条件，退出循环
        i = 8  # 判断8<3 False,循环执行结束
    else:
        if i < 5:
            gui.msgbox(msg='用户名或密码不正确，您还有' + str(4 - i) + '次机会', title='登录', ok_button='确定')
            # print('用户名或密码不正确，您还有',4-i,'次机会')
        i += 1  # 改变循环变量

if i == 5:  # 当用户或密码输入不正确的时候，循环执行结束时，i的最大值为3
    gui.msgbox(msg='对不起，五次均输入错', title='登录', ok_button='确定')
    # print('对不起，五次均输入错')
    quit()
# print('你好，',user_name,sep='');print('请选择功能：');print('1.账户管理');print('');input('\n')
while True:
    c = gui.choicebox(msg='你好，' + user_name + '\n请选择功能：', choices=['1.账户管理', '2.文件管理', '3.计算器','4.一键搜歌','5.打开外部组件','6.时间'])
    if c == '1' or '1' in c or '账户管理' in c:
        pwd1 = gui.passwordbox(msg='你好，' + user_name + '请输入你的密码：', title='账户管理')
        if pwd1 == yy:
            fieldValues = []  # we start with blanks for the values
            fieldValues = gui.multenterbox('账户管理', '账户管理', ['账户名称：', '账户密码：'])
            new_user_name = None
            new_user_pwd = None
            if fieldValues[1].isdigit():
                gui.msgbox(msg='密码不能全是数字!', title='账户管理', ok_button='退出')
            if fieldValues[0] == '':
                new_user_name = kk
                new_user_pwd = fieldValues[1]
            if fieldValues[1] == '':
                new_user_pwd = yy
                new_user_name = fieldValues[0]
            if new_user_name is None:
                new_user_name = fieldValues[0]
            if new_user_pwd is None:
                new_user_pwd = fieldValues[1]
            if new_user_name == kk and new_user_pwd == yy:
                gui.msgbox(msg='您没有进行更改！', ok_button='退出', title='账户管理')
            if new_user_name is not None and new_user_pwd is not None:
                with open(r'D:\my_work\Python\sys\user_name.txt', 'w') as yyy:
                    yyy.write(new_user_name)
                with open(r'D:\my_work\Python\sys\pwd.txt', 'w') as yyy1:
                    yyy1.write(new_user_pwd)
                gui.msgbox(msg='完成更改！', title='账户管理', ok_button='退出')
            quit()
    elif c == '2' or '2' in c or '文件管理' in c:
        c1 = gui.choicebox(msg='请选择功能：', choices=['1.txt文件编辑', '2.其他文件管理'])
        if c1 == '1.txt文件编辑':
            file = gui.fileopenbox(default='text.txt')
            c2 = gui.choicebox(msg='请选择功能：', choices=['1.覆写', '2.只读', '3.添加'])
            if c2 == '1.覆写':
                with open(file, 'w') as f:
                    f.write(gui.enterbox(msg='内容', title='覆写'))
            elif c2 == '2.只读':
                with open(file, 'r') as f:
                    gui.msgbox(msg=f.read(), title='文本内容')
            elif c2 == '3.添加':
                with open(file, 'a') as f:
                    f.write(gui.enterbox(msg='内容', title='添加'))
        elif c1 == '2.其他文件管理':
        #     c2 = gui.choicebox(msg='请选择功能：', choices=['1.覆写', '2.只读', '3.添加'])
            gui.msgbox(msg='此功能尚未开发',title='预览版本警告')
    elif c == '3.计算器':
        root = Tk()  # 设置窗口对象
        root.title('计算器')
        root.geometry("440x550")
        root['bg'] = 'yellow2'
        frame = LabelFrame(root, width=350, height=50)
        frame.pack()
        frame.place(x=0, y=0)
        # 显示框
        label = Label(frame, text="", font=('黑体', 20), height=3, width=31, fg='blue', bg='Pink3')
        label.pack()
        global s
        s = ""


        # 键.
        def figure_dot():
            global s
            s = s + "."
            label.config(text=s)


        # 键0
        def figure_0():
            global s
            s = s + "0"
            label.config(text=s)


        # 键1
        def figure_1():
            global s
            s = s + "1"
            label.config(text=s)


        # 键2
        def figure_2():
            global s
            s = s + "2"
            label.config(text=s)


        # 键3
        def figure_3():
            global s
            s = s + "3"
            label.config(text=s)


        # 键4
        def figure_4():
            global s
            s = s + "4"
            label.config(text=s)


        # 键5
        def figure_5():
            global s
            s = s + "5"
            label.config(text=s)


        # 键6
        def figure_6():
            global s
            s = s + "6"
            label.config(text=s)


        # 键7
        def figure_7():
            global s
            s = s + "7"
            label.config(text=s)


        # 键8
        def figure_8():
            global s
            s = s + "8"
            label.config(text=s)


        # 键9
        def figure_9():
            global s
            s = s + "9"
            label.config(text=s)


        # 加法键
        def figure_addition():
            global s
            s = s + "+"
            label.config(text=s)


        # 减法键
        def figure_subtraction():
            global s
            s = s + "-"
            label.config(text=s)


        # 乘法键
        def figure_multiplication():
            global s
            s = s + "*"
            label.config(text=s)


        # 除法键
        def figure_division():
            global s
            s = s + "/"
            label.config(text=s)


        # 清空键
        def figure_clear():
            global s
            s = ""
            label.config(text=s)


        # 百分键（python中%为求余数，此处从百分之几改为乘0.01，数值和百分之几相等）
        def figure_percent():
            global s
            global s
            s = s + "*0.01"
            label.config(text=s)


        # 退格键
        def figure_back():
            global s
            b = list(s)
            b.pop()
            s = ("".join(b))
            label.config(text=s)


        # 等于键
        def figure_vablue():
            global s
            x = eval(s)
            s = str(x)
            label.config(text=s)


        btn0 = Button(root, text=".", font=('黑体', 15), width=6, height=2, command=figure_dot, bg='Skyblue', bd=5)
        btn0.place(x=20, y=440)

        btn0 = Button(root, text="0", font=('黑体', 15), width=6, height=2, command=figure_0, bg='Skyblue', bd=5)
        btn0.place(x=110, y=440)

        btn1 = Button(root, text="1", font=('黑体', 15), width=6, height=2, command=figure_1, bg='Skyblue', bd=5)
        btn1.place(x=20, y=360)

        btn2 = Button(root, text="2", font=('黑体', 15), width=6, height=2, command=figure_2, bg='Skyblue', bd=5)
        btn2.place(x=110, y=360)

        btn3 = Button(root, text="3", font=('黑体', 15), width=6, height=2, command=figure_3, bg='Skyblue', bd=5)
        btn3.place(x=200, y=360)

        btn4 = Button(root, text="4", font=('黑体', 15), width=6, height=2, command=figure_4, bg='Skyblue', bd=5)
        btn4.place(x=20, y=280)

        btn5 = Button(root, text="5", font=('黑体', 15), width=6, height=2, command=figure_5, bg='Skyblue', bd=5)
        btn5.place(x=110, y=280)

        btn6 = Button(root, text="6", font=('黑体', 15), width=6, height=2, command=figure_6, bg='Skyblue', bd=5)
        btn6.place(x=200, y=280)

        btn7 = Button(root, text="7", font=('黑体', 15), width=6, height=2, command=figure_7, bg='Skyblue', bd=5)
        btn7.place(x=20, y=200)

        btn8 = Button(root, text="8", font=('黑体', 15), width=6, height=2, command=figure_8, bg='Skyblue', bd=5)
        btn8.place(x=110, y=200)

        btn9 = Button(root, text="9", font=('黑体', 15), width=6, height=2, command=figure_9, bg='Skyblue', bd=5)
        btn9.place(x=200, y=200)

        btn_add = Button(root, text="+", font=('黑体', 15), width=6, height=2, command=figure_addition, bg='Pink', bd=5)
        btn_add.place(x=290, y=280)

        btn_sub = Button(root, text="-", font=('黑体', 15), width=6, height=2, command=figure_subtraction, bg='Pink', bd=5)
        btn_sub.place(x=290, y=200)

        btn_multi = Button(root, text="×", font=('黑体', 15), width=6, height=2, command=figure_multiplication, bg='Pink',
                        bd=5)
        btn_multi.place(x=200, y=120)

        btn_divi = Button(root, text="÷", font=('黑体', 15), width=6, height=2, command=figure_division, bg='Pink', bd=5)
        btn_divi.place(x=110, y=120)

        btn_clear = Button(root, text="C", font=('黑体', 15), width=6, height=2, command=figure_clear, bg='Pink', bd=5)
        btn_clear.place(x=20, y=120)

        btn_back = Button(root, text="←", font=('黑体', 15), width=6, height=2, command=figure_back, bg='Pink', bd=5)
        btn_back.place(x=290, y=120)

        btn_back = Button(root, text="%", font=('黑体', 15), width=6, height=2, command=figure_percent, bg='Skyblue', bd=5)
        btn_back.place(x=200, y=440)

        btn_vablue = Button(root, text="=", font=('黑体', 15), width=6, height=6, command=figure_vablue, bg='white', bd=5)
        btn_vablue.place(x=290, y=360)
        root.mainloop()
    elif c == '4.一键搜歌':
        cmd.system('py 一键搜歌/一键搜歌GUI.py')
    elif c == '5.打开外部组件':
        # print(get_all_file_in_dir(r'sys\外部组件'))
        temporary_content = gui.choicebox(msg='请选择文件:',choices=get_all_file_in_dir(r'sys\外部组件'))
        # temporary_content = gui.enterbox(msg=r'''组件名称
        # 输入格式：sys\外部组件\名称.py
        # （必须为py文件,且必须放入外部组件文件夹）''',title='外部组件使用')
        temporary_content1 = 'py'+' '+temporary_content
        cmd.system(temporary_content1)
    elif c == '6.时间':
        cc = gui.choicebox(msg='选择功能:',title=date.today(),choices=['日历','时钟'])
        if cc == '时钟':
            if __name__ == "__main__":
                main()
        if cc == '日历':
                    # 平瑞年
            def leap_year(year):
                if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                    return True
                else:
                    return False


            # 月份的天数
            def getMonthDays(year, month):
                days = 31
                if month == 2:  # 确定2月天数
                    if leap_year(year):
                        days = 29
                    else:
                        days = 28
                elif month == 4 or month == 6 or month == 9 or month == 11:  # 4 6 9 11这些月份均为30天
                    days = 30
                return days


            # 星期
            def getTotalDays(year, month):
                totalDays = 0
                for i in range(1, year):  # 计算从第一年到查询年份的前一年的总天数
                    if leap_year(i):
                        totalDays += 366
                    else:
                        totalDays += 365
                for i in range(1, month):  # 再计算查询年份从一月到查询月份的前一个月的天数相加，得到总天数
                    totalDays += getMonthDays(year, i)
                return totalDays


            # 生成万年历
            def f():
                year = t1.get()  # 获取输入框的内容：年份
                month = t2.get()  # 获取输入框的内容：月份
                year = int(year)  # input接受的数据默认为字符串，需要转换为int型
                month = int(month)
                count = 0  # 计数，每7个一换行
                day = []  # 存储万年历的列表
                day.append("日\t一\t二\t三\t四\t五\t六\n")
                for i in range((getTotalDays(year, month) % 7) + 1):  # 前面的空出来
                    day.append('\t')  # end：可使print输出后不自动换行，接着输出数字
                    count += 1
                    if count == 7:  # 统一格式
                        day.append('\n')
                for i in range(1, getMonthDays(year, month) + 1):  # 输出日期
                    day.append(str(i))
                    count += 1
                    if count % 7 == 0:  # 每7个一换行,不换行则需要\t
                        day.append('\n')
                    else:
                        day.append('\t')
                if count % 7 != 0:  # 如果最后一天不为周六，则将空日期填满（原因：lable默认居中显示）
                    for i in range(7 - count % 7 - 1):
                        day.append('\t')
                    day.append('     ')
                w.config(text="".join(day))  # 更改lable显示内容


            # 创建窗口，从窗口键入年份月份，生成万年历

            window = Tk()  # 创建窗口对象
            window.title('万年历')  # 标题
            window.minsize(600, 350)  # 窗口大小，设置最大最小值相同，大小可固定
            window.maxsize(600, 350)

            # 标签、输入框、按钮

            show = Label(text='', anchor='se', font=('黑体', 30), fg='black')  # 显示框

            l1 = Label(window, text="请输入年份：")  # 年份
            l1.pack()

            t1 = StringVar()
            t1.set('')
            entry_year = Entry(window, textvariable=t1).pack()

            l2 = Label(window, text="请输入月份：")  # 月份
            l2.pack()

            t2 = StringVar()
            t2.set('')
            entry_mon = Entry(window, textvariable=t2).pack()

            b = Button(text='查看万年历', command=f)
            b.pack()

            # 万年历结果显示在lable中

            w = Label(window, text="")
            w.pack()

            # 显示窗口

            window.mainloop()