import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.AdminPage import AdminPage
from pages.LoginPage import LoginPage
from utility.ExcelUtility import ExcelUtility


class TestAdmin:
    def test_return_to_home(self,browser_instance):
        self.driver = browser_instance

        excel_utility = ExcelUtility()
        user_name_value = excel_utility.read_user_data(2, 1)
        password_value = excel_utility.read_user_data(2, 2)

        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")

        loginpage = LoginPage(self.driver)
        #loginpage.enter_user_name(user_name_value)
        #loginpage.enter_password(password_value)
        loginpage.enter_user_name(user_name_value).enter_password(password_value)

        home_page = loginpage.sign_in()
        #loginpage.sign_in()
        time.sleep(1)

        #admin = self.driver.find_element(By.XPATH, "//a[@href='https://groceryapp.uniqassosiates.com/admin/list-admin' and @class='small-box-footer']")
        #admin.click()
        #admin = AdminPage(self.driver)
        #admin.home_admin()

        admin_page = home_page.home_admin()
        time.sleep(1)

        #home = self.driver.find_element(By.XPATH, "//a[text() ='Home']")
        #home.click()
        #admin.return_home()
        home_page = admin_page.return_home()
        time.sleep(2)

        assert "home" in self.driver.current_url


    def test_create_new_user(self,browser_instance):
        self.driver = browser_instance

        excel_utility = ExcelUtility()
        user_name_value = excel_utility.read_user_data(2, 1)
        password_value = excel_utility.read_user_data(2, 2)

        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")

        loginpage = LoginPage(self.driver)
        #loginpage.enter_user_name(user_name_value)
        #loginpage.enter_password(password_value)
        loginpage.enter_user_name(user_name_value).enter_password(password_value)

        home_page = loginpage.sign_in()
        #loginpage.sign_in()
        time.sleep(1)

        #admin = AdminPage(self.driver)
        #admin.home_admin()

        admin_page = home_page.home_admin().new_user().enter_username().enter_password().select_dropdown().save_user()
        time.sleep(1)

        #new =self.driver.find_element(By.XPATH, "//a[@class='btn btn-rounded btn-danger']")
        #new.click()
        #admin.new_user()

        #admin_page.new_user()
        #time.sleep(1)

        #user_name = self.driver.find_element(By.XPATH, "//input[@id='username']")
        #user_name.click()
        #user_name.send_keys("admin")
        #admin.enter_username()

        #admin_page.enter_username()
        #time.sleep(1)

        #password = self.driver.find_element(By.XPATH, "//input[@id='password']")
        #password.click()
        #password.send_keys("12345")
        #admin.enter_password()

        #admin_page.enter_password()
        #time.sleep(1)


        #drop_down = self.driver.find_element(By.XPATH, "//select[@id='user_type']")
        #select = Select(drop_down)
        #select.select_by_visible_text('Staff')
        #admin.select_dropdown()

        #admin_page.select_dropdown()
        #time.sleep(1)

        #save = self.driver.find_element(By.XPATH, "//button[@name='Create']")
        #save.click()
        #admin.save_user()

        #admin_page.save_user()
        #time.sleep(2)

        alert = self.driver.find_element(By.XPATH,"//div[@class='alert alert-danger alert-dismissible']")
        assert alert.is_displayed()



    def test_reset(self,browser_instance):
        self.driver = browser_instance

        excel_utility = ExcelUtility()
        user_name_value = excel_utility.read_user_data(2, 1)
        password_value = excel_utility.read_user_data(2, 2)

        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")

        loginpage = LoginPage(self.driver)
        #loginpage.enter_user_name(user_name_value)
        #loginpage.enter_password(password_value)
        loginpage.enter_user_name(user_name_value).enter_password(password_value)

        home_page = loginpage.sign_in()
        #loginpage.sign_in()
        time.sleep(1)

        #admin = AdminPage(self.driver)
        #admin.home_admin()

        admin_page = home_page.home_admin()
        time.sleep(1)

        #reset =self.driver.find_element(By.XPATH, "//a[@class='btn btn-rounded btn-warning']")
        #reset.click()
        #time.sleep(2)

        current_url = self.driver.current_url
        #reset = self.driver.find_element(By.XPATH, "//a[@class='btn btn-rounded btn-warning']")
        #reset.click()
        #admin.refresh()

        admin_page.refresh()
        time.sleep(2)

        refresh_url = self.driver.current_url
        assert current_url == refresh_url


    def test_search(self,browser_instance):
        self.driver = browser_instance

        excel_utility = ExcelUtility()
        user_name_value = excel_utility.read_user_data(2, 1)
        password_value = excel_utility.read_user_data(2, 2)

        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")

        loginpage = LoginPage(self.driver)
        #loginpage.enter_user_name(user_name_value)
        #loginpage.enter_password(password_value)
        loginpage.enter_user_name(user_name_value).enter_password(password_value)

        home_page = loginpage.sign_in()
        #loginpage.sign_in()
        time.sleep(1)

        #admin = self.driver.find_element(By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/list-admin' and @class='small-box-footer']")
        #admin.click()
        #admin = AdminPage(self.driver)
        #admin.home_admin()

        #admin_page.home_admin()

        admin_page = home_page.home_admin().search_user().search_user_name().search_dropdown().search_bar()
        time.sleep(1)

        #search =self.driver.find_element(By.XPATH, "//a[@class='btn btn-rounded btn-primary']")
        #search.click()
        #admin.search_user()

        #admin_page.search_user()
        #time.sleep(1)

        #user_name = self.driver.find_element(By.XPATH, "//input[@name='un']")
        #user_name.click()
        #user_name.send_keys("admin")
        #admin.search_user_name()

        #admin_page.search_user_name()
        #time.sleep(1)

        #drop_down = self.driver.find_element(By.XPATH, "//select[@name='ut']")
        #select = Select(drop_down)
        #select.select_by_visible_text('Staff')
        #admin.search_dropdown()

        #admin_page.search_dropdown()
        #time.sleep(1)

        #search = self.driver.find_element(By.XPATH, "//button[@name='Search']")
        #search.click()
        #admin.search_bar()

        #admin_page.search_bar()
        #time.sleep(2)

        dropdown = Select(self.driver.find_element(By.XPATH, "//select[@name='ut']"))
        first_option = dropdown.first_selected_option.text
        assert first_option == "Staff"





        #if want second option
        '''dropdown.select_by_index(2)  ----admin index is (2)
        selected = dropdown.first_selected_option.text
        assert selected == "Admin"'''



