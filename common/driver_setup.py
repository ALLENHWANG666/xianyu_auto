from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.common import AppiumOptions


def get_driver():

    options = AppiumOptions()
    options.set_capability('platformName', 'Android')
    options.set_capability('platformVersion', '12')
    options.set_capability('appPackage', 'com.taobao.idlefish')
    options.set_capability('appActivity', 'com.taobao.idlefish.maincontainer.activity.MainActivity')
    options.set_capability('automationName', 'UiAutomator2')
    options.set_capability('noReset', True)



    driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
    return driver