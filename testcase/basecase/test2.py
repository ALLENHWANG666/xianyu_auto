"""
@FileName       :test2.py
@Author         : ALLENHWANG
@CreateTime     : 02:09
@Description    :
"""

from time import sleep
import setup_env
from common.driver_setup import get_driver
from base.app_manager import AppManager

# 在执行测试用例前进行环境检查和初始化
setup_env.setup_environment()

# 获取 driver 实例
driver = get_driver()

# 创建 AppManager 实例并处理应用启动后的操作
app_manager = AppManager(driver)
app_manager.start_app()


sleep(5)


