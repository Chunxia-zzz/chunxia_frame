# encoding:UTF-8

"""
author: yx
update at: 2021/10/26
info:测试更改模板分组名称
"""

import os

import allure
import pytest

# from Common.EnvConfig_copy import host, headers
from common.env_config import host, headers
from common.mysql_config import db_study_center
from Common.RootDirectory import root_path
from api.smart_template.smart_live_template_bank_put import smart_live_template_bank_put


@allure.description('更新模板组名称')
def test_1():
    resp = smart_live_template_bank_put(34, "更新模板组名称", host, headers)

    cursor = db_study_center.cursor()
    cursor.execute("SELECT name FROM smart_live_template_bank WHERE shop_id = 10016 AND id = 34 ")
    values = cursor.fetchall()

    assert resp.status_code == 200
    assert resp.json()["code"] == 0
    assert resp.json()["msg"] == "ok"
    assert values[0][0] == "更新模板组名称"


@allure.description('测试模板组不存在更改名称失败')
def test_2():
    resp = smart_live_template_bank_put(100000, "测试更改不存在的模板组名称", host, headers)
    assert resp.status_code == 200
    assert resp.json()["code"] == 1001
    assert resp.json()["msg"] == "该小组不存在！"


@allure.description('测试异常参数类型是否正常报错')
@pytest.mark.parametrize("template_bank_id", ["A", "a", "汉字", "$"])
def test_3(template_bank_id):
    resp = smart_live_template_bank_put(template_bank_id, "测试更改不存在的模板组名称", host, headers)
    assert resp.status_code == 422
    assert resp.json()["code"] == 422
    assert resp.json()["msg"] == "Invalid_Http_Request_Body"


if __name__ == '__main__':
    test_data = root_path + '/testreport/report_data'
    test_report = root_path + '/testreport/report'

    pytest_params = ['-s', '-q', '--alluredir', test_data, '--clean-alluredir']

    pytest.main(pytest_params)

    os.system('allure generate {} -o {} --clean'.format(test_data, test_report))
