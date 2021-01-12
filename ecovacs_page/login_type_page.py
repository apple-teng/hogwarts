from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from po_ecovacs.ecovacs_page.choose_login_type_page import ChooseLoginType
from appium.webdriver.webdriver import WebDriver


class LoginType:
    def __init__(self, driver: WebDriver = None):
        """
        初始化driver
        :param driver:
        """
        self.driver = driver

    # def private_popmsg(self):
        # agree_button = (MobileBy.ID, "com.eco.global.app:id/agreement_agree")
        # WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(agree_button))
        # self.drive.find_element(*agree_button).click()
        # # self.driver.find_element_by_id('com.eco.global.app:id/agreement_agree')

    def first_page(self):
        """
        打开app后的首页，选择其他登陆方式
        :return:
        """
        print("进入login page")
        agree_button = (MobileBy.ID, "com.eco.global.app:id/btn_change_login")
        try:
            WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(agree_button))
            self.driver.find_element(*agree_button).click()
            return ChooseLoginType(self.driver)
        except Exception as e:
            print("没有弹出用户协议")
            return False


