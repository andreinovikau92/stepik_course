from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "https://qa.getyournest.com/sign-up"

try:    
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element(By.ID, "name")
    input1.send_keys("Andrei")
    time.sleep(1)
    
    input2 = browser.find_element(By.ID, "email")
    input2.send_keys("andreinovikau+selenium2@ballastlane.com")
    time.sleep(1)
    
    input3 = browser.find_element(By.ID, "phone")
    input3.send_keys("7465283945")
    time.sleep(1)
    
    input4 = browser.find_element(By.ID, "password")
    input4.send_keys("1!Testtest")
    time.sleep(1)
    
    button = browser.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)
    
    browser.switch_to.window(new_window = browser.window_handles[0])
    
    


finally:
    time.sleep(3)
# закрываем браузер после всех манипуляций
    browser.quit()
    