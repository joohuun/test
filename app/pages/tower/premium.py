from selenium.webdriver.common.by import By
from pages.base import Base
from selenium.webdriver.common.keys import Keys
from config.tower import (
    tower_base_url,
)



class Premium(Base):
    main_url = 'http://10.2.1.100:5001/tower/'
    main_url = tower_base_url
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







