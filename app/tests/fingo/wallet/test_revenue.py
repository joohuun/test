import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

# from pages.fingo.account import Verification
from pages.fingo.wallet import Revenue
from .. import CustomerInfoAlert, CustomerInfoStatus, ProductALert
from ...base import FingoBase
from config.fingo import fingo_base_url, sell_amount

class TestSellProduct(FingoBase):
    def test_1_get_session(self):
        self.driver.get(fingo_base_url)

    def test_2_음원반환(self):
        """
        판매량, 판매음원 테스트
        """    
        sell_product = Revenue(self.driver)
        sell_product.get_revenue_page()

        sell_product.click(sell_product.product)
        page_1_product_name = sell_product.find_element(sell_product.product_name).text
        sell_product.send_keys_sell_amount()
        sell_product.click(sell_product.sell_btn)
        page_2_product_name = sell_product.find_element(sell_product.product_name2).text
        self.assertEqual(page_1_product_name, page_2_product_name)

        sell_product.click(sell_product.sell_btn2)
        sell_product.click(sell_product.sell_confirm_btn)

        alert = sell_product.find_element(sell_product.alert_sell_success).text
        self.assertEqual(alert, ProductALert.sell_success)

        sell_product.get_history_page()
        sell_product_name_by_history = sell_product.find_element(sell_product.history_sell_product_name).text
        sell_product_amount_by_history = sell_product.find_element(sell_product.history_sell_product_amount).text

        self.assertEqual(sell_product_name_by_history, page_1_product_name)
        self.assertEqual(sell_product_name_by_history, page_2_product_name)
        self.assertEqual(sell_product_amount_by_history, f'{sell_amount} PIE')

