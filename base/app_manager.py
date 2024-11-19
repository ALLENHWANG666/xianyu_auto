from appium.webdriver.common.appiumby import AppiumBy

class AppManager:
    def __init__(self, driver):
        self.driver = driver
        self.privacy_popup_accept_button = (AppiumBy.ID, "com.example:id/accept_privacy")
        self.login_popup_close_button = (AppiumBy.ID, "com.taobao.idlefish:id/ali_user_guide_close_layout")

    def start_app(self):
        """
        启动应用后处理常见的弹窗和启动逻辑。
        """
        self.handle_privacy_popup()
        self.handle_login_popup()
        # 如果有其他的启动相关逻辑可以在这里添加
        print("应用启动后的处理完成。")

    def handle_privacy_popup(self):
        """
        判断隐私弹窗是否出现，如果出现则点击同意按钮。
        """
        try:
            if self.is_element_present(self.privacy_popup_accept_button):
                self.driver.find_element(*self.privacy_popup_accept_button).click()
                print("隐私弹窗已处理。")
            else:
                print("隐私弹窗未出现。")
        except Exception as e:
            print(f"处理隐私弹窗时出错: {e}")

    def handle_login_popup(self):
        """
        判断登录弹窗是否出现，如果出现则点击关闭按钮。
        """
        try:
            if self.is_element_present(self.login_popup_close_button):
                self.driver.find_element(*self.login_popup_close_button).click()
                print("登录弹窗已关闭。")
            else:
                print("登录弹窗未出现。")
        except Exception as e:
            print(f"处理登录弹窗时出错: {e}")

    def is_element_present(self, locator, timeout=5):
        """
        判断元素是否存在。
        """
        try:
            self.wait_for_element(locator, timeout)
            return True
        except:
            return False

    def wait_for_element(self, locator, timeout=10):
        """
        等待元素出现的通用方法。
        """
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))