'''
打印一定范围内的素数（10分）
题目内容：

给定一个大于2的正整数n，打印出小于n（不包括n且n不大于100）的所有素数。

要求将符合条件的输出填入一个列表中，打印的结果为该列表。

输入格式:

共一行，为一个大于2的正整数

输出格式：

共一行，为一个列表
'''
n=int(input("请输入一个大于2的整数："))
p=[2]
for i in range(3,n):
    for j in range(2,int(i**0.5)+1):
        if i%j == 0:
            break
    else:
        p.append(i)
print(p)