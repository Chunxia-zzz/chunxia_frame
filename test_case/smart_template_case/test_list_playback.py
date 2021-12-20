# encoding:UTF-8

"""
author: yx
update at: 2021/10/15
info:测试查询回放接口
"""

import os

import allure
import pytest

from common.env_config import host, headers
from common.mysql_config import db_study_center
from common.root_directory import root_path
from api.smart_template.list_playback import list_playback


@allure.description('验证回放列表取最近200条数据')
def test_list_playback(db):
    resp = list_playback(host, headers)

    # cursor = db_study_center.cursor()
    # cursor.execute("SELECT * FROM content_template WHERE name = '默认分组智能直播模板' AND template_bank_id = 11 AND"
    #                " shop_id = 10016 AND is_deleted = 0")  # 测试数据库连接
    # values = cursor.fetchall()

    assert resp.status_code == 200
    assert resp.json()['code'] == 0
    assert resp.json()["data"]["total"] == 200


if __name__ == '__main__':
    test_data = root_path + '/testreport/report_data'
    test_report = root_path + '/testreport/report'

    pytest_params = ['-s', '-q', '--alluredir', test_data, '--clean-alluredir']

    pytest.main(pytest_params)

    os.system('allure generate {} -o {} --clean'.format(test_data, test_report))
