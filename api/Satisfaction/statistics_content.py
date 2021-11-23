# encoding:UTF-8

"""
author: yx
update at: 2021/10/22
info: B端-课程维度，根据内容id查看满意度评分统计概览
"""

import requests


def statistics_content(content_id, host, headers):
    path = "/study-center/admin/api/v1/course_content_satisfaction/statistics"
    url = host + path

    params = {"offset": 0,
              "limit": 10,
              "content_id": content_id
              }

    resp = requests.get(url=url, params=params, headers=headers)
    return resp
