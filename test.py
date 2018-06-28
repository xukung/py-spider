#! /usr/bin/env python3

from requests_html import HTMLSession
import requests
from lib.mysql import MSSQL
from lib.func import Func

session = HTMLSession()
ms = MSSQL(host="localhost", user="root", pwd="123456", db="spider")


# Func = Func()


# 保存图片到目录
def save_image(url, title):
    ms.ExecNonQuery("""INSERT INTO image(name,url) VALUES ("%s","%s")""" % (title, url))
    print(url, title, ' 保存成功！')

    img_response = requests.get(url)
    import time
    curDate = time.strftime('%Y%m%d', time.localtime())
    newPath = './download/image/' + curDate + '/'
    Func.createPath(newPath)
    with open(newPath + title + '.jpg', 'wb') as file:
        file.write(img_response.content)


r = session.get('http://www.win4000.com/zt/zhiwu_1.html')
arr = r.html.find('.Left_bar .tab_box ul li')

for li in arr:
    title = li.find('a p')[0].text
    imageUrl = li.find('a img')[0].attrs['data-original']
    save_image(imageUrl, title)
