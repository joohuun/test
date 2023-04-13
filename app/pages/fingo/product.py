from selenium.webdriver.common.by import By
from config.fingo import gift_phone_num
from pages.base import Base
from selenium.webdriver.common.keys import Keys


class Product(Base):
    main_url = "https://qa.fingo.run/"

    wallet_btn = (By.XPATH, '//*[@id="root"]/div[6]/button[4]')

    recommand_product = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div/div[2]/div[1]/img')
    buy_btn = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[2]/button[2]')
    buy_quantity_value_10 = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/button[1]')
    buy_btn2 = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div[2]/div[4]/button[2]')
    buy_confirm_btn = (By.XPATH, '//*[@id="modal"]/div/div[2]/div[2]/button[2]')
    alert_buy_success = (By.XPATH, '//*[@id="modal"]/div/div[2]/div[1]/div[1]/div')

    
    sell_btn = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div/div[2]/div/div[2]/div[3]/div[2]/div/button')
    sell_quantity_value_10 = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div/div[2]/div[3]/div/button[1]')
    sell_quantity_value_100 = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div/div[2]/div[3]/div/button[5]')
    sell_btn2 = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div/div[2]/button')
    sell_btn3 = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div/div[2]/div[2]/button')
    sell_confirm_btn = (By.XPATH, '//*[@id="modal"]/div/div[2]/div[2]/button[2]')
    sell_result_message = (By.XPATH, '//*[@id="modal"]/div/div[2]/div[1]/div[2]')

    gift_btn = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[2]/button[1]')
    # gift_btn = (By.CSS_SELECTOR, '#root > div.ptr.overflow > div.ptr__children > div.router__container > div.productScreen__footer > button:nth-child(1)')
    gift_quantity_value_10 = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/button[1]')
    gift_phone_input = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div[2]/div[3]/div/div[2]/div/input')
    gift_btn2 = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div[2]/div[5]/button[2]')
    gift_confirm_btn = (By.XPATH, '//*[@id="modal"]/div/div[2]/div[2]/button[2]')
    gift_result_message = (By.XPATH, '//*[@id="modal"]/div/div[2]/div[1]/div[1]/div')

    def __init__(self, driver):
        super(Product, self).__init__(driver)

    def get_login_page(self):
        self.get(self.signin_url)

    def send_keys_buy_btn2(self):
        self.send_keys(self.buy_btn2, Keys.ENTER)

    def send_keys_sell_btn(self):
        self.send_keys(self.sell_btn, Keys.ENTER)

    def send_keys_sell_btn2(self):
        self.send_keys(self.sell_btn2, Keys.ENTER)

    def send_keys_gift_btn(self):
        self.send_keys(self.gift_btn, Keys.ENTER)

    def send_keys_gift_phone_num(self):
        self.send_keys(self.gift_phone_input, gift_phone_num)

    def send_keys_gift_btn2(self):
        self.send_keys(self.gift_btn2, Keys.ENTER)