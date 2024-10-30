from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Настройка веб-драйвера (например, Chrome)
driver = webdriver.Chrome()

# Открытие страницы
driver.get("http://uitestingplayground.com/dynamicid")

# Нахождение синей кнопки по CSS селектору
blue_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")

# Клик по кнопке
blue_button.click()

# Задержка для визуального подтверждения клика (необязательно)
time.sleep(2)

# Закрытие драйвера
driver.quit()
