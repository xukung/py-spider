import os
import random
import string
import requests
import time
import imgspy

from .mysql import MSSQL


class Func:
    # def __init__(self):
    #     print('')

    # 创建路径相关目录
    def createPath(self, path):
        isExists = os.path.exists(path)
        if not isExists:
            os.makedirs(path)
            print(path + ' 文件夹创建成功！')
            return True
        else:
            # print(path + ' 目录已存在')
            return False

    # 生成随机16位字符
    def random_str(self, size=16, chars=string.ascii_letters + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    # 保存新闻
    def save_news(self, title, content, source_id, source):
        ms = MSSQL(host="localhost", user="root", pwd="123456", db="spider")
        rows = ms.ExecQuery("""SELECT id from news WHERE source_id="%s" """ % (source_id))
        # print('rows length:', len(rows))
        if len(rows) > 0:
            print(title + ' --已存在！')
        else:
            ms.ExecNonQuery("""INSERT INTO news(title,content,source_id,source) VALUES ("%s","%s","%s","%s")""" % (
                title, content, source_id, source))
            print(title + ' --保存成功')

    # 保存图片到目录
    def save_image(self, img_src):
        image_info = imgspy.info(img_src)
        new_name = self.random_str() + '.' + image_info['type']
        cur_date = time.strftime('%Y%m%d', time.localtime())
        new_path = './download/image/' + cur_date + '/'
        self.createPath(new_path)

        # ms = MSSQL(host="localhost", user="root", pwd="123456", db="spider")
        # ms.ExecNonQuery("""INSERT INTO image(name,source) VALUES ("%s","%s")""" % (new_name, img_src))

        img_response = requests.get(img_src)
        with open(new_path + new_name, 'wb') as file:
            file.write(img_response.content)
            print(img_src, ' --保存成功！')

    def save_video(self, video_src):
        new_name = self.random_str() + '.mp4'
        cur_date = time.strftime('%Y%m%d', time.localtime())
        new_path = './download/video/' + cur_date + '/'
        self.createPath(new_path)

        # ms = MSSQL(host="localhost", user="root", pwd="123456", db="spider")
        # ms.ExecNonQuery("""INSERT INTO video(name,source) VALUES ("%s","%s")""" % (new_name, video_src))

        img_response = requests.get(video_src)
        with open(new_path + new_name, 'wb') as file:
            file.write(img_response.content)
            print(video_src, ' --保存成功！')
