import time

from ..base import BaseTest
from pages.tower.account import ManagementAdminUser, ManagementCustomerUser


class TestAdminUser(BaseTest):
    def test_어드민_관리(self):
        print('어드민유저 페이지 테스트')
        management_admin_user = ManagementAdminUser(self.driver)
        management_admin_user.get(management_admin_user.main_url)
        management_admin_user.click(management_admin_user.menu_list)
        management_admin_user.click(management_admin_user.admin_user_management)
        management_admin_user.click(management_admin_user.admin_user_list)
        print(self.driver.current_url)
        time.sleep(2)
        self.assertEqual(self.driver.current_url, "http://10.2.1.100:5001/tower/admin/list")


class TestCustomerUser(BaseTest):
    def test_회원_관리(self):
        print("회원 페이지 테스트")
        management_customer_user = ManagementCustomerUser(self.driver)
        management_customer_user.get(management_customer_user.main_url)
        management_customer_user.click(management_customer_user.menu_list)
        management_customer_user.click(management_customer_user.customer_user)
        management_customer_user.click(management_customer_user.customer_user_list)
        print(self.driver.current_url)
        time.sleep(2)
        self.assertEqual(self.driver.current_url, "http://10.2.1.100:5001/tower/users/list")


    def test_search_user(self):
        print("검색테스트")
        search_user = ManagementCustomerUser(self.driver)
        search_user.get(search_user.user_list_url)
        search_user.send_keys_user_name()
        time.sleep(2)
        search_user.click(search_user.search_btn)
        search_user.click(search_user.search_result)
        result = search_user.find_element(search_user.search_result_user_name).text
        self.assertEqual(result, '관리자')

        
    def test_filter_by_normal_user_list(self):
        print('일반유저 필터 검색')
        search_normal_user = ManagementCustomerUser(self.driver)
        search_normal_user.get(search_normal_user.user_list_url)
        search_normal_user.click(search_normal_user.filter_by_normal)
        search_normal_user.click(search_normal_user.search_btn)
        time.sleep(2)
        try:
            result2 = search_normal_user.find_element(search_normal_user.user_list).text
            if result2 == "No data":
                print("가입된 유저가 없습니다.")
        except Exception:
            signup_type = search_normal_user.find_element(search_normal_user.user_result).text
            self.assertEqual(signup_type, '일반')
        
        
    def test_filter_by_kakao_user_list(self):
        print('카카오유저 필터 검색')
        seacrh_kakao_user = ManagementCustomerUser(self.driver)
        seacrh_kakao_user.get(seacrh_kakao_user.user_list_url)
        seacrh_kakao_user.click(seacrh_kakao_user.filter_by_kakao)
        seacrh_kakao_user.click(seacrh_kakao_user.search_btn)
        time.sleep(2)
        try:
            result = seacrh_kakao_user.find_element(seacrh_kakao_user.user_list).text
            if result == 'No data':
                print('가입된 유저가 없습니다.')
        except Exception:
            signup_type = seacrh_kakao_user.find_element(seacrh_kakao_user.user_result).text
            self.assertEqual(signup_type, 'kakao')
            

    def test_filter_by_naver_user_list(self):
        print('네이버유저 필터 검색')
        search_naver_user = ManagementCustomerUser(self.driver)
        search_naver_user.get(search_naver_user.user_list_url)
        search_naver_user.click(search_naver_user.filter_by_naver)
        search_naver_user.click(search_naver_user.search_btn)
        time.sleep(2)
        try:
            result = search_naver_user.find_element(search_naver_user.user_list).text
            if result == 'No data':
                print('가입된 유저가 없습니다.')
        except Exception:
            signup_type = search_naver_user.find_element(search_naver_user.user_result).text
            self.assertEqual(signup_type, 'naver')

        
    def test_filter_by_apple_user_list(self):
        print('애플유저 필터 검색')
        search_apple_user = ManagementCustomerUser(self.driver)
        search_apple_user.get(search_apple_user.user_list_url)
        search_apple_user.click(search_apple_user.filter_by_apple)
        search_apple_user.click(search_apple_user.search_btn)
        time.sleep(2)
        try:
            result = search_apple_user.find_element(search_apple_user.user_list).text
            if result == 'No data':
                print('가입된 유저가 없습니다.')
        except Exception:
            signup_type = search_apple_user.find_element(search_apple_user.user_result).text
            self.assertEqual(signup_type, 'apple')




    

    


