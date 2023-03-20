from selenium.webdriver.common.by import By
from pages.base import Base
from selenium.webdriver.common.keys import Keys
from config.tower import (
    tower_base_url,
    ProductData,
    CopyrightData,
)


class ProductList(Base):
    main_url = tower_base_url
    product_list_url = f"{tower_base_url}product/list"

    search_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[2]/button')
    status_sale = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[1]/div/div/label[2]/span[2]') 
    status_wait = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[1]/div/div/label[3]/span[2]')
    status_stop = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[1]/div/div/label[4]/span[2]')
    status = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[3]/div[1]/div[2]/div[2]/div/div/div/div/div/div[1]/div[13]/div')
    category_hiphop = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[2]/div/label[2]/span[2]')
    category_balad = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[2]/div/label[3]/span[2]')
    category_dance = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[2]/div/label[8]/span[2]')
    category = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[3]/div[1]/div[2]/div[2]/div/div/div/div/div/div[1]/div[3]/a')
    product = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[3]/div[1]/div[2]/div[2]/div/div/div/div/div/div[1]/div[1]/span/span[1]')
    product_status_sale = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[2]/div/div/div/div/label[1]/span[2]')
    product_status_wait = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[2]/div/div/div/div/label[2]/span[2]')
    product_status_stop = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[2]/div/div/div/div/label[3]/span[2]')
    apply_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[2]/div/div/button')
    product_status = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[3]/div[1]/div[2]/div[2]/div/div/div/div/div/div[1]/div[13]/div')

    def __init__(self, driver):
        super(ProductList, self).__init__(driver)

    def get_main_page(self):
        self.get(self.main_url)

    def get_product_list_page(self):
        self.get(self.product_list_url)


class ProductCreate(Base):
    main_url = tower_base_url
    product_create_url = f"{tower_base_url}product/create"
    select_copyright_option = (By.XPATH, '//*[@id="mui-component-select-copyrights0"]')
    select_copyright = (By.CSS_SELECTOR, '#menu-copyrights0 > div.MuiPaper-root.MuiMenu-paper.MuiPopover-paper.MuiPaper-elevation8.MuiPaper-rounded > ul > li:nth-child(80)')
    price_input = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/div[2]/div[1]/div/input')
    amount_input = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/div[2]/div[2]/div/input')
    create_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[2]/button')
    alert_msg = (By.XPATH, '/html/body/div[2]/div[3]/div[1]/p')
    
    create_success_alert = (By.CSS_SELECTOR, '#root > div.jss11 > div > div.MuiAlert-message')

    def __init__(self, driver):
        super(ProductCreate, self).__init__(driver)

    def get_main_page(self):
        self.get(self.main_url)

    def get_product_create_page(self):
        self.get(self.product_create_url)

    def send_keys_product_price(self):
        self.send_keys(self.price_input, ProductData.product_price)

    def send_keys_product_amount(self):
        self.send_keys(self.amount_input, ProductData.product_amount)

    
class CopyrightList(Base):
    main_url = tower_base_url
    copyright_list_url = f"{tower_base_url}product/copyrights"

    search_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[2]/button')
    search_input_copyright_id = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[1]/div[1]/div/div[2]/div/input')
    result_copyright_id = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[4]/div[2]/div/div[1]/table/tbody/tr/td[1]/span/a')
    category = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[4]/div[2]/div/div[1]/table/tbody/tr[1]/td[2]/span/a')
    category_hiphop = (By.CSS_SELECTOR, '#root > div.jss1 > div.jss28 > div > div.MuiPaper-root.jss30.MuiPaper-outlined.MuiPaper-rounded > div.MuiBox-root.jss38.jss31 > div:nth-child(2) > div > div.MuiFormControl-root > div > label:nth-child(2) > span.MuiButtonBase-root.MuiIconButton-root.jss44.MuiCheckbox-root.MuiCheckbox-colorSecondary.MuiIconButton-colorSecondary > span.MuiIconButton-label')
    category_balad = (By.CSS_SELECTOR, '#root > div.jss1 > div.jss28 > div > div.MuiPaper-root.jss30.MuiPaper-outlined.MuiPaper-rounded > div.MuiBox-root.jss38.jss31 > div:nth-child(2) > div > div.MuiFormControl-root > div > label:nth-child(3) > span.MuiButtonBase-root.MuiIconButton-root.jss44.MuiCheckbox-root.MuiCheckbox-colorSecondary.MuiIconButton-colorSecondary > span.MuiIconButton-label')
    category_dance = (By.CSS_SELECTOR, '#root > div.jss1 > div.jss28 > div > div.MuiPaper-root.jss30.MuiPaper-outlined.MuiPaper-rounded > div.MuiBox-root.jss38.jss31 > div:nth-child(2) > div > div.MuiFormControl-root > div > label:nth-child(8) > span.MuiButtonBase-root.MuiIconButton-root.jss44.MuiCheckbox-root.MuiCheckbox-colorSecondary.MuiIconButton-colorSecondary > span.MuiIconButton-label')

    def __init__(self, driver):
        super(CopyrightList, self).__init__(driver)

    def get_main_page(self):
        self.get(self.main_url)

    def get_copyright_list_page(self):
        self.get(self.copyright_list_url)

    def send_keys_categroy_id(self):
        self.send_keys(self.search_input_copyright_id, CopyrightData.copyrigt_id)


class CopyrightCretate(Base):
    main_url = tower_base_url
    copyright_create_url = f"{tower_base_url}product/copyright-create"
    copyright_id_input = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[3]/div[1]/div/div/input')
    copyright_name_input = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[3]/div[2]/div/div[1]/div[1]/div/input')
    copyrignt_singer_input = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[3]/div[2]/div/div[1]/div[2]/div/input')
    copyright_yield_rate1_input =(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[3]/div[3]/div/div[1]/div[2]/div[1]/div/input')
    copyright_yield_rate2_input =(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[3]/div[3]/div/div[1]/div[2]/div[2]/div/input')
    youtube_url_input = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[3]/div[3]/div/div[2]/div[1]/div/input')
    yotube_description_input = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[3]/div[3]/div/div[2]/div[2]/div[2]/div[1]/p')
    composer_input = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[3]/div[4]/div/div[1]/div[2]/div/input')
    lyricist_input = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[3]/div[4]/div/div[2]/div[1]/div/input')
    arranger_input = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[3]/div[4]/div/div[2]/div[2]/div/input')
    create_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[4]/button')
    create_alert_mgs = (By.XPATH, '/div/div[2]')
    create_alert_mgs = (By.CSS_SELECTOR, '#root > div.jss11')
    duple_alert_msg = (By.XPATH, '/div/div[2]')
    duple_alert_msg = (By.CSS_SELECTOR, '#root > div.jss11')

    def __init__(self, driver):
        super(CopyrightCretate, self).__init__(driver)

    def get_main_page(self):
        self.get(self.main_url)

    def get_copyright_create_page(self):
        self.get(self.copyright_create_url)

    def send_keys_copyrigt_id(self):
        self.send_keys(self.copyright_id_input, CopyrightData.copyright_id2)

    def send_keys_duplicated_copyright_id(self):
        self.send_keys(self.copyright_id_input, CopyrightData.duple_copyright_id)

    def send_keys_copyright_name(self):
        self.send_keys(self.copyright_name_input, CopyrightData.copyright_name)

    def send_keys_copyright_singer(self):
        self.send_keys(self.copyrignt_singer_input, CopyrightData.copyrignt_singer)

    def send_keys_copyright_yield_rate1(self):
        self.send_keys(self.copyright_yield_rate1_input, CopyrightData.copyright_yield_rate1)

    def send_keys_copyright_yield_rate2(self):
        self.send_keys(self.copyright_yield_rate2_input, CopyrightData.copyright_yield_rate2)

    def send_keys_youtube_url(self):
        self.send_keys(self.youtube_url_input, CopyrightData.youtube_url)

    def send_keys_yotube_description(self):
        self.send_keys(self.yotube_description_input, CopyrightData.yotube_description)

    def send_keys_composer(self):
        self.send_keys(self.composer_input, CopyrightData.composer)

    def send_keys_lyricist(self):
        self.send_keys(self.lyricist_input, CopyrightData.lyricist)

    def send_keys_arranger(self):
        self.send_keys(self.arranger_input, CopyrightData.arranger)








