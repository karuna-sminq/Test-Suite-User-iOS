from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time, os

success = True
desired_caps = {}
desired_caps['appium-version'] = '1.0'
desired_caps['platformName'] = 'iOS'
desired_caps['platformVersion'] = '10.2'
desired_caps['deviceName'] = 'iPhone 7'
desired_caps['app'] = os.path.abspath('/Users/sminq/Downloads/UICatalog.app')

wd = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
wd.implicitly_wait(60)

def is_alert_present(wd):
	try:
		wd.switch_to_alert().text
		return True
	except:
		return False

# try:
# finally:
# 	wd.quit()
# 	if not success:
# 		raise Exception("Test failed.")
