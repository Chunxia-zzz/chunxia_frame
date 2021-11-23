# encoding:UTF-8

"""
author: yx
update at: 2021/10/22
info: B端满意度导出为excel
"""

import requests


def excel(content_id, host, headers):
    path = "/study-center/admin/api/v1/course_content_satisfaction/excel"
    url = host + path

    payload = {"content_id": content_id,
               "has_suggestions": False,
               "search_key": ""}

    resp = requests.post(url=url, json=payload, headers=headers)
    return resp
