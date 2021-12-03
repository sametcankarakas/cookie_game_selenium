from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time

chrome_driver_path = r"C:\Users\Samet\AppData\Local\Programs\Python\Python310\chromedriver.exe"
ser = Service(chrome_driver_path)
driver = webdriver.Chrome(service=ser)
driver.maximize_window()

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")

t_end = time.time() + 60 * 5
print(t_end)
seconds = 300000
power_up_time = time.time() + 5
print(power_up_time)
while True:
    cookie.click()
    while time.time() > power_up_time:
        items = driver.find_elements(By.CSS_SELECTOR, "#store div")
        print("inside loop loop biaaattchh 1")
        for item in items[::-1]:
            try:
                power_up = driver.find_element(By.ID, item.get_attribute("id"))
                power_up.click()
            except WebDriverException:
                print("Element is not clickable")
        power_up_time = time.time() + 10
    if time.time() > t_end:
        cookie_per_s = driver.find_element(By.ID, "cps").text
        print(cookie_per_s)
        break

driver.quit()
