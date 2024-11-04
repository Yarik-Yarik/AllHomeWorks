from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Настройка драйвера Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Открытие страницы
driver.get("http://uitestingplayground.com/classattr")

# Нахождение кнопки и клик по ней
try:
    button = driver.find_element(
        By.XPATH,
        "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]",
    )

    button.click()
    time.sleep(2)  # Задержка для визуализации клика (по желанию)
finally:
    driver.quit()  # Закрытие браузера после выполнения скрипта
