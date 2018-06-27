#! /usr/bin/env python3

from requests_html import HTMLSession;
import requests;

session = HTMLSession();


# 保存图片到目录
def save_image(url, title):
    print('save:', title, url)
    img_response = requests.get(url)
    with open('./download/' + title + '.jpg', 'wb') as file:
        file.write(img_response.content);


r = session.get('http://www.win4000.com/zt/zhiwu_5.html');
arr = r.html.find('.tab_box ul li')

for li in arr:
    title = li.find('a p')[0].text;
    imageUrl = li.find('a img')[0].attrs['data-original'];
    save_image(imageUrl, title);
