from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_user_name(self, user_value):
        username = self.driver.find_element(By.XPATH, "//input[@name='username']")
        username.send_keys(user_value)

    def enter_password(self, pass_value):
        password = self.driver.find_element(By.XPATH, "//input[@name='password']")
        password.send_keys(pass_value)

    def sign_in(self):
        login = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        login.click()