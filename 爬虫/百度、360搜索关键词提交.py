#百度、360搜索关键词提交
import requests

def search(key,url):
    keyword = "Python"
    try:
        kv={key:keyword}
        r=requests.get(url,params=kv)
        print(r.request.url)
        r.raise_for_status()
        print(len(r.text))
    except:
        print("爬取失败")
info={"wd":"http://www.baidu.com/s","q":"http://www.so.com/s"}

for key,value in info.items():
    search(key,value)

