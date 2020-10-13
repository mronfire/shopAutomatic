from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
#import time
from websites.sites import Sites
from util import updater

class SearchEbay(Sites):

    def __init__(self):
        BASE_URL     = 'https://www.ebay.com/'
        super().__init__(BASE_URL, "Ebay")
        #assert 'Electronics, Cars, Fashion, Collectibles & More | eBay' in driver.title
        
    def login(self):
        #FIXME:
        # Need to figure out how to bypass captcha
        if updater.get_driver() != None and updater.get_login == True:
            logIn = updater.get_driver().find_element_by_id('gh-ug')
            logIn.click()
            emailField = updater.get_driver().find_element_by_id('userid')
            emailField.send_keys(self.email)
            emailField.send_keys(Keys.RETURN)
            passwordField = updater.get_driver().find_element_by_id('pass')
            passwordField.send_keys(self.password)
            passwordField.send_keys(Keys.RETURN)

            #check if recaptcha is present
            if updater.get_driver().find_element_by_id('distilCaptchaForm').is_displayed():
                print('Recaptcha is displayed and we need to complete to move on...')
                WebDriverWait(updater.get_driver(), 20)
            
            print('\nLogged in successfully...')

    def searchItem(self, item):
        if updater.get_driver() != None:
            print("Searching for " + item)
            searchField = updater.get_driver().find_element_by_id('gh-ac')
            searchField.send_keys(item)
            searchField.send_keys(Keys.RETURN)