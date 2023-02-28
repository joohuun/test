import time
from pages.wiprex.product import Product
from ..base import BaseTest


class TestBuyProduct(BaseTest):
    def test_추천음원상품구매(self):
        buy_product = Product(self.driver)
        # buy_product.get(buy_product.signin_url)
        # buy_product.send_keys_email_id()
        # buy_product.send_keys_email_pw()
        # buy_product.click(buy_product.login_btn)
        # time.sleep(2)
        buy_product.get(buy_product.main_url)
        buy_product.click(buy_product.recommand_product)
        buy_product.click(buy_product.buy_btn)
        time.sleep(2)
        buy_product.click(buy_product.buy_quantity_value_10)
        time.sleep(2)
        buy_product.send_keys_buy_btn2()
        buy_product.click(buy_product.buy_confirm_btn)
        result = buy_product.find_element(buy_product.buy_result_message).text
        time.sleep(2)

        self.assertEqual(result, "구매가 완료되었습니다.")


class TestSellProduct(BaseTest):
    def test_음원반환(self):
        sell_product = Product(self.driver)
        # sell_product.get(sell_product.signin_url)
        # sell_product.send_keys_email_id()
        # sell_product.send_keys_email_pw()
        # sell_product.click(sell_product.login_btn)
        # time.sleep(2)
        sell_product.get(sell_product.main_url)
        sell_product.click(sell_product.detail_btn)
        sell_product.click(sell_product.wallet_btn)
        sell_product.send_keys_sell_btn()
        time.sleep(2)
        sell_product.click(sell_product.sell_quantity_value_10)
        sell_product.send_keys_sell_btn2()
        time.sleep(2)
        sell_product.click(sell_product.sell_btn3)
        sell_product.click(sell_product.sell_confirm_btn)
        result = sell_product.find_element(sell_product.sell_result_message).text
        time.sleep(2)

        self.assertEqual(result, "반환이 완료되었습니다.")        


class TestGiftProduct(BaseTest):
    def test_음원선물(self):
        gift_product = Product(self.driver)
        # gift_product.get(gift_product.signin_url)
        # gift_product.send_keys_email_id()
        # gift_product.send_keys_email_pw()
        # gift_product.click(gift_product.login_btn)
        # time.sleep(2)
        gift_product.get(gift_product.main_url)
        gift_product.click(gift_product.recommand_product)
        time.sleep(2)
        gift_product.send_keys_gift_btn()
        time.sleep(2)
        gift_product.click(gift_product.gift_quantity_value_10)
        gift_product.send_keys_gift_phone_num()
        gift_product.click(gift_product.gift_btn2)
        gift_product.click(gift_product.gift_confirm_btn)
        result = gift_product.find_element(gift_product.gift_result_message).text
        time.sleep(2)

        self.assertEqual(result, "선물하기가 완료되었습니다.")