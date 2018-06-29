#! /usr/bin/env python3

from requests_html import HTMLSession
from lib.mysql import MSSQL
from lib.func import Func

import requests
import time

session = HTMLSession()
ms = MSSQL(host="localhost", user="root", pwd="123456", db="spider")
list_max_num = 3  # 列表最大数量

siteList = [
    # {
    #     'pages': [
    #         'http://www.win4000.com/zt/zhiwu_1.html',
    #     ],
    #     'listPath': '.Left_bar .tab_box ul li',
    #     'bigPicPath': '.main-wrap img.pic-large',
    #     'nextLinkPath': '.main-wrap .pic-next-img a',
    #     'attr': 'data-original',
    # },

    {
        'pages': [
            'http://soso.nipic.com/?q=%E8%8C%B6%E9%81%93',
        ],
        'listPath': 'ul#img-list-outer li',
        'bigPicPath': '.works-show #static img.works-img',
        'nextLinkPath': '',
        'attr': 'data-original',
    },
]


# 保存图片到目录
def save_image(img_src):
    newName = Func.randomId()
    curDate = time.strftime('%Y%m%d', time.localtime())
    newPath = './download/image/' + curDate + '/'
    Func.createPath(newPath)
    ms.ExecNonQuery("""INSERT INTO image(name,source) VALUES ("%s","%s")""" % (newName, img_src))

    img_response = requests.get(img_src)
    with open(newPath + newName + '.jpg', 'wb') as file:
        file.write(img_response.content)
        print(img_src, newName, ' 保存成功！')


def find_big_image(page_url, big_pic_path, next_link_path):
    r = session.get(page_url)
    bigPicSrc = r.html.find(big_pic_path)[0].attrs['src']
    save_image(bigPicSrc)

    # 递归开始查找下一页
    if r.html.find(next_link_path):
        next_link = r.html.find(next_link_path)[0].attrs['href']
        # print(next_link)
        find_big_image(next_link, big_pic_path, next_link_path)


for site in siteList:
    for page in site['pages']:
        r = session.get(page)
        items = r.html.find(site['listPath'])

        for index, item in enumerate(items):
            if index < list_max_num and item.find('a'):
                pageUrl = item.find('a')[0].attrs['href']
                find_big_image(pageUrl, site['bigPicPath'], site['nextLinkPath'])
