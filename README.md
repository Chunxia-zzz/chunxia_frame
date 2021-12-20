# AutotestFrame-From Chunxia

#### 介绍
这是春夏原创的自动化框架，使用了时下最流行的开源测试框架与各种测试组件。与业务深度结合，简单易用，轻松将中台里自己负责的模块自动化起来。目前已经在落地使用！

框架设计遵循如下核心思想：

- 测试用例（testcase）应该是完整且独立的，每条测试用例应该是都可以独立运行的

- 测试用例是测试步骤（teststep）的 `有序` 集合，每一个测试步骤对应一个 API 的请求描述

- 测试用例集（testsuite）是测试用例的 `无序` 集合，集合中的测试用例应该都是相互独立，不存在先后依赖关系的；如果确实存在先后依赖关系，那就需要在测试用例中完成依赖的处理



使用技术栈：python + pytest + requests + pymysql + allure



#### 解决的痛点

- postman与jmeter无法团队协作的问题
- 普通脚本可读性差，维护成本高
- 很难处理setup和teardown操作
- 数据驱动测试难
- 无法校验数据库数据
- 测试结果无法直观的体现出来




#### 框架架构与层级说明

1、common文件夹

**公共逻辑编写**：将不同的测试环境以及测试环境对应的店铺、测试账号集成在一个文件里面。通过改变变量的值，来实现测试环境的切换



2、api文件夹

**API定义**：使用独立的文件对接口描述进行存储，即每个文件对应一个接口描述，相同功能模块存放在一个文件夹里，便于管理。

接口定义描述的主要内容包括：**name**、variables、**request**、host、headers 等。在框架中，每个接口定义必须拥有host、headers两个参数。host用于域名的指定，headers用于不同测试环境的请求头（token鉴权）指定。

另外，API 描述需要尽量保持完整，做到可以单独运行。如果在接口描述中存在变量引用的情况，可在 variables 中对参数进行定义。通过这种方式，可以很好地实现单个接口的调试。



3、test_case文件夹

作为一个大的testsuite,存放测试用例。一个接口的测试用例可以这样编写

1. 引用已经定义好的公共逻辑和接口定义
2. 测试步骤直接使用api定义发起请求
3. 断言结果
4. 对接口输入参数作数据驱动测试



4、test_data文件夹

此文件夹只存放了用例需要的死水数据，通过data_config切换测试环境，通过字典来取值。



5、test_report文件夹

report文件夹存放了具体的测试报告

report_data文件夹存放了具体的测试数据，很多json文件

生成报告具体实现方式为：

1. 定义测试结果存放位置，root_path为项目根路径
2. 定义测试报告存放位置
3. 定义pytest运行参数
4. 使用pytest运行用例
5. os写入数据



每次运行完成后，打开report文件夹中的index.html文件，就可以查看这次运行的结果了



#### 如何使用

1.  clone本仓库
2.  在api文件夹里创建自己负责模块的api接口定义
3.  开始写测试用例，每一条用例都要import一下commom文件夹的公共逻辑以及需要用到的接口
4.  在具体的test_case文件里，直接调用api定义发送请求，然后对结果断言
5.  生成测试报告



#### 简单示例

测试接口：live_template_get

接口功能：根据模板组id查询当前组内所有智能直播模板

Step1：接口定义

```python
import requests


def live_template_get(template_bank_id, host, headers):
    path = "/study-center/admin/api/v1/live_template"
    url = host + path

    params = {"limit": 9999,
              "offset": 0,
              "template_bank_id": template_bank_id
              }

    resp = requests.get(url=url, params=params, headers=headers)
    return resp

```

Step2：测试用例，数据驱动测试，连接数据库断言，测试报告生成

```python
import os

import allure
import pytest

from common.env_config import host, headers
from common.root_directory import root_path
from api.smart_template.live_template_get import live_template_get


@allure.description('查询默认模板组所有智能直播模板')
def test_1(study_center):
    resp = live_template_get(11, host, headers)

    cursor = study_center.cursor()
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

```

