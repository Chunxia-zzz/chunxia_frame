# encoding:UTF-8

"""
author: yx
update at: 2021/10/22
info: B端根据课程id查询课程内所有满意度评价记录
"""

import requests


def overview(course_id, host, headers):
    path = "/study-center/admin/api/v1/content_satisfaction/overview?offset=0&limit=10&course_id=1271"
    url = host + path

    params = {"offset": 0,
              "limit": 10,
              "course_id": course_id}

    resp = requests.get(url=url, params=params, headers=headers)
    return resp
