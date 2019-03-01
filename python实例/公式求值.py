'''
公式求值（10分）
题目内容：

sin15°+(e^x-5x)/(√(x^2+1)-ln(3x)

接受一个正整数输入x，打印上述公式的输出值。

输入格式:

共一行，为一个正整数。

输出格式：

共一行，采用round函数保留10位小数。
'''
import math
x=int(input("请输入正整数x:"))
y=math.sin(math.pi/12)+(math.exp(x)-5*x)/(math.sqrt(x**2+1))-math.log(3*x,math.e)
print(round(y,10))