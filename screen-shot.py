from selenium import webdriver

driver = webdriver.Chrome(executable_path='/Users/nitukumari/Desktop/web-crawler/chromedriver')

driver.get(input('ENTER YOYR TARGET URL HERE'))

driver.get_screenshot_as_file('1.png')
driver.close()
