'''
求两个数的最小公倍数。（10分）
题目内容：

输入两个正整数num1和num2（不超过500），求它们的最小公倍数并输出。

我们定义求最小公倍数的函数为lcm，给出程序主体如下：
num1=int(input(""))
num2=int(input(""))
print(lcm(num1,num2))
请补充完成hcf函数的定义。

输入格式:

共两行，每一行输入一个不超过500的正整数。

输出格式：

共一行，输出一个正整数。
'''
num1=int(input("请输入一个正整数："))
num2=int(input("请输入一个正整数："))
def lcm(n1,n2):
    for i in range(max(n1,n2),n1*n2+1,1):
        if i%n1==i%n2==0:
            return i
print(lcm(num1,num2))