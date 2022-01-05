from selenium import webdriver
driver = webdriver.Chrome('C:/Users/Sky/Downloads/chromedriver_win32/chromedriver.exe')
driver.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')
messageField = driver.find_element_by_xpath('//*[@id="user-message"]')
messageField.send_keys('Hello World')
showMessageButtom = driver.find_element_by_xpath('//*[@id="get-input"]/button')
showMessageButtom.click()