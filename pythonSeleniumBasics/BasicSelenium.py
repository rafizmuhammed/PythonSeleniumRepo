from selenium import webdriver

class BasicSelenium:
    def __init__(self):
        self.driver = None
    def initialize_browser(self):
        #self.driver = webdriver.Chrome()
        self.driver = webdriver.Firefox()
        self.driver.get("https://selenium.qabible.in/")
        self.driver.maximize_window()

    def closeBrowser(self):
        #self.driver.close()
        self.driver.quit()

if __name__ == "__main__":
    base = BasicSelenium()
    base.initialize_browser()
    base.closeBrowser()
