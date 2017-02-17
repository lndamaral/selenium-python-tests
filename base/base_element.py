from helper import wait_until

class BaseElement():

    def __init__(self, driver):
        self.driver = driver

    def type(self, locator, value):
        print "Typing: '%s' - '%s' => '%s'" % (locator[0], locator[1], value)
        try:
            wait_until.presence_of_element_located(self.driver, locator).send_keys(value)
        except:
            self.driver.quit()
            raise

    def click(self, locator):
        print "Clicking: '%s' - '%s'" % (locator[0], locator[1])
        try:
            wait_until.element_to_be_clickable(self.driver, locator ).click()
        except:
            self.driver.quit()
            raise