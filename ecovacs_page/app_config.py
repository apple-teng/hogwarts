from appium import webdriver
from po_ecovacs.ecovacs_page.login_type_page import LoginType
from appium.webdriver.webdriver import WebDriver
from po_ecovacs.basepage import BasePage


class AppConfig(BasePage):

    def start_app(self):
        if self.driver is None:
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "127.0.0.1:21503"
            caps["appPackage"] = "com.eco.global.app"
            caps["appActivity"] = "com.eco.account.activity.login.domestic.EcoQuickLoginActivity"
            # caps["noReset"] = "true"
            caps["ensureWebviewsHavePages"] = True
            # 设置页面等待空闲状态的时间
            caps['settings[waitForIdleTimeout]'] = 0
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            self.driver.launch_app()
        # 操作，在 10 内，每 0.5 s 查找一次元素
        self.driver.implicitly_wait(10)
        return self
        # return LoginType(self.driver)

    def stop_app(self):
        self.driver.quit()

    def goto_login_type_page(self):
        return LoginType(self.driver)


# if __name__ == '__main__':
#     app = AppConfig()
#     app.start_app().first_page()


