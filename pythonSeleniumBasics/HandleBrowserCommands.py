from pythonSeleniumBasics.BasicSelenium import BasicSelenium


class HandleBrowserCommands(BasicSelenium):
    def verify_commands(self):
        title = self.driver.title
        print(title)

        url = self.driver.current_url
        print(url)

        handle_id = self.driver.current_window_handle
        print(handle_id)

commands = HandleBrowserCommands()
commands.initialize_browser()
commands.verify_commands()
