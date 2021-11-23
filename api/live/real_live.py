# encoding:UTF-8

"""
author: yx
update at: 2021/10/25
info: 给直播内容配置成为真直播
"""
from datetime import datetime, timedelta

import requests

now = datetime.now()
begin_time = now + timedelta(minutes=2)
expected_started_time = begin_time.timestamp()
end_time = now + timedelta(hours=2)
expected_finished_time = end_time.timestamp()


# 主播id,模板id,内容id
def real_live(anchor_id, question_id, content_id, host, headers):
    path = "/study-center/admin/api/v1/live"
    url = host + path

    payload = {
        "expected_started_at": expected_started_time,
        "expected_finished_at": expected_finished_time,
        "anchor_id": anchor_id,
        "cover": "https://bn-stage-1254108098.cos.ap-guangzhou.myqcloud.com/4131629708836192.jpg",
        "have_playback": 1,
        "live_mode_type": "real",
        "list_homework": [{"question_id": question_id, "content_id": content_id}],
        "has_practice": True,
        "people_amount": 1,
        "content_id": content_id
    }

    resp = requests.post(url=url, json=payload, headers=headers)
    return resp
