from appium.webdriver.common.mobileby import MobileBy

from po_ecovacs.ecovacs_page.choose_login_type_page import ChooseLoginType
from po_ecovacs.basepage import BasePage


class LoginType(BasePage):

    def first_page(self):
        """
        打开app后的首页，选择其他登陆方式
        :return:
        """
        print("进入login page")
        agree_button = (MobileBy.ID, "com.eco.global.app:id/btn_change_login")

        try:
            self.wait_for(*agree_button)
            self.find_and_click(*agree_button)
            return ChooseLoginType(self.driver)
        except Exception as e:
            print("没有弹出用户协议")
            return False
