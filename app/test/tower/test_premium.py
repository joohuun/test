import time

from ..base import BaseTest
from pages.tower.premium import PremiumProductList, PremiumProductCreate, PremiumCopyrigtList
from . import PremiumStatus, PremiumProductAlert, Category
from config.tower import PremiumCopyrightData


class TestPremiumProductList(BaseTest):
    def test_1_get_premium_product_list(self):
        prmeium_list = PremiumProductList(self.driver)
        prmeium_list.get_premium_product_list_page()
        self.assertEqual(self.driver.current_url, PremiumProductList.premium_product_list_url)


    def test_2_get_premium_product_list_by_status(self):
        premium_status = PremiumProductList(self.driver)
        premium_status.get_premium_product_list_page()
        premium_status.click(premium_status.status_sale)
        premium_status.click(premium_status.search_btn)
        premium_status.click(premium_status.status_wait)
        premium_status.click(premium_status.search_btn)
        premium_status.click(premium_status.status_stop)
        premium_status.click(premium_status.search_btn)

        
    def test_3_get_premium_product_list_by_category(self):
        premium_category = PremiumProductList(self.driver)
        premium_category.get_premium_product_list_page()
        premium_category.click(premium_category.category_hiphop)
        premium_category.click(premium_category.search_btn)
        premium_category.click(premium_category.category_hiphop)
        time.sleep(1)
        premium_category.click(premium_category.category_balad)
        premium_category.click(premium_category.search_btn)
        premium_category.click(premium_category.category_balad)
        time.sleep(1)

    def test_4_premium_product_status_update_to_sale(self):
        premium_status_update = PremiumProductList(self.driver)
        premium_status_update.get_premium_product_list_page()
        premium_status_update.click(premium_status_update.premium_product)
        premium_status_update.click(premium_status_update.update_status_sale)
        premium_status_update.click(premium_status_update.status_apply_btn)
        time.sleep(3)
        result = premium_status_update.find_element(premium_status_update.status_result).text
        self.assertEqual(result, PremiumStatus.sale)

    def test_5_premium_product_status_update_to_wait(self):
        premium_status_update = PremiumProductList(self.driver)
        premium_status_update.get_premium_product_list_page()
        premium_status_update.click(premium_status_update.premium_product)
        premium_status_update.click(premium_status_update.update_status_wait)
        premium_status_update.click(premium_status_update.status_apply_btn)
        time.sleep(3)
        result = premium_status_update.find_element(premium_status_update.status_result).text
        self.assertEqual(result, PremiumStatus.wait)


    def test_6_premium_product_status_update_to_stop(self):
        premium_status_update = PremiumProductList(self.driver)
        premium_status_update.get_premium_product_list_page()
        premium_status_update.click(premium_status_update.premium_product)
        premium_status_update.click(premium_status_update.update_status_stop)
        premium_status_update.click(premium_status_update.status_apply_btn)
        time.sleep(3)
        result = premium_status_update.find_element(premium_status_update.status_result).text
        self.assertEqual(result, PremiumStatus.stop)


class TestPremiumProductCreate(BaseTest):
    def test_1_create_premium_product(self):
        create_premium_product = PremiumProductCreate(self.driver)
        create_premium_product.get_premium_product_create_page()
        create_premium_product.click(create_premium_product.option_premium_copyright)
        create_premium_product.click(create_premium_product.select_premium_copyright)
        create_premium_product.send_keys_premium_product_price()
        create_premium_product.send_keys_premium_product_amount()
        create_premium_product.click(create_premium_product.create_btn)
        alert = create_premium_product.find_element(create_premium_product.create_alert).text
        self.assertEqual(alert, PremiumProductAlert.create_success)


    def test_2_create_premium_product_without_data(self):
        create_premium_product =PremiumProductCreate(self.driver)
        create_premium_product.get_premium_product_create_page()
        create_premium_product.click(create_premium_product.option_premium_copyright)
        create_premium_product.click(create_premium_product.select_premium_copyright)
        time.sleep(2)
        create_premium_product.click(create_premium_product.create_btn)
        alert = create_premium_product.find_element(create_premium_product.create_fail_alert).text
        self.assertEqual(alert, PremiumProductAlert.create_fail)

class TestPremiumCopyrightList(BaseTest):
    def test_1_get_premium_copyright_list(self):
        premium_copyright_list = PremiumCopyrigtList(self.driver)
        premium_copyright_list.get_premium_copyright_list_page()
        self.assertEqual(self.driver.current_url, PremiumCopyrigtList.premium_copyright_list_url)

    def test_2_get_premium_copyright_by_id(self):
        search_premium_by_id = PremiumCopyrigtList(self.driver)
        search_premium_by_id.get_premium_copyright_list_page()
        search_premium_by_id.send_keys_copyright_id()
        search_premium_by_id.click(search_premium_by_id.search_btn)
        result = search_premium_by_id.find_element(search_premium_by_id.copyright_id_result).text
        self.assertEqual(result, PremiumCopyrightData.copyright_id)


    def test_2_get_premium_copyright_by_category(self):
        premium_category = PremiumCopyrigtList(self.driver)
        premium_category.get_premium_copyright_list_page()
        premium_category.click(premium_category.category_hiphop)
        premium_category.click(premium_category.search_btn)
        premium_category.click(premium_category.category_hiphop)
        time.sleep(2)
        result = premium_category.find_element(premium_category.category_result).text
        self.assertEqual(result, Category.hiphop)
        premium_category.click(premium_category.category_balad)
        premium_category.click(premium_category.search_btn)
        premium_category.click(premium_category.category_balad)
        time.sleep(2)
        result = premium_category.find_element(premium_category.category_result).text
        self.assertEqual(result, Category.balad)



# class TestPremiumCopyrightCreate(BaseTest):
#     def test_1_create_premium_copyright(self):
#         pass

#     def test_2_create_premium_copyright_exist_id(self):
#         pass