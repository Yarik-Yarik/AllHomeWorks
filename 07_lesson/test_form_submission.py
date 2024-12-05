import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from form_page import FormPage

@pytest.fixture(scope="module")
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_form_submission(driver):
    form_page = FormPage(driver)

    form_page.open("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    form_page.fill_form(
        first_name='Иван',
        last_name='Петров',
        address='Ленина, 55-3',
        email='test@skypro.com',
        phone='+7985899998787',
        zip_code='',
        city='Москва',
        country='Россия',
        job_position='QA',
        company='SkyPro'
    )

    form_page.submit_form()
    form_page.wait_for_alerts()

    # Переносим проверки в класс страницы
    color_counts = form_page.check_alert_colors()

    expected_colors = {
        'red': 1,
        'green': 1
    }

    assert color_counts['red'] == expected_colors['red'], f"Ожидалось {expected_colors['red']} красных предупреждений, найдено {color_counts['red']}"

    assert color_counts['green'] >= expected_colors['green'], f"Ожидалось минимум {expected_colors['green']} зеленых предупреждений, найдено {color_counts['green']}"

    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    # Ожидание до 10 секунд, пока элемент не станет доступен
    first_name_input = WebDriverWait(driver, 40).until(
        EC.presence_of_element_located((By.NAME, "first_name"))
    )