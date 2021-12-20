# encoding:UTF-8

"""
author: yx
update at: 2021/10/21
info: 测试数据环境配置
"""

config = {
    "stage": "stage",
    "uat": "uat",
    "prod": "prod"
}

test_env = "uat"


class DataConfig:
    env = config[test_env]


data_env = DataConfig.env
