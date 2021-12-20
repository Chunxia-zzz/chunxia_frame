# encoding:UTF-8

"""
author: yx
update at: 2021/10/18
info:测试删除模板
"""
import pytest

from common.env_config import host, headers
from api.smart_template.live_template_delete import live_template_delete
from api.smart_template.live_template_post import live_template_post


@pytest.mark.skip(reason="删除已测")
def test_1(db):
    resp = live_template_post("默认分组智能直播模板", 6612, 11, host, headers)
    template_id = resp.json()["data"]["id"]

    res_del = live_template_delete(template_id, host, headers)
    assert res_del.status_code == 200
    assert resp.json()["code"] == 0

    # assert resp.status_code == 200
    # assert resp.json().get("code") == 0


# 模板已被删除,模板根本不存在
@pytest.mark.parametrize("template_id", [97, 100000])
def test_2(template_id):
    resp = live_template_delete(template_id, host, headers)
    assert resp.status_code == 500
    assert resp.json()["code"] == 500
    assert resp.json()["msg"] == "The bean is null?"


@pytest.mark.parametrize("template_id", ["A", "a", "汉字", "$"])
def test_3(template_id):
    resp = live_template_delete(template_id, host, headers)
    assert resp.status_code == 400
    assert resp.json()["code"] == 400
    assert resp.json()["msg"] == "参数类型错误"
