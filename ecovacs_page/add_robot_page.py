from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

import time
from po_ecovacs.basepage import BasePage
from po_ecovacs.ecovacs_page.search_rebot_page import SearchRobot


class AddRobot(BasePage):
    def add_robot(self):
        print("进入添加机器人页面")
        self.wait_for(MobileBy.XPATH, '//*[contain(@text,"设备列表空空如也"]')
        self.find_and_click(MobileBy.ID, "com.eco.global.app:id/btn_add_robot")
        return SearchRobot(self.driver)
