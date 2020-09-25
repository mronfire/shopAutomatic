from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#import time
from websites.sites import Sites

class SearchAmazon(Sites):

    def __init__(self):
        BASE_URL     = 'https://www.amazon.com/'
        super().__init__(BASE_URL, "Amazon")
        assert 'Amazon.com: Online Shopping for Electronics, Apparel, Computers, Books, DVDs & more' in self.driver.title

    def login(self):
        logIn = self.driver.find_element_by_id('nav-link-accountList')
        logIn.click()
        emailField = self.driver.find_element_by_id('ap_email')
        emailField.send_keys(self.email)
        emailField.send_keys(Keys.RETURN)
        passwordField = self.driver.find_element_by_id('ap_password')
        passwordField.send_keys(self.password)
        passwordField.send_keys(Keys.RETURN)
        print('\nLogged in successfully...')

    def searchItem(self, item):
        print("Searching for " + item)
        searchField = self.driver.find_element_by_id('twotabsearchtextbox')
        searchField.send_keys(item)
        searchField.send_keys(Keys.RETURN)