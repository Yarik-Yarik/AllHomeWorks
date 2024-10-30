from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Настройка веб-драйвера
driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# Клик на кнопку "Add Element" пять раз
add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")
for _ in range(5):
    add_button.click()

# Собираем список кнопок "Delete"
delete_buttons = driver.find_elements(By.XPATH, "//button[text()='Delete']")

# Выводим размер списка
print(f"Количество кнопок 'Delete': {len(delete_buttons)}")

# Закрываем драйвер
time.sleep(2)  # Задержка для просмотра результата перед закрытием
driver.quit()
