from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://qa.getyournest.com/sign-in"

try:    
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
    
    
    #input1 = browser.find_element(By.CLASS_NAME, "email")
    #input1.send_keys("andreinovikau+qa@ballastlane.com")
    #time.sleep(2)
    
    #input1 = browser.find_element(By.ID, "password")
    #input1.send_keys("1!Testtest")
    #time.sleep(2)
    
    #option1 = browser.find_element(By.TAG_NAME, "i")
    #option1.click()
    #time.sleep(2)
    
    #button = browser.find_element(By.TAG_NAME, "button")
    #button.click()
    
    link1 = browser.find_element(By.TAG_NAME, "h5")
    link1.click()
    time.sleep(5)
    
    input = browser.find_element(By.ID, "email")
    input.send_keys("andreinovikau@ballastlane.com")
    
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    time.sleep(2)
    
finally:    
    time.sleep(3)
    browser.quit()
    