# encoding:UTF-8

"""
author: yx
update at: 2021/10/26
info: 查询当前店铺所有模板分组
"""

import os

import allure
import pytest

from common.env_config import host, headers
from common.mysql_config import db_study_center
from common.root_directory import root_path
from api.smart_template.page_list import page_list


@allure.description("查询当前店铺所有模板分组")
def test_page_list(db):
    resp = page_list(host, headers)

    cursor = db_study_center.cursor()
    cursor.execute("SELECT COUNT(*) FROM smart_live_template_bank WHERE shop_id = 10016")
    values = cursor.fetchall()

    assert resp.status_code == 200
    assert resp.json()["code"] == 0
    assert resp.json()["data"]["total"] == values[0][0]


if __name__ == '__main__':
    test_data = root_path + '/testreport/report_data'
    test_report = root_path + '/testreport/report'

    pytest_params = ['-s', '-q', '--alluredir', test_data, '--clean-alluredir']

    pytest.main(pytest_params)

    os.system('allure generate {} -o {} --clean'.format(test_data, test_report))
