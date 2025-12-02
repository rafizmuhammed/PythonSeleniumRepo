from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AdminPage:
    def __init__(self, driver):
        self.driver = driver

    def home_admin(self):
        admin = self.driver.find_element(By.XPATH, "//a[@href='https://groceryapp.uniqassosiates.com/admin/list-admin' and @class='small-box-footer']")
        admin.click()

    def return_home(self):
        home = self.driver.find_element(By.XPATH, "//a[text() ='Home']")
        home.click()

    def new_user(self):
        new = self.driver.find_element(By.XPATH, "//a[@class='btn btn-rounded btn-danger']")
        new.click()

    def enter_username(self):
        user_name = self.driver.find_element(By.XPATH, "//input[@id='username']")
        user_name.click()
        user_name.send_keys("admin")

    def enter_password(self):
        password = self.driver.find_element(By.XPATH, "//input[@id='password']")
        password.click()
        password.send_keys("12345")

    def select_dropdown(self):
        drop_down = self.driver.find_element(By.XPATH, "//select[@id='user_type']")
        select = Select(drop_down)
        select.select_by_visible_text('Staff')

    def save_user(self):
        save = self.driver.find_element(By.XPATH, "//button[@name='Create']")
        save.click()

    def refresh(self):
        reset = self.driver.find_element(By.XPATH, "//a[@class='btn btn-rounded btn-warning']")
        reset.click()

    def search_user(self):
        search = self.driver.find_element(By.XPATH, "//a[@class='btn btn-rounded btn-primary']")
        search.click()

    def search_user_name(self):
        user_name = self.driver.find_element(By.XPATH, "//input[@name='un']")
        user_name.click()
        user_name.send_keys("admin")

    def search_dropdown(self):
        drop_down = self.driver.find_element(By.XPATH, "//select[@name='ut']")
        select = Select(drop_down)
        select.select_by_visible_text('Staff')

    def search_bar(self):
        search = self.driver.find_element(By.XPATH, "//button[@name='Search']")
        search.click()
