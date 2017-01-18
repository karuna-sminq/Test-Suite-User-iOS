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
desired_caps['noReset'] = True

driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
driver.implicitly_wait(60)

def is_alert_present(driver):
    try:
        driver.switch_to_alert().text
        return True
    except:
        return False

# # Onboarding
#
# driver.switch_to_alert().accept()
# driver.implicitly_wait(3)

# driver.find_element_by_name("NEXT").click()
# driver.implicitly_wait(3)
# driver.find_element_by_name("NEXT").click()
# driver.implicitly_wait(3)
# driver.find_element_by_name("START").click()
# driver.implicitly_wait(3)
#
# # driver.quit()
#
# # Login
#
# driver.find_element_by_xpath("//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTextField[1]").send_keys("9096553317")
# driver.implicitly_wait(3)
# driver.find_element_by_name("CONTINUE").click()
# driver.implicitly_wait(3)
# driver.find_element_by_xpath("//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton[1]").click()
# driver.implicitly_wait(3)
# driver.find_element_by_xpath("//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton[1]").click()
# driver.implicitly_wait(3)
# driver.find_element_by_xpath("//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton[1]").click()
# driver.implicitly_wait(3)
# driver.find_element_by_xpath("//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton[1]").click()
# driver.implicitly_wait(3)

# Business Queue Search Listing
driver.find_element_by_xpath("//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeButton[1]").click()
driver.implicitly_wait(3)

driver.find_element_by_name("Search for businesses, locations, tags...").send_keys("shree")
driver.implicitly_wait(3)
# Business listing
driver.find_element_by_name("JOIN").click()
driver.implicitly_wait(3)

# # Check for Business Listing Screen
# def test_business_listing(self):
#     title = driver.find_element_by_xpath("//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeNavigationBar[1]/XCUIElementTypeStaticText[1]").text
#     print title
#     self.assertEqual("T", title)
#
# test_business_listing()

# Queue listing
driver.find_element_by_name("JOIN").click()
driver.implicitly_wait(3)
# Queue Profile
driver.find_element_by_name("SEE SCHEDULE").click()
driver.implicitly_wait(3)
# Timeslot Selection
driver.find_element_by_name("JOIN").click()
driver.implicitly_wait(3)
# Confirm Dialog
driver.switch_to_alert().accept()
driver.implicitly_wait(3)

# # Check for Token Creation Screen
# def test_token_creation(self):
#     title = driver.find_element_by_xpath("//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeNavigationBar[1]/XCUIElementTypeStaticText[1]").text
#     self.assertEqual("Booking Done", title)
#
# test_token_creation()

# Token - Make Payment
driver.find_element_by_name("MAKE PAYMENT").click()
driver.implicitly_wait(3)

#Subscription Charges
title = driver.find_element_by_xpath("//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeNavigationBar[1]/XCUIElementTypeStaticText[1]").text
driver.assertEqual(title, 'Membership')

#Consultation Charges
driver.find_element_by_name("PAY BOOKING CHARGES").click()
