import time
from selenium.webdriver.common.by import By

from ...base import FingoBase
from pages.fingo.nav import SearchProduct
from selenium.webdriver.common.keys import Keys

class TestSearch(FingoBase):
    def test_음원검색(self):
        search_product = SearchProduct(self.driver)
        search_product.get_search_page()
        search_product.send_keys_singer()
        time.sleep(1)
        search_product.click(search_product.serach_result)
        
        self.assertEqual(self.driver.current_url, SearchProduct.search_result_page)

    def test_음원중복검색(self):
        # sourcery skip: extract-duplicate-method
        repeat_search = SearchProduct(self.driver)
        repeat_search.get_search_page()
        print('중복 검색 테스트')
        
        repeat_search.send_keys_singer()
        time.sleep(2)
        repeat_search.find_element(repeat_search.search_input_box).clear()
        repeat_search.send_keys_singer2()
        time.sleep(2)
        repeat_search.find_element(repeat_search.search_input_box).clear()

        repeat_search.send_keys_singer()
        time.sleep(2)
        repeat_search.find_element(repeat_search.search_input_box).clear()
        repeat_search.send_keys_singer2()
        time.sleep(2)
        repeat_search.find_element(repeat_search.search_input_box).clear()

        search_result_count = repeat_search.find_elements(repeat_search.repeat_item)
        print(len(search_result_count))
        self.assertEqual(len(search_result_count), 1)


