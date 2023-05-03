from selenium.webdriver.common.by import By

from config.fingo import (
    fingo_base_url,
    fingo_prod_url,
    resident_num,
    account_num,
    sell_amount,
    email,
    password,
)
from ..base import Base

"""
계좌인증
실명인증
입금하기
출금하기
"""


class Account(Base):
    account_url = f"{fingo_base_url}wallet?tab=account"
    detail_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[1]/div[1]/div[3]/div/button/img')
    wallet_btn = (By.XPATH, '//*[@id="root"]/div[6]/button[4]/div[1]/img')
    deposit_withdraw_btn = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div/div[1]/div[2]/button')
    
    # 실명인증
    email_confirm_status = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div/div[2]/div/div[1]/div[2]/div[1]/button/div')
    email_confirm_btn = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div/div[2]/div/div[1]/div[2]/div[1]/button/div')
    resident_num_input = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/input')
    agree_btn = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div[2]/div[3]/div/button')
    next_btn = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div[2]/button')
    # //*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div/div[2]/div/div[1]/div[2]/div[1]/button/div
    # //*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div/div[2]/div/div[1]/div[1]/div[1]/button/div
    # 계좌인증
    account_confirm_status = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div/div[2]/div/div[1]/div[1]/div[1]/button/div')
    account_confirm_btn = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div/div[2]/div/div[1]/div[1]/div[1]/button/div')
    account_num = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div[3]/div[2]/div/input')
    open_bank_list_btn = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div[2]/div[2]/span')
    bank_list = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div[2]/div[2]/div')
    select_my_bank = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div[2]/div[2]/div/div/div[12]')
    account_vertification_btn = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div[5]/button')
    save_btn = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div[5]/button')
    alert_save_success = (By.XPATH, '//*[@id="modal"]/div/div[2]/div[1]/div[2]')

    # 출금
    withdraw_btn = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div/div[2]/div/div[2]/div[1]/div[2]/button')
    withdraw_amount = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/button[1]')
    withdraw_btn_2 = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[4]/button')
    request_auth_num_btn = (By.XPATH, '//*[@id="modal"]/div/div[2]/div/div[2]/div[2]/div[2]/button')
    # request_auth_num_btn = (By.CSS_SELECTOR, '#modal > div > div.informationModal__container > div > div.walletScreen__account__label__wrapper.body > div:nth-child(2) > div:nth-child(2) > button')
    sms_alert_message = (By.XPATH, '//*[@id="modal"]/div[2]/div[2]/div[1]/div[2]')
    # sms_alert_message = (By.CSS_SELECTOR, '#modal > div.modal > div.modal__container > div.modal__container__contentWrapper > div.modal__body__container')
    close_btn = (By.XPATH, '//*[@id="modal"]/div[2]/div[2]/div[2]/button')

    # 입금 (실서버에서 테스트)
    prod_account_url = f"{fingo_prod_url}wallet?tab=account"
    prod_login_url = f"{fingo_prod_url}signin"
    email_input = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[2]/div[2]/input')
    password_input = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[2]/div[3]/input')
    login_btn = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[2]/div[4]/button')
    deposit_amount = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/button[1]')
    deposit_btn = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[4]/button')
    select_bank_option = (By.XPATH, '//*[@id="modal"]/div/div[2]/div/div[2]/div/span')
    select_bank = (By.XPATH, '//*[@id="modal"]/div/div[2]/div/div[2]/div/span')
    deposit_confirm_btn = (By.XPATH, '//*[@id="modal"]/div/div[2]/div/div[4]/button[2]')
    deposit_status = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div[1]/span')



    def __init__(self, driver):
            super(Account, self).__init__(driver)

    def get_account_page(self):
        self.get(self.account_url)

    def send_keys_resident_num(self):
        self.send_keys(self.resident_num_input, resident_num)

    def send_keys_account_num(self):
        self.send_keys(self.account_num, account_num)

    def get_prod_account_page(self):
        self.get(self.prod_account_url)

    def get_prod_login_page(self):
        self.get(self.prod_login_url)

    def send_keys_email(self):
        self.send_keys(self.email_input, email)

    def send_keys_password(self):
        self.send_keys(self.password_input, password)




class Revenue(Base):
    revenue_url = f'{fingo_base_url}wallet?tab=revenue'
    product = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div/div[2]/div/div[2]/div/div[3]/div[2]/button')
    product_name = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div/div[1]/div[2]/div[1]/h3')
    product_amount_input = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div/div[2]/input')
    sell_btn = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div/div[2]/button')
    product_name2 = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div/div[1]/div[1]/div[2]')
    sell_btn2 = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div/div[2]/div[2]/button')
    sell_confirm_btn = (By.XPATH, '//*[@id="modal"]/div/div[2]/div[2]/button[2]')
    alert_sell_success = (By.XPATH, '//*[@id="modal"]/div/div[2]/div[1]/div[2]')

    history_url = f'{fingo_base_url}wallet?tab=history&type=restore'
    history_sell_product_name = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div/div[2]/div/div/div[2]/div[2]/div[1]/div[1]/div[2]')
    history_sell_product_amount = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div/div[2]/div/div/div[2]/div[2]/div[1]/div[4]/div[2]') 

    def __init__(self, driver):
            super(Revenue, self).__init__(driver)

    def get_revenue_page(self):
        self.get(self.revenue_url)

    def get_history_page(self):
        self.get(self.history_url)

    def send_keys_sell_amount(self):
        self.send_keys(self.product_amount_input, sell_amount)