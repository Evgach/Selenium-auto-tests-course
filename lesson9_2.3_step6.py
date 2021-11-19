from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))  

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    #time.sleep(1)
    button = browser.find_element_by_class_name("trollface.btn.btn-primary")
    button.click()
    time.sleep(1) # Может понадобиться задержка
    #alert = browser.switch_to.alert
    #alert.accept()
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(str(y))
    button = browser.find_element_by_class_name("btn.btn-primary")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла