from selenium.webdriver.common.by import By


class NewsPage:
    def __init__(self, driver):
        self.driver = driver

    def manage_news(self):
        news = self.driver.find_element(By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/list-news' and @class='small-box-footer']")
        news.click()

    def create_news(self):
        new = self.driver.find_element(By.XPATH, "//a[@onclick='click_button(1)']")
        new.click()

    def news_info(self):
        news_info = self.driver.find_element(By.XPATH, "//textarea[@id='news']")
        news_info.send_keys("Welcome to News Page")

    def save_news(self):
        save = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        save.click()

    def search_news(self):
        search = self.driver.find_element(By.XPATH, "//a[@class='btn btn-rounded btn-primary']")
        search.click()

    def news_title(self):
        title = self.driver.find_element(By.XPATH, "//input[@name='un']")
        title.click()
        title.send_keys("its snowing")

    def search_news_title(self):
        search_news = self.driver.find_element(By.XPATH, "//button[@value='sr']")
        search_news.click()