import time

from ..base import BaseTest
from pages.tower.product import Premium



class TestPremiumProductList(BaseTest):
    def test_1_get_premium_product_list(self):
        pass

    def test_2_get_premium_product_list_by_status(self):
        pass

    def test_3_get_premium_product_list_by_category(self):
        pass

    def test_4_premium_product_status_update_to_wait(self):
        pass

    def test_5_premium_product_status_update_to_stop(self):
        pass

    def test_6_premium_product_status_update_to_sale(self):
        pass
        

class TestPremiumProductCreate(BaseTest):
    def test_1_create_premium_product(self):
        pass

    def test_2_create_premium_product_without_data(self):
        pass


class TestPremiumCopyrightList(BaseTest):
    def test_1_get_premium_copyright_list(self):
        pass

    def test_2_get_premium_copyright_by_id(self):
        pass

    def test_2_get_premium_copyright_by_category(self):
        pass


class TestPremiumCopyrightCreate(BaseTest):
    def test_1_create_premium_copyright(self):
        pass

    def test_2_create_premium_copyright_exist_id(self):
        pass