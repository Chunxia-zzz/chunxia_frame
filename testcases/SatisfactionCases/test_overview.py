# encoding:UTF-8

"""
author: yx
update at: 2021/10/22
info:B端满意度列表接口测试
"""

from Common.EnvConfig import host, headers
from api.Satisfaction.overview import overview


def test_1():
    resp = overview(1271, host, headers)
    print(resp.text)

    # assert resp.status_code == 200
    # assert resp.json().get("code") == 0
