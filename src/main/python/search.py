from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
import os
import yaml

class SearchAmazon():
    # Enter the path to chromedriver location (probably in downloads folder)
    DRIVER_PATH     = 'C:/Users/marod/myprojects/bookAutomatic/drivers/chromedriver.exe'  
    BASE_URL        = ''

    def __init__(self):
        # Reading email and password from yaml file
        with open('src/main/python/config.yaml') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            self.email       = data['username']
            self.password    = data['password']

        # Declare/Initialize driver variable and load the given URL in browser window
        self.driver = webdriver.Chrome(self.DRIVER_PATH)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(self.BASE_URL)
        # Test whether correct URL was loaded
        assert '' in self.driver.title
        print('\n---------- LOG SUMMARY ----------\n')

    

    # def login(self):
    #     logIn = self.driver.find_element_by_id('loginButton')
    #     logIn.click()
    #     emailField = self.driver.find_element_by_id()
    #     emailField.send_keys(self.email)
    #     passwordField = self.driver.find_element_by_id()
    #     passwordField.send_keys(self.password)
    #     passwordField.send_keys(Keys.RETURN)
    #     print('Logged in successfully...')
    #     time.sleep(1)

    def closeDriver(self):
        self.driver.close()


