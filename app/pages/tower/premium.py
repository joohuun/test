from selenium.webdriver.common.by import By
from pages.base import Base
from selenium.webdriver.common.keys import Keys
from config.tower import (
    tower_base_url,
)
from config.tower import PremiumProductData, PremiumCopyrightData



class PremiumProductList(Base):
    main_url = tower_base_url
    premium_product_list_url = f'{tower_base_url}premium/list'
    status_sale = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[1]/div/div/label[2]')
    status_wait = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[1]/div/div/label[3]')
    status_stop = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[1]/div/div/label[4]')

    category_hiphop = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[2]/div/label[2]')
    category_balad = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[2]/div/label[3]')

    premium_product = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[3]/div[1]/div[2]/div[2]/div/div/div/div/div/div[1]/div[1]/span/span[1]')
    premium_product = (By.CSS_SELECTOR, '#root > div.jss1 > div.jss28 > div > div.MuiPaper-root.jss46.MuiPaper-elevation1.MuiPaper-rounded > div.MuiDataGrid-root.MuiDataGrid-root.jss47.MuiDataGrid-autoHeight > div.MuiDataGrid-main > div:nth-child(2) > div > div > div > div > div > div:nth-child(1) > div.MuiDataGrid-cell.MuiDataGrid-cellCheckbox.MuiDataGrid-cellWithRenderer.MuiDataGrid-cellCenter > span > span.MuiIconButton-label')
    update_status_sale = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[2]/div/div/div/div/label[1]/span[1]/span[1]')
    update_status_wait = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[2]/div/div/div/div/label[2]/span[1]/span[1]')
    update_status_stop = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[2]/div/div/div/div/label[3]/span[1]/span[1]')
    status_result = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[3]/div[1]/div[2]/div[2]/div/div/div/div/div/div[1]/div[13]/div')

    status_apply_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[2]/div/div/button')
    
    search_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[2]/button')
    def __init__(self, driver):
        super(PremiumProductList, self).__init__(driver)

    def get_main_page(self):
        self.get(self.main_url)

    def get_premium_product_list_page(self):
        self.get(self.premium_product_list_url)


class PremiumProductCreate(Base):
    main_url = tower_base_url
    premium_product_create_url = f'{tower_base_url}premium/create'
    option_premium_copyright = (By.XPATH, '//*[@id="mui-component-select-copyrights0"]')
    select_premium_copyright = (By.XPATH, '//*[@id="menu-copyrights0"]/div[3]/ul/li[36]')
    price_input = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/div[2]/div[1]/div/input')
    
    amount_input = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/div[2]/div[2]/div/input')
    create_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[2]/button')
    create_alert = (By.XPATH, '//*[@id="root"]/div[2]')

    create_fail_alert = (By.XPATH, '/html/body/div[2]/div[3]/div[1]/p')

    def __init__(self, driver):
        super(PremiumProductCreate, self).__init__(driver)

    def get_main_page(self):
        self.get(self.main_url)

    def get_premium_product_create_page(self):
        self.get(self.premium_product_create_url)

    def send_keys_premium_product_price(self):
        self.send_keys(self.price_input, PremiumProductData.premium_product_price)

    def send_keys_premium_product_amount(self):
        self.send_keys(self.amount_input, PremiumProductData.premium_product_amount)
    

class PremiumCopyrigtList(Base):
    premium_copyright_list_url = f'{tower_base_url}premium/copyrights'
    copyright_id_input = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[1]/div[1]/div/div[2]/div/input')
    copyright_id_result = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[4]/div[2]/div/div[1]/table/tbody/tr/td[1]/span/a')
    search_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[2]/button')

    category_hiphop = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/div[2]/div/label[2]')
    category_balad = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/div[2]/div/label[3]')
    category_result = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[4]/div[2]/div/div[1]/table/tbody/tr[1]/td[2]/span/a')


    search_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[2]/button')

    def __init__(self, driver):
        super(PremiumCopyrigtList, self).__init__(driver)
    
    def get_premium_copyright_list_page(self):
        self.get(self.premium_copyright_list_url)

    def send_keys_copyright_id(self):
        self.send_keys(self.copyright_id_input, PremiumCopyrightData.copyright_id)

    

    







