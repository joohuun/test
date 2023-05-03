import time

from pages.fingo.home import Premium
from ...base import FingoBase
from .. import ProductALert
from config.fingo import fingo_base_url

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
"""
메인 홈 테스트 - 프리미업 탭
premium: vProductsNc(
            first: 10
            sortBy: { field: COPYRIGHT_CREATED_ID, direction: DESC }
            filter: { isPremium: true }
        )

query GetPremiumList(
        $first: Int
        $after: String
        $field: VProductOrderField!
        $filter: VProductFilterInput
        $direction: OrderDirection!
    ) {
        vProductsNc(first: $first, after: $after, sortBy: { field: $field, direction: $direction }, filter: $filter) {
            ...VProductsNcList
            edges {
                node {
                    yearSumval
                    premiumContractStatus
                }
            }
        }
    }
"""
# 좌우로 스크롤하는 함수를 만듭니다.





class TestPremiumProduct(FingoBase):


    def test_1_get_session(self):
        self.driver.get(fingo_base_url)

    def test_2_get_premium_product(self):
        get_premium_product = Premium(self.driver)
        get_premium_product.get_main_page()


        # 카운트
        # get_premium_product_count = get_premium_product.find_elements(get_premium_product.premium_item)
        # print(len(get_premium_product_count))
        # time.sleep(3)



