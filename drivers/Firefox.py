from helper import properties
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

@staticmethod
def get():
    return webdriver.Remote(
                command_executor=properties.get_settings()['SELENIUM-SERVER-URL'],
                desired_capabilities=DesiredCapabilities.FIREFOX
            )