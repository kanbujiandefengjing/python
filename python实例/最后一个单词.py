'''
最后一个单词
题目内容：

计算字符串最后一个单词的长度，单词以空格隔开。

可以使用以下语句实现字符串s的输入：

s=str(input())

输入格式:

一行字符串，非空，长度小于5000。

输出格式：

整数N，最后一个单词的长度。

'''
s=str(input('请输入一行字符串，单词以空格间隔：'))
for i in range(len(s)):
    if s[len(s)-1-i]==' ':
        count=i
        break
    else:
        count=i+1
print('最后一个单词的长度：{}'.format(count))