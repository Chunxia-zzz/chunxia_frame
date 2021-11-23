# encoding:UTF-8

"""
author: yx
update at: 2021/10/26
info:测试新建智能直播模板组，然后连接数据库删除它
"""

import pytest

from Common.EnvConfig import host, headers
from Common.MysqlConfig import db_study_center
from api.SmartTemplate.smart_live_template_bank_post import smart_live_template_bank_post


def test_1(db):
    resp = smart_live_template_bank_post("自动创建直播模板", host, headers)
    assert resp.status_code == 200
    assert resp.json()["code"] == 0
    assert resp.json()["msg"] == "ok"

    # cursor = db_study_center.cursor()
    # cursor.execute("SELECT * FROM smart_live_template_bank WHERE shop_id = 10016 ORDER BY id DESC")
    # values = cursor.fetchall()
    # assert values[0][1] == "自动创建直播模板"


def test_2(db):
    cursor = db_study_center.cursor()
    cursor.execute("DELETE FROM smart_live_template_bank WHERE shop_id = 10016 AND name = '自动创建直播模板'  ")
    cursor.execute("COMMIT")

    cursor.execute("SELECT * FROM smart_live_template_bank WHERE shop_id = 10016 AND name = '自动创建直播模板'")
    values = cursor.fetchall()
    assert len(values) == 0


@pytest.mark.parametrize('name', [""])
def test_data(name):
    resp = smart_live_template_bank_post(name, host, headers)
    assert resp.status_code == 400
    assert resp.json().get("code") == 400
    assert resp.json().get("msg") == "分组名不能为空"


# 数据库字段限制varchar(50)
def test_3():
    resp = smart_live_template_bank_post(
        "超过字符长度超过字符长度超过字符长度超过字符长度超过字符长度超过字符长度超过字符长度超出字度超过字符长度超出度超过字符长度超出度超过字符长度"
        "超出度超过字符长度超出度超过字符长度超出度超过字符长度超出度超过字符长度超出度超过字符长度超出",
        host, headers)
    assert resp.status_code == 500
    assert resp.json()["code"] == 500
    assert resp.json()["msg"] == "Error[Data truncation: Data too long for column 'name' at row 1]"
