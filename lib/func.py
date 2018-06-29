import os
import random
import string


class Func:
    # def __init__(self):
    # print('init')

    # 创建路径相关目录
    def createPath(path):
        isExists = os.path.exists(path)
        if not isExists:
            os.makedirs(path)
            print(path + ' 创建成功！')
            return True
        else:
            # print(path + ' 目录已存在')
            return False

    def randomId(size=16, chars=string.ascii_letters + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))
