import time

from selenium.webdriver.common.by import By


from pages.LoginPage import LoginPage
from pages.NewsPage import NewsPage
from utility.ExcelUtility import ExcelUtility


class TestNews:
    def test_new_news(self,browser_instance):
        self.driver = browser_instance

        excel_utility = ExcelUtility()
        user_name_value = excel_utility.read_user_data(2, 1)
        password_value = excel_utility.read_user_data(2, 2)

        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")

        loginpage = LoginPage(self.driver)
        #loginpage.enter_user_name(user_name_value)
        #loginpage.enter_password(password_value)
        loginpage.enter_user_name(user_name_value).enter_password(password_value)

        #loginpage.sign_in()
        home_page = loginpage.sign_in()
        time.sleep(1)

        #news = self.driver.find_element(By.XPATH, "//a[@href='https://groceryapp.uniqassosiates.com/admin/list-news' and @class='small-box-footer']")
        #news.click()
        #news = NewsPage(self.driver)
        #news.manage_news()

        news_page = home_page.manage_news()
        time.sleep(1)

        #new = self.driver.find_element(By.XPATH,"//a[@onclick='click_button(1)']")
        #new.click()
        #news.create_news()

        news_page.create_news().news_info().save_news()
        time.sleep(1)

        #news_info = self.driver.find_element(By.XPATH,"//textarea[@id='news']")
        #news_info.send_keys("Welcome to News Page")
        #news.news_info()

        #news_page.news_info()
        #time.sleep(2)

        #save = self.driver.find_element(By.XPATH,"//button[@type='submit']")
        #save.click()
        #news.save_news()

        #news_page.save_news()
        #time.sleep(1)

        alert_message = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
        assert 'News Created Successfully' in alert_message.text

    def test_search_news(self,browser_instance):
        self.driver = browser_instance

        excel_utility = ExcelUtility()
        user_name_value = excel_utility.read_user_data(2, 1)
        password_value = excel_utility.read_user_data(2, 2)

        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")

        loginpage = LoginPage(self.driver)
        #loginpage.enter_user_name(user_name_value)
        #loginpage.enter_password(password_value)
        loginpage.enter_user_name(user_name_value).enter_password(password_value)

        #loginpage.sign_in()
        home_page = loginpage.sign_in()
        time.sleep(1)

        #news = self.driver.find_element(By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/list-news' and @class='small-box-footer']")
        #news.click()
        #news = NewsPage(self.driver)
        #news.manage_news()

        news_page = home_page.manage_news().search_news().news_title().search_news_title()
        time.sleep(1)

        #search = self.driver.find_element(By.XPATH, "//a[@class='btn btn-rounded btn-primary']")
        #search.click()
        #news.search_news()

        #news_page.search_news()
        #time.sleep(1)

        #title = self.driver.find_element(By.XPATH, "//input[@name='un']")
        #title.click()
        #title.send_keys("its snowing")
        #news.news_title()

        #news_page.news_title()
        #time.sleep(1)

        #search_news = self.driver.find_element(By.XPATH, "//button[@value='sr']")
        #search_news.click()
        #news.search_news_title()

        #news_page.search_news_title()
        #time.sleep(3)

        not_found = self.driver.find_elements(By.XPATH, "//center[text()='.........RESULT NOT FOUND.......']")
        assert not_found == [] or not_found[0].text == ".........RESULT NOT FOUND......."

