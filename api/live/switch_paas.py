# encoding:UTF-8

"""
author: yx
update at: 2021/10/29
info: 切paas接口
"""

import requests


def switch_paas(content_id, host, headers):
    path = "/study-center/api/v1/live_practice/provider.change"
    url = host + path
    payload = {"content_id": content_id,
               "provider": 2}

    resp = requests.post(url=url, json=payload, headers=headers)
    return resp
