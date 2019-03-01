import requests
import os
url = "https://www.nationalgeographic.com./animals/2019/01/blue-eyes-mutation-coyotes-spreading-in-california/#/02-blue-eyes-coyote-carter-kremer-santa-cruz-dsc_6490-copy.jpg"
root = "F://图片//"
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root): #判断根目录是否存在
        os.mkdir(root)
    if not os.path.exists(path): #判断文件是否存在
        r = requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")
    