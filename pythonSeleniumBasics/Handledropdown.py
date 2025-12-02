from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By

from pythonSeleniumBasics.BasicSelenium import BasicSelenium


class Handle_dropdowns(BasicSelenium):
    def verify_dropdown(self):
        self.driver.get("https://www.webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html")
        dropdown = self.driver.find_element(By.XPATH, "//select[@id='dropdowm-menu-1']")
        select = Select(dropdown)
        select.select_by_index(1)
        select.select_by_value("python")
        select.select_by_visible_text("SQL")
        self.driver.back()
        self.driver.forward()
        self.driver.refresh()

    def verify_checkbox(self):
        self.driver.get("https://www.webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html")
        checkbox = self.driver.find_element(By.XPATH, "//input[@value='option-1']")
        #print(checkbox.is_selected()) false
        checkbox.click()
        print(checkbox.is_selected())
    def verify_radiobutton(self):
        self.driver.get("https://www.webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html")
        radiobutton = self.driver.find_element(By.XPATH, "//input[@value ='green']")
        radiobutton.click()



handle_drop_down = Handle_dropdowns()
handle_drop_down.initialize_browser()
handle_drop_down.verify_dropdown()
#handle_drop_down.verify_checkbox()
#handle_drop_down.verify_radiobutton()


