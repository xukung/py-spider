#! /usr/bin/env python3

import pymysql


def insert(name, url):
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "123456", "spider")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # 使用execute方法执行SQL语句
    # sql = "INSERT INTO image(name,url) VALUES (s%,s%)" % (name, url)
    sql = """INSERT INTO image(name,url) VALUES ('a123','http://')""";
    cursor.execute(sql)

    # 使用 fetchone() 方法获取一条数据
    # data = cursor.fetchone()
    # print(data);

    # 关闭数据库连接
    db.close()
