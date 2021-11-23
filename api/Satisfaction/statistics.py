# encoding:UTF-8

"""
author: yx
update at: 2021/10/22
info: B端-课程维度，根据课程id查看满意度评分统计概览
"""

import requests


def statistics(course_id, host, headers):
    path = "/study-center/admin/api/v1/course_satisfaction/statistics"
    url = host + path

    params = {"offset": 0,
              "limit": 10,
              "course_id": course_id
              }

    resp = requests.get(url=url, params=params, headers=headers)
    return resp
