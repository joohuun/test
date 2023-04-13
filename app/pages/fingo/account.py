from selenium.webdriver.common.by import By

from pages.base import Base
from config.fingo import email, password, resident_num, my_bank, account_num, new_password
from selenium.webdriver.common.keys import Keys


class EmailSginIn(Base):
    main_url = "https://qa.fingo.run/"
    signin_url = "https://qa.fingo.run/signin"
    email_input = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[2]/div[2]/input')
    password_input = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[2]/div[3]/input')
    login_btn = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[2]/div[4]/button')

    def __init__(self, driver):
        super(EmailSginIn, self).__init__(driver)

    def get_page(self):
        self.get(self.main_url)
    
    def get_login_page(self):
        self.get(self.signin_url)

    def send_keys_email(self):
        self.send_keys(self.email_input, email)

    def send_keys_password(self):
        self.send_keys(self.password_input, password)


class Verification(Base):
    main_url = "https://qa.fingo.run/"
    account_url = ''
    detail_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[1]/div[1]/div[3]/div/button/img')
    wallet_btn = (By.XPATH, '//*[@id="root"]/div[6]/button[4]/div[1]/img')
    deposit_withdraw_btn = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div/div[1]/div[2]/button')
    email_confirm_status = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div/div[2]/div/div[1]/div[1]/div[1]/button/div')
    # 이메일인증
    email_confirm_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[1]/div[4]/div/div[2]/div/div[1]/div[2]/div[1]/button')
    resident_num = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[1]/div[4]/div[2]/div[2]/div[2]/input')
    agree_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[1]/div[4]/div[2]/div[3]/div/button')
    next_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[1]/div[4]/div[2]/button')
    # 계좌인증
    account_num = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div[3]/div[2]/div/input')
    account_confirm_btn = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div/div[2]/div/div[1]/div[1]/div[1]/button/div')
    open_bank_list_btn = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div[2]/div[2]/span')
    bank_list = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div[2]/div[2]/div')
    select_my_bank = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div[2]/div[2]/div/div/div[12]')
    account_vertification_btn = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div[5]/button')
    save_btn = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div[5]/button')
    account_confirm_status = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div/div[2]/div/div[1]/div[1]/div[1]/button/div')
    alert_save_success = (By.XPATH, '//*[@id="modal"]/div/div[2]/div[1]/div[2]')


    def __init__(self, driver):
        super(Verification, self).__init__(driver)

    def get_page(self):
        self.get(self.main_url)

    def send_keys_resident_num(self):
        self.send_keys(self.resident_num, resident_num)

    def send_keys_account_num(self):
        self.send_keys(self.account_num, account_num)
    

class CustomerInfo(Base):
    main_url = 'https://qa.fingo.run/'
    info_url = 'https://qa.fingo.run/info'
    signin_url = 'https://qa.fingo.run/signin'

    mypage_btn = (By.XPATH, '//*[@id="root"]/div[6]/button[5]')
    # //*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]
    customer_info_btn = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]')
    # //*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div[2]/div[2]/input
    check_password_input = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div[2]/div[2]/input')
    # check_password_input = (By.CSS_SELECTOR ,'#root > div.ptr.overflow > div.ptr__children > div.router__container > div.passwordAuth__container > div.passwordAuth__container__info > div.input__container > input')
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
    info_url = 'https://qa.fingo.run/info'
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

