# encoding:UTF-8

"""
author: yx
update at: 2021/10/15
info: 查询当前店铺所有模板分组
"""

import requests


def page_list(host, headers):
    path = "/study-center/admin/api/v1/smart_live_template_bank/page_list"
    url = host + path

    params = {"limit": 9999,
              "offset": 0}

    resp = requests.get(url=url, params=params, headers=headers)
    return resp
