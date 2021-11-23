# encoding:UTF-8

"""
author: yx
update at: 2021/10/22
info: B端满意度列表接口
"""

import requests


def satisfaction_list(host, headers):
    path = "/study-center/admin/api/v1/course_satisfaction/statistics/list"
    url = host + path

    params = {"offset": 0,
              "limit": 10}

    resp = requests.get(url=url, params=params, headers=headers)
    return resp
