import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from form_page import FormPage  # Импортируем класс страницы


@pytest.fixture(scope="module")  # Используем scope="module" для оптимизации
def driver():
    # Запуск Chrome-драйвера с использованием ChromeDriverManager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


def test_form_submission(driver):
    # Создаем объект страницы
    form_page = FormPage(driver)

    # Открыть страницу с формой
    form_page.open("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Заполняем форму
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

    # Отправляем форму
    form_page.submit_form()

    # Ожидаем появления всех предупреждений
    form_page.wait_for_alerts()

    # Получаем все элементы предупреждений
    alerts = form_page.get_alerts()

    # Проверяем предупреждения на наличие ожидаемых цветов
    expected_colors = {
        'red': 1,  # Ожидаем одно красное поле
        'green': 1  # Ожидаем минимум одно зеленое поле
    }

    color_counts = {'red': 0, 'green': 0}

    for alert in alerts:
        color = alert.get_color()  # Предполагается, что метод get_color() возвращает цвет предупреждения
        if color in color_counts:
            color_counts[color] += 1

    # Ассерты должны быть в коде тестов, а не в коде страницы
    assert color_counts['red'] == expected_colors[
        'red'], f"Ожидалось {expected_colors['red']} красных предупреждений, найдено {color_counts['red']}"

    assert color_counts['green'] >= expected_colors[
        'green'], f"Ожидалось минимум {expected_colors['green']} зеленых предупреждений, найдено {color_counts['green']}"