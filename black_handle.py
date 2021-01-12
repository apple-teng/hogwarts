from appium.webdriver.common.mobileby import MobileBy

from appium.webdriver.webdriver import WebDriver


class BlackList:
    def __init__(self):
        self.black_list = [(MobileBy.ID, 'com.eco.global.app:id/agreement_content'),
                           (MobileBy.XPATH, '//*[contains(@text,"下一步")]')]  # 同意/下一步


# 初始化黑名单
BLACK_LIST = BlackList()


# 装饰器
def black_wrapper_click(fun):
    def run(*args, **kwargs):
        basedriver = args[0]
        try:
            return fun(*args, **kwargs)
        except Exception as e:
            for black in BLACK_LIST:
                eles = basedriver.find_elements(*black)
                if len(eles) > 0:
                    eles[0].click()
                    return fun(*args, **kwargs)
            raise e
    return run

