import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json, requests
from pages.base import LocalStorage
class BaseTest(unittest.TestCase, LocalStorage):
    @classmethod
    def setUpClass(cls) -> None:

        # url = 'http://10.2.1.100:8000/graphql/'
        # query = """
        # mutation toeknCreate{
        #     tokenCreate(email: "kimju0612@naver.com",
        #     password: "1234Qwer!!") {
        #         token
        #         refreshToken
        #         csrfToken
        #         user {
        #             email
        #         }
        #         errors {
        #             field
        #             message
        #         }
        #     }
        # }
        # """
        

        # response = requests.post(url, json={'query': query})
        # data = json.loads(response.text)
        # jwt = data['data']['tokenCreate']['token']


        options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--headless")
        options.set_capability('browserName', 'chrome')
        options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        # options.add_argument("user-Agent=Mozilla/4.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36")
        # options.add_argument({"authorization" : f"JWT {jwt}"})
        options.add_argument("content-type=application/json")
        cls.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), options=options
        )

        # LOGIN_INFO = {
        #     'id': 'kimju0612@naver.com',
        #     'password': '1234Qwer!!'
        # }
        # s = requests.Session()
        # s.get('http://10.2.1.100:5001/tower')
        # s.post('http://10.2.1.100:5001/tower', data=LOGIN_INFO)
        # cls.driver.get('http://10.2.1.100:5001/tower') # 여기에 이 부분이 들어가지 않으면 에러가 발생합니다.
        # for c in s.cookies:
        #     cls.driver.add_cookie({'name': c.name, 'value': c.value, 'path': c.path, 'expiry': c.expires})
        # cls.driver.refresh()
        # return

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        


