import time

from ..base import BaseTest
from pages.tower.product import ProductList, ProductCreate, CopyrightList, CopyrightCretate
from selenium.webdriver import ActionChains
from config.tower import (
    ProductData,
    CopyrightData
)
from . import (
    AssertUrl,
    ProductStatus,
    Category,
    ProductCreateAlert,
    CopyrightCreateAlert,
)

class TestProductLis(BaseTest):
    def test_1_get_product_list(self):
        product_list = ProductList(self.driver)
        product_list.get_main_page()
        product_list.click(product_list.menu_list)
        product_list.click(product_list.product_btn)
        product_list.click(product_list.product_list)
        self.assertEqual(self.driver.current_url, AssertUrl.product_list_url)
    
    def test_2_get_product_list_by_status(self):
        product_status = ProductList(self.driver)
        product_status.get_product_list_page()
        product_status.click(product_status.status_sale)
        product_status.click(product_status.search_btn)
        status = product_status.find_element(product_status.status).text
        self.assertEqual(status, ProductStatus.sale)
        product_status.click(product_status.status_wait)
        product_status.click(product_status.search_btn)
        status = product_status.find_element(product_status.status).text
        self.assertEqual(status, ProductStatus.wait)
        product_status.click(product_status.status_stop)
        product_status.click(product_status.search_btn)
        status = product_status.find_element(product_status.status).text
        self.assertEqual(status, ProductStatus.stop)


    def test_3_get_product_list_by_category(self):
        product_category = ProductList(self.driver)
        product_category.get_product_list_page()
        product_category.click(product_category.category_hiphop)
        product_category.click(product_category.search_btn)
        category = product_category.find_element(product_category.category).text
        self.assertEqual(category, Category.hiphop)
        product_category.click(product_category.category_hiphop)
        product_category.click(product_category.category_balad)
        product_category.click(product_category.search_btn)
        category = product_category.find_element(product_category.category).text
        self.assertEqual(category, Category.balad)
        product_category.click(product_category.category_balad)
        product_category.click(product_category.category_dance)
        product_category.click(product_category.search_btn)
        category = product_category.find_element(product_category.category).text
        self.assertEqual(category, Category.dance)
        product_category.click(product_category.category_dance)


    def test_4_product_status_update_to_wait(self):
        update_product_status = ProductList(self.driver)
        update_product_status.get_product_list_page()
        update_product_status.click(update_product_status.product)
        update_product_status.click(update_product_status.product_status_wait)
        update_product_status.click(update_product_status.apply_btn)
        time.sleep(1)
        product_status = update_product_status.find_element(update_product_status.product_status).text
        self.assertEqual(product_status, ProductStatus.wait)


    def test_5_product_status_update_to_stop(self):
        update_product_status = ProductList(self.driver)
        update_product_status.get_product_list_page()
        update_product_status.click(update_product_status.product)
        update_product_status.click(update_product_status.product_status_stop)
        update_product_status.click(update_product_status.apply_btn)
        time.sleep(1)
        product_status = update_product_status.find_element(update_product_status.product_status).text
        self.assertEqual(product_status, ProductStatus.stop)


    def test_6_product_status_update_to_sale(self):
        update_product_status = ProductList(self.driver)
        update_product_status.get_product_list_page()
        update_product_status.click(update_product_status.product)
        update_product_status.click(update_product_status.product_status_sale)
        update_product_status.click(update_product_status.apply_btn)
        time.sleep(1)
        product_status = update_product_status.find_element(update_product_status.product_status).text
        self.assertEqual(product_status, ProductStatus.sale)


class TestProductCreate(BaseTest):
    def test_1_create_product(self):
        product_create = ProductCreate(self.driver)
        product_create.get_main_page()
        product_create.click(product_create.menu_list)
        product_create.click(product_create.product_btn)
        product_create.click(product_create.product_create)
        self.assertEqual(self.driver.current_url, AssertUrl.product_create_url)
        product_create.click(product_create.select_copyright_option)
        time.sleep(3)
        option = product_create.find_element(product_create.select_copyright)
        action = ActionChains(self.driver)
        action.move_to_element(option).perform()
        option.click()
        time.sleep(2)
        product_create.send_keys_product_price()
        product_create.send_keys_product_amount()
        # product_create.click(product_create.create_btn)
        # alert = product_create.find_element(product_create.create_success_alert).text
        # self.assertEqual(alert, ProductCreateAlert.product_create_success)


    def test_2_create_product_without_data(self):
        product_create = ProductCreate(self.driver)
        product_create.get_main_page()
        product_create.click(product_create.menu_list)
        product_create.click(product_create.product_btn)
        product_create.click(product_create.product_create)
        self.assertEqual(self.driver.current_url, AssertUrl.product_create_url)
        product_create.click(product_create.select_copyright_option)
        time.sleep(3)
        option = product_create.find_element(product_create.select_copyright)
        action = ActionChains(self.driver)
        action.move_to_element(option).perform()
        option.click()
        time.sleep(2)
        product_create.click(product_create.create_btn)
        alert = product_create.find_element(product_create.alert_msg).text
        self.assertEqual(alert, ProductCreateAlert.product_create_without_data)


class TestCopyrightList(BaseTest):
    def test_1_get_copyright_list(self):
        copyright_list = CopyrightList(self.driver)
        copyright_list.get_main_page()
        copyright_list.click(copyright_list.menu_list)
        copyright_list.click(copyright_list.product_btn)
        copyright_list.click(copyright_list.copyright_list)
        self.assertEqual(self.driver.current_url, AssertUrl.copyright_list_url)


    def test_2_get_copyright_by_id(self):
        copyright_category = CopyrightList(self.driver)
        copyright_category.get_copyright_list_page()
        copyright_category.send_keys_categroy_id()
        copyright_category.click(copyright_category.search_btn)
        time.sleep(2)
        result = copyright_category.find_element(copyright_category.result_copyright_id).text
        self.assertEqual(result, CopyrightData.copyrigt_id)


    def test_3_get_copyright_list_by_category(self):
        copyright_category = CopyrightList(self.driver)
        copyright_category.get_copyright_list_page()

        copyright_category.click(copyright_category.category_hiphop)
        copyright_category.click(copyright_category.search_btn)
        category = copyright_category.find_element(copyright_category.category).text
        time.sleep(2)
        self.assertEqual(category, Category.hiphop)

        copyright_category.get_copyright_list_page()
        copyright_category.click(copyright_category.category_balad)
        copyright_category.click(copyright_category.search_btn)
        time.sleep(2)
        category = copyright_category.find_element(copyright_category.category).text
        self.assertEqual(category, Category.balad)

        copyright_category.get_copyright_list_page()
        copyright_category.click(copyright_category.category_dance)
        copyright_category.click(copyright_category.search_btn)
        time.sleep(2)
        category = copyright_category.find_element(copyright_category.category).text
        self.assertEqual(category, Category.dance)


class TestCopyrightCreate(BaseTest):
    def test_1_create_copyright(self):
        copyright_create = CopyrightCretate(self.driver)
        copyright_create.get_main_page()
        copyright_create.click(copyright_create.menu_list)
        copyright_create.click(copyright_create.product_btn)
        copyright_create.click(copyright_create.copyright_create)
        self.assertEqual(self.driver.current_url, AssertUrl.copyright_create_url)
        
        copyright_create.send_keys_copyrigt_id()
        copyright_create.send_keys_copyright_name()
        copyright_create.send_keys_copyright_singer()
        copyright_create.send_keys_copyright_yield_rate1()
        copyright_create.send_keys_copyright_yield_rate2()
        copyright_create.send_keys_youtube_url()
        copyright_create.send_keys_yotube_description()
        copyright_create.send_keys_composer()
        copyright_create.send_keys_lyricist()
        copyright_create.send_keys_arranger()

        # copyright_create.click(copyright_create.create_btn)
        # alert = copyright_create.find_element(copyright_create.create_alert_mgs).text
        # self.assertEqual(alert, CopyrightCreateAlert.copyright_create_alert)

    def test_2_create_copyright_exist_id(self):
        copyright_create = CopyrightCretate(self.driver)
        copyright_create.get_main_page()
        copyright_create.click(copyright_create.menu_list)
        copyright_create.click(copyright_create.product_btn)
        copyright_create.click(copyright_create.copyright_create)
        self.assertEqual(self.driver.current_url, AssertUrl.copyright_create_url)
        
        copyright_create.send_keys_duplicated_copyright_id()
        copyright_create.send_keys_copyright_name()
        copyright_create.send_keys_copyright_singer()
        copyright_create.send_keys_copyright_yield_rate1()
        copyright_create.send_keys_copyright_yield_rate2()
        copyright_create.send_keys_youtube_url()
        copyright_create.send_keys_yotube_description()
        copyright_create.send_keys_composer()
        copyright_create.send_keys_lyricist()
        copyright_create.send_keys_arranger()
        copyright_create.click(copyright_create.create_btn)

        alert = copyright_create.find_element(copyright_create.duple_alert_msg).text
        self.assertEqual(alert, CopyrightCreateAlert.copyright_id_duplicated_alert)














# class TestPremiumProduct(BaseTest):
#     def test_get_premium_list(self):
#         premium_list = Premium(self.driver)
#         premium_list.get_main_page()
#         premium_list.click(premium_list.menu_list)
#         premium_list.click(premium_list.premium_btn)
#         premium_list.click(premium_list.premium_list)
#         self.assertEqual(self.driver.current_url, 'http://10.2.1.100:5001/tower/premium/list')
        

#     def test_create_premium(self):
#         prmium_create = Premium(self.driver)
#         prmium_create.get_main_page()
#         prmium_create.click(prmium_create.menu_list)
#         prmium_create.click(prmium_create.premium_btn)
#         prmium_create.click(prmium_create.premium_create)
#         self.assertEqual(self.driver.current_url, 'http://10.2.1.100:5001/tower/premium/create')
    

#     def test_get_premium_copyright_list(self):
#         premium_copyright_list = Premium(self.driver)
#         premium_copyright_list.get_main_page()
#         premium_copyright_list.click(premium_copyright_list.menu_list)
#         premium_copyright_list.click(premium_copyright_list.premium_btn)
#         premium_copyright_list.click(premium_copyright_list.premium_copyright_list)
#         self.assertEqual(self.driver.current_url, 'http://10.2.1.100:5001/tower/premium/copyrights')

    
#     def test_create_premium_copyright(self):
#         premium_copyright_create = Premium(self.driver)
#         premium_copyright_create.get_main_page()
#         premium_copyright_create.click(premium_copyright_create.menu_list)
#         premium_copyright_create.click(premium_copyright_create.premium_btn)
#         premium_copyright_create.click(premium_copyright_create.premium_copyright_create)
#         self.assertEqual(self.driver.current_url, 'http://10.2.1.100:5001/tower/premium/copyright-create')


# class TestPremiumContract(BaseTest):
#     def test_get_premium_contract_list(self):
#         premium_contract_list = PremiumContract(self.driver)
#         premium_contract_list.get_main_page()
#         premium_contract_list.click(premium_contract_list.menu_list)
#         premium_contract_list.click(premium_contract_list.premium_contract_btn)
#         premium_contract_list.click(premium_contract_list.premium_contract_list)
#         self.assertEqual(self.driver.current_url, 'http://10.2.1.100:5001/tower/contract/list')


# class TestPremiumCopyrightInfo(BaseTest):
#     def test_get_premium_copyright_info_list(self):
#         premium_copyright_info_list = PremiumCopyrightInfo(self.driver)
#         premium_copyright_info_list.get_main_page()
#         premium_copyright_info_list.click(premium_copyright_info_list.menu_list)
#         premium_copyright_info_list.click(premium_copyright_info_list.premium_copyright_info_btn)
#         premium_copyright_info_list.click(premium_copyright_info_list.premium_copyright_info_list)
#         self.assertEqual(self.driver.current_url, 'https://qa.wiprex.com:5003/tower/premiumCopyright/list')

