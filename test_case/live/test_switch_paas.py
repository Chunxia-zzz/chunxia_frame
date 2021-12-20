# encoding:UTF-8

"""
author: 春夏
update at: 2021/10/29
info: 测试切换机器到paas平台
"""

import pytest

from Common.EnvConfig import host, headers
from api.live.switch_paas import switch_paas


@pytest.mark.parametrize("content_id", 15905)
def test_1(content_id):
    resp = switch_paas(content_id, host, headers).json()
    assert resp.status_code == 200
    assert resp.json()["code"] == 0
    assert resp.json()["msg"] == "ok"
    assert resp.json()["data"] == "true"
