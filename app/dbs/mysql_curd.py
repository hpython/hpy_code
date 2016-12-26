#!/usr/bin/env python
# -*- encoding: utf-8 -*-
__author__ = 'Ryan'
__email__ = "liuwei412552703@163.com"


import MySQLdb


def print_data(datas):
    for r in datas:
        print(r)



if __name__ == '__main__':
    conn = MySQLdb.connect(host='localhost', user='root',passwd='123456',db="test", charset='utf8')
    #获取操作游标
    cursor = conn.cursor()

    #选择数据库
    #conn.select_db('test')

    #执行SQL,并查询数据
    cursor.execute("select * from users")
    results = cursor.fetchmany(5)
    print_data(results)

    #重置游标位置，0,为偏移量，mode＝absolute | relative,默认为relative,
    cursor.scroll(0,mode='absolute')

    #获取所有结果
    results = cursor.fetchall()
    print_data(results)

    # 插入数据
    cursor.execute ("""INSERT INTO users(ID, username, password, address) VALUES (1, 'a', 'b', 'c'),(3, 'aaa', 'bbb', 'ccc') """)
    conn.commit()


    #关闭连接，释放资源
    cursor.close()

