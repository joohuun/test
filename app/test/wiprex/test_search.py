
import time
from pages.wiprex.search import SearchProduct
from ..base import BaseTest


class Search(BaseTest):
    def test_search_product(self):
        search_product = SearchProduct(self.driver)
        search_product.get(search_product.search_in_url)
        search_product.send_keys_keyworld()
        time.sleep(1)
        search_product.click(search_product.search_result_page)
        
        self.assertEqual(self.driver.current_url, "https://qa.fingo.run/copyright/UHJvZHVjdDoxNjI=")
