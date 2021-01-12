from po_ecovacs.ecovacs_page.app_config import AppConfig


# class TestEcovacs:
#     def setup(self):
#         self.app = AppConfig()
#         self.main = self.app.start_app().goto_login_type_page()
#
#     def test_login(self):
#         self.main.first_page().\
#             choose_login_type('phone_num').\
#             add_username_pwd('15190019467', '123456')
#
#     def teardown(self):
#         self.app.stop_app()
#
# print(__name__)
# if __name__ == '__main__':
#     test1 = TestEcovacs()
#     test1.setup()
#     test1.teardown()


app = AppConfig()
app.start_app().goto_login_type_page().\
    first_page().choose_phone_login().\
    add_username_pwd('15190019467', '123456').add_robot().search_robot('T9')
