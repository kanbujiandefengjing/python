#中国大学排名定向爬虫
'''
程序的结构设计
步骤1：从网络上获取大学排名网页内容
步骤2：提取网页内容中信息到合适的数据结构
步骤3：利用数据结构展示并输出结果
'''
import requests
from bs4 import BeautifulSoup
import bs4
def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)#获取url信息
        r.raise_for_status()  #产生异常信息
        r.encoding = r.apparent_encoding  #修改编码
        return r.text     #返回信息
    except:
        return ""       #返回异常
def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,"html.parser") #解析网页
    for tr in soup.find('tbody').children:  #遍历查找'tbody'的儿子
        if isinstance(tr,bs4.element.Tag):  #检测过滤tr中非bs4.element.Tag标签类型
            tds = tr('td') #存储td为tds(列表类型）
            ulist.append([tds[0].string,tds[1].string,tds[3].string])#加到列表ulist中
            
def printUnivList(ulist,num): 
    tplt = "{0:^10}\t{1:{3}^15}\t{2:^10}"   #输出变量模板  {3}：使用format中第三个变量chr(12288)填充
    print(tplt.format("排名","学校名称","总分",chr(12288))) #格式化输出表头
    for i in range(num):
        u=ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))

def main():
    uinfo=[]
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2018.html'#
    html = getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,20) #20univs
main()

