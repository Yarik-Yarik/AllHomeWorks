from selenium import webdriver
from selenium.webdriver.common.by import By

# Запуск веб-драйвера
driver = webdriver.Chrome()  # Убедитесь, что у вас установлен драйвер Chrome

try:
    # Шаг 1: Перейдите на сайт
    driver.get("http://uitestingplayground.com/textinput")

    # Шаг 2: Укажите в поле ввода текст SkyPro
    input_field = driver.find_element(By.ID, "newButtonName")
    input_field.send_keys("SkyPro")

    # Шаг 3: Нажмите на синюю кнопку
    button = driver.find_element(By.XPATH, "//button[@id='updatingButton']")
    button.click()

    # Шаг 4: Получите текст кнопки и выведите в консоль
    button_text = button.text
    print(button_text)  # Ожидается вывод "SkyPro"

finally:
    # Закрытие драйвера
    driver.quit()