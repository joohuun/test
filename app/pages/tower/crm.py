from selenium.webdriver.common.by import By
from pages.base import Base
from selenium.webdriver.common.keys import Keys
from config.data import crm_content_body, crm_content_title, news_link, crm_content_title_update, crm_content_body_update, news_link_udpate


class Notice(Base):
    main_url = 'http://10.2.1.100:5001/tower/'
    notice_list_url = 'http://10.2.1.100:5001/tower/service/list?tab=0'
    menu_list = (By.XPATH, '//*[@id="root"]/div[1]/header/div/button[1]')
    crm_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/ul/div[10]')
    crm_content_type_news = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[3]/div[1]/div/div/label[2]/span[2]')
    crm_content_create = (By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/ul/div[11]/div/div/div/div[1]')
    crm_content_list = (By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/ul/div[11]/div/div/div/div[2]')
    crm_content_title_input = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[3]/div[2]/div/div/div/input')
    crm_content_body_input = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[3]/div[3]/div/div/div[2]/div[1]')
    crm_content_create_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[3]/div[4]/button')
    crm_content_create_confirm_btn = (By.XPATH, '/html/body/div[2]/div[3]/div[3]/div/button[2]')
    crm_content_create_alert_msg = (By.XPATH, '//*[@id="root"]/div[2]')
    crm_top_content = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[3]/div[1]/div[2]/div[2]/div/div/div/div/div/div[1]/div[1]')
    content_post_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[1]/div/div/label[1]')
    content_wait_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[1]/div/div/label[2]')                                  
    content_delete_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[1]/div/div/label[3]')
    content_status_btn = (By.CSS_SELECTOR, '#root > div.jss1 > div.jss28 > div > div.jss30 > div.MuiBox-root.jss45.jss32 > div > button')
    status_alert_msg = (By.CSS_SELECTOR, 'div > div.MuiAlert-message')
    status_result = (By.CSS_SELECTOR, '#root > div.jss1 > div.jss28 > div > div.jss30 > div.MuiPaper-root.jss37.MuiPaper-elevation1.MuiPaper-rounded > div.MuiDataGrid-root.MuiDataGrid-root.jss38.MuiDataGrid-autoHeight > div.MuiDataGrid-main > div:nth-child(2) > div > div > div > div > div > div:nth-child(1) > div:nth-child(6) > div')
    crm_top_content_detail = (By.CSS_SELECTOR, '#root > div.jss1 > div.jss28 > div > div.jss30 > div.MuiPaper-root.jss37.MuiPaper-elevation1.MuiPaper-rounded > div.MuiDataGrid-root.MuiDataGrid-root.jss38.MuiDataGrid-autoHeight > div.MuiDataGrid-main > div:nth-child(2) > div > div > div > div > div > div:nth-child(1) > div:nth-child(4) > a')


    def __init__(self, driver):
        super(Notice, self).__init__(driver)

    def get_main_page(self):
        self.get(self.main_url)

    def get_notice_list_url(self):
        self.get(self.notice_list_url)   

    def send_keys_notice_title(self):
        self.send_keys(self.crm_content_title_input, crm_content_title)
    
    def send_keys_notice_body(self):
        self.send_keys(self.crm_content_body_input, crm_content_body)

    def send_keys_notice_title_update(self):
        self.send_keys(self.crm_content_title_input, crm_content_title_update)
    
    def send_keys_notice_body_update(self):
        self.send_keys(self.crm_content_body_input, crm_content_body_update)


class News(Base):
    main_url = 'http://10.2.1.100:5001/tower/'
    news_list_url = 'http://10.2.1.100:5001/tower/service/list?tab=1'
    menu_list = (By.XPATH, '//*[@id="root"]/div[1]/header/div/button[1]')
    crm_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/ul/div[10]')
    crm_content_type_news = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[3]/div[1]/div/div/label[2]/span[2]')
    crm_content_create = (By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/ul/div[11]/div/div/div/div[1]')
    crm_content_list = (By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/ul/div[11]/div/div/div/div[2]')
    crm_content_title_input = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[3]/div[2]/div/div/div/input')
    crm_news_link_input = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[3]/div[3]/div/div/div/input')
    crm_content_create_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[3]/div[4]/button')
    crm_content_create_confirm_btn = (By.XPATH, '/html/body/div[2]/div[3]/div[3]/div/button[2]')
    crm_content_create_alert_msg = (By.XPATH, '//*[@id="root"]/div[2]')
    crm_top_content = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[3]/div[1]/div[2]/div[2]/div/div/div/div/div/div[1]/div[1]')
    content_post_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[1]/div/div/label[1]')
    content_wait_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[1]/div/div/label[2]')                                  
    content_delete_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[1]/div/div/label[3]')
    content_status_btn = (By.CSS_SELECTOR, '#root > div.jss1 > div.jss28 > div > div.jss30 > div.MuiBox-root.jss45.jss32 > div > button')
    status_alert_msg = (By.CSS_SELECTOR, 'div > div.MuiAlert-message')
    status_result = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[3]/div[1]/div[2]/div[2]/div/div/div/div/div/div[1]/div[7]/div')
    crm_top_content_detail = (By.CSS_SELECTOR, '#root > div.jss1 > div.jss28 > div > div.jss30 > div.MuiPaper-root.jss37.MuiPaper-elevation1.MuiPaper-rounded > div.MuiDataGrid-root.MuiDataGrid-root.jss38.MuiDataGrid-autoHeight > div.MuiDataGrid-main > div:nth-child(2) > div > div > div > div > div > div:nth-child(1) > div:nth-child(4) > a')


    def __init__(self, driver):
        super(News, self).__init__(driver)

    def get_main_page(self):
        self.get(self.main_url)

    def get_news_list_url(self):
        self.get(self.news_list_url)  
    
    def send_keys_news_title(self):
        self.send_keys(self.crm_content_title_input, crm_content_title)

    def send_keys_news_link(self):
        self.send_keys(self.crm_news_link_input, news_link)

    def send_keys_news_title_update(self):
        self.send_keys(self.crm_content_title_input, crm_content_title_update)
    
    def send_keys_news_link_update(self):
        self.send_keys(self.crm_news_link_input, news_link_udpate)
        
    
class FAQ(Base):
    main_url = 'http://10.2.1.100:5001/tower/'
    faq_list_url = 'http://10.2.1.100:5001/tower/service/list?tab=2'
    menu_list = (By.XPATH, '//*[@id="root"]/div[1]/header/div/button[1]')
    crm_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/ul/div[10]')
    crm_content_create = (By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/ul/div[11]/div/div/div/div[1]')
    crm_content_title_input = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[3]/div[2]/div/div/div/input')
    crm_content_body_input = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[3]/div[3]/div/div/div[2]/div[1]')
    crm_content_create_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[3]/div[5]/button')
    crm_content_create_confirm_btn = (By.XPATH, '/html/body/div[2]/div[3]/div[3]/div/button[2]')
    crm_content_create_alert_msg = (By.XPATH, '//*[@id="root"]/div[2]')
    crm_content_type_faq = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[3]/div[1]/div/div/label[3]/span[2]')
    crm_faq_title_input = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[3]/div[3]/div/div/div/input')
    crm_faq_booy_input = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[3]/div[4]/div/div/div[2]/div[1]')
    crm_top_content = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[3]/div[1]/div[2]/div[2]/div/div/div/div/div/div[1]/div[1]')
    content_post_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[1]/div/div/label[1]')
    content_wait_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[1]/div/div/label[2]')                                  
    content_delete_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[1]/div/div/label[3]')
    content_status_btn = (By.CSS_SELECTOR, '#root > div.jss1 > div.jss28 > div > div.jss30 > div.MuiBox-root.jss45.jss32 > div > button')
    status_alert_msg = (By.CSS_SELECTOR, 'div > div.MuiAlert-message')
    status_result = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[3]/div[1]/div[2]/div[2]/div/div/div/div/div/div[1]/div[7]/div')
    crm_top_content_detail = (By.CSS_SELECTOR, '#root > div.jss1 > div.jss28 > div > div.jss30 > div.MuiPaper-root.jss37.MuiPaper-elevation1.MuiPaper-rounded > div.MuiDataGrid-root.MuiDataGrid-root.jss38.MuiDataGrid-autoHeight > div.MuiDataGrid-main > div:nth-child(2) > div > div > div > div > div > div:nth-child(1) > div:nth-child(4) > a')


    def __init__(self, driver):
        super(FAQ, self).__init__(driver)

    def get_main_page(self):
        self.get(self.main_url)
    
    def get_faq_list_url(self):
        self.get(self.faq_list_url)

    def send_keys_faq_title(self):
        self.send_keys(self.crm_faq_title_input, crm_content_title)

    def send_keys_faq_body(self):
        self.send_keys(self.crm_faq_booy_input, crm_content_body)

    def send_keys_faq_title_update(self):
        self.send_keys(self.crm_faq_title_input, crm_content_title_update)

    def send_keys_faq_body_update(self):
        self.send_keys(self.crm_faq_booy_input, crm_content_body_update)


class Guide(Base):
    main_url = 'http://10.2.1.100:5001/tower/'
    guide_url = 'http://10.2.1.100:5001/tower/service/list?tab=3'
    menu_list = (By.XPATH, '//*[@id="root"]/div[1]/header/div/button[1]')
    crm_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/ul/div[10]')
    crm_content_create = (By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/ul/div[11]/div/div/div/div[1]')
    crm_content_list = (By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/ul/div[11]/div/div/div/div[2]')
    crm_content_title_input = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[3]/div[2]/div/div/div/input')
    crm_content_body_input = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[3]/div[3]/div/div/div[2]/div[1]')
    crm_content_create_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[3]/div[4]/button')
    crm_content_create_confirm_btn = (By.XPATH, '/html/body/div[2]/div[3]/div[3]/div/button[2]')
    crm_content_create_alert_msg = (By.XPATH, '//*[@id="root"]/div[2]')
    crm_content_type_guide = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[3]/div[1]/div/div/label[4]/span[2]')
    crm_top_content = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[3]/div[1]/div[2]/div[2]/div/div/div/div/div/div[1]/div[1]')
    content_post_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[1]/div/div/label[1]')
    content_wait_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[1]/div/div/label[2]')                                  
    content_delete_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[1]/div/div/label[3]')
    content_status_btn = (By.CSS_SELECTOR, '#root > div.jss1 > div.jss28 > div > div.jss30 > div.MuiBox-root.jss45.jss32 > div > button')
    status_alert_msg = (By.CSS_SELECTOR, 'div > div.MuiAlert-message')
    status_result = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[3]/div[1]/div[2]/div[2]/div/div/div/div/div/div[1]/div[7]/div')
    crm_top_content_detail = (By.CSS_SELECTOR, '#root > div.jss1 > div.jss28 > div > div.jss30 > div.MuiPaper-root.jss37.MuiPaper-elevation1.MuiPaper-rounded > div.MuiDataGrid-root.MuiDataGrid-root.jss38.MuiDataGrid-autoHeight > div.MuiDataGrid-main > div:nth-child(2) > div > div > div > div > div > div:nth-child(1) > div:nth-child(4) > a')


    def __init__(self, driver):
        super(Guide, self).__init__(driver)

    def get_main_page(self):
        self.get(self.main_url)

    def get_guide_list_url(self):
        self.get(self.guide_url)
    
    def send_keys_guide_title(self):
        self.send_keys(self.crm_content_title_input, crm_content_title)
    
    def send_keys_guide_body(self):
        self.send_keys(self.crm_content_body_input, crm_content_body)

    def send_keys_guide_title_update(self):
        self.send_keys(self.crm_content_title_input, crm_content_title_update)

    def send_keys_guide_body_update(self):
        self.send_keys(self.crm_content_body_input, crm_content_body_update)
