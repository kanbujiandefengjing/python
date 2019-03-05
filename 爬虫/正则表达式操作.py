'''
正则表达式
regular expression     regex   RE
正则表达式是用来简洁表达一组字符串的表达式
'PN'
'PYN'             正则表达式：
'PYTN'       <=> P(Y|YT|YTH|YTHO)?N  
'PYTHN'
'PYTHON'

通用的字符串表达框架
简洁表达一组字符串的表达式
针对字符串表达“简洁”和“特征”思想的工具
判断某字符串的特征归属

表达文本类型的特征（病毒、入侵等）
同时查找或替换一组字符串
匹配字符串的全部或部分

使用：
编译：将符合正则表达式的字符串转换成正则表达式特征

常用正则表达式操作符
.      表示任何单个字符
[]     字符集，对单个字符给出取值范围  [abc]表示a、b、c,[a-z]表示a-z单个字符
[^]    非字符集，对单个字符给出排除范围[^abc]表示非a或b或c的单个字符
*      前一个字符0次或无限次扩展       abc*表示ab、abc、abcc、abccc等
+      前一个字符1次或无限次扩展       abc+表示abc、abcc、abccc等
?      前一个字符0次或1次扩展          abc?表示ab、abc
|      左右表达式任意一个              abc|def表示abc或def
{m}    扩展前一个字符m次               ab{2}c表示abbc
{m,n}  扩展前一个字符m至n次（含n）      ab{1,2}c表示abc、abbc
^      匹配字符串开头                  ^abc表示abc且在一个字符串的开头
$      匹配字符串结尾                  abc$表示abc且在一个字符串的结尾
()     分组标记，内部只能使用|操作符    (abc)表示abc,(abc|def)表示abc、def
\d     数字，等价于[0-9]
\w     单词字符，等价于[A-Za-z0-9_]

实例：
   正则表达式                           对应字符串
P(Y|YT|YTH|YTHO)?N                'PN','PYN','PYTHN','PYTHON'
PYTHON+                           'PYTHON','PYTHONN','PYTHONNN'...
PY[TH]ON                          'PYTON','PYHON'
PY[^TH]?ON                        'PYON','PYAON','PYBON','PYGON','PYSON','PYUON'
PY{:3}N                           'PN','PYN','PYYN','PYYYN'

经典正则表达式实例
^[A-Za-z]+$                        由26个字母组成的字符串
^[A-Za-z0-9]+$                     由26个字母和数字组成的字符串
^-?\d+$                            整数形式的字符串
^[0-9]*[1-9][0-9]*$                正整数形式的字符串
[1-9]\d{5}                         中国境内邮政编码，6位
[\u4e00-\u9fa5]                    匹配中文字符
'''

'''
Re库为python标准库，主要用于字符串匹配
调用方式：import re

正则表达式的表示类型
raw string类型(原生字符串类型)
re库采用raw string类型表示正则表达式，表示为：r:'text'
例如：
     r'[1-9]\d{5}'
     r'\d{3}-\d{8}|\d{4}-d{7}'
     raw string 是不包含转义符的字符串

Re库主要功能函数
re.search()    在一个字符串中搜索匹配正则表达式的第一个位置，返回match对象
re.match()     从一个字符串的开始位置起匹配正则表达式，返回match对象
re.findall()   搜索字符串，以列表类型返回全部能匹配的子串
re.split()     将一个字符串按照正则表达式匹配结果进行分割，返回列表类型
re.finditer()  搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素是match对象
re.sub()       在一个字符串中替换所有匹配正则表达式的子串，返回替换后的字符串
 
 
re.search(pattern,string,flags=0)
在一个字符串中搜索匹配正则表达式的第一个位置，返回match对象
 pattern:正则表达式的字符串或原生字符串表示
 string：待匹配字符串
 flags:正则表达式使用时的控制标记
 
   flags:正则表达式使用时的控制标记
   常用标记                           说明
re.I  re.IGNORECASE    忽略正则表达式的大小写，[A-Z]能够匹配小写字符
re.M  re.MuLTILINE     正则表达式中的^操作符能够将给定字符串的每行当做匹配开始
re.S  re.DOTALL        正则表达式中的.操作符能够匹配所有字符，默认匹配除换行外所有字符

示例：
>>> import re
>>> match=re.search(r'[1-9]\d{5}','BIT 100081')
>>> if match:
    print(match.group(0))
100081

>>> import re
>>> content='Hellow 123456 world.'
>>> content=re.sub('\d+',r'\1 8910',content)
>>> print(content)
Hello 123456 8910 world


'''
