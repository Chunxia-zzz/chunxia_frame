# encoding:UTF-8

"""
author: yx
update at: 2021/10/21
info:创建直播内容
"""
import requests


# 营期id
def create_course_content(name, object_id, host, headers):
    path = "/study-center/admin/api/v1/course_content.create"
    url = host + path

    payload = {
        "title": name,
        "cover_picture": "",
        "content_type": "live",
        "object_id": object_id,
        "course_type": "training",
        "qcloud_video_file_id": "",
        "video_url": "",
        "support_terminals": "",
        "sale_relations": [
            {
                "key": "1",
                "sale_ids": [
                    130
                ],
                "sale_name_str": "春夏-超级管理员",
                "user_count": 0,
                "user_range": "current"
            },
            {
                "key": "2",
                "sale_ids": [],
                "sale_name_str": "",
                "user_count": 0,
                "user_range": "past",
                "user_range_camps": []
            }
        ]
    }

    resp = requests.post(url=url, json=payload, headers=headers)
    return resp


'''
stage:130 春夏-超级管理员
uat:130 春夏-超级管理员
prod: 175 李米
'''
