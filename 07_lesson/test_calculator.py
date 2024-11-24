import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver

    def set_delay(self, input_value):
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(input_value)

    def click_button(self, button):
        button_element = self.driver.find_element(By.XPATH, f"//button[text()='{button}']")
        button_element.click()

    def get_result(self):
        result_element = self.driver.find_element(By.ID, "result")
        return result_element.text


@pytest.fixture
def setup():
    # Установка драйвера (например, Chrome)
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_calculate_15(setup):
    input_value = "45"
    button_sequence = ["7", "+", "8", "="]
    expected_result = "15"

    # Открываем страницу калькулятора
    setup.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # Создаем объект страницы калькулятора
    calculator_page = CalculatorPage(setup)

    # Вводим значение в поле ввода
    calculator_page.set_delay(input_value)

    # Нажимаем на кнопки
    for button in button_sequence:
        calculator_page.click_button(button)

    # Ждем указанное время (в данном случае 45 секунд)
    time.sleep(int(input_value))

    # Проверяем результат
    assert calculator_page.get_result() == expected_result, f"Expected {expected_result}, but got {calculator_page.get_result()}"