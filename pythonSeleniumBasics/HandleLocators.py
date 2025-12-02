from selenium.webdriver.common.by import By

from pythonSeleniumBasics.BasicSelenium import BasicSelenium


class HandleLocators(BasicSelenium):
    def verifylocators(self):
        self.driver.get("https://selenium.qabible.in/simple-form-demo.php")
        self.driver.find_element(By.ID,"single-input-field")
        self.driver.find_element(By.CLASS_NAME,"form-control")
        self.driver.find_element(By.TAG_NAME,"button")
        self.driver.find_element(By.LINK_TEXT,"Checkbox Demo")
        self.driver.find_element(By.PARTIAL_LINK_TEXT,"Checkbox")
        self.driver.find_element(By.CSS_SELECTOR,"button[id ='button-one']")
        self.driver.find_element(By.XPATH,"//button[@id='button-one']")
        self.driver.find_element(By.XPATH, "//div[@class='card']//child::button[@id='button-one']")

        # XPath access using following
        self.driver.find_element(By.XPATH, "//button[@id='button-one']//following::div[@class='card']")

        # XPath access using preceding
        self.driver.find_element(By.XPATH, "//button[@id='button-one']//preceding::div[@class='card']")

        # XPath access using ancestor
        self.driver.find_element(By.XPATH, "//div/ancestor::div[@class='card']")

        # XPath access using descendant
        self.driver.find_element(By.XPATH, "//div[@class='card']//descendant::div")