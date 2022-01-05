from selenium import webdriver
from selenium.webdriver.common import action_chains

driver = webdriver.Chrome('C:/Users/Sky/Downloads/chromedriver_win32/chromedriver.exe')
driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')
driver.maximize_window()

source = driver.find_element_by_xpath('//*[@id="box2"]')
dest = driver.find_element_by_xpath('//*[@id="box102"]')
actions = action_chains.ActionChains(driver)

actions.drag_and_drop(source, dest).perform()