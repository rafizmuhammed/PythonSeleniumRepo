import time

from selenium.webdriver.common.by import By

from pythonSeleniumBasics.BasicSelenium import BasicSelenium


class HandleAlerts(BasicSelenium):
    def verify_simple_alert(self):
        self.driver.get("https://demoqa.com/alerts")
        simple_alert_button = self.driver.find_element(By.XPATH, "//button[@id='alertButton']")
        simple_alert_button.click()

        # Switch to alert and accept it
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        print(alert_text)
        alert.accept()

        time.sleep(10)

    def verify_confirm_alert(self):
        self.driver.get("https://demoqa.com/alerts")
        self.driver.find_element(By.XPATH, "//button[@id='confirmButton']").click()
        alert = self.driver.switch_to.alert
        #alert.accept()
        alert.dismiss()

        confirm_alert_message = self.driver.find_element(By.XPATH, "//span[@id='confirmResult']")
        print(confirm_alert_message.text)
        time.sleep(10)

    def verify_prompt_alert(self):
        self.driver.get("https://demoqa.com/alerts")
        self.driver.find_element(By.XPATH, "//button[@id='promtButton']").click()
        alert = self.driver.switch_to.alert

        alert.send_keys("Welcome")
        alert.accept()
        time.sleep(10)

        #Not need
        '''prompt_message = self.driver.find_element(By.XPATH, "//span[@id='promptResult']")
        print(prompt_message.text)
        time.sleep(10)'''


simple_alert = HandleAlerts()
simple_alert.initialize_browser()
#simple_alert.verify_simple_alert()
#simple_alert.verify_confirm_alert()
simple_alert.verify_prompt_alert()