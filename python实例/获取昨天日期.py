#获取昨天日期
#引入datetime模块
import datetime
def getYesterday():
    today=datetime.date.today()
    oneday=datetime.timedelta(days=1)#days=2为前两天，依次类推
    yesterday=today-oneday
    return yesterday

#输出

print(getYesterday())
