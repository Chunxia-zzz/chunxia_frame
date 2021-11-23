# encoding:UTF-8

"""
author: yx
update at: 2021/10/15
info: 更改模板分组名称
"""

import requests


def smart_live_template_bank_put(template_bank_id, name, host, headers):
    path = "/study-center/admin/api/v1/smart_live_template_bank"
    url = host + path

    payload = {"name": name,
               "id": template_bank_id}

    resp = requests.put(url=url, json=payload, headers=headers)
    return resp
