# import time

# from ..base import BaseTest
# from pages.tower.product import Premium



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


