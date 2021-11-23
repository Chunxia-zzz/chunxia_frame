# encoding:UTF-8

"""
author: yx
update at: 2021/10/15
info: 查询回放列表
"""

import requests


def list_playback(host, headers):
    path = "/study-center/admin/api/v1/course_content.list_playback"
    url = host + path

    params = {"limit": 200,
              "offset": 0,
              "template_bank_id": "live"}

    resp = requests.get(url=url, params=params, headers=headers)
    return resp
