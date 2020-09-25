from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#from Websites import sites

class SearchEbay():
    # Enter the path to chromedriver location (probably in downloads folder)
    DRIVER_PATH  = 'C:/Users/marod/myprojects/bookAutomatic/drivers/chromedriver.exe'  
    BASE_URL     = 'https://www.ebay.com/'

    def __init__(self):
        print('\n---------- LOG SUMMARY ----------\n')

        # Reading email and password from yaml file
        with open('config.yaml') as f:
            import yaml
            data = yaml.load(f, Loader=yaml.FullLoader)
            self.email       = data['usernameEbay']
            self.password    = data['passwordEbay']

        # Declare/Initialize driver variable and load the given URL in browser window
        self.driver = webdriver.Chrome(self.DRIVER_PATH)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(self.BASE_URL)
        # Test whether correct URL was loaded
        assert 'Electronics, Cars, Fashion, Collectibles & More | eBay' in self.driver.title

    def login(self):
        logIn = self.driver.find_element_by_id('gh-ug')
        logIn.click()
        emailField = self.driver.find_element_by_id('userid')
        emailField.send_keys(self.email)
        emailField.send_keys(Keys.RETURN)
        passwordField = self.driver.find_element_by_id('pass')
        passwordField.send_keys(self.password)
        passwordField.send_keys(Keys.RETURN)
        print('Logged in successfully...')
        time.sleep(1)

    def searchItem(self, item):
        print("Searching for " + item)
        searchField = self.driver.find_element_by_id('twotabsearchtextbox')
        searchField.send_keys(item)
        searchField.send_keys(Keys.RETURN)

    def closeDriver(self):
        self.driver.close()