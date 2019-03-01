'''
斜边上的高
输入直角三角形两直角边a,b的值，输出斜边上的高

输入格式:
2行，每行一个整数，分别为a，b的值

输出格式：
一个数，即斜边上的高，保留2位小数
'''

import math
a=int(input('请输入一条直角边长:'))
b=int(input('请输入另一条直角边长：'))
c=math.sqrt(a*a+b*b)
h=a*b/c
h=round(h,2)
print('三角形的斜边高为: {}'.format(h))

