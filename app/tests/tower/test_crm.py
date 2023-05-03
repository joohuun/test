import time
from ..base import TowerBase
from pages.tower.crm import Notice, News, FAQ, Guide
from config.tower import (
    CRMData,
)
from . import (
    CRMAlert,
    CRMStatus,
)

class TestNotice(TowerBase):
    def test_1_get_notice_list(self):
        notice_list = Notice(self.driver)
        notice_list.get_notice_list_page()
        self.assertEqual(self.driver.current_url, Notice.notice_list_url)

    def test_2_create_notice(self):
        notice_create = Notice(self.driver)
        notice_create.get_noticle_create_page()
        self.assertEqual(self.driver.current_url, Notice.noticle_create_url)
        notice_create.send_keys_notice_title()
        notice_create.send_keys_notice_body()
        notice_create.click(notice_create.create_btn)
        notice_create.click(notice_create.create_confirm_btn)
        alert = notice_create.find_element(notice_create.create_success_alert).text
        self.assertEqual(alert, CRMAlert.crm_create_success)

    def test_3_status_delete_notice(self):
        notice_status_delete = Notice(self.driver)
        notice_status_delete.get_notice_list_page()
        notice_status_delete.click(notice_status_delete.crm_top_content)
        notice_status_delete.click(notice_status_delete.content_delete_btn)
        notice_status_delete.click(notice_status_delete.content_status_btn)
        alert = notice_status_delete.find_element(notice_status_delete.status_alert_msg).text
        self.assertEqual(alert, CRMAlert.crm_status_update_success)
        time.sleep(3)
        result = notice_status_delete.find_element(notice_status_delete.status_result).text
        self.assertEqual(result, CRMStatus.delete)

    def test_4_status_post_notice(self):
        notice_stauts_post = Notice(self.driver)
        notice_stauts_post.get_notice_list_page()
        notice_stauts_post.click(notice_stauts_post.crm_top_content)
        notice_stauts_post.click(notice_stauts_post.content_post_btn)
        notice_stauts_post.click(notice_stauts_post.content_status_btn)
        alert = notice_stauts_post.find_element(notice_stauts_post.status_alert_msg).text
        self.assertEqual(alert, CRMAlert.crm_status_update_success)
        time.sleep(2)
        result = notice_stauts_post.find_element(notice_stauts_post.status_result).text
        self.assertEqual(result, CRMStatus.post)

    def test_5_update_notice(self):
        notice_update = Notice(self.driver)
        notice_update.get_notice_list_page()
        notice_update.click(notice_update.crm_top_content_detail)
        notice_update.send_keys_notice_title_update()
        notice_update.send_keys_notice_body_update()
        notice_update.click(notice_update.update_btn)
        alert = notice_update.find_element(notice_update.status_alert_msg).text
        self.assertEqual(alert, CRMAlert.crm_update_success)


class TestNews(TowerBase):
    def test_1_get_news_list(self):
        news_list = News(self.driver)
        news_list.get_news_list_page()
        self.assertEqual(self.driver.current_url, News.news_list_url)
        
    def test_2_create_news(self):
        news_create = News(self.driver)
        news_create.get_news_create_page()
        news_create.click(news_create.type_news)
        news_create.send_keys_news_title()
        news_create.send_keys_news_link()
        news_create.click(news_create.news_create_btn)
        news_create.click(news_create.news_create_btn2)
        alert = news_create.find_element(news_create.create_success_alert).text
        self.assertEqual(alert, CRMAlert.crm_create_success)

    def test_3_status_delete_news(self):
        news_status_delete = News(self.driver)
        news_status_delete.get_news_list_page()
        news_status_delete.click(news_status_delete.crm_top_content)
        news_status_delete.click(news_status_delete.content_delete_btn)
        news_status_delete.click(news_status_delete.content_status_btn)
        alert = news_status_delete.find_element(news_status_delete.status_alert_msg).text
        self.assertEqual(alert, CRMAlert.crm_status_update_success)
        time.sleep(2)
        result = news_status_delete.find_element(news_status_delete.status_result).text
        self.assertEqual(result, CRMStatus.delete)

    def test_4_status_post_news(self):
        news_status_post = News(self.driver)
        news_status_post.get_news_list_page()
        news_status_post.click(news_status_post.crm_top_content)
        news_status_post.click(news_status_post.content_post_btn)
        news_status_post.click(news_status_post.content_status_btn)
        alert = news_status_post.find_element(news_status_post.status_alert_msg).text
        self.assertEqual(alert, CRMAlert.crm_status_update_success)
        time.sleep(2)
        result = news_status_post.find_element(news_status_post.status_result).text
        self.assertEqual(result, CRMStatus.post)

    def test_5_update_news(self):
        news_update = News(self.driver)
        news_update.get_news_list_page()
        news_update.click(news_update.crm_top_content_detail)
        news_update.send_keys_news_title_update()
        news_update.click(news_update.news_update_btn)
        alert = news_update.find_element(news_update.status_alert_msg).text
        self.assertEqual(alert, CRMAlert.crm_update_success)


class TestFAQ(TowerBase):
    def test_1_get_faq_list(self):
        faq_list = FAQ(self.driver)
        faq_list.get_faq_list_page()
        self.assertEqual(self.driver.current_url, FAQ.faq_list_url)

    def test_2_create_faq(self):
        faq_create = FAQ(self.driver)
        faq_create.get_faq_create_page()
        faq_create.click(faq_create.type_faq)
        faq_create.send_keys_faq_title()
        faq_create.send_keys_faq_body()
        faq_create.click(faq_create.create_btn)
        faq_create.click(faq_create.create_btn2)
        alert = faq_create.find_element(faq_create.create_success_alert).text
        self.assertEqual(alert, CRMAlert.crm_create_success)

    def test_3_status_delete_faq(self):
        faq_status_delete = FAQ(self.driver)
        faq_status_delete.get_faq_list_page()
        faq_status_delete.click(faq_status_delete.crm_top_content)
        faq_status_delete.click(faq_status_delete.content_delete_btn)
        faq_status_delete.click(faq_status_delete.content_status_btn)
        alert = faq_status_delete.find_element(faq_status_delete.status_alert_msg).text
        self.assertEqual(alert, CRMAlert.crm_status_update_success)
        time.sleep(2)
        result = faq_status_delete.find_element(faq_status_delete.status_result).text
        self.assertEqual(result, CRMStatus.delete)


    def test_4_status_post_faq(self):
        faq_status_post = FAQ(self.driver)
        faq_status_post.get_faq_list_page()
        faq_status_post.click(faq_status_post.crm_top_content)
        faq_status_post.click(faq_status_post.content_post_btn)
        faq_status_post.click(faq_status_post.content_status_btn)
        alert = faq_status_post.find_element(faq_status_post.status_alert_msg).text
        self.assertEqual(alert, CRMAlert.crm_status_update_success)
        time.sleep(2)
        result = faq_status_post.find_element(faq_status_post.status_result).text
        self.assertEqual(result, CRMStatus.post)


    def test_5_update_faq(self):
        faq_update = FAQ(self.driver)
        faq_update.get_faq_list_page()
        faq_update.click(faq_update.crm_top_content_detail)
        faq_update.send_keys_faq_title_update()
        faq_update.send_keys_faq_body_update()
        faq_update.click(faq_update.update_btn)
        alert = faq_update.find_element(faq_update.status_alert_msg).text
        self.assertEqual(alert, CRMAlert.crm_update_success)


class TestGuide(TowerBase):
    def test_1_get_guide_list(self):
        guide_list = Guide(self.driver)
        guide_list.get_guide_list_page()
        self.assertEqual(self.driver.current_url, Guide.guide_list_url)

    def test_2_create_guide(self):
        guide_create = Guide(self.driver)
        guide_create.get_guide_create_page()
        guide_create.click(guide_create.type_guide)
        guide_create.send_keys_guide_title()
        guide_create.send_keys_guide_body()
        guide_create.click(guide_create.create_btn)
        guide_create.click(guide_create.create_btn2)
        alert = guide_create.find_element(guide_create.create_success_alert).text
        self.assertEqual(alert, CRMAlert.crm_create_success)
        
    def test_3_status_delete_guide(self):
        guide_status_delete = Guide(self.driver)
        guide_status_delete.get_guide_list_page()
        guide_status_delete.click(guide_status_delete.crm_top_content)
        guide_status_delete.click(guide_status_delete.content_delete_btn)
        guide_status_delete.click(guide_status_delete.content_status_btn)
        alert = guide_status_delete.find_element(guide_status_delete.status_alert_msg).text
        self.assertEqual(alert, CRMAlert.crm_status_update_success)
        time.sleep(2)
        result = guide_status_delete.find_element(guide_status_delete.status_result).text
        self.assertEqual(result, CRMStatus.delete)

    def test_4_status_post_guide(self):
        guide_status_post = Guide(self.driver)
        guide_status_post.get_guide_list_page()
        guide_status_post.click(guide_status_post.crm_top_content)
        guide_status_post.click(guide_status_post.content_post_btn)
        guide_status_post.click(guide_status_post.content_status_btn)
        alert = guide_status_post.find_element(guide_status_post.status_alert_msg).text
        self.assertEqual(alert, CRMAlert.crm_status_update_success)        
        time.sleep(2)
        result = guide_status_post.find_element(guide_status_post.status_result).text 
        self.assertEqual(result, CRMStatus.post)

    def test_5_update_guide(self):
        guide_update = Guide(self.driver)
        guide_update.get_guide_list_page()
        guide_update.click(guide_update.crm_top_content_detail) 
        guide_update.send_keys_guide_title_update()
        guide_update.send_keys_guide_body_update()
        guide_update.click(guide_update.update_btn)
        alert = guide_update.find_element(guide_update.status_alert_msg).text
        self.assertEqual(alert, CRMAlert.crm_update_success)


    





