# encoding:UTF-8

"""
Author: yx
Update at: 2021/10/21
info: 公共逻辑配置文件
branch:yx
"""

import requests


shop_code_collection = {"stage": "00001",
                        "uat": "nwb540fd11e8063c",
                        "prod": "nw00b13940a00004"}

host_collection = {"stage": "https://janus.stage.tenclass.com",
                   "uat": "https://janus-uat.tenclass.com",
                   "prod": "https://janus.tenclass.com"}

account_collection = {"stage": {"user": "ChunXia1@gmail.com", "passwd": "stage123"},
                      "uat": {"user": "putong@gmail.com", "passwd": 1},
                      "prod": {"user": "putong@gmail.com", "passwd": 1}}

test_env = "uat"


class EnvConfig(object):

    @staticmethod
    def login_config():
        path = "/bbg-crm/api/v1/admin_user.login"
        url = host_collection[test_env] + path

        data = {"user_email": account_collection[test_env]["user"],
                "user_password": account_collection[test_env]["passwd"]}

        res = requests.post(url=url, json=data).json()
        token = res["data"]["auth_token"]

        env_headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "authorization": token,
            "x-shop-code": shop_code_collection[test_env]}

        return host_collection[test_env], env_headers


host, headers = EnvConfig.login_config()

if __name__ == '__main__':
    pass
