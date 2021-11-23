# encoding:UTF-8

"""
author: 春夏
update at: 2021/10/21
info: 测试配置直播内容为伪直播
"""

import pytest

from Common.EnvConfig import host, headers
from api.live.create_course_content import create_course_content
from api.live.fake_live import fake_live
from testdata.live.data_fake_live import test_env, fake_live_data


def test_initial():
    res = create_course_content("yx接口创建", fake_live_data[test_env]["object_id"], host, headers).json()
    content_id = res['data']['id']

    resp = fake_live(fake_live_data[test_env]["anchor_id"], fake_live_data[test_env]["template_id"], host, headers,
                     content_id)
    assert resp.status_code == 200
    assert resp.json().get("code") == 0
    assert resp.json().get("msg") == "ok"


# @pytest.mark.skip(reason='活水测试专用')
def test_1():
    res = create_course_content("肖威伪直播", 853, host, headers).json()
    content_id = res['data']['id']
    print(content_id)

    resp = fake_live(226, 75, host, headers, content_id)
    print(resp.text)
