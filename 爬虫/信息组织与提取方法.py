#信息组织与提取方法
'''
信息的标记
标记后的信息可形成信息组织结构，增加了信息维度
标记后的信息可用于通信、存储或展示
标记的结构与信息一样具有重要价值
标记后的信息更利于程序理解和运用

HTML的信息标记
通过预定义的<>...</>标签形式组织不同类型的信息

三种信息标记的形式
 XML,JSON,YAML

XML eXtensible Markup Language

                标签Tag
<img src="china.jpg" size="10">...</img>
名字Name     属性 Attribute        名称Name

JSON  JavsScript Obeject Notation
 有类型的键值对 key:value
       "name":"北京理工大学"
多个值方括号 "key":["value1","value2"]  
键值对嵌套用 {,} "name":{
                       "newName":"北京理工大学",
                       "oldName":"延安自然科学院"
                       }
YAML YAML Ain't Markup Language
 无类型键值对 key:value
        name:北京理工大学
        -表达并列关系
        name:
        -北京理工大学
        -延安自然科学院
        |表达整块数据 #表示注释
        嵌套
        name:
            newName:北京理工大学

三种信息标记形式比较
XML 最早的通用信息标记语言，可扩展性好，但繁琐
    Internet上的信息交互与传递
JSON 信息有类型，适合程序处理(js),较XML简洁
     移动应用云端和节点的信息通信，无注释
YAML 信息无类型，文本信息比例最高，可读性好
     各类系统配置文件，有注释易读
     
'''

'''
信息提取的一般方法

方法一：完整解析信息的标记形式，再提取关键信息
XML JSON YAML
需要标记解析器  例如：bs4库的标签树遍历
优点：信息解析准确
缺点：提取过程繁琐，速度慢

方法二：无视标记形式，直接搜索关键信息
搜索
对信息文本查找函数即可
优点：提取过程简洁，速度较快
缺点：提取结果准确性与信息内容相关

融合方法
融合方法；结合形式解析与搜索方法，提取关键信息。

XML JSON YAML 搜索
需要标记解析器及文本查找函数

示例
提取HTML中所有URL链接
思路：1）搜索到所有<a>标签
      2）解析<a>标签格式，提取href后的链接内容

'''
import requests
from bs4 import BeautifulSoup
r=requests.get("https://python123.io/ws/demo.html")
r.raise_for_status
demo=r.text
soup=BeautifulSoup(demo,"html.parser")
for link in soup.find_all('a'):
    print(link.get('href'))
'''
结果：
http://www.icourse163.org/course/BIT-268001
http://www.icourse163.org/course/BIT-1001870001
'''
'''
基于bs4库的内容查找方法
<>.find_all(name,attrs,recursive,string,**kwargs)
返回一个列表类型，存储查找的结果
name:对标签名称的检索字符串
#接上方import requests代码

import re
for tag in soup.find_all():
    print(tag.name)
结果:
html
head
title
body
p
b
p
a
a

for tag in soup.find_all(re.compile('b')):
    print(tag.name)
结果：
body
b

attrs:对标签属性值的检索字符串，可标注属性检索
soup.find_all('p','course')
结果：
[<p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:
<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a> and <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>.</p>]

soup.find_all(id='link1')
结果：
[<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a>]
soup.find_all(id='link')
结果：
[]
import re
soup.find_all(id=re.compile('link'))
结果：
[<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a>, <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>]

recursive:是否对子孙全部检索，默认True
soup.find_all('a')
结果：
[<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a>, <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>]
soup.find_all('a',recursive=False)
结果：
[]    #儿子节点无'a'标签

string:<>...</>中字符串区域的检索字符串
soup
结果：
<html><head><title>This is a python demo page</title></head>
<body>
<p class="title"><b>The demo python introduces several python courses.</b></p>
<p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:
<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a> and <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>.</p>
</body></html>
soup.find_all(string='Basic Python')
结果：
['Basic Python']

'''
'''
简写
<tag>(..) 等价于 <tag>.find_all(..)
soup(..) 等价于 soup.find_all(..)

'''