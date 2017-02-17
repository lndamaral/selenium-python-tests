from helper import properties
from selenium import webdriver

@staticmethod
def get():
    return webdriver.Remote(
                command_executor=properties.get_settings( )['APPIUM-SERVER-URL'],
                desired_capabilities={
                    'platformName': "iOS",
                    'platformVersion': properties.get_settings( )['DEFAULT-PLATFORM-VERSION'],
                    'deviceName': properties.get_settings( )['DEFAULT-DEVICE-NAME'],
                    'automationName': 'XCUITest',
                    'app': properties.get_settings( )['DEFAULT-APP-DIR'],
                    'newCommandTimeout': 72000,
                    'fullReset': True,
                }
            )