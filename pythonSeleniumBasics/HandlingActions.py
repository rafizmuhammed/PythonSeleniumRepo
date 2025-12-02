import time

import pyautogui
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pythonSeleniumBasics.BasicSelenium import BasicSelenium


class HandlingActions(BasicSelenium):
    def verify_mousehover(self):
        home = self.driver.find_element(By.XPATH, "//a[text()='Home']")
        actions = ActionChains(self.driver)
        actions.move_to_element(home).perform()
    def verify_right_click(self):
        home = self.driver.find_element(By.XPATH, "//a[text()='Home']")
        actions = ActionChains(self.driver)
        actions.context_click(home).perform()
    def verify_drag_and_drop(self):
        self.driver.get("https://demoqa.com/droppable")
        drag = self.driver.find_element(By.XPATH,"//div[@id ='draggable']")
        drop = self.driver.find_element(By.XPATH,"//div[@id ='droppable']")
        actions = ActionChains(self.driver)
        actions.drag_and_drop(drag,drop).perform()

    def verify_keyboard_action(self):
        # Simulate pressing Ctrl + T to open a new tab (using pyautogui)
        pyautogui.hotkey('ctrl', 't')
        time.sleep(2)  # Adding delay for visibility
        pyautogui.write('https://www.google.com')  # Typing URL
        pyautogui.press('enter')  # Pressing Enter

action = HandlingActions()
action.initialize_browser()
#action.verify_mousehover()
#action.verify_right_click()
#action.verify_drag_and_drop()
action.verify_keyboard_action()