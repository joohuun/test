import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

# from pages.fingo.account import Verification
from pages.fingo.wallet import Account
from config.fingo import fingo_base_url, fingo_prod_url
from .. import CustomerInfoAlert, CustomerInfoStatus, DepositStatus, WithdrawAlert
from ...base import FingoBase, FingoProdBase
# from .. import DepositStatus, WithdrawAlert

# class TestDeposit(FingoProdBase):
#     def test_1_get_prod_page(self):
#         self.driver.get(fingo_prod_url)

#     def test_2_출금(self):
#         deposit = Account(self.driver)
#         deposit.get_prod_login_page()
#         deposit.send_keys_email()
#         deposit.send_keys_password()
#         time.sleep(3)
#         deposit.click(deposit.login_btn)
#         time.sleep(3)

#         deposit.get_prod_account_page()
#         status = deposit.find_element(deposit.deposit_status).text
#         if status == DepositStatus.progress:
#             print('진행중인 입금대기가 있습니다')
#         else:
#             deposit.click(deposit.deposit_amount)
#             deposit.click(deposit.deposit_btn)
#             deposit.click(deposit.select_bank_option)
#             deposit.click(deposit.select_bank)
#             deposit.click(deposit.deposit_confirm_btn)
#             result = deposit.find_element(deposit.deposit_status).text
#             self.assertEqual(result, DepositStatus.progress)


# class TestWithdraw(FingoBase):
#     def test_1_get_session(self):
#         self.driver.get(fingo_base_url)

#     def test_2_입금(self):
#         withdraw = Account(self.driver)
#         withdraw.get_account_page()
#         withdraw.click(withdraw.withdraw_btn)
#         time.sleep(4)
#         withdraw.click(withdraw.withdraw_amount)
#         time.sleep(4)
#         withdraw.click(withdraw.withdraw_btn_2)
#         time.sleep(4)
#         withdraw.click(withdraw.request_auth_num_btn)
#         time.sleep(4)
#         alert = withdraw.find_element(withdraw.sms_alert_message).text
#         self.assertEqual(alert, WithdrawAlert.request_alert)


class TestVerificatin(FingoBase):
    def test_1_get_session(self):
        self.driver.get(fingo_base_url)

    # 실명인증
    def test_2_실명인증(self):
        confirm_email = Account(self.driver)
        confirm_email.get_account_page()
        status = confirm_email.find_element(confirm_email.email_confirm_status).text
        print(status)
        time.sleep(2)

        if status == CustomerInfoStatus.complete:
            print("실명 인증이 완료된 계정입니다.")
        else:
            confirm_email.click(confirm_email.email_confirm_btn)
            confirm_email.send_keys_resident_num()
            confirm_email.click(confirm_email.agree_btn)
            confirm_email.click(confirm_email.next_btn)

            self.assertEqual(status, CustomerInfoStatus.complete)
            self.assertEqual(self.driver.current_url, Account.account_url)

    # 계좌인증
    def test_3_계좌인증(self):
        confirm_account = Account(self.driver)
        confirm_account.get_account_page()
        status = confirm_account.find_element(confirm_account.account_confirm_status).text
        time.sleep(2)

        if status == CustomerInfoStatus.complete:
            print("계좌 인증이 완료된 계정입니다.")
        else:
            confirm_account.click(confirm_account.account_confirm_btn)
            confirm_account.click(confirm_account.open_bank_list_btn)
            source = confirm_account.find_element(confirm_account.bank_list)
            action = ActionChains(self.driver)
            action.move_to_element(source).perform()
            for _ in range(5):
                action.send_keys(Keys.PAGE_DOWN).perform()
                try:
                    # 국민은행 클릭
                    element = self.driver.find_element(By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div[2]/div[2]/div/div/div[12]')
                    element.click()
                    break
                except Exception:
                    print('은행 찾는 중.')
                time.sleep(2)
            confirm_account.send_keys_account_num()
            confirm_account.click(confirm_account.account_vertification_btn)
            confirm_account.click(confirm_account.save_btn)
            alert = confirm_account.find_element(confirm_account.alert_save_success).text
            self.assertEqual(alert, CustomerInfoAlert.save_success)
            confirm_account.get(confirm_account.account_url)
            result = confirm_account.find_element(confirm_account.account_confirm_status).text
            self.assertEqual(result, CustomerInfoStatus.complete)








