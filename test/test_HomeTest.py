import time

from selenium.webdriver.common.by import By

from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from utility.ExcelUtility import ExcelUtility


class Testlogout:


    def test_sign_out(self,browser_instance):
        self.driver = browser_instance

        excel_utility = ExcelUtility()
        user_name_value =excel_utility.read_user_data(2,1)
        password_value = excel_utility.read_user_data(2,2)

        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")

        loginpage = LoginPage(self.driver)
        loginpage.enter_user_name(user_name_value)
        loginpage.enter_password(password_value)

        loginpage.sign_in()
        time.sleep(1)

        #admin = self.driver.find_element(By.XPATH,"//a[@data-toggle='dropdown']")
        #admin.click()

        admin = HomePage(self.driver)
        admin.admin_icon()
        time.sleep(1)

        #logout = self.driver.find_element(By.XPATH,"//i[@class='ace-icon fa fa-power-off']")
        #logout.click()
        admin.sign_out()
        time.sleep(2)

        is_logged_out = True
        assert is_logged_out
