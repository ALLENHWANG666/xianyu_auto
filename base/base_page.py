import re
from time import sleep
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from data.page import elements
from data.page.elements import MARKET_BACK_BUTTON_XPATH


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def perform_search(self, search_name):
        try:
            # 点击搜索背景元素
            search_bg_element = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((AppiumBy.ID, elements.SEARCH_BG_IMG_FRONT_ID))
            )
            search_bg_element.click()

            # 等待输入框出现，并确认可以输入
            search_input_element = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((AppiumBy.CLASS_NAME, elements.SEARCH_INPUT_XPATH))
            )

            # 清除旧的内容，并输入新的搜索词
            search_input_element.click()  # 先点击输入框再进行清空和输入
            search_input_element.clear()  # 清空已有的内容
            search_input_element.send_keys(search_name)

            # 点击搜索按钮
            search_button_element = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, elements.SEARCH_BUTTON_XPATH))
            )
            search_button_element.click()
            print(f"搜索关键词 '{search_name}' 成功。")

        except TimeoutException:
            print("搜索操作超时，页面加载缓慢或未找到搜索框元素。")
            self.driver.quit()
        except NoSuchElementException:
            print("搜索框或搜索按钮未找到，搜索操作失败。")
            self.driver.quit()



    def click_market_button(self):
        try:
            market_button_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, elements.MARKET_BUTTON_XPATH))
            )
            market_button_element.click()
            print("行情按钮已点击。")
        except NoSuchElementException:
            print("行情按钮未出现。")
            self.driver.quit()

    def wait_for_market_page_loaded(self):
        try:
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((AppiumBy.XPATH, elements.MARKET_PAGE_LOADED_XPATH))
            )
            print("市场页面加载完成，找到成交记录元素。")
        except TimeoutException:
            print("未找到成交记录元素，市场页面可能没有成功加载。")
            self.driver.quit()

    def scroll_to_bottom(self, max_scrolls=5):
        for scroll_attempt in range(max_scrolls):
            initial_page_source = self.driver.page_source
            scroll_args = {
                "left": 100,
                "top": 800,
                "width": 800,
                "height": 1000,
                "direction": "down",
                "percent": 1.0
            }
            try:
                self.driver.execute_script("mobile: scrollGesture", scroll_args)
            except TimeoutException:
                print(f"第 {scroll_attempt + 1} 次滑动失败。")
            new_page_source = self.driver.page_source
            if initial_page_source == new_page_source:
                print("已滑动到底部。")
                break
        else:
            print("已达到最大滑动次数，可能未完全滑动到底部。")

    def find_all_price_elements(self):
        page_source = self.driver.page_source
        matches = re.finditer(elements.PRICE_ELEMENT_PATTERN, page_source)
        elements_xpaths = []
        for index, match in enumerate(matches, start=1):
            xpath = f"(//android.view.View[@content-desc='{match.group(0).split('\"')[1]}'])[{index}]"
            elements_xpaths.append(xpath)
        return elements_xpaths

    def click_element_by_xpath(self, element_xpath):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, element_xpath))
            )
            element.click()
        except NoSuchElementException:
            print(f"未找到元素：{element_xpath}，点击失败。")

    def extract_current_price(self):
        try:
            current_price_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, elements.CURRENT_PRICE_UIAUTOMATOR))
            )
            current_price_text = current_price_element.get_attribute("content-desc")
            cleaned_text = current_price_text.replace("\n", "").replace("\r", "").strip()
            print(f"现价完整信息（去除换行符后）: {cleaned_text}")
            price_match = re.search(r"现价(\d+)", cleaned_text)
            if price_match:
                current_price = price_match.group(1)
                print(f"现价金额: {current_price}")
            else:
                print("未找到现价金额。")
        except NoSuchElementException:
            print("未找到现价元素。")

    def extract_product_description(self):
        try:
            parent_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, elements.PRODUCT_DESCRIPTION_PARENT_XPATH))
            )
            target_elements = parent_element.find_elements(AppiumBy.CLASS_NAME, "android.view.View")
            content_desc_list = []
            for child in target_elements:
                content_desc = child.get_attribute("content-desc")
                if content_desc and content_desc.strip() and content_desc.lower() != "null":
                    content_desc_list.append(content_desc)
            combined_content_desc = ''.join(content_desc_list).replace('\n', '')
            return combined_content_desc
        except NoSuchElementException:
            print("无法找到符合条件的子元素。")
            return ""

    def click_back_button(self):
        try:
            back_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, elements.BACK_BUTTON_XPATH))
            )
            back_button.click()
        except NoSuchElementException:
            print("未找到返回按钮，点击失败。")

    def iterate_price_elements(self):
        elements_xpaths = self.find_all_price_elements()
        print(f"找到的成交价元素数量: {len(elements_xpaths)}")
        for i, element_xpath in enumerate(elements_xpaths):
            try:
                self.click_element_by_xpath(element_xpath)
                print(f"点击了第 {i + 1} 个成交价元素，XPath: {element_xpath}")
                self.extract_current_price()
                combined_content_desc = self.extract_product_description()
                print("拼接后的完整文本内容：", combined_content_desc)
                self.click_back_button()
                print("返回到行情页面。")
            except NoSuchElementException as e:
                print(f"在处理第 {i + 1} 个成交价元素时出错：{str(e)}")
                break



    def click_back_to_home(self):
        """
        点击两次返回按钮，以返回到首页并清除搜索词
        """
        for i in range(2):
            back_button_element = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((AppiumBy.XPATH, MARKET_BACK_BUTTON_XPATH))
            )
            back_button_element.click()
            print(f"第 {i + 1} 次点击返回按钮成功。")
            sleep(2)  # 等待页面切换