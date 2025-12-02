from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pythonSeleniumBasics.BasicSelenium import BasicSelenium

class HandlingWebElements(BasicSelenium):
    def verify_web_element_commands(self):
        self.driver.get("https://selenium.qabible.in/simple-form-demo.php")
        messagebox = self.driver.find_element(By.XPATH, "//input[@id='single-input-field']")
        messagebox.send_keys("welcome")
        show_message_button = self.driver.find_element(By.XPATH, "//button[@id='button-one']")
        show_message_button.click()
        get_message = self.driver.find_element(By.XPATH, "//div[@id='message-one']")
        print(get_message.text)

        print(get_message.is_displayed())
        print(get_message.is_enabled())
        messagebox.clear()

elements = HandlingWebElements()
elements.initialize_browser()
elements.verify_web_element_commands()