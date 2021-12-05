# encoding:UTF-8

"""
Author: yx
Update at: 2021/10/18
info: 数据库连接(弃用)
"""

import pymysql


class DbCollection(object):
    study_center = pymysql.connect(host='172.18.80.26',
                                   port=3309,
                                   user='root',
                                   database='study_center',
                                   passwd='PKC6FBuix4&Cj0Mi')


# 可以指定字符集：charset="utf8"

db_study_center = DbCollection.study_center

if __name__ == '__main__':
    cursor = db_study_center.cursor()
    # cursor = DbCollection.study_center.cursor()
    cursor.execute("SELECT 1+1")  # 测试数据库连接
    values = cursor.fetchall()
    assert values[0][0] == 2
