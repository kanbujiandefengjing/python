'''
列表元素改写（10分）
题目内容：

输入一个列表alist，要求列表中的每个元素都为正整数且不超过10；

将列表中的奇数变为它的平方，偶数除以2后打印新的列表（新的列表中所有元素仍都为整数）。

可以使用以下实现列表alist的输入：

alist=list(map(int,input().split()))
同时为保证输出结果一致，请将集合内元素排序之后再输出。

如对于列表alist，可输出sorted(alist)。

输入格式:

共一行，用来输入列表的元素值，以空格隔开。

输出格式：

共一行，以列表形式打印输出。

'''
alist=list(map(int,input("请输入列表的元素值，以空格隔开：").split()))

for i in range(len(alist)):
    if alist[i]%2==0:
        alist[i]//=2
    else:
       alist[i]**=2
print(sorted(alist))