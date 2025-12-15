import string
import time
import random

import pytest
from selenium.webdriver.common.by import By

from pages.LoginPage import LoginPage
from utility.ExcelUtility import ExcelUtility


def generate_random_username():
    return "user_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))

class Testlogin:

    @pytest.mark.run(order=1)
    @pytest.mark.smoke
    def test_loginValidCredentials(self,browser_instance):
        self.driver = browser_instance

        excel_utility = ExcelUtility()
        user_name_value =excel_utility.read_user_data(2,1)
        password_value = excel_utility.read_user_data(2,2)

        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")

        self.driver.implicitly_wait(5)

        #username = self.driver.find_element(By.XPATH,"//input[@name='username']")
        #username.send_keys(user_name_value)
        #password = self.driver.find_element(By.XPATH,"//input[@name='password']")
        #password.send_keys(password_value)

        loginpage = LoginPage(self.driver)
        loginpage.enter_user_name(user_name_value).enter_password(password_value)         #chaining of methods
        #loginpage.enter_password(password_value)

        home_page = loginpage.sign_in()

        #loginpage.sign_in()
        #login = self.driver.find_element(By.XPATH,"//button[@type='submit']")
        #login.click()
        time.sleep(2)

        nav = self.driver.current_url
        assert nav == "https://groceryapp.uniqassosiates.com/admin"






    #@pytest.mark.parametrize("username_value",  [generate_random_username()])
    @pytest.mark.parametrize("username_value",  ["user","admin","password"])
    @pytest.mark.run(order=2)
    def test_loginInvalidPassword(self,browser_instance,username_value):
        self.driver = browser_instance

        excel_utility = ExcelUtility()
        #user_name_value =excel_utility.read_user_data(3,1)
        password_value = excel_utility.read_user_data(3,2)

        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")

        loginpage = LoginPage(self.driver)
        loginpage.enter_user_name(username_value).enter_password(password_value).sign_in()
        #loginpage.enter_password(password_value)

        #loginpage.sign_in()
        time.sleep(2)

        nav = self.driver.current_url
        assert nav == "https://groceryapp.uniqassosiates.com/admin/login"

    @pytest.mark.run(order=3)
    def test_loginInvalidUser(self, browser_instance):
        self.driver = browser_instance

        excel_utility = ExcelUtility()
        user_name_value = excel_utility.read_user_data(4, 1)
        password_value = excel_utility.read_user_data(4, 2)

        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")

        loginpage = LoginPage(self.driver)
        loginpage.enter_user_name(user_name_value).enter_password(password_value).sign_in()
        #loginpage.enter_password(password_value)

        #loginpage.sign_in()
        time.sleep(2)

        nav = self.driver.current_url
        assert nav == "https://groceryapp.uniqassosiates.com/admin/login"

    @pytest.mark.run(order=4)
    def test_loginInvalidCredentials(self, browser_instance):
        self.driver = browser_instance

        excel_utility = ExcelUtility()
        user_name_value = excel_utility.read_user_data(5, 1)
        password_value = excel_utility.read_user_data(5, 2)

        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")

        loginpage = LoginPage(self.driver)
        loginpage.enter_user_name(user_name_value).enter_password(password_value).sign_in()
        #loginpage.enter_password(password_value)

        #loginpage.sign_in()
        time.sleep(2)

        nav = self.driver.current_url
        assert nav == "https://groceryapp.uniqassosiates.com/admin/login"






























