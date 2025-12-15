from selenium.webdriver.common.by import By

from utility.PageUtility import PageUtility
from utility.WaitUtility import WaitUtility


class NewsPage:
    def __init__(self, driver):
        self.driver = driver
        self.waitutility = WaitUtility()
        self.PageUtility = PageUtility()

    '''def manage_news(self):
        news = self.driver.find_element(By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/list-news' and @class='small-box-footer']")
        self.waitutility.wait_until_clickable(self.driver, news)
        self.PageUtility.click_on_element(news)

        #news.click()
        return NewsPage(self.driver)'''

    def create_news(self):
        new = self.driver.find_element(By.XPATH, "//a[@onclick='click_button(1)']")
        self.waitutility.wait_until_clickable(self.driver, new)
        self.PageUtility.click_on_element(new)

        #new.click()
        return self

    def news_info(self,text = "Welcome to News Page"):
        news_info = self.driver.find_element(By.XPATH, "//textarea[@id='news']")
        self.waitutility.wait_until_clickable(self.driver, news_info)
        self.PageUtility.send_data_to_element(news_info,text)

        #news_info.send_keys("Welcome to News Page")
        return self

    def save_news(self):
        save = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        self.waitutility.wait_until_clickable(self.driver, save)
        self.PageUtility.click_on_element(save)

        #save.click()
        return self

    def search_news(self):
        search = self.driver.find_element(By.XPATH, "//a[@class='btn btn-rounded btn-primary']")
        self.waitutility.wait_until_clickable(self.driver, search)
        self.PageUtility.click_on_element(search)

        #search.click()
        return self

    def news_title(self,text = "its snowing"):
        title = self.driver.find_element(By.XPATH, "//input[@name='un']")
        self.waitutility.wait_until_clickable(self.driver, title)
        self.PageUtility.click_on_element(title)

        #title.click()

        self.PageUtility.send_data_to_element(title,text)

        #title.send_keys("its snowing")
        return self

    def search_news_title(self):
        search_news = self.driver.find_element(By.XPATH, "//button[@value='sr']")
        self.waitutility.wait_until_clickable(self.driver, search_news)
        self.PageUtility.click_on_element(search_news)

        #search_news.click()
        return self