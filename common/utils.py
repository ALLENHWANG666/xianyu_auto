import re
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# 封装搜索功能
def perform_search(driver, search_term):
    try:
        # 点击搜索入口
        search_entry_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.EditText[@content-desc='请输入搜索内容']"))
        )
        search_entry_element.click()

        # 输入搜索词
        search_entry_element.send_keys(search_term)
        print(f"输入了搜索词：{search_term}")

        # 点击搜索按钮
        search_button_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, "//android.view.View[@content-desc='搜索']"))
        )
        search_button_element.click()
        print("搜索按钮已点击。")
    except NoSuchElementException:
        print("无法找到搜索入口或搜索按钮，搜索失败。")
        driver.quit()

# 封装滚动操作
def scroll_down(driver, scroll_args):
    try:
        driver.execute_script("mobile: scrollGesture", scroll_args)
        print("页面已下滑。")
    except Exception as e:
        print(f"下滑页面时出现错误：{e}")

# 查找成交价元素
def find_deal_elements(driver):
    # 获取页面源代码
    page_source = driver.page_source
    # 使用正则表达式查找所有包含 "成交价" 的元素
    matches = re.finditer(r'content-desc="成.*?交.*?价.*?"', page_source)
    elements_xpaths = []
    # 遍历匹配的结果，存储 XPath
    for index, match in enumerate(matches, start=1):
        xpath = f"(//android.view.View[@content-desc='{match.group(0).split('\"')[1]}'])[{index}]"
        elements_xpaths.append(xpath)
    return elements_xpaths

# 封装返回操作
def go_back(driver):
    try:
        back_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, "//android.view.View[@content-desc='返回']"))
        )
        back_button.click()
        print("返回按钮已点击。")
    except NoSuchElementException:
        print("未找到返回按钮。")
