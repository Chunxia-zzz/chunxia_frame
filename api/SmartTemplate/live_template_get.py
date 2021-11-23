# encoding:UTF-8

"""
author: yx
update at: 2021/10/15
info: 依据模板组id查询当前组内所有模板live_template
"""

import requests


def live_template_get(template_bank_id, host, headers):
    path = "/study-center/admin/api/v1/live_template"
    url = host + path

    params = {"limit": 9999,
              "offset": 0,
              "template_bank_id": template_bank_id
              }

    resp = requests.get(url=url, params=params, headers=headers)
    return resp
