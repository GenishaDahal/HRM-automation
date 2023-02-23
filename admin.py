from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = 'C:/Program Files (x86)/Google/Update/1.3.36.152/chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get('https://opensource-demo.orangehrmlive.com/')

admin_menu = driver.find_element(By.XPATH, "//a[@class='oxd-main-menu-item']")
admin_menu.click()
