from appium.webdriver.common.mobileby import MobileBy
from po_ecovacs.basepage import BasePage
from po_ecovacs.ecovacs_page.add_robot_page import AddRobot


class AddAccount(BasePage):

    def add_username_pwd(self, username, pwd):
        """
        填写用户名和密码
        :return:
        """
        self.find_send(MobileBy.XPATH, '//*[@text="手机号"]', username)
        self.find_send(MobileBy.ID, "com.eco.global.app:id/edit_password", pwd)
        self.find_and_click(MobileBy.ID, "com.eco.global.app:id/btn_login")
        return AddRobot(self.driver)
