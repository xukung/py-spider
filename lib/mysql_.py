#! /usr/bin/env python3

import pymysql


def insert(name, url):
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "123456", "spider")
    print('connect db')
    print(name, url)

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # 使用execute方法执行SQL语句，s%不能用单引号
    sql = """INSERT INTO image(name,url) VALUES ("%s","%s")""" % (name, url)
    # sql = """INSERT INTO image(name,url) VALUES ('a123','http://')"""

    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

    # 使用 fetchone() 方法获取一条数据
    # data = cursor.fetchone()
    # print(data);

    # 关闭数据库连接
    db.close()
    print('close db')
