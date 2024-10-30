from selenium import webdriver
from selenium.webdriver.common.by import By


# Настройка драйвера Firefox
driver = webdriver.Firefox()

try:
    # Открытие страницы
    driver.get("http://the-internet.herokuapp.com/login")

    # Поиск полей ввода и кнопки
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

    # Ввод данных
    username_field.send_keys("tomsmith")
    password_field.send_keys("SuperSecretPassword!")

    # Нажатие на кнопку Login
    login_button.click()

finally:
    # Закрытие браузера через 5 секунд для просмотра результата
    driver.implicitly_wait(5)
    driver.quit()
