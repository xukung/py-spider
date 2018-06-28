#! /usr/bin/env python3

from requests_html import HTMLSession;
import requests;
import os;
import lib.mysql;

session = HTMLSession();


def createPath(path):
    isExists = os.path.exists(path);
    if not isExists:
        os.makedirs(path);
        print(path + ' 创建成功！');
        return True;
    else:
        # print(path + ' 目录已存在');
        return False;


# 保存图片到目录
def save_image(url, title):
    lib.mysql.insert(title, url);
    print(url, title, ' 保存成功！')
    img_response = requests.get(url)
    import time;
    curDate = time.strftime('%Y%m%d', time.localtime());
    newPath = './download/image/' + curDate + '/';
    createPath(newPath);
    # with open(newPath + title + '.jpg', 'wb') as file:
    #     file.write(img_response.content);


r = session.get('http://www.win4000.com/zt/zhiwu_1.html');
arr = r.html.find('.Left_bar .tab_box ul li')

for li in arr:
    title = li.find('a p')[0].text;
    imageUrl = li.find('a img')[0].attrs['data-original'];
    # save_image(imageUrl, title);


lib.mysql.insert('abc', 'huanqiu');