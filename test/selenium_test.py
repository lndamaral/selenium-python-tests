from pages.selenium_homepage import SeleniumHomepage
from base.base_test import TestCase

class TestSelenium(TestCase):

    def a_Test(self):
        seleniumPage = SeleniumHomepage( self.driver )

        seleniumPage.type_search( "abc" )
        seleniumPage.click_go( )

    def b_Test(self):
        seleniumPage = SeleniumHomepage( self.driver )

        seleniumPage.type_search( "abc" )
        seleniumPage.click_go( )

    def c_Test(self):
        seleniumPage = SeleniumHomepage( self.driver )

        seleniumPage.type_search( "abc" )
        seleniumPage.click_go( )
