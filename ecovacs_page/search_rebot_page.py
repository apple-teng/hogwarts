from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

import time
from po_ecovacs.basepage import BasePage


class SearchRobot(BasePage):

    def click_popmsg(self):
        # print(self.driver.page_source)
        time.sleep(2)
        while True:
            if "下一步" in self.driver.page_source:
                self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"下一步")]').click()
                print("点掉引导页”下一步“")
                # time.sleep(2)
                WebDriverWait(self.driver, 10).until(lambda x: "知道了" in x.page_source)
            elif "知道了" in self.driver.page_source:
                self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"知道了")]').click()
                print("点掉引导页”知道了“")
            else:
                print("添加机器人页面,当前页面没有引导页了")
                break

    def search_robot(self, robot_type):
        """
        1.在搜索框中填写机型
        2.点击搜索
        3.选中搜索结果
        :param robot_type:
        :return:
        """
        self.find_and_click(MobileBy.ID, 'com.eco.global.app:id/search_edit')
        # self.driver.find_element_by_id('com.eco.global.app:id/search_edit').click()
        self.find_send(MobileBy.ID, "com.eco.global.app:id/edit_search", robot_type)
        # self.driver.find_element_by_id("com.eco.global.app:id/edit_search").send_keys(robot_type)
        print(self.driver.find_element_by_xpath(f"//*[@text='{robot_type}']"))
        self.driver.find_element_by_xpath(f"//*[@text='{robot_type}']").click()

        # return ConnectWifi(self.driver)

