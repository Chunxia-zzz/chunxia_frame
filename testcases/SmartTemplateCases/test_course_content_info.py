# encoding:UTF-8

"""
author: yx
update at: 2021/10/15
info:测试查询原课程内容信息接口
"""

import pytest

from Common.EnvConfig import host, headers
from api.SmartTemplate.course_content_info import course_content_info


def test_1():
    resp = course_content_info(4958, host, headers)
    assert resp.status_code == 200
    assert resp.json().get("code") == 0
    assert resp.json().get("data")["id"] == 4958


def test_2():
    resp = course_content_info(1000000000, host, headers)
    assert resp.status_code == 200
    assert resp.json().get("code") == 1001
    assert resp.json().get("msg") == "数据不存在"


@pytest.mark.parametrize("content_id", ["A", "a", "汉字", "$"])
def test_3(content_id):
    resp = course_content_info(content_id, host, headers)
    assert resp.status_code == 400
    assert resp.json().get("code") == 400
    assert resp.json().get("msg") == "参数类型错误"
