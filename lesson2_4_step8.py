from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    
    text = WebDriverWait(browser, 12).until( # функция в которую передаётся правило ожидания и значения по которому будет выполняться поиск
        EC.text_to_be_present_in_element((By.ID, "price"), "$100") 
    )
    button = browser.find_element(By.ID, "book")
    button.click()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
    
    button = browser.find_element(By.ID, "solve")
    button.click()
        
finally:
    time.sleep(3)
    browser.quit()
        