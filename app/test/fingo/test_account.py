import time
from selenium.webdriver.common.by import By
from pages.fingo.account import EmailSginIn, Verification, CustomerInfo, Maketing
from ..base import BaseTest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from . import CustomerInfoAlert, CustomerInfoStatus

# class TestSginin(BaseTest):
#     def test_1_signin(self):
#         email_signin = EmailSginIn(self.driver)
#         email_signin.get(email_signin.signin_url)
#         time.sleep(2)
#         email_signin.get_login_page()
#         email_signin.send_keys_email()
#         email_signin.send_keys_password()
#         email_signin.click(email_signin.login_btn)
#         time.sleep(2)
#         self.assertEqual(self.driver.current_url, "https://qa.fingo.run/")

# class TestVerificatin(BaseTest):
    # def test_1_email_verification(self):
    #     confirm_email = Verification(self.driver)
    #     confirm_email.get(confirm_email.main_url)
    #     confirm_email.click(confirm_email.wallet_btn)
    #     confirm_email.click(confirm_email.deposit_withdraw_btn)
    #     status = confirm_email.find_element(confirm_email.email_confirm_status).text
    #     # time.sleep(2)

    #     if status == '인증완료':
    #         print("이메일 인증이 완료된 계정입니다.")
    #     else:
    #         confirm_email.click(confirm_email.email_confirm_btn)
    #         confirm_email.click(confirm_email.email_confirm_status)
    #         confirm_email.send_keys_resident_num()
    #         confirm_email.click(confirm_email.agree_btn)
    #         confirm_email.click(confirm_email.next_btn)

    #     self.assertEqual(status, "인증완료")
    #     self.assertEqual(self.driver.current_url, "https://qa.fingo.run/wallet?tab=account")

    # def test_2_account_verification(self):
    #     confirm_account = Verification(self.driver)
    #     confirm_account.get(confirm_account.main_url)
    #     confirm_account.click(confirm_account.wallet_btn)
    #     confirm_account.click(confirm_account.deposit_withdraw_btn)
    #     status = confirm_account.find_element(confirm_account.account_confirm_status).text
    #     time.sleep(2)

    #     if status == "인증완료":
    #         print("계좌 인증이 완료된 계정입니다.")
    #     else:
    #         confirm_account.click(confirm_account.account_confirm_btn)
    #         confirm_account.click(confirm_account.open_bank_list_btn)
    #         source = confirm_account.find_element(confirm_account.bank_list)
    #         action = ActionChains(self.driver)
    #         action.move_to_element(source).perform()
    #         for _ in range(10):
    #             action.send_keys(Keys.PAGE_DOWN).perform()
    #             try:
    #                 # 국민은행 클릭
    #                 element = self.driver.find_element(By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div[2]/div[2]/div/div/div[12]')
    #                 element.click()
    #                 break
    #             except Exception:
    #                 print('은행 찾는 중..')
    #             time.sleep(2)
    #         confirm_account.send_keys_account_num()
    #         confirm_account.click(confirm_account.account_vertification_btn)
    #         confirm_account.click(confirm_account.save_btn)
    #         alert = confirm_account.find_element(confirm_account.alert_save_success).text
    #         self.assertEqual(alert, CustomerInfoAlert.save_success)
    #         confirm_account.get(confirm_account.account_url)
    #         result = confirm_account.find_element(confirm_account.account_confirm_status).text
    #         self.assertEqual(result, CustomerInfoStatuscomplete)


# class TestCustomerInfo(BaseTest):
#     def test_1_customer_info(self):
#         customer_info = CustomerInfo(self.driver)
#         customer_info.get_main_page()
#         customer_info.click(customer_info.mypage_btn)
#         time.sleep(1)
#         customer_info.click(customer_info.customer_info_btn)
#         customer_info.send_keys_check_password()
#         customer_info.click(customer_info.confirm_btn)
#         time.sleep(1)
#         self.assertEqual(self.driver.current_url, CustomerInfo.info_url)

#     def test_2_change_password(self):
#         change_password = CustomerInfo(self.driver)
#         change_password.click(change_password.password_change_btn)
#         change_password.send_keys_origin_password()
#         change_password.send_keys_new_password()
#         change_password.send_keys_confirm_new_password()
#         time.sleep(2)
#         change_password.click(change_password.password_save_btn)
#         alert = change_password.find_element(change_password.confirm_alert_msg).text
#         self.assertEqual(alert, CustomerInfoAlert.password_change_success)

#     def test_3_reset_password(self):
#         reset_origin_password = CustomerInfo(self.driver)
#         reset_origin_password.get_main_page()
#         reset_origin_password.click(reset_origin_password.mypage_btn)
#         time.sleep(2)
#         reset_origin_password.click(reset_origin_password.customer_info_btn)
#         reset_origin_password.send_keys_check_password2()
#         reset_origin_password.click(reset_origin_password.confirm_btn)
#         reset_origin_password.click(reset_origin_password.password_change_btn)
#         time.sleep(2)
#         reset_origin_password.send_keys_orgin_password2()
#         reset_origin_password.send_keys_new_password2()
#         reset_origin_password.send_keys_confirm_new_password2()
#         time.sleep(2)
#         reset_origin_password.click(reset_origin_password.password_save_btn)
#         alert = reset_origin_password.find_element(reset_origin_password.confirm_alert_msg).text
#         self.assertEqual(alert, CustomerInfoAlert.password_change_success)


# class TestMaketing(BaseTest):
#     def test_1_maketing_agree(self):
#         agree = Maketing(self.driver)
#         agree.get_info_page()
#         agree.send_keys_check_password()
#         agree.click(agree.confirm_btn)
#         time.sleep(1)
#         agree.click(agree.phone)
#         time.sleep(1)
#         agree.click(agree.email)
#         time.sleep(1)
#         agree.click(agree.push)
#         time.sleep(1)
#         agree.click(agree.save_btn)
#         alert = agree.find_element(agree.alert_save_success).text
#         self.assertEqual(alert, CustomerInfoAlert.save_success)

