# encoding:UTF-8

"""
author: yx
update at: 2021/11/4
info:测试新建智能直播模板接口
"""

import pytest

from Common.EnvConfig import host, headers
from Common.MysqlConfig import db_study_center
from api.SmartTemplate.live_template_delete import live_template_delete
from api.SmartTemplate.live_template_post import live_template_post


def test_1():
    resp = live_template_post("默认分组智能直播模板", 6612, 11, host, headers)

    cursor = db_study_center.cursor()
    cursor.execute("SELECT * FROM content_template WHERE name = '默认分组智能直播模板' AND template_bank_id = 11 AND"
                   " shop_id = 10016 AND is_deleted = 0")
    values = cursor.fetchall()
    assert len(values) >= 1
    assert values[0][4] == 6612

    template_id = resp.json()["data"]["id"]

    res_del = live_template_delete(template_id, host, headers)
    assert res_del.status_code == 200
    assert resp.json()["code"] == 0


# 回放模板不可用，回放模板不存在
@pytest.mark.parametrize("playback_id", [6099, 1000000])
def test_3(playback_id):
    resp = live_template_post("自动默认分组创建智能直播模板", playback_id, 11, host, headers)
    assert resp.status_code == 500
    assert resp.json()["code"] == 500
