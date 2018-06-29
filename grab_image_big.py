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
    #     'listPath': '.Left_bar .tab_box ul li',
    #     'bigPicPath': '.main-wrap img.pic-large',
    #     'nextLinkPath': '.main-wrap .pic-next-img a',
    #     'attr': 'data-original',
    # },

    {
        'pages': [
            'http://soso.nipic.com/?q=%E8%8C%B6%E9%81%93&page=2',
        ],
        'listPath': 'ul#img-list-outer li',
        'bigPicPath': '.works-show #static img.works-img',
        'nextLinkPath': '',
        'attr': 'data-original',
    },
]


def find_big_image(page_url, big_pic_path, next_link_path):
    r = session.get(page_url)
    bigPicSrc = r.html.find(big_pic_path)[0].attrs['src']
    func.save_image(bigPicSrc)

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
