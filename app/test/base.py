import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json, requests
from pages.base import LocalStorage
from pages.tower.account import SignIn

class BaseTest(unittest.TestCase, LocalStorage):
    @classmethod
    def setUpClass(cls) -> None:
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.set_capability('browserName', 'chrome')

        options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        cls.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), options=options
        )
        # cls.driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub', options=options)

    def setUp(self) -> None:
        url = 'http://10.2.1.100:8000/graphql/'
        query = """
        mutation toeknCreate{
            tokenCreate(email: "kimju0612@naver.com",
            password: "1234Qwer!!") {
                token
                refreshToken
                csrfToken
                user {
                    email
                }
                errors {
                    field
                    message
                }
            }
        }
        """
        response = requests.post(url, json={'query': query})
        data = json.loads(response.text)
        jwt = data['data']['tokenCreate']['token']
        self.set('token', jwt)

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()