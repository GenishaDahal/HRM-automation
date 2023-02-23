from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = 'C:/Program Files (x86)/Google/Update/1.3.36.152/chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get('https://opensource-demo.orangehrmlive.com/')
driver.maximize_window()
time.sleep(5)

user_name = driver.find_element(By.XPATH,"//input[@name = 'username']")
user_name.send_keys("Admin")

u_password = driver.find_element(By.XPATH,"//input[@name = 'password']")
u_password.send_keys("admin123")

login_button = driver.find_element(By.XPATH,"//button[@type = 'submit']")
login_button.click()
time.sleep(5)

admin_menu = driver.find_element(By.XPATH, "//a[@class='oxd-main-menu-item']")
admin_menu.click()
time.sleep(5)





