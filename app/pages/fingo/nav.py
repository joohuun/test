from selenium.webdriver.common.by import By

from config.fingo import (
    fingo_base_url,
)
from ..base import Base

class SearchProduct(Base):
    search_url = f"{fingo_base_url}search"
    search_input_box = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/input')
    serach_result = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[2]/div/div[2]/div[1]/img')
    search_result_page = f"{fingo_base_url}copyright/UHJvZHVjdDoxNjI="
    # root > div.ptr.overflow > div.ptr__children > div.router__container > div.search__container > div > div.card.search
    repeat_item = (By.CSS_SELECTOR, '.card.search')
     
    def __init__(self, driver):
        super(SearchProduct, self).__init__(driver)

    def get_search_page(self):
        self.get(self.search_url)

    def send_keys_singer(self):
        self.send_keys(self.search_input_box, "사랑 이딴 거")

    def send_keys_singer2(self):
        self.send_keys(self.search_input_box, "꿈처럼 내린")