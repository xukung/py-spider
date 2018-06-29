#! /usr/bin/env python3

from requests_html import HTMLSession
from lib.func import Func

session = HTMLSession()
func = Func()

siteList = [
    {
        'pages': [
            'http://v.huanqiu.com/observation/2018-06/12374053.html',
        ],
        'path': '.con_left #vt-video',
        'attr': 'src',
    },
]

for site in siteList:
    for page in site['pages']:
        r = session.get(page)
        items = r.html.find(site['path'])

        for index, item in enumerate(items):
            if item.find('video'):
                video_src = item.find('video')[0].attrs[site['attr']]
                func.save_video(video_src)
