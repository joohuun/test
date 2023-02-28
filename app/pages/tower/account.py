from selenium.webdriver.common.by import By

from pages.base import Base



user_name = '관리자'

class ManagementAdminUser(Base):
    main_url = 'http://10.2.1.100:5001/tower/'
    menu_list = (By.XPATH, '//*[@id="root"]/div[1]/header/div/button[1]')
    admin_user_management = (By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/ul/div[2]/div[2]/span')
    admin_user_list = (By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/ul/div[3]/div/div/div/div/div')
    result_msg = (By.XPATH, '//*[@id="root"]/div[2]')


class ManagementCustomerUser(Base):
    main_url = 'http://10.2.1.100:5001/tower/'
    user_list_url = 'http://10.2.1.100:5001/tower/users/list'
    menu_list = (By.XPATH, '//*[@id="root"]/div[1]/header/div/button[1]')
    customer_user = (By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/ul/div[3]')
    customer_user_list = (By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/ul/div[4]/div/div/div/div/div')
    search_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div/div[2]/button')
    serach_input_box = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div/div[1]/div[1]/div[1]/div[2]/div/input')

    search_result = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[3]/div/div[2]/div/div[1]/table/tbody/tr/td[4]/span/a')
    search_result_user_name = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[4]/div[1]/div/div[3]/div[5]/p[2]')

    user_list = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[3]/div/div[2]/div/div[1]/table/caption')
    user_result = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[3]/div/div[2]/div/div[1]/table/tbody/tr[1]/td[2]/span/a')
    
    filter_by_normal = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div/div[1]/div[2]/div[1]/div/div/label[2]/span[1]/span[1]')
    filter_by_kakao = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div/div[1]/div[2]/div[1]/div/div/label[3]/span[1]/span[1]')
    filter_by_naver = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div/div[1]/div[2]/div[1]/div/div/label[4]/span[1]/span[1]')
    filter_by_apple = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div/div[1]/div[2]/div[1]/div/div/label[5]/span[1]/span[1]')


    def __init__(self, driver):
        super(ManagementCustomerUser, self).__init__(driver)

    def send_keys_user_name(self):
        self.send_keys(self.serach_input_box, user_name)
