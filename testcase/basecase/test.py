from time import sleep
from appium.webdriver.common.appiumby import AppiumBy

import setup_env
from common.driver_setup import get_driver
from base.app_manager import AppManager
from common.data_handler import DataHandler
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# 在执行测试用例前进行环境检查和初始化
setup_env.setup_environment()

# 获取 driver 实例
driver = get_driver()

# 创建 AppManager 实例并处理应用启动后的操作
app_manager = AppManager(driver)
app_manager.start_app()

# 点击搜索入口元素
search_bg_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((AppiumBy.ID, "com.taobao.idlefish:id/search_bg_img_front"))
)
search_bg_element.click()

# 读取商品名称
data_handler = DataHandler()
factory, search_name_1, search_name_2, search_name_3 = data_handler.read_first_item()
print(f"读取到的厂商: {factory}, 搜索词1: {search_name_1}, 搜索词2: {search_name_2}, 搜索词3: {search_name_3}")

# 在搜索页面中输入商品名称
search_input_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.EditText"))
)
search_input_element.send_keys(search_name_1)

# 点击搜索按钮
search_button_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((AppiumBy.XPATH, "//android.view.View[@content-desc='搜索']"))
)
search_button_element.click()

# 判断页面中是否出现行情按钮
try:
    market_button_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((AppiumBy.XPATH, "//android.view.View[@content-desc='行情']"))
    )
    market_button_element.click()
    print("行情按钮已点击。")
except NoSuchElementException:
    # 如果行情按钮未出现，点击返回按钮
    print("行情按钮未出现，点击返回按钮。")
    back_button_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]"))
    )
    back_button_element.click()

    # 点击搜索框并将内容替换为下一个搜索词
    search_input_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.EditText[@text='hottoys凯恩']"))
    )
    search_input_element.clear()
    search_input_element.send_keys(search_name_2)

    # 再次点击搜索按钮
    search_button_element.click()



# 使用 mobile: scrollGesture 进行屏幕下滑操作
args = {
    "left": 500,
    "top": 1500,
    "width": 500,
    "height": 1000,
    "direction": "down",
    "percent": 1.0
}

driver.execute_script("mobile: scrollGesture", args)



# 尝试通过 UiSelector 组合 class 和 contentDescription 来定位元素
element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                              'new UiSelector().className("android.view.View").description("成交价")')





# # 爬取商品的近7日成交均价
# average_price_element = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((AppiumBy.ID, "com.example:id/average_price"))
# )
# average_price = average_price_element.text
# print(f"近7日成交均价: {average_price}")
#
# # 保存结果
# data_handler.save_report([{"商品名称": search_name_1, "近7日成交均价": average_price}])