'''
与7相关的数：如果一个正整数，它能被7整除或者它的十进制表示法中某个位数上的数字为7，则称之为与7相关的数。（10分）
题目内容：

现在我们给定一个正整数n（n<1000），求所有小于等于n的与7无关的正整数的平方和。

输入格式:

共一行，为一个正整数。

输出格式：

共一行，为一个正整数。
'''
n=int(input("请输入一个正整数："))
s=0
for i in range(1,n+1):
    if i%7==0 or '7' in str(i):
        continue
    else:
        s=s+i*i
print(s)