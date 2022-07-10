# print("被除数：")
# a = int(input())
# print("除数：")
# b = int(input())
# print(a,"÷",b,"=",a // b,"……",a % b)
import easygui
import pyperclip
a = easygui.enterbox("被除数：", "带余数的除法")
if a=='' or a==None:
    easygui.msgbox(msg='被除数不能为0或空！',title='带余数的除法-警告',ok_button='退出',image='E:\PPTOS工程文件\图标\ICO\Warning.ico')
    quit()
a = int(a)
b = easygui.enterbox("除数：", "带余数的除法")
if b == '0' or b=='' or a==None:
    easygui.msgbox(msg='除数不能为0或空！',title='带余数的除法-警告',ok_button='退出',image='E:\PPTOS工程文件\图标\ICO\Warning.ico')
    quit()
b = int(b)

if a % b == 0:
    c = easygui.ccbox(msg='没有余数！',title='带余数的除法-提示',choices=('继续','退出'),image='E:\PPTOS工程文件\图标\ICO\Info.ico')
    if c == True:
        d = a//b
    else:
        quit()
else:
    d = str(a) + "÷" + str(b) + "=" + str(a // b) + "……" + str(a % b)
e = easygui.ccbox(msg=d,title='带余数的除法-结果',choices=('完成并复制','完成并退出'))
if e == True:
    pyperclip.copy(d)
else:
    quit()


