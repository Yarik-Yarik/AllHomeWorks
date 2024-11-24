from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.ID, "user-name").send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, "password").send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, "login-button").click()


class ProductsPage:
    def __init__(self, driver):
        self.driver = driver

    def add_product_to_cart(self, product_name):
        product_element = self.driver.find_element(By.XPATH, f"//div[text()='{product_name}']/following-sibling::div/button")
        product_element.click()

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_checkout_form(self, first_name, last_name, postal_code):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()

    def get_total_amount(self):
        total_text = self.driver.find_element(By.CLASS_NAME, "summary_total_label").text
        return float(total_text.split('$')[1])


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

# Создание объектов страниц
login_page = LoginPage(driver)
products_page = ProductsPage(driver)
checkout_page = CheckoutPage(driver)

# Авторизация
login_page.enter_username(username)
login_page.enter_password(password)
login_page.click_login()

# Добавление товаров в корзину
for product in products_to_add:
    products_page.add_product_to_cart(product)

# Переход в корзину
products_page.go_to_cart()

# Нажатие на Checkout
driver.find_element(By.ID, "checkout").click()

# Заполнение формы данными
checkout_page.fill_checkout_form("Имя", "Фамилия", "12345")

# Получение итоговой стоимости
total_amount = checkout_page.get_total_amount()

# Проверка итоговой суммы
assert total_amount == expected_total, f"Ожидалось {expected_total}, но получено {total_amount}"

# Закрытие браузера
driver.quit()