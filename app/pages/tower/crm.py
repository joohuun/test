from selenium.webdriver.common.by import By
from pages.base import Base
from config.tower import (
    tower_base_url,
    CRMData,
)


class Notice(Base):
    main_url = tower_base_url
    notice_list_url = f'{tower_base_url}service/list?tab=0'
    noticle_create_url = f'{tower_base_url}service/create'
    title_input = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[2]/div/div/div/input')
    body_input = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]')
    create_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[4]/button')
    create_confirm_btn = (By.XPATH, '/html/body/div[2]/div[3]/div[3]/div/button[2]')
    create_success_alert = (By.XPATH, '//*[@id="root"]/div[2]')
    crm_top_content = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[3]/div[1]/div[2]/div[2]/div/div/div/div/div/div[1]/div[1]')
    content_post_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[1]/div/div/label[1]')
    content_wait_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[1]/div/div/label[2]')                                  
    content_delete_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[1]/div/div/label[3]')
    content_status_btn = (By.CSS_SELECTOR, '#root > div.jss1 > div.jss28 > div > div.jss30 > div.MuiBox-root.jss45.jss32 > div > button')
    status_alert_msg = (By.CSS_SELECTOR, 'div > div.MuiAlert-message')
    status_result = (By.CSS_SELECTOR, '#root > div.jss1 > div.jss28 > div > div.jss30 > div.MuiPaper-root.jss37.MuiPaper-elevation1.MuiPaper-rounded > div.MuiDataGrid-root.MuiDataGrid-root.jss38.MuiDataGrid-autoHeight > div.MuiDataGrid-main > div:nth-child(2) > div > div > div > div > div > div:nth-child(1) > div:nth-child(6) > div')
    crm_top_content_detail = (By.CSS_SELECTOR, '#root > div.jss1 > div.jss28 > div > div.jss30 > div.MuiPaper-root.jss37.MuiPaper-elevation1.MuiPaper-rounded > div.MuiDataGrid-root.MuiDataGrid-root.jss38.MuiDataGrid-autoHeight > div.MuiDataGrid-main > div:nth-child(2) > div > div > div > div > div > div:nth-child(1) > div:nth-child(4) > a')
    update_title_input = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[3]/div[2]/div/div/div/input')
    update_body_input = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[3]/div[3]/div/div/div[2]/div[1]')
    update_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[3]/div[4]/button')

    def __init__(self, driver):
        super(Notice, self).__init__(driver)

    def get_main_page(self):
        self.get(self.main_url)

    def get_notice_list_page(self):
        self.get(self.notice_list_url)   

    def get_noticle_create_page(self):
        self.get(self.noticle_create_url)

    def send_keys_notice_title(self):
        self.send_keys(self.title_input, CRMData.content_title)
    
    def send_keys_notice_body(self):
        self.send_keys(self.body_input, CRMData.content_body)

    def send_keys_notice_title_update(self):
        self.send_keys(self.update_title_input, CRMData.content_update_title)
    
    def send_keys_notice_body_update(self):
        self.send_keys(self.update_body_input, CRMData.content_update_body)


class News(Base):
    main_url = tower_base_url
    news_list_url = f'{tower_base_url}service/list?tab=1'
    news_create_url = f'{tower_base_url}service/create'
    type_news = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[1]/div/div/label[2]/span[1]/span[1]')
    news_title_input = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[2]/div/div/div/input')
    news_link_input = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[3]/div/div/div/input')
    news_create_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[4]/button')
    news_create_btn2 = (By.XPATH, '/html/body/div[2]/div[3]/div[3]/div/button[2]')
    create_success_alert = (By.XPATH, '//*[@id="root"]/div[2]')
    crm_top_content = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[3]/div[1]/div[2]/div[2]/div/div/div/div/div/div[1]/div[1]')
    content_post_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[1]/div/div/label[1]')
    content_wait_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[1]/div/div/label[2]')                                  
    content_delete_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[1]/div/div/label[3]')
    content_status_btn = (By.CSS_SELECTOR, '#root > div.jss1 > div.jss28 > div > div.jss30 > div.MuiBox-root.jss45.jss32 > div > button')
    status_alert_msg = (By.CSS_SELECTOR, 'div > div.MuiAlert-message')
    status_result = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[3]/div[1]/div[2]/div[2]/div/div/div/div/div/div[1]/div[7]/div')
    crm_top_content_detail = (By.CSS_SELECTOR, '#root > div.jss1 > div.jss28 > div > div.jss30 > div.MuiPaper-root.jss37.MuiPaper-elevation1.MuiPaper-rounded > div.MuiDataGrid-root.MuiDataGrid-root.jss38.MuiDataGrid-autoHeight > div.MuiDataGrid-main > div:nth-child(2) > div > div > div > div > div > div:nth-child(1) > div:nth-child(4) > a')
    news_update_title_input = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[3]/div[2]/div/div/div/input')
    news_update_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[3]/div[4]/button')

    def __init__(self, driver):
        super(News, self).__init__(driver)

    def get_main_page(self):
        self.get(self.main_url)

    def get_news_list_page(self):
        self.get(self.news_list_url)  

    def get_news_create_page(self):
        self.get(self.news_create_url)
    
    def send_keys_news_title(self):
        self.send_keys(self.news_title_input, CRMData.content_title)

    def send_keys_news_link(self):
        self.send_keys(self.news_link_input, CRMData.news_link)

    def send_keys_news_title_update(self):
        self.send_keys(self.news_update_title_input, CRMData.content_update_title)
    
    
class FAQ(Base):
    main_url = tower_base_url
    faq_list_url = f'{tower_base_url}service/list?tab=2'
    faq_create_url = f'{tower_base_url}service/create'
    type_faq = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[1]/div/div/label[3]/span[1]')
    title_input = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[3]/div/div/div/input')
    body_input = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[4]/div/div/div[2]/div[1]')
    create_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[5]/button')
    create_btn2 = (By.XPATH, '/html/body/div[2]/div[3]/div[3]/div/button[2]')
    create_success_alert = (By.XPATH, '//*[@id="root"]/div[2]')
    crm_top_content = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[3]/div[1]/div[2]/div[2]/div/div/div/div/div/div[1]/div[1]')
    content_post_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[1]/div/div/label[1]')
    content_wait_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[1]/div/div/label[2]')                                  
    content_delete_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[1]/div/div/label[3]')
    content_status_btn = (By.CSS_SELECTOR, '#root > div.jss1 > div.jss28 > div > div.jss30 > div.MuiBox-root.jss45.jss32 > div > button')
    status_alert_msg = (By.CSS_SELECTOR, 'div > div.MuiAlert-message')
    status_result = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[3]/div[1]/div[2]/div[2]/div/div/div/div/div/div[1]/div[7]/div')
    crm_top_content_detail = (By.CSS_SELECTOR, '#root > div.jss1 > div.jss28 > div > div.jss30 > div.MuiPaper-root.jss37.MuiPaper-elevation1.MuiPaper-rounded > div.MuiDataGrid-root.MuiDataGrid-root.jss38.MuiDataGrid-autoHeight > div.MuiDataGrid-main > div:nth-child(2) > div > div > div > div > div > div:nth-child(1) > div:nth-child(4) > a')
    update_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[3]/div[5]/button')
    update_title_input = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[3]/div[3]/div/div/div/input')
    update_body_input = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[3]/div[4]/div/div/div[2]/div[1]')

    def __init__(self, driver):
        super(FAQ, self).__init__(driver)

    def get_main_page(self):
        self.get(self.main_url)
    
    def get_faq_list_page(self):
        self.get(self.faq_list_url)

    def get_faq_create_page(self):
        self.get(self.faq_create_url)

    def send_keys_faq_title(self):
        self.send_keys(self.title_input, CRMData.content_title)

    def send_keys_faq_body(self):
        self.send_keys(self.body_input, CRMData.content_body)

    def send_keys_faq_title_update(self):
        self.send_keys(self.update_title_input, CRMData.content_update_title)

    def send_keys_faq_body_update(self):
        self.send_keys(self.update_body_input, CRMData.content_update_body)


class Guide(Base):
    main_url = tower_base_url
    guide_list_url = f'{tower_base_url}service/list?tab=3'
    guide_create_url = f'{tower_base_url}service/create'
    type_guide = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[1]/div/div/label[4]/span[2]')
    title_input = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[2]/div/div/div/input')
    body_input = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]')
    create_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[4]/button')
    create_btn2 = (By.XPATH, '/html/body/div[2]/div[3]/div[3]/div/button[2]')
    create_success_alert = (By.XPATH, '//*[@id="root"]/div[2]')
    crm_top_content = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[3]/div[1]/div[2]/div[2]/div/div/div/div/div/div[1]/div[1]')
    content_post_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[1]/div/div/label[1]')
    content_wait_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[1]/div/div/label[2]')                                  
    content_delete_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[1]/div/div/label[3]')
    content_status_btn = (By.CSS_SELECTOR, '#root > div.jss1 > div.jss28 > div > div.jss30 > div.MuiBox-root.jss45.jss32 > div > button')
    status_alert_msg = (By.CSS_SELECTOR, 'div > div.MuiAlert-message')
    status_result = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/div[3]/div[1]/div[2]/div[2]/div/div/div/div/div/div[1]/div[7]/div')
    crm_top_content_detail = (By.CSS_SELECTOR, '#root > div.jss1 > div.jss28 > div > div.jss30 > div.MuiPaper-root.jss37.MuiPaper-elevation1.MuiPaper-rounded > div.MuiDataGrid-root.MuiDataGrid-root.jss38.MuiDataGrid-autoHeight > div.MuiDataGrid-main > div:nth-child(2) > div > div > div > div > div > div:nth-child(1) > div:nth-child(4) > a')
    update_title_input = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[3]/div[2]/div/div/div/input')
    update_body_input = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[3]/div[3]/div/div/div[2]/div[1]')
    update_btn = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[3]/div[4]/button')

    def __init__(self, driver):
        super(Guide, self).__init__(driver)

    def get_main_page(self):
        self.get(self.main_url)

    def get_guide_list_page(self):
        self.get(self.guide_list_url)

    def get_guide_create_page(self):
        self.get(self.guide_create_url)
    
    def send_keys_guide_title(self):
        self.send_keys(self.title_input, CRMData.content_title)
    
    def send_keys_guide_body(self):
        self.send_keys(self.body_input, CRMData.content_body)

    def send_keys_guide_title_update(self):
        self.send_keys(self.update_title_input, CRMData.content_update_title)

    def send_keys_guide_body_update(self):
        self.send_keys(self.update_body_input, CRMData.content_update_body)
