项目 README

这是一个基于 Appium 的自动化测试项目，本文档将介绍项目结构以及各个文件夹的作用，方便日后查阅和维护。

目录结构

.
├── base                # 项目基础类
│   ├── __init__.py     # 标记为 Python 包
│   └── base_page.py    # 基础页面类，包含常用的页面操作方法
├── common              # 公共工具类
│   ├── __init__.py     # 标记为 Python 包
│   └── utils.py        # 工具类文件，存放公共函数
├── data                # 测试数据和报告
│   ├── page            # 页面数据，如元素定位信息
│   ├── report          # 测试报告存放目录
│   └── screen_shot     # 截图存放目录，记录测试过程中失败的截图
├── testcase            # 测试用例
│   ├── __init__.py     # 标记为 Python 包
│   ├── test.py         # 测试用例文件
│   └── test2.py        # 其他测试用例文件
├── config.py           # 配置文件，存放设备和应用的配置信息
└── pytest.ini          # pytest 配置文件，用于设置测试参数

目录说明

base：存放项目的基础类。base_page.py 是所有页面类的基类，包含了页面通用的方法（如查找元素、点击等）。

common：存放常用的工具类和公共方法。utils.py 中包含了各种常用的辅助函数，方便复用。

data：存放测试数据和报告。

page：用于存放页面的数据信息，比如页面元素的定位。

report：存放测试执行后的报告，帮助分析测试结果。

screen_shot：用于存放测试失败时的截图，便于调试。

testcase：存放具体的测试用例文件，包括对 App 各种功能的测试。

config.py：存放配置信息，比如设备信息、应用的参数设置等。

pytest.ini：pytest 的配置文件，用于设置日志级别、插件等信息。