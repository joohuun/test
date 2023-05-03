from selenium.webdriver.common.by import By
from config.fingo import gift_phone_num, fingo_base_url
from pages.base import Base
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Product(Base):
    main_url = fingo_base_url
    wallet_btn = (By.XPATH, '//*[@id="root"]/div[6]/button[4]')
    # //*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div/div[2]/div[1]/img[2]
    # #root > div.ptr.overflow > div.ptr__children > div.router__container > div.landingScreen__container > div:nth-child(3) > div.landingScreen__componentWrapper > div.indiana-scroll-container.indiana-scroll-container--hide-scrollbars > div > div:nth-child(2) > div.card__pos > img.card__thumbnail
    # recommand_product = (By.CSS_SELECTOR, '#root > div.ptr.overflow > div.ptr__children > div.router__container > div.landingScreen__container > div:nth-child(3) > div.landingScreen__componentWrapper > div.indiana-scroll-container.indiana-scroll-container--hide-scrollbars > div > div:nth-child(2) > div.card__pos > img.card__thumbnail')
    recommand_product = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div/div[2]/div[1]/img[2]')
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
    gift_quantity_value_10 = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/button[1]')
    gift_phone_input = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div[2]/div[3]/div/div[2]/div/input')
    gift_btn2 = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div[2]/div[5]/button[2]')
    gift_confirm_btn = (By.XPATH, '//*[@id="modal"]/div/div[2]/div[2]/button[2]')
    gift_result_message = (By.XPATH, '//*[@id="modal"]/div/div[2]/div[1]/div[1]/div')


    def __init__(self, driver):
        super(Product, self).__init__(driver)

    def get_main_page(self):
        self.get(self.main_url)

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


class Premium(Base):
    main_url = fingo_base_url
    # .landingScreen__repeater__container__premium 
    # .swiper-slide.swiper-slide-active
    premium_item = (By.CSS_SELECTOR, '.swiper-slide.swiper-slide-active')
    # //*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div[2]/div[2]/div/div
    # //*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div[2]
    # //*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div[2]/div[2]/div
    # //*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div[2]/div[2]/div/div
    premium_list = (By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div[1]/div[2]/div[2]/div/div')
    # premium_list = (By.CSS_SELECTOR, '#root > div.ptr.overflow > div.ptr__children > div.router__container > div.landingScreen__container > div.landingScreen__componentWrapper.landingScreen__componentWrapper__premium > div.landingScreen__repeater__container__premium')

    def __init__(self, driver):
        super(Premium, self).__init__(driver)

    def get_main_page(self):
        self.get(self.main_url)

    def scroll_horizontally(self, element, direction):
    # ActionChains 객체를 생성합니다.
        actions = ActionChains(self.driver)
        # element에 focus를 주기 위해 moveToElement를 호출합니다.
        actions.move_to_element(element)
        # direction에 따라 왼쪽 또는 오른쪽으로 스크롤합니다.
        if direction == "left":
            actions.key_down(Keys.SHIFT).send_keys(Keys.ARROW_LEFT).key_up(Keys.SHIFT).perform()
        elif direction == "right":
            actions.key_down(Keys.SHIFT).send_keys(Keys.ARROW_RIGHT).key_up(Keys.SHIFT).perform()
        elif direction == "down":
            actions.key_down(Keys.SHIFT).send_keys(Keys.PAGE_DOWN).key_up(Keys.SHIFT).perform()


    

