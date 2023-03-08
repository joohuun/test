import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class BaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:

        options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--headless")
        options.set_capability('browserName', 'chrome')
        options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        cls.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), options=options
        )

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        