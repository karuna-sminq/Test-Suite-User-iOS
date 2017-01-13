from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, os
from selenium import webdriver

success = True
desired_caps = {}
desired_caps['appium-version'] = '1.0'
desired_caps['platformName'] = 'iOS'
desired_caps['platformVersion'] = '10.2'
desired_caps['deviceName'] = 'iPhone 6'
desired_caps['app'] = os.path.abspath('/Users/sminq/Library/Developer/Xcode/DerivedData/Sminq_iOS-dgmqgdowxzqvxwgazckdwteycqix/Build/Products/Debug-iphonesimulator/Sminq iOS.app')

wd = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
wd.implicitly_wait(60)

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

wd.switch_to_alert().accept()
wd.implicitly_wait(3)
wd.find_element_by_name("NEXT").click()
wd.implicitly_wait(3)
wd.find_element_by_name("NEXT").click()
wd.implicitly_wait(3)
wd.find_element_by_name("START").click()
wd.implicitly_wait(3)

        # finally:
        #     wd.quit()
        #     if not success:
        #         raise Exception("Test failed.")
