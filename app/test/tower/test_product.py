import time

from ..base import BaseTest
from pages.tower.product import Product, PremiumContract, Premium, PremiumCopyrightInfo

class TestProduct(BaseTest):
    def test_get_product_list(self):
        product_list = Product(self.driver)
        product_list.get_main_page()
        product_list.click(product_list.menu_list)
        product_list.click(product_list.product_btn)
        product_list.click(product_list.product_list)
        self.assertEqual(self.driver.current_url, 'http://10.2.1.100:5001/tower/product/list')

    def test_create_product(self):
        product_create = Product(self.driver)
        product_create.get_main_page()
        product_create.click(product_create.menu_list)
        product_create.click(product_create.product_btn)
        product_create.click(product_create.product_create)
        self.assertEqual(self.driver.current_url, 'http://10.2.1.100:5001/tower/product/create')
        
        product_create.click(product_create.select_copyright_option)
        time.sleep(2)
        product_create.click(product_create.select_copyright)

    def test_get_copyright_list(self):
        copyright_list = Product(self.driver)
        copyright_list.get_main_page()
        copyright_list.click(copyright_list.menu_list)
        copyright_list.click(copyright_list.product_btn)
        copyright_list.click(copyright_list.copyright_list)
        self.assertEqual(self.driver.current_url, 'http://10.2.1.100:5001/tower/product/copyrights')

    def test_create_copyright(self):
        copyright_create = Product(self.driver)
        copyright_create.get_main_page()
        copyright_create.click(copyright_create.menu_list)
        copyright_create.click(copyright_create.product_btn)
        copyright_create.click(copyright_create.copyright_create)
        self.assertEqual(self.driver.current_url, 'http://10.2.1.100:5001/tower/product/copyright-create')


class TestPremiumProduct(BaseTest):
    def test_get_premium_list(self):
        premium_list = Premium(self.driver)
        premium_list.get_main_page()
        premium_list.click(premium_list.menu_list)
        premium_list.click(premium_list.premium_btn)
        premium_list.click(premium_list.premium_list)
        self.assertEqual(self.driver.current_url, 'http://10.2.1.100:5001/tower/premium/list')
        

    def test_create_premium(self):
        prmium_create = Premium(self.driver)
        prmium_create.get_main_page()
        prmium_create.click(prmium_create.menu_list)
        prmium_create.click(prmium_create.premium_btn)
        prmium_create.click(prmium_create.premium_create)
        self.assertEqual(self.driver.current_url, 'http://10.2.1.100:5001/tower/premium/create')
    

    def test_get_premium_copyright_list(self):
        premium_copyright_list = Premium(self.driver)
        premium_copyright_list.get_main_page()
        premium_copyright_list.click(premium_copyright_list.menu_list)
        premium_copyright_list.click(premium_copyright_list.premium_btn)
        premium_copyright_list.click(premium_copyright_list.premium_copyright_list)
        self.assertEqual(self.driver.current_url, 'http://10.2.1.100:5001/tower/premium/copyrights')

    
    def test_create_premium_copyright(self):
        premium_copyright_create = Premium(self.driver)
        premium_copyright_create.get_main_page()
        premium_copyright_create.click(premium_copyright_create.menu_list)
        premium_copyright_create.click(premium_copyright_create.premium_btn)
        premium_copyright_create.click(premium_copyright_create.premium_copyright_create)
        self.assertEqual(self.driver.current_url, 'http://10.2.1.100:5001/tower/premium/copyright-create')


class TestPremiumContract(BaseTest):
    def test_get_premium_contract_list(self):
        premium_contract_list = PremiumContract(self.driver)
        premium_contract_list.get_main_page()
        premium_contract_list.click(premium_contract_list.menu_list)
        premium_contract_list.click(premium_contract_list.premium_contract_btn)
        premium_contract_list.click(premium_contract_list.premium_contract_list)
        self.assertEqual(self.driver.current_url, 'http://10.2.1.100:5001/tower/contract/list')


# class TestPremiumCopyrightInfo(BaseTest):
#     def test_get_premium_copyright_info_list(self):
#         premium_copyright_info_list = PremiumCopyrightInfo(self.driver)
#         premium_copyright_info_list.get_main_page()
#         premium_copyright_info_list.click(premium_copyright_info_list.menu_list)
#         premium_copyright_info_list.click(premium_copyright_info_list.premium_copyright_info_btn)
#         premium_copyright_info_list.click(premium_copyright_info_list.premium_copyright_info_list)
#         self.assertEqual(self.driver.current_url, 'https://qa.wiprex.com:5003/tower/premiumCopyright/list')

