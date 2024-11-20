from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Условия для теста
url = "https://www.saucedemo.com/"
username = "standard_user"
password = "secret_sauce"
products_to_add = [
    "Sauce Labs Backpack",
    "Sauce Labs Bolt T-Shirt",
    "Sauce Labs Onesie"
]
expected_total = 58.29

# Настройка веб-драйвера
driver = webdriver.Chrome()  # Убедитесь, что у вас установлен ChromeDriver
driver.get(url)

# Авторизация
driver.find_element(By.ID, "user-name").send_keys(username)
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.ID, "login-button").click()

# Добавление товаров в корзину
for product in products_to_add:
    product_element = driver.find_element(By.XPATH, f"//div[text()='{product}']/following-sibling::div/button")
    product_element.click()

# Переход в корзину
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

# Нажатие на Checkout
driver.find_element(By.ID, "checkout").click()

# Заполнение формы данными
driver.find_element(By.ID, "first-name").send_keys("Имя")
driver.find_element(By.ID, "last-name").send_keys("Фамилия")
driver.find_element(By.ID, "postal-code").send_keys("12345")
driver.find_element(By.ID, "continue").click()

# Получение итоговой стоимости
total_text = driver.find_element(By.CLASS_NAME, "summary_total_label").text
total_amount = float(total_text.split('$')[1])

# Проверка итоговой суммы
assert total_amount == expected_total, f"Ожидалось {expected_total}, но получено {total_amount}"

# Закрытие браузера
driver.quit()