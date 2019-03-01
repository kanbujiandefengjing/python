'''
from bs4 import BeautifulSoup
soup = BeautifulSoup('<p>data</p>','html.parser')
soup = BeautifulSoup("<html>data</html>","html.parser")
soup = BeautifulSoup(open("D://demo.html"),"html.parser")
<p class="title">...</p>
BeautifulSoup对应一个HTML/XML文档的全部内容

BeautifulSoup类的基本元素
Tag          标签 以<>和</>标明开头和结尾  例：soup.a
Name         标签的名字，<p>...</P>的名字是'p',格式：<tag>.name
Attributes   标签的属性，字典形式组织，格式：<tag>.attrs
NavigableString  标签内非属性字符串，<>...</>中字符串，格式：<tag>.string
Comment      标签内字符串的注释部分，一种特殊的Comment类型

'''

'''
标签树的下行遍历
soup.body.contents   子节点的列表 将<tag>所有儿子节点存入列表
soup.body.children   子节点的迭代类型，与上类似，用于循环遍历儿子节点
soup.body.descendants子孙节点的迭代类型，包含所有子孙节点，用于循环遍历
'''
'''
标签树的上行遍历
.parent  节点的父亲标签
.parents 节点先辈标签的迭代类型，用于循环遍历先辈节点
'''

'''
标签树的平行遍历
.next_sibling    返回按照HTML文本顺序的下一个平行节点标签
.previous_sibling  返回按照HTML文本顺序的上一个平行节点标签
.next_siblings    迭代类型，返回按照HTML文本顺序的后续所有平行节点标签
.previous_siblings迭代类型，返回按照HTML文本顺序的前序所有平行节点标签

注意：平行遍历发生在同一父亲节点的各节点间

'''
import requests
from bs4 import BeautifulSoup
r = requests.get("https://python123.io/ws/demo.html")
demo=r.text
soup =BeautifulSoup(demo,"html.parser")
print(soup.head)
print(soup.a)
print(soup.body.contents)
print(soup.a.next_siblings)
print(soup.prettify())  #增加标签和内容换行符
print(soup.a.prettify()) #对标签处理


