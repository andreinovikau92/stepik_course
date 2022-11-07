from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(a):
    return str(math.log(abs(12 * math.sin(int(a)))))

try:
    browser = webdriver.Chrome()
    #browser.implicitly_wait(12)
    browser.get(link)
    
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = browser.find_element(By.ID, "book")
    button.click()
    
    a = browser.find_element(By.ID, "input_value")
    a = a.text
    b = calc(a)
    
    input = browser.find_element(By.ID, "answer")
    input.send_keys(b)
    
    button1 = browser.find_element(By.ID, "solve")
    button1.click()
    
finally:
    time.sleep(2)
    browser.quit()
        