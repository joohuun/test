from selenium.webdriver.common.by import By
from pages.base import Base

from config.fingo import (
    email, password, 
    new_password, 
    fingo_base_url
    )


class CustomerInfo(Base):
    main_url = fingo_base_url
    info_url = f"{fingo_base_url}info"
    signin_url = f"{fingo_base_url}signin"

    mypage_btn = (By.XPATH, '//*[@id="root"]/div[6]/button[5]')
    customer_info_btn = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]')
    check_password_input = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div[2]/div[2]/input')
    confirm_btn = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div[2]/div[3]/button')

    # 비밀번호 변경
    password_change_btn = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div[2]/div[5]/div[2]/div')
    origin_password_input = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div[1]/input')
    new_password_input = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div[3]/input')
    confirm_new_password_input = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div[5]/input')
    password_save_btn = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div[7]/button')
    confirm_alert_msg = (By.XPATH, '//*[@id="modal"]/div/div[2]/div[1]/div[1]/div')
    confirm_alert_btn = (By.XPATH, '//*[@id="modal"]/div/div[2]/div[2]/button')
    detail_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[1]/div[1]/div[3]/div/button')
    logount_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[1]/div[3]/div/div[4]/div[2]')
    # origin_password 로 다시 변경
    email_input = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[1]/div[5]/div[2]/input')
    password_input = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[1]/div[5]/div[3]/input')
    login_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[1]/div[5]/div[4]/button')


    def __init__(self, driver):
        super(CustomerInfo, self).__init__(driver)

    def get_main_page(self):
        self.get(self.main_url)

    def get_login_page(self):
        self.get(self.signin_url)

    def get_info_page(self):
        self.get(self.info_url)

    def send_keys_check_password(self):
        self.send_keys(self.check_password_input, password)

    def send_keys_origin_password(self):
        self.send_keys(self.origin_password_input, password)

    def send_keys_new_password(self):
        self.send_keys(self.new_password_input, new_password)

    def send_keys_confirm_new_password(self):
        self.send_keys(self.confirm_new_password_input, new_password)

    def send_keys_email(self):
        self.send_keys(self.email_input, email)

    def send_keys_password(self):
        self.send_keys(self.password_input, new_password)

    def send_keys_check_password2(self):
        self.send_keys(self.check_password_input, new_password)

    def send_keys_orgin_password2(self):
        self.send_keys(self.origin_password_input, new_password)

    def send_keys_new_password2(self):
        self.send_keys(self.new_password_input, password)

    def send_keys_confirm_new_password2(self):
        self.send_keys(self.confirm_new_password_input, password)


class Maketing(Base):
    info_url = f"{fingo_base_url}info"
    phone = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div[4]/div[2]/div[1]/button')
    email = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div[4]/div[2]/div[2]/button')
    push = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div[4]/div[2]/div[3]/button')
    save_btn = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div[5]/button')
    alert_save_success = (By.XPATH, '//*[@id="modal"]/div/div[2]/div[1]/div[2]')

    check_password_input = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div[2]/div[2]/input')
    confirm_btn = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div[2]/div[3]/button')


    def __init__(self, driver):
        super(Maketing, self).__init__(driver)

    def get_info_page(self):
        self.get(self.info_url)

    def send_keys_check_password(self):
        self.send_keys(self.check_password_input, password)