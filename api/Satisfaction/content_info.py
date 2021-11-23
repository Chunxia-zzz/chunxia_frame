# encoding:UTF-8

"""
author: yx
update at: 2021/10/22
info: B端内容信息
"""

import requests


def content_info(content_id, host, headers):
    path = "/study-center/admin/api/v1/course_content_satisfaction/content_info"
    url = host + path

    params = {
              "content_id": content_id
              }

    resp = requests.get(url=url, params=params, headers=headers)
    return resp
