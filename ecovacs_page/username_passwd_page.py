from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from po_ecovacs.ecovacs_page.search_rebot_page import SearchRobot
from appium.webdriver.webdriver import WebDriver


class AddAccount:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver
        print("进入用户名&密码登陆界面")

    def add_username_pwd(self, username, pwd):
        """
        填写用户名和密码
        :return:
        """
        # username_ele = (MobileBy, '//*[@text, "手机号"]')
        # pwd_ele = (MobileBy.ID, "com.eco.global.app:id/edit_password")

        # WebDriverWait(self.driver, 10).until(expected_conditions.text_to_be_present_in_element(username_ele, '手机号'))
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手机号"]').send_keys(username)
        # self.driver.find_element(pwd_ele).send_keys(pwd)
        self.driver.find_element_by_id("com.eco.global.app:id/edit_password").send_keys(pwd)
        self.driver.find_element_by_id("com.eco.global.app:id/btn_login").click()
        return SearchRobot(self.driver)
