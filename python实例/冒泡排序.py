'''
冒泡排序。（10分）
题目内容：

冒泡排序是一种简单的排序算法。它重复地遍历要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。遍历数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。这个算法的名字由来是因为越小的元素会经由交换慢慢“浮”到数列的顶端。

已知输入为一个列表，列表中的元素都为整数，我们定义冒泡排序函数为bubbleSort，将列表中的元素按从小到大进行排序后得到一个新的列表并输出，给出程序主体如下：

alist=list(map(int,input().split()))
print(bubbleSort(alist))
请补充完成对bubbleSort函数的定义。

输入格式:

共一行，列表中的元素值，以空格隔开。

输出格式：

共一行，为一个列表。
'''
alist=list(map(int,input("请输入列表中的元素值，以空格隔开:").split()))
def bubbleSort(n):
    for i in range(len(n)):
        for j in range(len(n)-i-1):
            if n[j]>n[j+1]:
                n[j],n[j+1]=n[j+1],n[j]
    return n
print(bubbleSort(alist))