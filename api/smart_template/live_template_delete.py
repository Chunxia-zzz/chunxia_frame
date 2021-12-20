# encoding:UTF-8

"""
author: yx
update at: 2021/10/18
info: 依据模板id删除此模板
"""

import requests


def live_template_delete(template_id, host, headers):
    path = "/study-center/admin/api/v1/live_template/{}".format(template_id)
    url = host + path

    resp = requests.delete(url=url, headers=headers)
    return resp
