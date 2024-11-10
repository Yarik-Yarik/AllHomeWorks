from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настройка веб-драйвера (например, Chrome)
driver = webdriver.Chrome()

try:
    # Переход на сайт
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    # Ожидание загрузки всех изображений
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "img"))
    )

    # Получение всех изображений
    images = driver.find_elements(By.TAG_NAME, "img")

    # Проверка наличия как минимум трех изображений
    if len(images) >= 3:
        # Получение третьего изображения
        third_image = images[2]  # Индекс 2 соответствует третьему изображению

        # Получение значения атрибута src
        src_value = third_image.get_attribute("src")

        # Вывод значения в консоль
        print(src_value)
    else:
        print("Недостаточно изображений на странице.")

finally:
    # Закрытие драйвера
    driver.quit()