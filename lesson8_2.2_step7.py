from selenium import webdriver
import time
import os  

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Zhendos")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Parovoz")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("parovoz@mail.ru")
    input4 = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла 
    input4.send_keys(file_path)
    button = browser.find_element_by_class_name("btn.btn-primary")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла