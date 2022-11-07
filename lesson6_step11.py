from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element(By.LINK_TEXT, "Input your name")
    input1.send_keys("Andrei")
    time.sleep(3)
    input2 = browser.find_element(By.LINK_TEXT, "Input your email")
    input2.send_keys("Petrov")
    time.sleep(3)
    input3 = browser.find_element(By.LINK_TEXT, "Input your phone")
    input3.send_keys("Smolensk")
    time.sleep(3)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    