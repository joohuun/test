from selenium.webdriver.common.by import By

from pages.base import Base, LocalStorage
from config.tower import (
    tower_base_url,
    email,
    password,
    query,
    AccountData,
)



class getToken(Base):
    graphql_url = 'http://10.2.1.100:8000/graphql/'
    # query_input = (By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div/div/div[1]/div[2]/div[1]/div[1]')
    query_input = (By.CSS_SELECTOR, '#root > div > div > div > div.sc-fONwsr.hFUbho > div > div > div.sc-ifAKCX.dAtAHQ > div.sc-eXEjpC.bdygHZ > div.sc-hZSUBg.HwDAJ > div.sc-ifAKCX.dAtAHQ > div > div > div.CodeMirror-scroll')
    query_btn = (By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/div')
    token = (By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div[3]/div/div/div/div/div[6]/div[1]/div/div/div/div[5]/pre[1]/span/span[5]')
    signin_url = f'{tower_base_url}signin'
    main_url = f'{tower_base_url}produt/list'

    def __init__(self, driver):
        super(getToken, self).__init__(driver)

    def get_graphql_page(self):
        self.get(self.graphql_url)

    def send_keys_query(self):
        self.send_keys(self.query_input, query)

    def get_main_page(self):
        self.get(self.main_url)

    def get_login_page(self):
        self.get(self.signin_url)


class SignIn(Base):
    main_url = f'{tower_base_url}produt/list'
    signin_url = f'{tower_base_url}signin'
    email_input = (By.XPATH, '//*[@id="email"]')
    password_input = (By.XPATH, '//*[@id="password"]')
    login_btn = (By.XPATH, '//*[@id="root"]/div[1]/main/div/form/button/span[1]')



    def __init__(self, driver):
        super(SignIn, self).__init__(driver)

    def get_main_page(self):
        self.get(self.main_url)

    def get_login_page(self):
        self.get(self.signin_url)

    def send_keys_email(self):
        self.send_keys(self.email_input, email)

    def send_keys_password(self):
        self.send_keys(self.password_input, password)


class ManagementAdminUser(Base):
    main_url = tower_base_url
    admin_list_url = f'{tower_base_url}admin/list'
    menu_list = (By.XPATH, '//*[@id="root"]/div[1]/header/div/button[1]')
    admin_user_management = (By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/ul/div[2]/div[2]/span')
    admin_user_list = (By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/ul/div[3]/div/div/div/div/div')
    result_msg = (By.XPATH, '//*[@id="root"]/div[2]')

    def __init__(self, driver):
        super(ManagementAdminUser, self).__init__(driver)

    def get_admin_list_page(self):
        self.get(self.admin_list_url)


class ManagementCustomerUser(Base):
    main_url = tower_base_url
    user_list_url = f'{tower_base_url}users/list'
    menu_list = (By.XPATH, '//*[@id="root"]/div[1]/header/div/button[1]')
    customer_user = (By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/ul/div[3]')
    customer_user_list = (By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/ul/div[4]/div/div/div/div/div')
    search_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div/div[2]/button')
    serach_input_box = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div/div[1]/div[1]/div[1]/div[2]/div/input')
    search_result = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[3]/div/div[2]/div/div[1]/table/tbody/tr/td[4]/span/a')
    search_result_user_name = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[4]/div[1]/div/div[3]/div[5]/p[2]')
    user_list = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[3]/div/div[2]/div/div[1]/table/caption')
    user_result = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[3]/div/div[2]/div/div[1]/table/tbody/tr[1]/td[2]/span/a')
    
    filter_by_normal = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div/div[1]/div[2]/div[1]/div/div/label[2]/span[2]')
    filter_by_kakao = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div/div[1]/div[2]/div[1]/div/div/label[3]/span[2]')
    filter_by_naver = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div/div[1]/div[2]/div[1]/div/div/label[4]/span[2]')
    filter_by_apple = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div/div[1]/div[2]/div[1]/div/div/label[5]/span[2]')


    def __init__(self, driver):
        super(ManagementCustomerUser, self).__init__(driver)

    def get_user_list_page(self):
        self.get(self.user_list_url) 

    def send_keys_user_name(self):
        self.send_keys(self.serach_input_box, AccountData.username)

