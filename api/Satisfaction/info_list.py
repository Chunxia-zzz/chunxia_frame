# encoding:UTF-8

"""
author: yx
update at: 2021/10/22
info: B端-根据内容id查询所有用户满意度提交列表
"""

import requests


def info_list(content_id, host, headers):
    path = "/study-center/admin/api/v1/course_content_satisfaction/info.list"
    url = host + path

    payload = {"offset": 0,
               "limit": 10,
               "content_id": content_id,
               "has_suggestions": False
               }

    resp = requests.post(url=url, json=payload, headers=headers)
    return resp
