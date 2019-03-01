'''
列表反转
题目内容：

输入一个列表，将其反转后输出新的列表。

可以使用以下实现列表alist的输入：

alist=list(map(int,input().split()))

输入格式:

共一行，列表中的元素值，以空格隔开。

输出格式：

共一行，为一个列表。

'''
alist=list(map(int,input("请输入列表中的元素，以空格隔开：").split()))
alist.reverse()
print(alist)
