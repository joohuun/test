from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium import webdriver


class Base():
    def __init__(self, driver):
        self.driver = driver

    def get(self, url):
        """ URL 이동 """
        self.driver.get(url)

    def click(self, locator):
        """ 클릭 """
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()
        except NoSuchElementException:
            raise NoSuchElementException("NoSuchElementException : %s" % str(locator))
        except TimeoutException:
            raise TimeoutException("TimeoutException : %s" % str(locator))
        
    def find_element(self, locator):
        """ 엘리먼트 찾기 """
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return self.driver.find_element(*locator)
        except NoSuchElementException:
            raise NoSuchElementException("NoSuchElementException : %s" % str(locator))
        except TimeoutException:
            raise TimeoutException("TimeoutException : %s" % str(locator))
        
    def find_elements(self, locator):
        """ 엘리먼트 찾기 (배열로 리턴) """
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return self.driver.find_elements(*locator)
        except NoSuchElementException:
            raise NoSuchElementException("NoSuchElementException : %s" % str(locator))
        except TimeoutException:
            raise TimeoutException("TimeoutException : %s" % str(locator))

    def send_keys(self, locator, value):
        """ 인풋 필드 값 입력 """
        self.find_element(locator).send_keys(value)