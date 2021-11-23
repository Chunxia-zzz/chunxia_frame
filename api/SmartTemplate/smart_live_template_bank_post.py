# encoding:UTF-8

"""
author: yx
update at: 2021/10/15
info: 创建智能直播模板分组
"""

import requests


def smart_live_template_bank_post(name, host, headers):
    path = "/study-center/admin/api/v1/smart_live_template_bank"
    url = host + path

    payload = {"name": name}

    resp = requests.post(url=url, json=payload, headers=headers)
    return resp
