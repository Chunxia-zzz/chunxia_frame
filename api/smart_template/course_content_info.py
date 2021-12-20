# encoding:UTF-8

"""
author: yx
update at: 2021/10/15
info: 查询原内容信息
"""

import requests


def course_content_info(content_id, host, headers):
    path = "/study-center/admin/api/v1/course_content.info"
    url = host + path

    params = {"id": content_id}

    resp = requests.get(url=url, params=params, headers=headers)
    return resp
