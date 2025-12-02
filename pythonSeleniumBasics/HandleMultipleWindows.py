import time

from selenium.webdriver.common.by import By

from pythonSeleniumBasics.BasicSelenium import BasicSelenium


class HandleMultipleWindows(BasicSelenium):
    def verify_multiple_windows(self):
        self.driver.get("https://demo.guru99.com/popup.php")

        click_here = self.driver.find_element(By.XPATH, "//a[text()='Click Here']")
        click_here.click()
        handle_id = self.driver.current_window_handle

        handle_ids = self.driver.window_handles
        print(handle_ids)

        # Switch to the new window
        for handle in handle_ids:
            if handle != handle_id:
                # Switch to the new window
                self.driver.switch_to.window(handle)
                time.sleep(5)

                # Perform actions on the new window
                email_fld = self.driver.find_element(By.XPATH, "//input[@name='emailid']")
                email_fld.send_keys("abc@gmail.com")

                submit_fld = self.driver.find_element(By.XPATH, "//input[@name='btnLogin']")
                submit_fld.click()

                # Switch back to the main window
                self.driver.switch_to.window(handle_id)

                # Optional: Wait for a few seconds to observe results
                time.sleep(2)

multiple_windows = HandleMultipleWindows()
multiple_windows.initialize_browser()
multiple_windows.verify_multiple_windows()