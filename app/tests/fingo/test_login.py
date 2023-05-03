# import time

# from pages.fingo.login import Login
# from ..base import FingoBase
# # from ...pages.fingo.login import Login
# # from ...pages

# import requests


# class TestSginin(FingoBase):
#     def test_1_signin(self):
#         email_signin = Login(self.driver)
#         email_signin.get_login_page()
#         email_signin.send_keys_email()
#         email_signin.send_keys_password()
#         email_signin.click(email_signin.login_btn)
#         # r = requests.get(self.driver.current_url)
#         # print(r.headers)
#         # print(r.cookies)
#         time.sleep(2)
#         self.assertEqual(self.driver.current_url, Login.main_url)
#         print("login successful")