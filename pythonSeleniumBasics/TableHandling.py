from selenium.webdriver.common.by import By

from pythonSeleniumBasics.BasicSelenium import BasicSelenium


class Table_handling(BasicSelenium):
    def verify_tables(self):
        self.driver.get("https://money.rediff.com/indices/nse")
        table = self.driver.find_element(By.XPATH,"//table[@id='dataTable']")
        print(table.text)

        table_row = self.driver.find_element(By.XPATH, "//table[@id='dataTable']/tbody/tr[3]")
        print("Third row text is ", table_row.text)  # Get the text of the row

        table_column = self.driver.find_element(By.XPATH, "//table[@id='dataTable']/tbody/tr[3]/td[2]")
        print("Third row second column text is ", table_column.text)  # Get the text of the column

        table_row_last = self.driver.find_element(By.XPATH, "//table[@id='dataTable']/tbody/tr[last()]")
        print('Last row text is ', table_row_last.text)

        table_row_last_column = self.driver.find_element(By.XPATH, "//table[@id='dataTable']/tbody/tr[3]/td[last()]")
        print('Third row last column text is ',table_row_last_column.text)

table_handling = Table_handling()
table_handling.initialize_browser()
table_handling.verify_tables()