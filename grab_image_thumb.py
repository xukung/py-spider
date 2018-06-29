#! /usr/bin/env python3

from requests_html import HTMLSession
import requests
from lib.mysql import MSSQL
from lib.func import Func

session = HTMLSession()
ms = MSSQL(host="localhost", user="root", pwd="123456", db="spider")
siteList = [
    # {
    #     'pages': [
    #         'http://www.win4000.com/zt/zhiwu_1.html',
    #     ],
    #     'path': '.Left_bar .tab_box ul li',
    #     'attr': 'data-original',
    # },
    {
        'pages': [
            'http://soso.nipic.com/?q=%E8%8C%B6%E9%81%93',
        ],
        'path': 'ul#img-list-outer li',
        'attr': 'data-original',
    },
]


# 保存图片到目录
def save_image(imgSrc):
    import time

    newName = Func.randomId()
    curDate = time.strftime('%Y%m%d', time.localtime())
    newPath = './download/image/' + curDate + '/'
    Func.createPath(newPath)
    ms.ExecNonQuery("""INSERT INTO image(name,source) VALUES ("%s","%s")""" % (newName, imgSrc))

    img_response = requests.get(imgSrc)
    with open(newPath + newName + '.jpg', 'wb') as file:
        file.write(img_response.content)
        print(imgSrc, newName, ' 保存成功！')


for site in siteList:
    for page in site['pages']:
        r = session.get(page)
        items = r.html.find(site['path'])

        for item in items:
            if item.find('img'):
                imageUrl = item.find('img')[0].attrs[site['attr']]
                save_image(imageUrl)
