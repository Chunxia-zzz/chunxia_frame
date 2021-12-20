# encoding:UTF-8

"""
author: yx
update at: 2021/11/3
info:定义公共固件
"""

import time

import pymysql
import pytest


# 默认作用域也是function
@pytest.fixture(scope='function')
def study_center():
    study_center = pymysql.connect(host='172.18.80.26',
                                   port=3309,
                                   user='root',
                                   database='study_center',
                                   passwd='PKC6FBuix4&Cj0Mi')
    cursor = study_center.cursor()
    cursor.execute("SELECT 1+1")  # 测试数据库连接
    values = cursor.fetchall()
    assert values[0][0] == 2
    print("数据库正常开启")

    yield

    study_center.close()
    try:
        cursor.execute("SELECT 1+1")
    except pymysql.err.InterfaceError:
        print("数据库正常关闭")


@pytest.fixture(autouse=True)
def timer_function_scope():
    start = time.time()
    yield
    print(' Time cost: {:.3f}s'.format(time.time() - start))


DATE_FORMAT = '%Y-%m-%d %H:%M:%S'


@pytest.fixture(scope='session', autouse=True)
def timer_session_scope():
    start = time.time()
    print('\nstart: {}'.format(time.strftime(DATE_FORMAT, time.localtime(start))))

    yield

    finished = time.time()
    print('finished: {}'.format(time.strftime(DATE_FORMAT, time.localtime(finished))))
    print('Total time cost: {:.3f}s'.format(finished - start))


def test_postcode(db):
    assert 10 == 10
