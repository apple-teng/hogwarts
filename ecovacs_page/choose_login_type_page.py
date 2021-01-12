from appium.webdriver.common.mobileby import MobileBy

from po_ecovacs.basepage import BasePage
from po_ecovacs.ecovacs_page.username_passwd_page import AddAccount


class ChooseLoginType(BasePage):

    def choose_phone_login(self):
        self.find_and_click(MobileBy.ID, "com.eco.global.app:id/method1Btn")
        return AddAccount(self.driver)

    def choose_id_login(self):
        self.find_and_click(MobileBy.LINK_TEXT, "科沃斯ID、密码登录")
        return AddAccount(self.driver)

    def choose_wechat_login(self):
        self.find_and_click(MobileBy.XPATH, "//*[contains(@text,'微信登录']")
        return AddAccount(self.driver)


    # def choose_login_type(self, login_type):
    #     """
    #     在弹出的登陆方式中选择
    #     :param login_type:选择登陆方式，有[phone_num, ecovacs_id, wechat_id]
    #     :return:
    #     """
    #     cancel_ele = (MobileBy.ID, "com.eco.global.app:id/cancelBtn")
    #     try:
    #         WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id("com.eco.global.app:id/cancelBtn"))
    #         if login_type == 'phone_num':
    #             self.driver.find_element_by_id("com.eco.global.app:id/method1Btn").click()
    #         elif login_type == "ecovacs_id":
    #             self.driver.find_element_by_link_text("科沃斯ID、密码登录")
    #         elif login_type == "wechat_id":
    #             self.driver.find_element_by_xpath()
    #         else:
    #             assert '登陆方式内容写错，参数内容为phone_num, ecovacs_id, wechat_id'
    #         return AddAccount(self.driver)
    #     except Exception as e:
    #         assert '点击切换登陆，没有找到弹出的登陆方式选择元素'