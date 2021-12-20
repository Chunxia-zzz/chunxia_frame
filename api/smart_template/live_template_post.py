# encoding:UTF-8

"""
author: yx
update at: 2021/10/15
info: 定义此接口：新建智能直播模板
"""

import requests


def live_template_post(name, content_id, template_bank_id, host, headers):
    path = "/study-center/admin/api/v1/live_template"
    url = host + path

    payload = {"template_bank_id": template_bank_id,
               "content_id": content_id,
               "content_type": "live",
               "name": name}

    resp = requests.post(url=url, json=payload, headers=headers)
    return resp
