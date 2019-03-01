'''
求两个数的最大公约数。（10分）
题目内容：

输入两个正整数num1和num2（不超过1000），求它们的最大公约数并输出。

我们定义求最大公约数的函数为hcf，给出程序主体如下：
num1=int(input(""))
num2=int(input(""))
print(hcf(num1,num2))
请补充完成hcf函数的定义。

输入格式:

共两行，每一行输入一个不超过1000的正整数。

输出格式：

共一行，输出一个正整数。
'''
num1=int(input("请输入一个正整数："))
num2=int(input("请输入一个正整数："))
def hcf(num1,mum2):
    if num1>num2:
        smaller=num2
    else:
        smaller=num1
    for i in range(1,smaller+1):
        if num1%i==0 and num2%i==0:
            hcf =i
    return hcf
print(hcf(num1,num2))