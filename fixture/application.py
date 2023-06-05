from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from fixture.session import SessionHelper
from fixture.projects import ProjectHelper


class Application:
    def __init__(self, browser, base_url):
        if browser == "firefox":
            # расположение firefox отличается от дефолтного(?)
            options = Options()
            options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
            self.wd = webdriver.Firefox(options=options)
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)

        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)
        self.base_url = base_url

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False
