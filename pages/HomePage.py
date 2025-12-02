from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def admin_icon(self):
        admin = self.driver.find_element(By.XPATH, "//a[@data-toggle='dropdown']")
        admin.click()

    def sign_out(self):
        logout = self.driver.find_element(By.XPATH, "//i[@class='ace-icon fa fa-power-off']")
        logout.click()