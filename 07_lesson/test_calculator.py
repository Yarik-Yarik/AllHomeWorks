import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def setup():
    # Установка драйвера (например, Chrome)
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def slow_calculator_test(driver, input_value, button_sequence, expected_result):
    # Открываем страницу калькулятора
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # Вводим значение в поле ввода
    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys(input_value)

    # Нажимаем на кнопки
    for button in button_sequence:
        button_element = driver.find_element(By.XPATH, f"//button[text()='{button}']")
        button_element.click()

    # Ждем указанное время (в данном случае 45 секунд)
    time.sleep(int(input_value))

    # Проверяем результат
    result_element = driver.find_element(By.ID, "result")
    assert result_element.text == expected_result, f"Expected {expected_result}, but got {result_element.text}"


def test_calculate_15(setup):
    input_value = "45"
    button_sequence = ["7", "+", "8", "="]
    expected_result = "15"

    slow_calculator_test(setup, input_value, button_sequence, expected_result)