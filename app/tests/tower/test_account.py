import time
from ..base import TowerBase
from pages.tower.account import (
    ManagementAdminUser, 
    ManagementCustomerUser,
)
from . import (
    UserType,
)
from config.tower import (
    AccountData,
)
import requests, json

# class TestAdminUser(TowerBase):
#     def test_get_admin_list(self):
#         management_admin_user = ManagementAdminUser(self.driver)

#         management_admin_user.get_admin_list_page()
#         # self.driver.execute_script("window.location.reload();")
#         # jwt_token_from_storage = self.driver.execute_script("return window.sessionStorage.getItem('jwt');")
#         # print(jwt_token_from_storage)
#         time.sleep(2)
        

#         print(self.driver.current_url, "admin_list")
#         self.assertEqual(self.driver.current_url, ManagementAdminUser.admin_list_url)

class TestCustomerUser(TowerBase):
    def test_1_get_user_list(self):
        management_customer_user = ManagementCustomerUser(self.driver)

        management_customer_user.get_user_list_page()
        self.assertEqual(self.driver.current_url, ManagementCustomerUser.user_list_url)

    def test_2_search_user(self):
        search_user = ManagementCustomerUser(self.driver)
        search_user.get_user_list_page()
        search_user.send_keys_user_name()
        search_user.click(search_user.search_btn)
        search_user.click(search_user.search_result)
        result = search_user.find_element(search_user.search_result_user_name).text
        self.assertEqual(result, AccountData.username)
        
#     def test_3_filter_by_normal_user_list(self):
#         search_normal_user = ManagementCustomerUser(self.driver)
#         search_normal_user.get_user_list_page()
#         search_normal_user.click(search_normal_user.filter_by_normal)
#         search_normal_user.click(search_normal_user.search_btn)
#         time.sleep(2)
#         try:
#             result2 = search_normal_user.find_element(search_normal_user.user_list).text
#             if result2 == "No data":
#                 print("가입된 유저가 없습니다.")
#         except Exception:
#             signup_type = search_normal_user.find_element(search_normal_user.user_result).text
#             self.assertEqual(signup_type, UserType.normal)
        
        
#     def test_4_filter_by_kakao_user_list(self):
#         seacrh_kakao_user = ManagementCustomerUser(self.driver)
#         seacrh_kakao_user.get_user_list_page()
#         seacrh_kakao_user.click(seacrh_kakao_user.filter_by_kakao)
#         seacrh_kakao_user.click(seacrh_kakao_user.search_btn)
#         time.sleep(2)
#         try:
#             result = seacrh_kakao_user.find_element(seacrh_kakao_user.user_list).text
#             if result == 'No data':
#                 print('가입된 유저가 없습니다.')
#         except Exception:
#             signup_type = seacrh_kakao_user.find_element(seacrh_kakao_user.user_result).text
#             self.assertEqual(signup_type, UserType.kakao)
            

#     def test_5_filter_by_naver_user_list(self):
#         search_naver_user = ManagementCustomerUser(self.driver)
#         search_naver_user.get_user_list_page()
#         search_naver_user.click(search_naver_user.filter_by_naver)
#         search_naver_user.click(search_naver_user.search_btn)
#         time.sleep(2)
#         try:
#             result = search_naver_user.find_element(search_naver_user.user_list).text
#             if result == 'No data':
#                 print('가입된 유저가 없습니다.')
#         except Exception:
#             signup_type = search_naver_user.find_element(search_naver_user.user_result).text
#             self.assertEqual(signup_type, UserType.naver)

        
#     def test__6_filter_by_apple_user_list(self):
#         search_apple_user = ManagementCustomerUser(self.driver)
#         search_apple_user.get_user_list_page()
#         search_apple_user.click(search_apple_user.filter_by_apple)
#         search_apple_user.click(search_apple_user.search_btn)
#         time.sleep(2)
#         try:
#             result = search_apple_user.find_element(search_apple_user.user_list).text
#             if result == 'No data':
#                 print('가입된 유저가 없습니다.')
#         except Exception:
#             signup_type = search_apple_user.find_element(search_apple_user.user_result).text
#             self.assertEqual(signup_type, UserType.apple)



