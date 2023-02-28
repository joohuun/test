from selenium.webdriver.common.by import By
from pages.base import Base
from selenium.webdriver.common.keys import Keys


class Product(Base):
    main_url = 'http://10.2.1.100:5001/tower/'
    menu_list = (By.XPATH, '//*[@id="root"]/div[1]/header/div/button[1]')
    product_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/ul/div[4]')
    product_list = (By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/ul/div[5]/div/div/div/div[1]')
    product_create = (By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/ul/div[5]/div/div/div/div[2]')
    select_copyright_option = (By.XPATH, '//*[@id="mui-component-select-copyrights0"]')
    select_copyright = (By.XPATH, '//*[@id="menu-copyrights0"]/div[3]/ul/li[1]')
    copyright_list = (By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/ul/div[5]/div/div/div/div[3]')
    copyright_create = (By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/ul/div[5]/div/div/div/div[4]')

    def __init__(self, driver):
        super(Product, self).__init__(driver)

    def get_main_page(self):
        self.get(self.main_url)


class Premium(Base):
    main_url = 'http://10.2.1.100:5001/tower/'
    menu_list = (By.XPATH, '//*[@id="root"]/div[1]/header/div/button[1]')
    premium_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/ul/div[5]')
    premium_list = (By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/ul/div[6]/div/div/div/div[1]')
    premium_create = (By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/ul/div[6]/div/div/div/div[2]')
    premium_copyright_list = (By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/ul/div[6]/div/div/div/div[3]')
    premium_copyright_create = (By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/ul/div[6]/div/div/div/div[4]')


    def __init__(self, driver):
        super(Premium, self).__init__(driver)

    def get_main_page(self):
        self.get(self.main_url)


class PremiumContract(Base):
    main_url = 'http://10.2.1.100:5001/tower/'
    menu_list = (By.XPATH, '//*[@id="root"]/div[1]/header/div/button[1]')
    premium_contract_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/ul/div[6]')
    premium_contract_list = (By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/ul/div[7]/div/div/div/div')

    def __init__(self, driver):
        super(PremiumContract, self).__init__(driver)

    def get_main_page(self):
        self.get(self.main_url)


class PremiumCopyrightInfo(Base):
    main_url = 'https://qa.wiprex.com:5003/tower/'
    menu_list = (By.XPATH, '//*[@id="root"]/div[1]/header/div/button[1]')
    premium_copyright_info_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/ul/div[7]')
    premium_copyright_info_list = (By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/ul/div[8]/div/div/div/div[1]')
    premium_copyright_info_create = (By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/ul/div[8]/div/div/div/div[2]')
    premium_copyright_analysis_list = (By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/ul/div[8]/div/div/div/div[3]')
    premium_copyright_analysis_create = (By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/ul/div[8]/div/div/div/div[4]')


    def __init__(self, driver):
        super(PremiumCopyrightInfo, self).__init__(driver)

    def get_main_page(self):
        self.get(self.main_url)








