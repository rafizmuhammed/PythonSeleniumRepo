import time

import pytest
from selenium.webdriver.common.by import By

from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from utility.ExcelUtility import ExcelUtility


class Testlogout:

    #@pytest.mark.timeout(15)                      #pytest timeout
    def test_sign_out(self,cross_browser):
        self.driver = cross_browser

        excel_utility = ExcelUtility()
        user_name_value =excel_utility.read_user_data(2,1)
        password_value = excel_utility.read_user_data(2,2)

        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")

        loginpage = LoginPage(self.driver)

        loginpage.enter_user_name(user_name_value).enter_password(password_value)         #chaining of methods
        #loginpage.enter_password(password_value)

        home_page = loginpage.sign_in()

        #loginpage.enter_user_name(user_name_value)
        #loginpage.enter_password(password_value)

        #loginpage.sign_in()
        time.sleep(1)

        #admin = self.driver.find_element(By.XPATH,"//a[@data-toggle='dropdown']")
        #admin.click()

        #admin = HomePage(self.driver)
        #admin.admin_icon()

        home_page = home_page.admin_icon()
        time.sleep(1)

        #logout = self.driver.find_element(By.XPATH,"//i[@class='ace-icon fa fa-power-off']")
        #logout.click()
        #admin.sign_out()
        loginpage = home_page.sign_out()
        time.sleep(2)

        assert "login" in self.driver.current_url.lower()
