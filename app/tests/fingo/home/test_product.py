import time
from pages.fingo.home import Product
from ...base import FingoBase
from .. import ProductALert
from config.fingo import fingo_base_url
"""
추천 음원 상품
신규 음원 상품
인기 음원 상품
"""

class TestBuyProduct(FingoBase):
    def test_1_get_session(self):
        self.driver.get(fingo_base_url)

    def test_2_추천음원탭_구매(self):
        buy_product = Product(self.driver)
        buy_product.get_main_page()
        time.sleep(2)
        buy_product.get_main_page()
        buy_product.click(buy_product.recommand_product)
        buy_product.click(buy_product.buy_btn)
        time.sleep(1)
        buy_product.click(buy_product.buy_quantity_value_10)
        buy_product.send_keys_buy_btn2()
        # buy_product.click(buy_product.buy_confirm_btn)
        # alert = buy_product.find_element(buy_product.alert_buy_success).text
        # self.assertEqual(alert, ProductALert.buy_success)


class TestGiftProduct(FingoBase):
    def test_1_get_session(self):
        self.driver.get(fingo_base_url)

    def test_2_추천음원탭_선물(self):
        gift_product = Product(self.driver)
        gift_product.get(gift_product.main_url)
        gift_product.click(gift_product.recommand_product)
        gift_product.send_keys_gift_btn()
        time.sleep(1)
        gift_product.click(gift_product.gift_quantity_value_10)
        gift_product.send_keys_gift_phone_num()
        gift_product.click(gift_product.gift_btn2)
        # gift_product.click(gift_product.gift_confirm_btn)
        # result = gift_product.find_element(gift_product.gift_result_message).text
        # self.assertEqual(result, ProductALert.gift_success)