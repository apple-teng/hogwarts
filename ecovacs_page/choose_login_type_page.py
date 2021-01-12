from selenium.webdriver.support.wait import WebDriverWait

from po_ecovacs.black_handle import black_wrapper_click
from po_ecovacs.ecovacs_page.username_passwd_page import AddAccount


class ChooseLoginType:
    def __init__(self, driver):
        self.driver = driver

    @black_wrapper_click
    def choose_login_type(self, login_type):
        """
        在弹出的登陆方式中选择
        :param login_type:选择登陆方式，有[phone_num, ecovacs_id, wechat_id]
        :return:
        """
        try:
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id("com.eco.global.app:id/cancelBtn"))
            if login_type == 'phone_num':
                self.driver.find_element_by_id("com.eco.global.app:id/method1Btn").click()
            elif login_type == "ecovacs_id":
                self.driver.find_element_by_link_text("科沃斯ID、密码登录")
            elif login_type == "wechat_id":
                self.driver.find_element_by_xpath("//*[contains(@text,'微信登录']")
            else:
                assert '登陆方式内容写错，参数内容为phone_num, ecovacs_id, wechat_id'
            return AddAccount(self.driver)
        except Exception as e:
            assert '点击切换登陆，没有找到弹出的登陆方式选择元素'