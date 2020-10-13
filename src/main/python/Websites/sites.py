from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import yaml
import time, os
from util import updater

class Sites():
    # Enter the path to chromedriver location
    # DRIVER_PATH  = 'C:/Users/marod/myprojects/shopAutomatic/driver/chromedriver.exe'
    #TODO: have to be the current directory location where project is cloned or download
    currentDir = os.getcwd()
    print(f"CurrentDir of project: {currentDir}\driver\chromedriver.exe")
    DRIVER_PATH = f"{currentDir}\driver\chromedriver.exe"

    def __init__(self, pageURL, page):
        print('\n---------- LOG SUMMARY ----------\n')
        print('Opening ' + pageURL + '...')
        print('driver value: ' + str(updater.get_driver()))
        print('new_tab value: ' + str(updater.get_new_tab()))

        # Reading email and password from yaml file
        with open('./src/main/resources/base/config.yaml') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            self.email       = data['username' + page]
            self.password    = data['password' + page]

        # Declare/Initialize driver variable and load the given URL in browser window
        if updater.get_new_tab() == False:
            self.initializeDriver()
        else:
            try:
                #current_handle = updater.get_driver().current_window_handle
                tab = updater.get_tab_num()
                updater.get_driver().execute_script("window.open('about:blank', 'tab" + str(tab) + "');")
                updater.update_tab_num(tab + 1)
                all_handles = updater.get_driver().window_handles
                print("\nAll handles created: " + str(all_handles))
                num_handles = len(all_handles)
                WebDriverWait(updater.get_driver(), 10).until(EC.number_of_windows_to_be(num_handles))
                print("Page Title before switching: " + updater.get_driver().title)
                print("Total Windows: " + str(num_handles))
                updater.get_driver().switch_to_window(all_handles[num_handles - 1])

            except WebDriverException as e:
                print("Sites-Exception: " + str(e))
                updater.update_new_tab(False)
                updater.update_driver(None)
                self.initializeDriver()

        if updater.get_new_tab != False:
            updater.get_driver().get(pageURL)  
            time.sleep(1) 

    def initializeDriver(self):
        print("\nInitializing driver...")
        options = webdriver.ChromeOptions()
        options.add_argument("disable-infobards")
        driver = webdriver.Chrome(chrome_options=options, executable_path=self.DRIVER_PATH)
        driver.maximize_window()
        driver.implicitly_wait(10)
        updater.update_driver(driver)
        updater.update_new_tab(True)
        print("Done initializing driver!")

    def login(self):
        pass

    def searchItem(self, item):
        pass

    def tearDown(self):
        updater.get_driver().quit()