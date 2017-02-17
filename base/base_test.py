import unittest
from helper import properties
from base_page import BasePage

class TestCase(unittest.TestCase):

    def setUp(self):
        self.driver = BasePage().get_driver( )
        self.driver.get( properties.get_settings()['DEFAULT-BASE-URL'] )

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()