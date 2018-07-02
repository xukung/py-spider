#! /usr/bin/env python3

from requests_html import HTMLSession
from lib.func import Func
import pymysql

session = HTMLSession()
func = Func()

list_max_num = 3  # 列表最大数量
siteList = [
    {
        'siteName': 'thepaper-financial',
        'host': 'https://www.thepaper.cn/',
        'pages': [
            'https://www.thepaper.cn/channel_25951',
        ],
        'listPath': '.newsbox .news_li',
        'detailTitlePath': '.newscontent .news_title',
        'detailContentPath': '.newscontent .news_txt',
    },
]


def find_detail(page_url, detail_title_path, detail_content_path, source_id, source):
    r = session.get(page_url)
    title = r.html.find(detail_title_path)[0].text
    content = r.html.find(detail_content_path)[0].html
    content_escape = pymysql.escape_string(content)  # 需要转移单引号双引号，否则sql语句插入报错
    func.save_news(title, content_escape, source_id, source)


for site in siteList:
    for page in site['pages']:
        r = session.get(page)
        items = r.html.find(site['listPath'])

        for index, item in enumerate(items):
            if index < list_max_num and item.find('a'):
                pageUrl = site['host'] + item.find('a')[0].attrs['href']
                pageId = item.find('a')[0].attrs['data-id']
                # print('attrs:', item.find('a')[0].attrs)
                # print('pageUrl:', pageUrl)
                find_detail(pageUrl, site['detailTitlePath'], site['detailContentPath'], pageId, site['siteName'])
