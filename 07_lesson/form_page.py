from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FormPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def fill_form(self, first_name, last_name, address, email, phone, zip_code, city, country, job_position, company):
        self.driver.find_element(By.NAME, 'first_name').send_keys(first_name)
        self.driver.find_element(By.NAME, 'last_name').send_keys(last_name)
        self.driver.find_element(By.NAME, 'address').send_keys(address)
        self.driver.find_element(By.NAME, 'email').send_keys(email)
        self.driver.find_element(By.NAME, 'phone').send_keys(phone)
        self.driver.find_element(By.NAME, 'zip_code').send_keys(zip_code)
        self.driver.find_element(By.NAME, 'city').send_keys(city)
        self.driver.find_element(By.NAME, 'country').send_keys(country)
        self.driver.find_element(By.NAME, 'job_position').send_keys(job_position)
        self.driver.find_element(By.NAME, 'company').send_keys(company)

    def submit_form(self):
        self.driver.find_element(By.ID, 'submit-button').click()

    def wait_for_alerts(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'alert')))

    def get_alerts(self):
        return self.driver.find_elements(By.CLASS_NAME, 'alert')

    def check_alert_colors(self):
        alerts = self.get_alerts()
        color_counts = {'red': 0, 'green': 0}

        for alert in alerts:
            color = alert.get_attribute('class')  # Предполагается использование CSS классов для определения цвета
            if 'alert-danger' in color:
                color_counts['red'] += 1
            elif 'alert-success' in color:
                color_counts['green'] += 1

        return color_counts