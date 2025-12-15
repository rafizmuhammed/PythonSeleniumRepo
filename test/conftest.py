import os
from _pydatetime import datetime

import pytest
from selenium import webdriver

from utility import ScreenshotUtility

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


'''@pytest.fixture
def browser_instance():
    driver = webdriver.Firefox()
    yield driver
    driver.close()'''

@pytest.fixture
def browser_instance():
    options = FirefoxOptions()
    if is_ci():
        options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    #driver = webdriver.Firefox()
    yield driver
    driver.quit()

def pytest_configure(config):
    global REPORT_FOLDER
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") # Generate unique timestamp
    '''Create a folder structure in format /project/reports '''
    REPORT_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), 'reports', timestamp))
    os.makedirs(REPORT_FOLDER, exist_ok=True)
    # Override the HTML report output path dynamically and forces pytest-html to store the test report at:
    config.option.htmlpath = os.path.join(REPORT_FOLDER, "report.html")

@pytest.hookimpl(hookwrapper=True) #This hook runs after each phase of a test ("setup", "call", "teardown")
def pytest_runtest_makereport(item):
    global REPORT_FOLDER
    pytest_html = item.config.pluginmanager.getplugin('html') #Get HTML plugin
    '''Gets the final report of the test. 
    Initializes an extra list which will store screenshot HTML.'''
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extras', [])

    if report.when in ('setup', 'call'): # Checks if setup/call is failed
        xfail = hasattr(report, 'wasxfail')
        '''If test expected to fail but was skipped → include screenshot.
            If test failed normally → include screenshot.'''
        if (report.skipped and xfail) or (report.failed and not xfail):
            safe_name = report.nodeid.replace("::", "_").replace("/", "_")#Generate a safe filename. test_login.py::test_invalid_password becomes test_login.py_test_invalid_password.png
            screenshot_path = os.path.join(REPORT_FOLDER, f"{safe_name}.png")
            print(f"Capturing screenshot: {screenshot_path}")

            ScreenshotUtility.capture_screenshot(item, screenshot_path)#Invoke screenshot utility function
            #Add screenshot to the reports folder
            if os.path.exists(screenshot_path):
                html = (
                    f'<div><img src="file://{screenshot_path}" alt="screenshotscreenshot" '
                    'style="width:304px;height:228px;" onclick="window.open(this.src)" align="right"/></div>'
                )
                extra.append(pytest_html.extras.html(html))
        #Writes extras (screenshots) into the final report output.
        report.extras = extra


def is_ci():
    return os.getenv("CI") == "true"


@pytest.fixture(params=["chrome", "firefox"])
def cross_browser(request):

    if request.param == "chrome":
        options = ChromeOptions()
        if is_ci():
            options.add_argument("--headless")
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--disable-gpu")
        driver = webdriver.Chrome(options=options)
        #driver = webdriver.Chrome()

    elif request.param == "firefox":
        options = FirefoxOptions()
        if is_ci():
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
        #driver = webdriver.Firefox()
    elif request.param == "edge":
        options = EdgeOptions()
        if is_ci():
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")
        driver = webdriver.Edge(options=options)
        #driver = webdriver.Edge()
    yield driver
    driver.quit()

''''@pytest.fixture(params=["chrome", "firefox", "edge"])
def cross_browser(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    elif request.param == "edge":
        driver = webdriver.Edge()

    driver.maximize_window()
    yield driver'''