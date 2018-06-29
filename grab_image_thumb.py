#! /usr/bin/env python3

from requests_html import HTMLSession
from lib.func import Func

session = HTMLSession()
func = Func()

list_max_num = 3  # 列表最大数量
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

for site in siteList:
    for page in site['pages']:
        r = session.get(page)
        items = r.html.find(site['path'])

        for index, item in enumerate(items):
            if index < list_max_num and item.find('img'):
                imageUrl = item.find('img')[0].attrs[site['attr']]
                func.save_image(imageUrl)
