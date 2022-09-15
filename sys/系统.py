import sys
import easygui as gui
from tkinter import *
import os as cmd
from turtle import *
from datetime import *
from requests import *
from json import *
cmd.chdir(sys.path[0])
def 一言(t:str):
    global i,response,r1,hitokoto,from1,from_who
    # t: m:默认 a:动画 b:漫画 c:游戏 d:文学 e:原创 f:来自网络 g:其他 h:影视 i:诗词 j:网易云 k:哲学 l:抖机灵
    i = {'m': 'https://v1.hitokoto.cn/', 'a': 'http://v1.hitokoto.cn/?c=a', 'b': 'http://v1.hitokoto.cn/?c=b',
         'c': 'http://v1.hitokoto.cn/?c=c', 'd': 'http://v1.hitokoto.cn/?c=d', 'e': 'http://v1.hitokoto.cn/?c=e',
         'f': 'http://v1.hitokoto.cn/?c=f', 'g': 'http://v1.hitokoto.cn/?c=g', 'h': 'http://v1.hitokoto.cn/?c=h',
         'i': 'http://v1.hitokoto.cn/?c=i', 'j': 'http://v1.hitokoto.cn/?c=j', 'k': 'http://v1.hitokoto.cn/?c=k',
         'l': 'http://v1.hitokoto.cn/?c=l'}
    if t not in ['m', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']:
        return "错误"
    else:
        response = get(i[t])
        r1 = response.text
        r1 = loads(r1)
        hitokoto = r1['hitokoto']
        from1 = r1['from']
        from_who = r1['from_who']
        if from_who == 'null':
            from_who=None
        return [hitokoto,from1,from_who]

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
    if new_user1[0].isspace():
        gui.msgbox(msg='账号名不能全是空格！', title='账户注册-错误', ok_button='退出')
        quit()
    if new_user1[1].isdigit():
        gui.msgbox(msg='密码不能全是数字！', title='账户注册-错误', ok_button='退出')
        quit()
    if new_user1[1].isspace():
        gui.msgbox(msg='密码不能全是空格！', title='账户注册-错误', ok_button='退出')
        quit()   
    with open(r'user_name.txt', 'r+') as y:
        y.write(new_user1[0])
    with open(r'pwd.txt', 'r+') as y1:
        y1.write(new_user1[1])
    gui.msgbox(msg='设置完毕，请重启')
    quit()

i = 0  # 统计循环执行的次数
while i < 5:  # 0,1,2 ,当i=3时 3<3False，循环执行结束
    user_input = str.split(gui.enterbox(msg='请输入您的用户名+密码（使用空格分隔）：', title='登录'), ' ')
    user_name = user_input[0]
    pwd = user_input[1]
    # 判断
    with open(r'pwd.txt', 'r') as y2:
        yy = y2.read()
    if user_name == kk and pwd == yy:
        gui.msgbox(msg='系统正在登录，请稍后', title='登录', ok_button='确定')
        # 改变循环条件，退出循环
        i = 8  # 判断8<3 False,循环执行结束
    else:
        gui.msgbox(msg=f'用户名或密码不正确，您还有{str(4 - i)}次机会', title='登录', ok_button='确定')
        i += 1  # 改变循环变量

if i == 5:  # 当用户或密码输入不正确的时候，循环执行结束时，i的最大值为3
    gui.msgbox(msg='对不起，五次均输入错', title='登录', ok_button='确定')
    # print('对不起，五次均输入错')
    quit()
# print('你好，',user_name,sep='');print('请选择功能：');print('1.账户管理');print('');input('\n')
while True:
    yiyan=一言(t='i')
    if yiyan[2] is None:
        yiyan1 = f"{yiyan[0]}——「{yiyan[1]}」"
    else:
        yiyan1 = f"{yiyan[0]}——「{yiyan[1]}」{yiyan[2]}"
    c = gui.choicebox(msg='你好，' + user_name + '\n请选择功能：', choices=['1.账户管理', '2.文件管理', '3.计算器','4.一键搜歌','5.打开外部组件','6.时间','7.查看一言'],title=yiyan1)
    if c == '1' or '1' in c or '账户管理' in c:
        pwd1 = gui.passwordbox(msg='你好，' + user_name + '请输入你的密码：', title='账户管理')
        if pwd1 == yy:
            fieldValues = []  # we start with blanks for the values
            fieldValues = gui.multenterbox('账户管理', '账户管理', ['账户名称：', '账户密码：'])
            new_user_name = None
            new_user_pwd = None
            if fieldValues[1].isdigit():
                gui.msgbox(msg='密码不能全是数字!', title='账户管理', ok_button='退出')
            if fieldValues[1].isspace():
                gui.msgbox(msg='密码不能全是空格！', title='账户管理', ok_button='退出')
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
                with open(r'user_name.txt', 'w') as yyy:
                    yyy.write(new_user_name)
                with open(r'pwd.txt', 'w') as yyy1:
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
        cmd.system('py 计算器\启动.py')
    elif c == '4.一键搜歌':
        cmd.system('py 一键搜歌/一键搜歌GUI.py')
    elif c == '5.打开外部组件':
        # print(get_all_file_in_dir(r'sys\外部组件'))
        temporary_content = gui.choicebox(msg='请选择文件:',choices=get_all_file_in_dir(r'外部组件'))
        # temporary_content = gui.enterbox(msg=r'''组件名称
        # 输入格式：sys\外部组件\名称.py
        # （必须为py文件,且必须放入外部组件文件夹）''',title='外部组件使用')
        temporary_content1 = 'py'+' '+temporary_content
        cmd.system(temporary_content1)
    elif c == '6.时间':
        cc = gui.choicebox(msg='选择功能:',title=date.today(),choices=['日历','时钟','系统(beta)'])
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
        elif cc == '系统(beta)':
            cmd.system('py 日历.py')
    elif c == '7.查看一言':
        gui.msgbox(msg=yiyan1,ok_button='确定')