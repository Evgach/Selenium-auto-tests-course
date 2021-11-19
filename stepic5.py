# используется 4 версия Selenium

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# # 4 версия Selenium!!! используется вместо path, в ковычках должен быть прописан путь до хромдрайвера
service = Service(r"C:\chromedriver")

link = "http://suninjuly.github.io/registration1.html"

data = {'first_name':'Ivan', 'last_name':'Petrov', 'email':'test@gmail.com'}

element = {'first_name':'//input[@placeholder="Input your first name" and @required=""]',
           'last_name':'//input[@placeholder="Input your last name" and @required=""]',
           'email':'//input[@placeholder="Input your email" and @required=""]'}

try:
    browser = webdriver.Chrome(service=service)
    browser.get(link)

    for key1, key2 in zip(data.keys(), element.keys()):
        browser.find_element(By.XPATH, element[key1]).send_keys(data[key2])

    browser.find_element(By.XPATH, '//button').click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    #browser.close()
    time.sleep(15)
    browser.quit()