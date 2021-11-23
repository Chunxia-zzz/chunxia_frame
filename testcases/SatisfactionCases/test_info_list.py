# encoding:UTF-8

"""
author: yx
update at: 2021/10/22
info:B端根据内容id查询所有用户满意度提交列表 接口测试
"""

from Common.EnvConfig import host, headers
from api.Satisfaction.info_list import info_list


def test_1():
    resp = info_list(10297, host, headers)
    # print(resp.text)

    assert resp.status_code == 200
    assert resp.json().get("code") == 0
