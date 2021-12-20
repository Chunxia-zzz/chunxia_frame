# encoding:UTF-8

"""
author: yx
update at: 2021/10/26
info:测试查询模板详情
"""

import pytest

from common.env_config import host, headers
# from Common.EnvConfig import host, headers
from api.smart_template.live_template_detail import live_template_detail


def test_1():
    resp = live_template_detail(63, host, headers)

    assert resp.status_code == 200
    assert resp.json()["code"] == 0
    assert resp.json()["data"]["id"] == 63


def test_2():
    resp = live_template_detail(-1, host, headers)
    assert resp.status_code == 200
    assert resp.json().get("code") == 1001
    assert resp.json().get("msg") == "该模版不存在"


@pytest.mark.parametrize("content_id", ["A", "a", "汉字", "$"])
def test_3(content_id):
    resp = live_template_detail(content_id, host, headers)
    assert resp.status_code == 400
    assert resp.json().get("code") == 400
    assert resp.json().get("msg") == "参数类型错误"
