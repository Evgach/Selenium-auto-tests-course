from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
url = 'http://suninjuly.github.io/registration2.html'
browser = webdriver.Chrome()
try:
    browser.get(url)
    for i in range(1, 4): # обязательных три поля
        browser.find_element(By.CSS_SELECTOR, f'div.first_block .form-group:nth-child({i}) input').send_keys('vlad')
    sleep (10)
    browser.find_element(By.CSS_SELECTOR, 'button').click()
    sleep(4)
    parc_text = browser.find_element(By.CSS_SELECTOR, 'h1').text
    assert "Congratulations! You have successfully registered!" == parc_text

finally:
    sleep(3)
    browser.quit()
