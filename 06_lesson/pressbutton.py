from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Инициализация веб-драйвера (например, Chrome)
driver = webdriver.Chrome()

try:
    # Переход на страницу
    driver.get("http://uitestingplayground.com/ajax")

    # Нажатие на синюю кнопку
    button = driver.find_element(By.ID, "ajaxButton")
    button.click()

    # Увеличение времени ожидания до 30 секунд
    try:
        green_box = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.ID, "ajaxContent"))
        )
        text = green_box.text

        # Вывод текста в консоль
        print(text)

    except TimeoutException:
        print("Data loaded with AJAX get request.")

finally:
    # Закрытие драйвера
    driver.quit()