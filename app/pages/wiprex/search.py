from selenium.webdriver.common.by import By

from pages.base import Base

class SearchProduct(Base):
    search_in_url = "https://qa.wiprex.com/search"
    search_input_box = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[4]/div[1]/input')
    search_result_page = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[4]/div[2]/div/div[2]/div[1]/div[2]')

    def __init__(self, driver):
        super(SearchProduct, self).__init__(driver)

    def get_search_page(self):
        self.get(self.search_in_url)

    def send_keys_keyworld(self):
        self.send_keys(self.search_input_box, "임한별")