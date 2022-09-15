import sys
from easygui import *
import os
os.chdir(sys.path[0])
print("================================")
print("\t 请保留命令行！")
print("================================")
msgbox("请保留命令行！",ok_button="我已知晓")
def run(参数):
    if 参数 == 1:
        os.system("py 程序组\计算器GUI.py")
    elif 参数 == 2:
        os.system("py 命令行\计算器#已完成.py")
    elif 参数 == 3:
        os.system("py 命令行\高级.py")
    elif 参数 == 0:
        os.system("py 程序组\计算器（新）.py")
    elif 参数 == 4:
        os.system("py 命令行\步骤科学计算器.py")
    elif 参数 == 5:
        os.system('py ./程序组/高级计算器.py')
    elif 参数 == 6:
        os.system('py 程序组\计算器经典-纯白.py')
    elif 参数 == 7:
        os.system('py 程序组\calculator.py')
choices = choicebox(msg='选择类别',title='选择',choices=['命令行', '图形化'])
if choices == '命令行':
    answer = choicebox(msg='选择计算器',title='选择',choices=['步骤科学计算器','高级计算器','计算器#已完成'])
    if answer == '步骤科学计算器':
        run(4)
    elif answer == '高级计算器':
        run(3)
    elif answer == '计算器#已完成':
        run(2)
elif choices == '图形化':
    answer = choicebox(msg='选择计算器',title='选择',choices=['高级计算器(普通)','高级计算器(专业)','计算器(现代)','计算器经典(纯白)','计算器经典'])
    if answer == '高级计算器(普通)':
        run(5)
    elif answer == '高级计算器(专业)':
        run(7)
    elif answer == '计算器(现代)':
        run(0)
    elif answer == '计算器经典(纯白)':
        run(6)
    elif answer == '计算器经典':
        run(1)