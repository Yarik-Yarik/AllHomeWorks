from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настройка драйвера Firefox
driver = webdriver.Firefox()

try:
    # Открываем страницу
    driver.get("http://the-internet.herokuapp.com/entry_ad")

    # Ожидаем появления модального окна и находим кнопку "Close"
    close_button = WebDriverWait(driver, 10).until(
      EC.element_to_be_clickable((By.XPATH, "//div[@class='modal-footer']/p/button")))

    close_button.click()

finally:
    # Закрываем браузер
    driver.quit()
