# elements.py

# 搜索页面元素
SEARCH_BG_IMG_FRONT_ID = "com.taobao.idlefish:id/search_bg_img_front"
SEARCH_INPUT_XPATH = "android.widget.EditText"
SEARCH_BUTTON_XPATH = "//android.view.View[@content-desc='搜索']"

# 行情页面元素
MARKET_BUTTON_XPATH = "//android.view.View[@content-desc='行情']"
MARKET_PAGE_LOADED_XPATH = "//android.view.View[@content-desc='成交记录']"

# 滑动页面元素
PRICE_ELEMENT_PATTERN = r'content-desc="成.*?交.*?价.*?"'

# 商品详情页面元素
CURRENT_PRICE_UIAUTOMATOR = 'new UiSelector().descriptionContains("现价")'
PRODUCT_DESCRIPTION_PARENT_XPATH = "//android.widget.ScrollView/android.view.View[2]"
BACK_BUTTON_XPATH = "//android.view.View[@content-desc='返回']"


# 行情页面的返回按钮，点击两次直接回到首页并清除搜索词
MARKET_BACK_BUTTON_XPATH = "//android.view.View[@content-desc='返回, 返回按钮']"