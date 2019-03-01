'''
合并两个列表并去重
题目内容：

输入两个列表alist和blist，要求列表中的每个元素都为正整数且不超过10；

合并alist和blist，并将重复的元素去掉后输出一个新的列表clist。

可以使用以下实现列表alist的输入：

alist=list(map(int,input().split()))

同时为保证输出结果一致，请将集合内元素排序之后再输出。

如对于列表alist，可输出sorted(alist)。

输入格式:

共两行，每一行都用来输入列表中的元素值，以空格隔开。

输出格式：

共一行，以列表形式打印输出。
'''
alist=list(map(int,input("请输入列表a的元素：").split()))
blist=list(map(int,input("请输入列表b的元素：").split()))
clist=set(alist+blist)
print('合并去重后列表为：',sorted(clist))