from selenium import webdriver
from selenium.webdriver.common.by import By

import time

# Настройка драйвера Firefox
driver = webdriver.Firefox()

try:
    # Открываем страницу
    driver.get("http://the-internet.herokuapp.com/inputs")

    # Находим поле ввода по его селектору
    input_field = driver.find_element(By.TAG_NAME, "input")

    # Вводим текст "1000"
    input_field.send_keys("1000")

    # Ждем немного, чтобы увидеть введенный текст (опционально)
    time.sleep(2)

    # Очищаем поле ввода
    input_field.clear()

    # Вводим текст "999"
    input_field.send_keys("999")

    # Ждем немного, чтобы увидеть введенный текст (опционально)
    time.sleep(2)

finally:
    # Закрываем браузер
    driver.quit()
