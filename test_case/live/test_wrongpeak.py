# encoding:UTF-8

"""
author: 春夏
update at: 2021/11/3
info: 线上:伪直播错峰测试
"""

import pytest

from Common.EnvConfig import host, headers
from api.live.create_course_content import create_course_content
from api.live.fake_live import fake_live, fake_live_delay


def test_1():
    res = create_course_content("春夏错峰测试1", 1101, host, headers).json()
    content_id = res['data']['id']
    print(content_id)

    # 测错峰的时候调人数为24，创建完成调回来
    resp = fake_live(336, 351, host, headers, content_id)
    print(resp.text)


def test_2():
    res = create_course_content("春夏错峰测试2", 1101, host, headers).json()
    content_id = res['data']['id']
    print(content_id)

    resp = fake_live_delay(337, 335, host, headers, content_id)
    print(resp.text)
