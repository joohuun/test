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
        options.add_argument("User-Agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36")
        options.add_argument("content-type=application/json")
        cls.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), options=options
        )
        # cookies = cls.driver.get_cookies()
        # for cookie in cookies:
        #     print(cookie)

        # cookies_dict = {}
        # for cookie in all_cookies:
        #     cookies_dict[cookie['name']] = cookie['value']
        
        # string = ''
        # for key in cookies_dict:
        #     string += f'{key}={cookies_dict[key]},'
        # print(string)

        # with open("all_cookies.txt", 'w') as f:
        #     f.write(string)

        # cls.driver.quit()

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        