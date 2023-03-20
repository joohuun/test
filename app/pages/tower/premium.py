from selenium.webdriver.common.by import By
from pages.base import Base
from selenium.webdriver.common.keys import Keys
from config.tower import (
    tower_base_url,
)



class PremiumProductList(Base):
    main_url = tower_base_url
    premium_product_list_url = f'{tower_base_url}'

    def __init__(self, driver):
        super(PremiumProductList, self).__init__(driver)

    def get_main_page(self):
        self.get(self.main_url)

    def get_premium_product_list_page(self):
        self.get(self.premium_product_list_url)


class PremiumProductCreate(Base):
    main_url = tower_base_url
    premium_product_create_url = f'{tower_base_url}'

    def __init__(self, driver):
        super(PremiumProductCreate, self).__init__(driver)

    def get_main_page(self):
        self.get(self.main_url)

    def get_premium_product_create_page(self):
        self.get(self.premium_product_create_url)

    

    







