from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Путь к chromedriver
driver = webdriver.Chrome()

# Открыть сайт
driver.get("http://uitestingplayground.com/ajax")

# Нажать на синюю кнопку
button = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '#ajaxButton'))
)
button.click()
print("Кнопка нажата, ожидаем появление зелёной плашки.")

# Увеличиваем тайм-аут до 30 секунд для надежности
try:
    green_text_element = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'p.bg-success'))
    )
    green_text = green_text_element.text
    print("Зелёная плашка найдена:", green_text)
except TimeoutException:
    print("Не удалось найти зелёную плашку в течение времени ожидания.")

# Закрыть браузер
driver.quit()