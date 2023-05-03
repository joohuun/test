import time

from pages.fingo.mypage import CustomerInfo, Maketing
from config.fingo import fingo_base_url
from ...base import FingoBase
from .. import CustomerInfoAlert



class TestCustomerInfo(FingoBase):
    def test_1_get_session(self):
        self.driver.get(fingo_base_url)

    def test_2_회원정보조회(self):
        customer_info = CustomerInfo(self.driver)
        customer_info.get_main_page()
        customer_info.click(customer_info.mypage_btn)
        time.sleep(1)
        customer_info.click(customer_info.customer_info_btn)
        customer_info.send_keys_check_password()
        customer_info.click(customer_info.confirm_btn)
        time.sleep(1)
        self.assertEqual(self.driver.current_url, CustomerInfo.info_url)

    def test_3_비밀번호변경(self):
        change_password = CustomerInfo(self.driver)
        change_password.click(change_password.password_change_btn)
        change_password.send_keys_origin_password()
        change_password.send_keys_new_password()
        change_password.send_keys_confirm_new_password()
        time.sleep(2)
        # change_password.click(change_password.password_save_btn)
        # alert = change_password.find_element(change_password.confirm_alert_msg).text
        # self.assertEqual(alert, CustomerInfoAlert.password_change_success)

    # def test_4_비밀번호원복(self):
    #     reset_origin_password = CustomerInfo(self.driver)
    #     reset_origin_password.get_main_page()
    #     reset_origin_password.click(reset_origin_password.mypage_btn)
    #     time.sleep(2)
    #     reset_origin_password.click(reset_origin_password.customer_info_btn)
    #     reset_origin_password.send_keys_check_password2()
    #     reset_origin_password.click(reset_origin_password.confirm_btn)
    #     reset_origin_password.click(reset_origin_password.password_change_btn)
    #     time.sleep(2)
    #     reset_origin_password.send_keys_orgin_password2()
    #     reset_origin_password.send_keys_new_password2()
    #     reset_origin_password.send_keys_confirm_new_password2()
    #     time.sleep(2)
    #     reset_origin_password.click(reset_origin_password.password_save_btn)
    #     alert = reset_origin_password.find_element(reset_origin_password.confirm_alert_msg).text
    #     self.assertEqual(alert, CustomerInfoAlert.password_change_success)


class TestMaketing(FingoBase):
    def test_1_get_session(self):
        self.driver.get(fingo_base_url)

    def test_2_마케팅_수신동의(self):
        agree = Maketing(self.driver)
        agree.get_info_page()
        agree.send_keys_check_password()
        agree.click(agree.confirm_btn)
        time.sleep(1)
        agree.click(agree.phone)
        time.sleep(1)
        agree.click(agree.email)
        time.sleep(1)
        agree.click(agree.push)
        time.sleep(1)
        agree.click(agree.save_btn)
        alert = agree.find_element(agree.alert_save_success).text
        self.assertEqual(alert, CustomerInfoAlert.save_success)