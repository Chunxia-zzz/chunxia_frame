# encoding:UTF-8

"""
author: yx
update at: 2021/10/18
info: 控堂页随机机器人接口
"""

import requests


def random_list(host, headers):
    path = "/ucenter/admin/api/v1/user/random_list"
    url = host + path

    resp = requests.get(url=url, headers=headers)
    return resp
