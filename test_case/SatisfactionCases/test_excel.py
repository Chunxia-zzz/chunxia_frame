# encoding:UTF-8

"""
author: yx
update at: 2021/10/22
info:导出满意度excel,IO读写
"""

from Common.EnvConfig import host, headers
from api.Satisfaction.excel import excel


def test_1():
    resp = excel(7133, host, headers)
    print(resp.text)

    assert resp.status_code == 200  # content-type: application/vnd.ms-excel;charset=utf-8 浏览器响应标头是这个，可以将返回的乱码转换成excel文件
    with open("content_Satisfaction.xlsx", "wb") as f:
        f.write(resp.content)
