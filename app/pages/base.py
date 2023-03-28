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


class LocalStorage:
    def __init__(self, driver) :
        self.driver = driver

    def __len__(self):
        return self.driver.execute_script("return window.localStorage.length;")

    def items(self) :
        return self.driver.execute_script( \
            "var ls = window.localStorage, items = {}; " \
            "for (var i = 0, k; i < ls.length; ++i) " \
            "  items[k = ls.key(i)] = ls.getItem(k); " \
            "return items; ")

    def keys(self) :
        return self.driver.execute_script( \
            "var ls = window.localStorage, keys = []; " \
            "for (var i = 0; i < ls.length; ++i) " \
            "  keys[i] = ls.key(i); " \
            "return keys; ")

    def get(self, key):
        return self.driver.execute_script("return window.localStorage.getItem(arguments[0]);", key)

    def set(self, key, value):
        self.driver.execute_script("window.localStorage.setItem(arguments[0], arguments[1]);", key, value)

    def has(self, key):
        return key in self.keys()

    def remove(self, key):
        self.driver.execute_script("window.localStorage.removeItem(arguments[0]);", key)

    def clear(self):
        self.driver.execute_script("window.localStorage.clear();")

    def __getitem__(self, key) :
        value = self.get(key)
        if value is None :
          raise KeyError(key)
        return value

    def __setitem__(self, key, value):
        self.set(key, value)

    def __contains__(self, key):
        return key in self.keys()

    def __iter__(self):
        return self.items().__iter__()

    def __repr__(self):
        return self.items().__str__()