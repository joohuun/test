# from selenium.webdriver.common.by import By

# from config.fingo import (
#     fingo_base_url,
#     email,
#     password,
# )
# from ..base import Base


# class Login(Base):
#     main_url = fingo_base_url
#     signin_url = f"{fingo_base_url}signin"
#     email_input = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[2]/div[2]/input')
#     password_input = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[2]/div[3]/input')
#     login_btn = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[2]/div[4]/button')

#     def __init__(self, driver):
#         super(Login, self).__init__(driver)

#     def get_login_page(self):
#         self.get(self.signin_url)

#     def send_keys_email(self):
#         self.send_keys(self.email_input, email)

#     def send_keys_password(self):
#         self.send_keys(self.password_input, password)