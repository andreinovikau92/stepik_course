from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(a):
    return str(math.log(abs(12 * math.sin(int(a)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
   
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    time.sleep(2)
    
    # смещение фокуса на новую вкладку
    browser.switch_to.window(browser.window_handles[1])
    
    a = browser.find_element(By.ID, "input_value")
    a = a.text
    b = calc(a)
    
    input = browser.find_element(By.ID, "answer")
    input.send_keys(b)
    time.sleep(2)
    
    button1 = browser.find_element(By.TAG_NAME, "button")
    button1.click()
    
finally:
    time.sleep(5)
    browser.quit()    