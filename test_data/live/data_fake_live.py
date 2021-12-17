# encoding:UTF-8

"""
author: yx
update at: 2021/10/21
info: 伪直播死水数据管理
"""
from test_data.data_config import data_env

test_env = data_env

fake_live_data = {"stage": {"object_id": 1429, "anchor_id": 123, "template_id": 306},
                  "uat": {"object_id": 755, "anchor_id": 150, "template_id": 63},
                  "prod": {"object_id": 1101, "anchor_id": 166, "template_id": 413}}


# class LiveDate(object):
#
#     @staticmethod
#     def fake_live_data(env):
#         global object_id, anchor_id, template_id
#         if env == "stage":
#             object_id = 1
#             anchor_id = 2
#             template_id = 3
#
#         if env == "uat":
#             object_id = 4
#             anchor_id = 25
#             template_id = 36
#
#         if env == "prod":
#             object_id = 40
#             anchor_id = 250
#             template_id = 365
#
#         return object_id, anchor_id, template_id
#
#     @staticmethod
#     def real_live_data(env):
#         global object_id, anchor_id, template_id
#         if env == "stage":
#             object_id = 1
#             anchor_id = 2
#             template_id = 3
#
#         if env == "uat":
#             object_id = 4
#             anchor_id = 25
#             template_id = 36
#
#         if env == "prod":
#             object_id = 40
#             anchor_id = 250
#             template_id = 365
#
#         return object_id, anchor_id, template_id
#
#
# object_id, anchor_id_fake, template_id = LiveDate.fake_live_data(test_env)
# anchor_id_real, question_id, content_id = LiveDate.real_live_data(test_env)
#
#
# if __name__ == '__main__':
#     pass
