from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("https://qa.getyournest.com")
    
    button = browser.find_element(By.TAG_NAME, "h5")
    button.click()
    
    input1 = browser.find_element(By.ID, "name")
    input1.send_keys("Selenium")
    
    input2 = browser.find_element(By.ID, "email")
    input2.send_keys("andreinovikau+testselenium@ballastlane.com")
    
    input3 = browser.find_element(By.ID, "phone")
    input3.send_keys("2587463")
    time.sleep(5)
    
    input4 = browser.find_element(By.ID, "password")
    input4.send_keys("1!Testtest")
    
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    time.sleep(5)
    
    
finally:
    time.sleep(10)
    browser.quit()    