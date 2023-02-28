import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class BaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        
        chrome_options = webdriver.ChromeOptions()
        # 웹페이지 끄고 테스트하는 옵션
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        # chrome_options.add_argument("--headless")
        cls.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), options=chrome_options
        )
        
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        