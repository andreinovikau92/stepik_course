from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "http://suninjuly.github.io/execute_script.html"

def calc(a):
    return str(math.log(abs(12 * math.sin(int(a)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    a = browser.find_element(By.ID, "input_value")
    a = a.text
    b = calc(a)
    
    
    input = browser.find_element(By.ID, "answer")
    input.send_keys(b)
    #time.sleep()
    
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()
    #time.sleep()
    
    option2 = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
    option2.click()
    #time.sleep()
    
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    #time.sleep()
    
finally:
    time.sleep(10)
    browser.quit()
    