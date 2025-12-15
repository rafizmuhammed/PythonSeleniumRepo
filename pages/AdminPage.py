from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


from utility.PageUtility import PageUtility
from utility.WaitUtility import WaitUtility


class AdminPage:
    def __init__(self, driver):
        self.driver = driver
        self.waitutility = WaitUtility()
        self.PageUtility = PageUtility()

    '''def home_admin(self):
        admin = self.driver.find_element(By.XPATH, "//a[@href='https://groceryapp.uniqassosiates.com/admin/list-admin' and @class='small-box-footer']")
        self.waitutility.wait_until_clickable(self.driver, admin)
        self.PageUtility.click_on_element(admin)
        #admin.click()
        return AdminPage(self.driver)'''

    def return_home(self):
        home = self.driver.find_element(By.XPATH, "//a[text() ='Home']")
        self.waitutility.wait_until_clickable(self.driver,home)
        self.PageUtility.click_on_element(home)
        #home.click()

        from pages.HomePage import HomePage
        return HomePage(self.driver)


    def new_user(self):
        new = self.driver.find_element(By.XPATH, "//a[@class='btn btn-rounded btn-danger']")
        self.waitutility.wait_until_clickable(self.driver,new)
        self.PageUtility.click_on_element(new)
        #new.click()
        return self

    def enter_username(self):
        user_name = self.driver.find_element(By.XPATH, "//input[@id='username']")
        self.waitutility.wait_until_clickable(self.driver,user_name)
        self.PageUtility.click_on_element(user_name)
        #user_name.click()
        self.PageUtility.send_data_to_element(user_name,"admin")
        #user_name.send_keys("admin")
        return self

    def enter_password(self):
        password = self.driver.find_element(By.XPATH, "//input[@id='password']")
        self.waitutility.wait_until_clickable(self.driver,password)
        self.PageUtility.click_on_element(password)
        #password.click()
        self.PageUtility.send_data_to_element(password, "12345")
        #password.send_keys("12345")
        return self

    def select_dropdown(self):
        drop_down = self.driver.find_element(By.XPATH, "//select[@id='user_type']")
        self.waitutility.wait_until_clickable(self.driver,drop_down)
        self.PageUtility.select_data_with_value(drop_down, "Staff")
        #select = Select(drop_down)
        #select.select_by_visible_text('Staff')
        return self

    def save_user(self):
        save = self.driver.find_element(By.XPATH, "//button[@name='Create']")
        self.waitutility.wait_until_clickable(self.driver,save)
        self.PageUtility.click_on_element(save)
        #save.click()
        return self

    def refresh(self):
        reset = self.driver.find_element(By.XPATH, "//a[@class='btn btn-rounded btn-warning']")
        self.waitutility.wait_until_clickable(self.driver,reset)
        self.PageUtility.click_on_element(reset)
        #reset.click()
        return self

    def search_user(self):
        search = self.driver.find_element(By.XPATH, "//a[@class='btn btn-rounded btn-primary']")
        self.waitutility.wait_until_clickable(self.driver,search)
        self.PageUtility.click_on_element(search)
        #search.click()
        return self

    def search_user_name(self):
        user_name = self.driver.find_element(By.XPATH, "//input[@name='un']")
        self.waitutility.wait_until_clickable(self.driver,user_name)
        self.PageUtility.click_on_element(user_name)
        #user_name.click()
        self.PageUtility.send_data_to_element(user_name, "admin")
        #user_name.send_keys("admin")
        return self

    def search_dropdown(self):
        drop_down = self.driver.find_element(By.XPATH, "//select[@name='ut']")
        self.waitutility.wait_until_clickable(self.driver,drop_down)
        self.PageUtility.select_data_with_value(drop_down,"Staff")
        #select = Select(drop_down)
        #select.select_by_visible_text('Staff')
        return self

    def search_bar(self):
        search = self.driver.find_element(By.XPATH, "//button[@name='Search']")
        self.waitutility.wait_until_clickable(self.driver,search)
        self.PageUtility.click_on_element(search)
        #search.click()
        return self
