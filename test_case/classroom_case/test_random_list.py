# encoding:UTF-8

"""
author: yx
update at: 2021/10/15
info:测试随机机器人接口
"""
import pytest

from Common.EnvConfig import host, headers
from api.Classroom.random_list import random_list


@pytest.mark.skip(reason='需求已完成')
def test_1():
    resp = random_list(host, headers)
    array = resp.json()
    user_data_list = array["data"]

    user_array = []
    for i in user_data_list:
        uid = i["uid"]
        user_array.append(uid)

    print(tuple(user_array))

    # SELECT id, is_robot FROM account_user WHERE id IN ('471208', '471648', '471244', '471158', '471482', '471333',
    # '471399', '471675', '471626', '471453') 即tuple(user_array)
    # assert resp.status_code == 200
    # assert resp.json().get("code") == 0
