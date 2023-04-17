import time
from pages.fingo.product import Product
from ..base import FingoBase
from . import ProductALert


# class TestBuyProduct(FingoBase):
#     def test_1_추천음원상품구매(self):
#         buy_product = Product(self.driver)
#         buy_product.get(buy_product.main_url)
#         buy_product.click(buy_product.recommand_product)
#         buy_product.click(buy_product.buy_btn)
#         time.sleep(1)
#         buy_product.click(buy_product.buy_quantity_value_10)
#         buy_product.send_keys_buy_btn2()
#         buy_product.click(buy_product.buy_confirm_btn)
#         alert = buy_product.find_element(buy_product.alert_buy_success).text

#         self.assertEqual(alert, ProductALert.buy_success)


# class TestSellProduct(FingoBase):
#     def test_2_음원반환(self):
#         sell_product = Product(self.driver)
#         sell_product.get(sell_product.main_url)
#         sell_product.click(sell_product.wallet_btn)
#         sell_product.send_keys_sell_btn()
#         sell_product.click(sell_product.sell_quantity_value_100)
#         sell_product.send_keys_sell_btn2()
#         sell_product.click(sell_product.sell_btn3)
#         sell_product.click(sell_product.sell_confirm_btn)
#         alert = sell_product.find_element(sell_product.sell_result_message).text

#         self.assertEqual(alert, ProductALert.sell_success)        


# class TestGiftProduct(FingoBase):
#     def test_3_음원선물(self):
#         gift_product = Product(self.driver)
#         gift_product.get(gift_product.main_url)
#         gift_product.click(gift_product.recommand_product)
#         gift_product.send_keys_gift_btn()
#         time.sleep(1)
#         gift_product.click(gift_product.gift_quantity_value_10)
#         gift_product.send_keys_gift_phone_num()
#         gift_product.click(gift_product.gift_btn2)
#         gift_product.click(gift_product.gift_confirm_btn)
#         result = gift_product.find_element(gift_product.gift_result_message).text

#         self.assertEqual(result, "선물하기가 완료되었습니다.")


class TestProductList(FingoBase):
    def test_1_product_list_filter_by_남은수량(self):
        pass

    def test_2_product_list_filter_by_가격(self):
        pass

    def test_3_product_list_filter_by_좋아요(self):
        pass

    def test_4_product_list_filter_by_등록날짜(self):
        pass
