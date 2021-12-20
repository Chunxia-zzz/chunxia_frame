# encoding:UTF-8

"""
Author: yx
Update at: 2021/11/30
Info: 脱敏处理
"""

import requests


shop_code_collection = {"stage": "xxx",
                        "uat": "xxx",
                        "prod": "xxx"}

host_collection = {"stage": "xxx",
                   "uat": "xxx",
                   "prod": "xxx"}

account_collection = {"stage": {"user": "xxx", "passwd": "xxx"},
                      "uat": {"user": "xxx", "passwd": "xxx"},
                      "prod": {"user": "xxx", "passwd": "xxx"}}

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
