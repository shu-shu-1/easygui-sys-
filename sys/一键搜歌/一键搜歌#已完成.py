# import os
import webbrowser
a = input("请输入歌名：")
b = 'https://tonzhon.com/search?keyword=' + a
webbrowser.open(b, new=0, autoraise=True) 
# os.system("C:/Program Files/Internet Explorer/iexplore.exe" b)