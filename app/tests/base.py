import unittest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json, requests
# from pages.base import LocalStorage
from config.fingo import fingo_base_url, fingo_prod_url
from config.tower import tower_base_url

class TowerBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        options = webdriver.ChromeOptions()
        options.set_capability('browserName', 'chrome')
        options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        cls.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), options=options
        )
        # options = webdriver.ChromeOptions()
        # options.add_argument('headless')
        # options.add_argument('--disable-gpu')
        # options.add_argument("--no-sandbox")
        # options.add_argument("--disable-dev-shm-usage")
        # cls.driver = webdriver.Chrome(service=Service(
        #     ChromeDriverManager().install()), options=options
        #     )
        

    def setUp(self) -> None:
        url = f'{tower_base_url}gql/'
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
        self.driver.execute_script("window.localStorage.setItem(arguments[0], arguments[1]);", 'token', jwt)
        # self.driver.get('https://qa.fingo.run:5003/tower/')
        # self.driver.add_cookie({'name': 'token', 'value': jwt})

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

from selenium.webdriver.common.by import By


class FingoBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:

        options = webdriver.ChromeOptions()
        options.set_capability('browserName', 'chrome')
        options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        cls.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), options=options
        )

        # options = webdriver.ChromeOptions()
        # # options.add_argument('headless')
        # options.add_argument('--disable-gpu')
        # options.add_argument("--no-sandbox")
        # options.add_argument("--disable-dev-shm-usage")
        # cls.driver = webdriver.Chrome(service=Service(
        #     ChromeDriverManager().install()), options=options)
        

        
    def setUp(self) -> None:
        url = f"{fingo_base_url}gql/"
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
        self.driver.execute_script("window.localStorage.setItem(arguments[0], arguments[1]);", 'token', jwt)
        # self.driver.get(self.driver.current_url)
        # self.driver.add_cookie({'name': 'token', 'value': jwt})

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


class FingoProdBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('--disable-gpu')
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        cls.driver = webdriver.Chrome(service=Service(
            ChromeDriverManager().install()), options=options)
        

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()