import re
from math import *


# 将算式从字符串处理成列表，解决横杠是负号还是减号的问题
def formula_format(formula):
    """
    :param formula: str
    """
    formula = re.sub(' ', '', formula)  # 去掉算式中的空格s
    # 以 '横杠数字' 分割， 其中正则表达式：(\-\d+\.?\d*) 括号内：
    # \- 表示匹配横杠开头；\d+ 表示匹配数字1次或多次；\.?表示匹配小数点0次或1次;\d*表示匹配数字0次或多次。
    formula_list = [i for i in re.split('(-[\d+,π,e]\.?\d*)', formula) if i]
    final_formula = []  # 最终的算式列表
    for item in formula_list:
        # 算式以横杠开头，则第一个数字为负数，横杠为负号
        if len(final_formula) == 0 and re.match('-[\d+,π,e]\.?\d*$', item):
            final_formula.append(item)
            continue
        # 如果当前的算式列表最后一个元素是运算符['+', '-', '*', '/', '('， '%'， '^'], 则横杠为减号
        if len(final_formula) > 0:
            if re.match('[\+\-\*\/\(\%\^]$', final_formula[-1]):
                final_formula.append(item)
                continue
        # 按照运算符分割开
        item_split = [i for i in re.split('([\+\-\*\/\(\)\%\^\√])', item) if i]
        final_formula += item_split
    return final_formula


# 判断是否是运算符，如果是返回True
def is_operator(e):
    """
    :param e: str
    :return: bool
    """
    opers = ['+', '-', '*', '/', '(', ')', '%', '^', '√', 'sin', 'arcsin', 'ln']
    return True if e in opers else False  # 在for循环中嵌套使用if和else语句


# 比较连续两个运算符来判断是压栈还是弹栈
def decision(tail_op, now_op):
    """
    :param tail_op: 运算符栈的最后一个运算符
    :param now_op: 从算式列表取出的当前运算符
    :return: 1代表弹栈运算，0代表弹出运算符栈最后一个元素'('，-1表示压栈
    """
    # 定义4种运算符级别
    rate1 = ['+', '-']
    rate2 = ['*', '/', '%']
    rate3 = ['^', '√', 'sin', 'arcsin', 'ln']
    rate4 = ['(']
    rate5 = [')']

    if tail_op in rate1:
        if now_op in rate2 or now_op in rate3 or now_op in rate4:
            return -1  # 说明当前运算符优先级高于运算符栈的最后一个运算符，需要压栈
        else:
            return 1  # 说明当前运算符优先级等于运算符栈的最后一个运算符，需要弹栈运算

    elif tail_op in rate2:
        if now_op in rate3 or now_op in rate4:
            return -1
        else:
            return 1

    elif tail_op in rate3:
        if now_op in rate4:
            return -1
        else:
            return 1

    elif tail_op in rate4:
        if now_op in rate5:
            return 0  # '('遇上')',需要弹出'('并丢掉')',表明该括号内的算式已计算完成并将结果压入数字栈中
        else:
            return -1  # 只要栈顶元素为'('且当前元素不是')'，都应压入栈中


# 传入两个数字，一个运算符，根据运算符不同返回相应结果
def calculate(n1, n2, operator):
    """
    :param n1: float
    :param n2: float
    :param operator: + - * / % ^
    :return: float
    """
    result = 0
    if operator == '+':
        result = n1 + n2
    if operator == '-':
        result = n1 - n2
    if operator == '*':
        result = n1 * n2
    if operator == '/':
        result = n1 / n2
    if operator == '%':
        result = n1 % n2
    if operator == '^':
        result = n1 ** n2
    return result


# 括号内的算式求出计算结果后，计算√()、sin()或arcsin()
def gaojie(op_stack, num_stack):
    if op_stack[-1] == '√':
        op = op_stack.pop()
        num2 = num_stack.pop()
        num_stack.append(sqrt(num2))
    elif op_stack[-1] == 'sin':
        op = op_stack.pop()
        num2 = num_stack.pop()
        num_stack.append(sin(num2))
    elif op_stack[-1] == 'arcsin':
        op = op_stack.pop()
        num2 = num_stack.pop()
        num_stack.append(asin(num2))
    elif op_stack[-1] == 'ln':
        op = op_stack.pop()
        num2 = num_stack.pop()
        num_stack.append(log(num2))


# 负责遍历算式列表中的字符，决定压入数字栈中或压入运算符栈中或弹栈运算
def final_calc(formula_list):
    """
    :param formula_list: 算式列表
    :return: 计算结果
    """
    num_stack = []  # 数字栈
    op_stack = []  # 运算符栈
    for item in formula_list:
        operator = is_operator(item)
        # 压入数字栈
        if not operator:
            # π和e转换成可用于计算的值
            if item == 'π':
                num_stack.append(pi)
            elif item == '-π':
                num_stack.append(-pi)
            elif item == 'e':
                num_stack.append(e)
            elif item == '-e':
                num_stack.append(-e)
            else:
                num_stack.append(float(item))  # 字符串转换为浮点数
        # 如果是运算符
        else:
            while True:
                # 如果运算符栈为空，则无条件入栈
                if len(op_stack) == 0:
                    op_stack.append(item)
                    break
                # 决定压栈或弹栈
                tag = decision(op_stack[-1], item)
                # 如果是-1，则压入运算符栈并进入下一次循环
                if tag == -1:
                    op_stack.append(item)
                    break
                # 如果是0，则弹出运算符栈内最后一个'('并丢掉当前')'，进入下一次循环
                elif tag == 0:
                    op_stack.pop()
                    gaojie(op_stack, num_stack)  # '('前是'√'、'sin'或'arcsin'时，对括号内算式的计算结果作相应的运算
                    break
                # 如果是1，则弹出运算符栈内最后一个元素和数字栈内最后两个元素
                elif tag == 1:
                    if item in ['√', 'sin', 'arcsin']:
                        op_stack.append(item)
                        break
                    op = op_stack.pop()
                    num2 = num_stack.pop()
                    num1 = num_stack.pop()
                    # 将计算结果压入数字栈并接着循环，直到遇到break跳出循环
                    num_stack.append(calculate(num1, num2, op))
    # 大循环结束后，数字栈和运算符栈中可能还有元素的情况
    while len(op_stack) != 0:
        op = op_stack.pop()
        num2 = num_stack.pop()
        num1 = num_stack.pop()
        num_stack.append(calculate(num1, num2, op))
    result = str(num_stack[0])
    # 去掉无效的0和小数点，例：1.0转换为1
    if result[len(result) - 1] == '0' and result[len(result) - 2] == '.':
        result = result[0:-2]
    return result


if __name__ == '__main__':
    # formula = "2 * ( 3 - 5 * ( - 6 + 3 * 2 / 2 ) )"
    formula = "arcsin ( 0 )"
    formula_list = formula_format(formula)
    result = final_calc(formula_list)
    print("算式：", formula)
    print("计算结果：", result)

