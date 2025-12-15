from selenium.webdriver.common.by import By

#from pages.HomePage import HomePage
from utility.PageUtility import PageUtility
from utility.WaitUtility import WaitUtility


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.waitutility = WaitUtility()
        self.PageUtility = PageUtility()

    def enter_user_name(self, user_value):
        username = self.driver.find_element(By.XPATH, "//input[@name='username']")
        #username.send_keys(user_value)
        self.PageUtility.send_data_to_element(username,user_value)
        return self

    def enter_password(self, pass_value):
        password = self.driver.find_element(By.XPATH, "//input[@name='password']")
        #password.send_keys(pass_value)
        self.PageUtility.send_data_to_element(password,pass_value)
        return self

    def sign_in(self):
        login = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        self.waitutility.wait_until_clickable(self.driver, login)
        self.PageUtility.send_data_to_element(login,login.text)
        #login.click()

        from pages.HomePage import HomePage
        return HomePage(self.driver)                         #chaining of classes