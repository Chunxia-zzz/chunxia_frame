# encoding:UTF-8

"""
author: yx
update at: 2021/10/26
info:依据模板组id查询当前组内所有模板
"""

import os

import allure
import pytest

from common.env_config import host, headers
from common.mysql_config import db_study_center
from Common.RootDirectory import root_path
from api.smart_template.live_template_get import live_template_get


@allure.description('查询默认模板组所有智能直播模板')
def test_1(db):
    resp = live_template_get(11, host, headers)

    cursor = db_study_center.cursor()
    cursor.execute(
        "SELECT COUNT(*) FROM content_template WHERE shop_id = 10016 AND template_bank_id = 11 AND is_deleted = 0")
    values = cursor.fetchall()

    assert resp.status_code == 200
    assert resp.json()['code'] == 0
    assert resp.json()["data"]["total"] == values[0][0]


@allure.description('测试异常参数类型是否正常报错')
@pytest.mark.parametrize("template_bank_id", ["A", "a", "汉字", "$"])
def test_2(template_bank_id):
    resp = live_template_get(template_bank_id, host, headers)
    assert resp.status_code == 400
    assert resp.json()["code"] == 400
    assert resp.json()["msg"] == "参数类型错误"


if __name__ == '__main__':
    test_data = root_path + '/testreport/report_data'  # 用例执行结果数据目录
    test_report = root_path + '/testreport/report'  # 测试报告目录

    pytest_params = ['-s', '-q', '--alluredir', test_data, '--clean-alluredir']  # pytest参数

    pytest.main(pytest_params)  # 执行测试

    os.system('allure generate {} -o {} --clean'.format(test_data, test_report))  # 生成报告
