'''
求阶乘。（10分）
题目内容：

我们定义求n（n为正整数且n<=20）的阶乘的函数为fact，给出程序主体如下：

n=int(input(""))
print(fact(n))
请补充完成对fact函数的定义。

输入格式:

共一行，为一个小于20的正整数。

输出格式：

共一行，为一个正整数。
'''
n=int(input("请输入一个小于20的正整数："))
def fact(n):
    s=1
    for i in range(1,n+1):
        s*=i
    return s
print(fact(n))