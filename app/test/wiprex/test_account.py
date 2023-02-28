import time
from selenium.webdriver.common.by import By
from pages.wiprex.account import EmailSginIn, ConfirmAccount, ConfirmEamil
from ..base import BaseTest



# chromeDriverPath = 'chrome_driver_path'
# driver = webdriver.Chrome(chromeDriverPath)

# class TestSginin(BaseTest):
#     def test_로그인(self):
#         email_signin = EmailSginIn(self.driver)
#         email_signin.get(email_signin.signin_url)
#         email_signin.send_keys_email_id()
#         email_signin.send_keys_email_pw()
#         email_signin.click(email_signin.login_btn)
#         time.sleep(2)
#         self.assertEqual(self.driver.current_url, "https://qa.wiprex.com/")


class TestConfirmEmail(BaseTest):
    def test_이메일인증(self):
        confirm_email = ConfirmEamil(self.driver)
        # confirm_email.get(confirm_email.signin_url)
        # confirm_email.send_keys_email_id()
        # confirm_email.send_keys_email_pw()
        # confirm_email.click(confirm_email.login_btn)
        # time.sleep(2)
        confirm_email.get(confirm_email.main_url)
        confirm_email.click(confirm_email.detail_btn)
        confirm_email.click(confirm_email.wallet_btn)
        confirm_email.click(confirm_email.deposit_withdraw_btn)
        status = confirm_email.find_element(confirm_email.email_confirm_status).text
        time.sleep(2)

        if status == '인증완료':
            print("인증이 완료된 계정입니다.")
        else:
            confirm_email.click(confirm_email.email_confirm_btn)
            confirm_email.click(confirm_email.email_confirm_status)
            confirm_email.send_keys_resident_num()
            confirm_email.click(confirm_email.check_resident_num_btn)
            confirm_email.click(confirm_email.verification_completed_btn)

        self.assertEqual(status, "인증완료")
        self.assertEqual(self.driver.current_url, "https://qa.wiprex.com/wallet?tab=account")


class TestConfirmAccount(BaseTest):
    def test_계좌인증(self):
        time.sleep(2)
        confrim_account = ConfirmAccount(self.driver)
        # confrim_account.get(confrim_account.signin_url)
        # confrim_account.send_keys_email_id()
        # confrim_account.send_keys_email_pw()
        # confrim_account.click(confrim_account.login_btn)
        # time.sleep(2)
        confrim_account.get(confrim_account.main_url)
        confrim_account.click(confrim_account.detail_btn)
        confrim_account.click(confrim_account.wallet_btn)
        confrim_account.click(confrim_account.deposit_withdraw_btn)
        time.sleep(2)

        confrim_account.click(confrim_account.account_confirm_btn)
        confrim_account.click(confrim_account.open_bank_list_btn)

        option = self.driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[4]/div[1]/div[2]/div[2]/div/div/div[12]')
        self.driver.execute_script("arguments[0].scrollIntoView();", option)
        option.click()
        confrim_account.send_keys_account_num()
        confrim_account.click(confrim_account.account_vertification_btn)
        status = confrim_account.find_element(confrim_account.account_confirm_status).text
        
        self.assertEqual(self.driver.current_url, "https://qa.wiprex.com/info")
        self.assertEqual(status, "변경하기")

        confrim_account.click(confrim_account.detail_btn)
        confrim_account.click(confrim_account.wallet_btn)
        confrim_account.click(confrim_account.deposit_withdraw_btn)

        status2 = confrim_account.find_element(confrim_account.account_confirm_status2).text

        self.assertEqual(self.driver.current_url, "https://qa.wiprex.com/wallet?tab=account")
        self.assertEqual(status2, "인증완료")
