from selenium.webdriver.common.by import By


from pages.NewsPage import NewsPage
#from pages.LoginPage import LoginPage
from utility.PageUtility import PageUtility
from utility.WaitUtility import WaitUtility


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.waitutility = WaitUtility()
        self.PageUtility = PageUtility()

    def admin_icon(self):
        admin = self.driver.find_element(By.XPATH, "//a[@data-toggle='dropdown']")
        self.waitutility.wait_until_clickable(self.driver,admin)
        self.PageUtility.click_on_element(admin)
        #admin.click()
        return self


    def sign_out(self):
        logout = self.driver.find_element(By.XPATH, "//i[@class='ace-icon fa fa-power-off']")
        self.waitutility.wait_until_clickable(self.driver,logout)
        self.PageUtility.click_on_element(logout)
        #logout.click()

        from pages.LoginPage import LoginPage
        return LoginPage(self.driver)


    def home_admin(self):
        admin = self.driver.find_element(By.XPATH, "//a[@href='https://groceryapp.uniqassosiates.com/admin/list-admin' and @class='small-box-footer']")
        self.waitutility.wait_until_clickable(self.driver, admin)
        self.PageUtility.click_on_element(admin)
        #admin.click()

        from pages.AdminPage import AdminPage
        return AdminPage(self.driver)


    def manage_news(self):
        news = self.driver.find_element(By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/list-news' and @class='small-box-footer']")
        self.waitutility.wait_until_clickable(self.driver, news)
        self.PageUtility.click_on_element(news)

        #news.click()
        return NewsPage(self.driver)