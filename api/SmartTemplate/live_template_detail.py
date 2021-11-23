# encoding:UTF-8

"""
author: yx
update at: 2021/10/18
info: 依据模板id查询此模板详情
"""

import requests


def live_template_detail(template_id, host, headers):
    path = "/study-center/admin/api/v1/live_template/{}".format(template_id)
    url = host + path

    resp = requests.get(url=url, headers=headers)
    return resp
