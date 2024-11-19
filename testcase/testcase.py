
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait

import setup_env
from common.driver_setup import get_driver
from base.app_manager import AppManager
from common.data_handler import DataHandler
from base.base_page import BasePage

# 设置环境，启动模拟器和 Appium
setup_env.setup_environment()

# 获取 driver 实例
driver = get_driver()

# 创建 AppManager 实例并处理应用启动后的操作
app_manager = AppManager(driver)
app_manager.start_app()

# 读取商品名称
data_handler = DataHandler()
factory, search_name_1, search_name_2, search_name_3 = data_handler.read_first_item()
print(f"读取到的厂商: {factory}, 搜索词1: {search_name_1}, 搜索词2: {search_name_2}, 搜索词3: {search_name_3}")

# 创建 BasePage 实例
base_page = BasePage(driver)

# 定义搜索词列表
search_names = [search_name_1, search_name_2, search_name_3]

# 遍历搜索词
for search_name in search_names:
    if search_name is None:
        break

    print(f"正在使用关键词：{search_name}")

    # 执行搜索操作
    base_page.perform_search(search_name)

    # 点击行情按钮
    base_page.click_market_button()

    # 等待页面加载完成
    base_page.wait_for_market_page_loaded()

    # 滑动屏幕到底部
    base_page.scroll_to_bottom()

    # 查找并遍历成交价元素
    base_page.iterate_price_elements()


    # 返回到首页，清除搜索词
    base_page.click_back_to_home()




# 结束测试用例
print("所有搜索关键词已处理完毕，结束测试。")
driver.quit()
