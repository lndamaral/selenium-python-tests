from selenium.webdriver.common.by import By
from base.base_element import BaseElement

class SeleniumHomepage(BaseElement):

    BTN_GO = (By.XPATH, "//input[@id='submit']")

    def __init__(self, driver):
        BaseElement.__init__(self, driver)

    def type_search(self, value):
        self.type( (By.XPATH, "//input[@id='q']"), value )

    def click_go(self):
        self.click( self.BTN_GO )
