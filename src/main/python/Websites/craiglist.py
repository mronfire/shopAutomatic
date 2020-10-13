from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from websites.sites import Sites
from util import updater

class SearchCraiglist(Sites):

    def __init__(self):
        BASE_URL     = 'http://www.craigslist.org'
        super().__init__(BASE_URL, "Craiglist")
        #assert 'Amazon.com: Online Shopping for Electronics, Apparel, Computers, Books, DVDs & more' in driver.title

    def login(self):
        if updater.get_driver() != None and updater.get_login == True:
            logIn = updater.get_driver().find_element_by_link_text("my account")
            logIn.click()
            emailField = updater.get_driver().find_element_by_id('inputEmailHandle')
            emailField.send_keys(self.email)
            #emailField.send_keys(Keys.RETURN)
            passwordField = updater.get_driver().find_element_by_id('inputPassword')
            passwordField.send_keys(self.password)
            updater.get_driver().find_element_by_id('login').click()
            updater.get_driver().find_element_by_link_text('craigslist').click()
            print('\nLogged in successfully...')

    def searchItem(self, item):
        if updater.get_driver() != None:
            print("Searching for " + item)
            searchField = updater.get_driver().find_element_by_id('query')
            searchField.clear()
            searchField.send_keys(item)
            searchField.send_keys(Keys.RETURN)