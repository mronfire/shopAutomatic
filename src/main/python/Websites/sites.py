from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import yaml

class Sites():
    # Enter the path to chromedriver location
    DRIVER_PATH  = 'C:/Users/marod/myprojects/bookAutomatic/drivers/chromedriver.exe'

    def __init__(self, pageURL, page):
        print('\n---------- LOG SUMMARY ----------\n')
        print('Opening ' + pageURL + '...')

        # Reading email and password from yaml file
        with open('config.yaml') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            self.email       = data['username' + page]
            self.password    = data['password' + page]

        # Declare/Initialize driver variable and load the given URL in browser window
        self.driver = webdriver.Chrome(self.DRIVER_PATH)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(pageURL)

    def login(self):
        pass

    def searchItem(self, item):
        pass

    def closeDriver(self):
        self.driver.close()