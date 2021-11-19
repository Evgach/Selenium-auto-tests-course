from selenium import webdriver
import time

link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)    

    x_element = browser.find_element_by_css_selector(".nowrap#num1") # Находим первое слагаемое
    y_element = browser.find_element_by_css_selector(".nowrap#num2") # Находим второе слагаемое
    x = x_element.text # Переводим первое слагаемое в текст
    y = y_element.text # Переводим второе слагаемое в текст
    summa = int(x) + int(y) # Суммируем первое и второе слагаемые
    
    from selenium.webdriver.support.ui import Select # Импорт метода Select
    select = Select(browser.find_element_by_tag_name("select")) # Присваиваем переменной выпадающий список 
    select.select_by_value(str(summa)) # Выбираем в выпадающем списке нужное число
    button = browser.find_element_by_class_name("btn.btn-default") # Находим кнопку Submit
    button.click() # Кликаем по кнопке Submit

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла