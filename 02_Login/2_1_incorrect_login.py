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

try:
	wd.find_element_by_xpath("//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTextField[1]").send_keys("9096553317")
	wd.find_element_by_name("CONTINUE").click()
	wd.find_element_by_xpath("//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]").send_keys("1111")
	wd.find_element_by_xpath("//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton[1]").click()
	wd.find_element_by_name("(null)").click()
	wd.find_element_by_xpath("//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]").click()
	wd.find_element_by_xpath("//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]").click()
	wd.find_element_by_xpath("//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]").click()
	wd.switch_to_alert().accept()

finally:
	wd.quit()
	if not success:
		raise Exception("Test failed.")
