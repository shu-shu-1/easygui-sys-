import sympy

while(1):
    while(1):
        print("--------------------")
        total = 0.0
        num1 = input ("输入第一个数字:")
        if("." in num1):
            pass
        elif(num1.isalnum() == False):
            print("无效的输入,请重新输入。")
            break
        opeSym = input ("输入操作（阶乘factorial）:")
        if(opeSym != "+" and opeSym != "-" and opeSym != "*" and opeSym != "/" and opeSym != "**" and opeSym != "//" and opeSym != "sqrt" and opeSym != "log" and opeSym != "factorial"):
            print("无效的输入,请重新输入。")
            break
        num2 = input ("输入第二个数:")
        if("." in num2):
            pass
        if(opeSym == "factorial"):
            pass
        elif(num2.isalnum() == False):
            print("无效的输入,请重新输入。")
            break
 
        if(opeSym == "+"):
            print(float(num1) + float(num2))
 
        elif(opeSym == "-"):
            print(float(num1) - float(num2))
 
        elif(opeSym == "*"):
            print(float(num1) * float(num2))
 
        elif(opeSym == "/"):
            print(float(num1)/float(num2))
 
        elif(opeSym == "**"):
            print(float(num1)**float(num2))
 
        elif(opeSym == "//"):
            print(float(num1)//float(num2))
 
        elif(opeSym == "sqrt"):
            print(sympy.root(float(num1),float(num2)))
 
        elif(opeSym == "log"):
            print(sympy.log(float(num1),float(num2)))
 
        elif(opeSym == "factorial"):
            print(sympy.factorial(float(num1)))
      
