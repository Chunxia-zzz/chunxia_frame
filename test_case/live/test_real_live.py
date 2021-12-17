# encoding:UTF-8

"""
author: 春夏
update at: 2021/10/25
info: 测试配置直播内容为真直播
"""

import pytest

from Common.EnvConfig import host, headers
from api.live.create_course_content import create_course_content
from api.live.real_live import real_live
from test_data.live.data_real_live import real_live_data, test_env


# @pytest.mark.skip(reason='死水数据专用')
def test_initial():
    res = create_course_content("yx接口创建", real_live_data[test_env]["object_id"], host, headers).json()
    content_id = res['data']['id']

    resp = real_live(real_live_data[test_env]["anchor_id"], real_live_data[test_env]["question_id"], content_id, host,
                     headers)
    assert resp.status_code == 200
    assert resp.json().get("code") == 0
    assert resp.json().get("msg") == "ok"


@pytest.mark.skip(reason='活水测试专用')
def test_1():
    res = create_course_content("yx接口创建", real_live_data[test_env]["object_id"], host, headers).json()
    content_id = res['data']['id']
    print(content_id)

    resp = real_live(real_live_data[test_env]["anchor_id"], real_live_data[test_env]["question_id"], content_id, host,
                     headers)
    print(resp.text)
