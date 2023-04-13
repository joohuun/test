from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests

# WebDriver를 초기화합니다.
driver = webdriver.Chrome()
driver.get("http://10.2.1.100:5001/tower/signin")

# 로그인 정보를 입력합니다.
username_input = driver.find_element_by_name("username")
username_input.send_keys("your_username")
password_input = driver.find_element_by_name("password")
password_input.send_keys("your_password")
password_input.send_keys(Keys.ENTER)

# JWT 토큰 값을 가져옵니다.
jwt_url = "https://example.com/api/token"
response = requests.post(jwt_url, json={"username": "your_username", "password": "your_password"})
jwt_token = response.json()["token"]

# HTTP 요청 헤더에 JWT 토큰 값을 추가합니다.
headers = {"Authorization": f"Bearer {jwt_token}"}
driver.execute_script("window.localStorage.setItem('token', arguments[0]);", jwt_token)

# 로그인 후의 페이지로 이동합니다.
driver.get("https://example.com/dashboard")

# 로그인 후의 페이지에서 필요한 작업을 수행합니다.
# ...

# WebDriver를 종료합니다.
driver.quit()