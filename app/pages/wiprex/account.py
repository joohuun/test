from selenium.webdriver.common.by import By

from pages.base import Base
from config.account import email, password, resident_num, my_bank, account_num


class EmailSginIn(Base):
    signin_url = "https://qa.wiprex.com/signin"
    email = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[4]/div[2]/div[2]/input')
    password = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[4]/div[2]/div[3]/input')
    login_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[4]/div[2]/div[4]/button')

    def __init__(self, driver):
        super(EmailSginIn, self).__init__(driver)

    def get_page(self):
        self.get(self.signin_url)

    def send_keys_email_id(self):
        self.send_keys(self.email, email)

    def send_keys_email_pw(self):
        self.send_keys(self.password, password)



class ConfirmEamil(Base):
    signin_url = "https://qa.wiprex.com/signin"
    main_url = "https://qa.wiprex.com/"
    email = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[4]/div[2]/div[2]/input')
    password = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[4]/div[2]/div[3]/input')
    resident_num = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[4]/div[1]/div[2]/div[2]/div[2]/input')
    login_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[4]/div[2]/div[4]/button')
    detail_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[1]/div[2]/div/button/img')
    wallet_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[3]/div/div[3]/div[5]')
    deposit_withdraw_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[4]/div[1]/div/div[1]/div[2]/button')
    email_confirm_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[4]/div[1]/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/div[2]/button')
    email_confirm_status = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[4]/div[1]/div/div[2]/div/div[1]/div[2]/div[1]/button/div')
    check_resident_num_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[4]/div[1]/div[2]/div[3]/div/button')
    verification_completed_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[4]/div[1]/div[2]/button')

    def __init__(self, driver):
        super(ConfirmEamil, self).__init__(driver)

    def get_page(self):
        self.get(self.signin_url)

    def send_keys_email_id(self):
        self.send_keys(self.email, email)

    def send_keys_email_pw(self):
        self.send_keys(self.password, password)

    def send_keys_resident_num(self):
        self.send_keys(self.resident_num, resident_num)


class ConfirmAccount(Base):
    signin_url = "https://qa.wiprex.com/signin"
    main_url = "https://qa.wiprex.com/"
    email = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[4]/div[2]/div[2]/input')
    password = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[4]/div[2]/div[3]/input')
    login_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[4]/div[2]/div[4]/button')
    detail_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[1]/div[2]/div/button/img')
    wallet_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[3]/div/div[3]/div[5]')
    deposit_withdraw_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[4]/div[1]/div/div[1]/div[2]/button')
    account_num = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[4]/div[1]/div[3]/div[2]/div/input')

    account_confirm_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[4]/div[1]/div/div[2]/div/div[1]/div[1]/div[1]/button/div')
    open_bank_list_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[4]/div[1]/div[2]/div[2]/span')


    bank_list = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[4]/div[1]/div[2]/div[2]/div')
    select_my_bank = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[4]/div[1]/div[2]/div[2]/div/div/div[12]')

    # 계좌인증요청버튼 만들어서 로직 작성
    account_vertification_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[4]/div[1]/div[5]/button')
    account_confirm_status = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[4]/div[1]/div[3]/div[2]/div[2]/div[2]/div/div[2]/button')
    account_confirm_status2 = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[4]/div[1]/div/div[2]/div/div[1]/div[1]/div[1]/button/div')
    def __init__(self, driver):
        super(ConfirmAccount, self).__init__(driver)

    def get_page(self):
        self.get(self.signin_url)

    def send_keys_email_id(self):
        self.send_keys(self.email, email)

    def send_keys_email_pw(self):
        self.send_keys(self.password, password)

    def send_keys_account_num(self):
        self.send_keys(self.account_num, account_num)