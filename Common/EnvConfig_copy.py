# encoding:UTF-8

"""
Author: yx
Update at: 2021/11/30
info: 重写公共逻辑,脱敏处理
"""

import requests


class EnvConfig(object):

    def __init__(self, env_host, env_shop_code, env_user, env_passwd):
        self.env_host = env_host
        self.env_shop_code = env_shop_code
        self.env_user = env_user
        self.env_passwd = env_passwd

    def login_config(self):
        path = "/bbg-crm/api/v1/admin_user.login"
        url = self.env_host + path

        data = {"user_email": self.env_user,
                "user_password": self.env_passwd}

        res = requests.post(url=url, json=data).json()
        token = res["data"]["auth_token"]

        env_headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "authorization": token,
            "x-shop-code": self.env_shop_code}

        return self.env_host, env_headers


# 字典实现环境切换。key: 实例
test_env = {"stage": EnvConfig("xxx", "xxx", "xxx", "xxx").login_config(),
            "uat": EnvConfig("xxx", "xxx", "xxx","xxx").login_config(),
            "prod": EnvConfig("xxx", "xxx", "xxx", "xxx").login_config()}

host, headers = test_env["uat"]

# 函数实现环境切换
# def env(env_id):
#     if env_id == 1:
#         return EnvConfig("xxx", "xxx", "xxx", "xxx").login_config()
#     elif env_id == 2:
#         return EnvConfig("xxx", "xxx", "xxx", "xxx").login_config()
#     elif env_id == 3:
#         return EnvConfig("xxx", "xxx", "xxx", "xxx").login_config()
#
#
# host, headers = env(2)

if __name__ == '__main__':
    print(host, headers)
