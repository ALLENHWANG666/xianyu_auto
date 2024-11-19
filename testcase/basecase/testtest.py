"""
@FileName       : testtest.py
@Author         : ALLENHWANG
@CreateTime     : 2024/11/13 15:23
@Description    : 
"""



from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.interaction import Interaction
import time
from appium.webdriver.common.appiumby import AppiumBy

import re
import time

from base.app_manager import AppManager
from common.driver_setup import get_driver

# 获取 driver 实例
driver = get_driver()

# 创建 AppManager 实例并处理应用启动后的操作
# app_manager = AppManager(driver)
# app_manager.start_app()




#
# # 使用 mobile: scrollGesture 执行滑动操作
# args = {
#     "left": 0,    # 滑动起点相对于屏幕左边的偏移量
#     "top": 800,   # 滑动起点相对于屏幕顶部的偏移量
#     "width": 1080,  # 滑动区域的宽度
#     "height": 1500, # 滑动区域的高度
#     "direction": "down",  # 滑动方向: down/up/left/right
#     "percent": 0.75  # 滑动的距离百分比
# }
#
# driver.execute_script("mobile: scrollGesture", args)
#
# # 停留 5 秒钟，方便查看效果
# time.sleep(5)



# 查找所有成交价元素的 XPath 并存储在列表中
page_source = driver.page_source
matches = re.finditer(r'content-desc="成.*?交.*?价.*?"', page_source)
elements_xpaths = []
for index, match in enumerate(matches, start=1):
    xpath = f"(//android.view.View[@content-desc='{match.group(0).split('"')[1]}'])[{index}]"
    elements_xpaths.append(xpath)

# 点击第二个元素
if len(elements_xpaths) >= 2:
    second_element_xpath = elements_xpaths[1]
    try:
        second_element = driver.find_element(AppiumBy.XPATH, second_element_xpath)
        second_element.click()
        print(f"成功点击元素：{second_element_xpath}")
    except NoSuchElementException:
        print(f"未找到元素：{second_element_xpath}，点击失败。")
else:
    print("未找到足够的成交价元素，无法点击第二个元素。")








# 所有操作完成后，退出
print("所有匹配的元素已完成点击操作")




