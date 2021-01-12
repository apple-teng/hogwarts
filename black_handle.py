from appium.webdriver.common.mobileby import MobileBy

from appium.webdriver.webdriver import WebDriver


class BlackList:
    def __init__(self):
        self.black_list = [(MobileBy.ID, 'com.eco.global.app:id/agreement_content'),
                           (MobileBy.XPATH, '//*[contains(@text,"下一步")]')]  # 同意/下一步

    # 装饰器
    def black_wrapper_click(self, fun):

        def run(*args, **kwargs):
            basedriver = args[0]
            try:
                return fun(*args, **kwargs)
            except Exception as e:
                for black in self.black_list:
                    print(f"本次使用的元素为{black}")
                    eles = basedriver.find_elements(*black)
                    if len(eles) > 0:
                        eles[0].click()
                        return fun(*args, **kwargs)
                raise e
        return run

