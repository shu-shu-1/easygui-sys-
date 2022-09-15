    # print("请输入计算符号序号：")
    # print("1.+")
    # print("2.-")
    # print("3.×")
    # print("4.÷")
import time
while True:
    print("""请输入计算符号序号：
    1.+
    2.-
    3.×
    4.÷
    5.带余数÷
    6.面积计算
    7.退出""")
    jisuanmoshi = input()
    jisuanshuru1 = None
    jisuanshuru2 = None
    jisuanshuchu1 = None
    jisuanshuchu2 = None
    jisuanjieguo = None
    yushujisuanjieguo2 = None
    yushujisuanjieguo1 = None
    if jisuanmoshi == "1":
        jisuanshuchu1 = '>加数1：'
        jisuanshuchu2 = '>加数2：'
        jisuanshuru1 = int(input(jisuanshuchu1))
        jisuanshuru2 = int(input(jisuanshuchu2))
    elif jisuanmoshi == "2":
        jisuanshuchu1 = '>被减数：'
        jisuanshuchu2 = '>减数：'
        jisuanshuru1 = int(input(jisuanshuchu1))
        jisuanshuru2 = int(input(jisuanshuchu2))
    elif jisuanmoshi == "3":
        jisuanshuchu1 = '>乘数1：'
        jisuanshuchu2 = '>乘数2：'
        jisuanshuru1 = int(input(jisuanshuchu1))
        jisuanshuru2 = int(input(jisuanshuchu2))
    elif jisuanmoshi in ["4", "5"]:
        jisuanshuchu1 = '>被除数：'
        jisuanshuchu2 = '>除数：'
        jisuanshuru1 = int(input(jisuanshuchu1))
        jisuanshuru2 = int(input(jisuanshuchu2))
    if jisuanmoshi == "1":
        jisuanjieguo = jisuanshuru1 + jisuanshuru2
        print('结果是',jisuanjieguo)
    elif jisuanmoshi == "2":
            jisuanjieguo = jisuanshuru1 - jisuanshuru2
            print('结果是',jisuanjieguo)
    elif jisuanmoshi == "3":
            jisuanjieguo = jisuanshuru1 * jisuanshuru2
            print('结果是',jisuanjieguo)
    elif jisuanmoshi == "4":
            jisuanjieguo = jisuanshuru1 / jisuanshuru2
            print('结果是',jisuanjieguo)
    elif jisuanmoshi == "5":
        yushujisuanjieguo1 = jisuanshuru1 % jisuanshuru2
        int(yushujisuanjieguo1)
        yushujisuanjieguo2 = jisuanshuru1 - yushujisuanjieguo1
        int(yushujisuanjieguo2)
        jisuanjieguo = f"{str(yushujisuanjieguo2 // jisuanshuru2)}……{str(yushujisuanjieguo1)}"

        print('结果是',jisuanjieguo)
    elif jisuanmoshi == '6':
        print('''计算图形：
        1，平行四边形
        2，正方形
        3，三角形
        4，梯形''')
        a = int(input('>序号：'))
        if a == 1:
            di = int(input('>底：'))
            gao = int(input('>高：'))
            jisuan_out = di * gao
            leibie_out = '平行四边形'
            gongshi_out = '底×高'
            jisuan_gongshi_out = f'{di}×{gao}'
        elif a == 2:
            bian_chang = int(input('>边长：'))
            jisuan_out = bian_chang**2
            leibie_out = '正方形'
            gongshi_out = '边长×边长'
            jisuan_gongshi_out = f'{bian_chang}×{bian_chang}'
        elif a == 3:
            di = int(input('>底：'))
            gao = int(input('>高：'))
            jisuan_out = di * gao
            jisuan_out = jisuan_out / 2
            leibie_out = '三角形'
            gongshi_out = '底×高÷2'
            jisuan_gongshi_out = f'{di}×{gao}÷2'
        elif a == 4:
            shang_di = int(input('>上底：'))
            xia_di = int(input('>下底：'))
            gao = int(input('>高：'))
            jisuan_out = shang_di + xia_di
            jisuan_out = jisuan_out * gao
            jisuan_out = jisuan_out / 2
            leibie_out = '梯形'
            gongshi_out = '(上底+下底)×高÷2'
            jisuan_gongshi_out = f'({shang_di}+{xia_di})×{gao}÷2'
        print(leibie_out,'的面积是',jisuan_out,'(',leibie_out,'的面积计算公式是',gongshi_out,'，所以这个图形是这样计算的：',jisuan_gongshi_out,')')
    elif jisuanmoshi == '7':
            print('欢迎下次使用')
            time.sleep(3)
            exit("已退出")