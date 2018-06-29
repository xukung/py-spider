#! /usr/bin/env python3

from requests_html import HTMLSession
import requests
from lib.mysql import MSSQL
from lib.func import Func

session = HTMLSession()
ms = MSSQL(host="localhost", user="root", pwd="123456", db="spider")
pageList = [
    'http://www.win4000.com/zt/zhiwu_1.html',
    'http://www.win4000.com/zt/zhiwu_2.html',
]
queryPath = '.Left_bar .tab_box ul li'


# 保存图片到目录
def save_image(imgSrc):
    import time

    newName = Func.randomId()
    curDate = time.strftime('%Y%m%d', time.localtime())
    newPath = './download/image/' + curDate + '/'
    Func.createPath(newPath)
    ms.ExecNonQuery("""INSERT INTO image(name,src) VALUES ("%s","%s")""" % (newName, imgSrc))

    img_response = requests.get(imgSrc)
    with open(newPath + newName + '.jpg', 'wb') as file:
        file.write(img_response.content)
        print(imgSrc, newName, ' 保存成功！')


for page in pageList:
    r = session.get(page)
    items = r.html.find(queryPath)

    for item in items:
        imageUrl = item.find('img')[0].attrs['data-original']
        save_image(imageUrl)
