from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import yaml
import time
from util import updater

class Sites():
    # Enter the path to chromedriver location
    DRIVER_PATH  = 'C:/Users/marod/myprojects/shopAutomatic/drivers/chromedriver.exe'
    #new_tab = False

    def __init__(self, pageURL, page):
        print('\n---------- LOG SUMMARY ----------\n')
        print('Opening ' + pageURL + '...')
        print('driver value: ' + str(updater.get_driver()))
        print('new_tab value: ' + str(updater.get_new_tab()))

        # Reading email and password from yaml file
        with open('config.yaml') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            self.email       = data['username' + page]
            self.password    = data['password' + page]

        # Declare/Initialize driver variable and load the given URL in browser window
        if updater.get_new_tab() == False:
            self.initializeDriver()
        else:
            try:
                #FIXME: creating new tab is not working when I select a new site
                #current_handle = updater.get_driver().current_window_handle
                #updater.get_driver().find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
                updater.get_driver().execute_script("window.open('about:blank', 'tab');")
                all_handles = updater.get_driver().window_handles
                num_handles = len(all_handles)
                WebDriverWait(updater.get_driver(), 10).until(EC.number_of_windows_to_be(num_handles))
                print("\nPage Title before switching: " + updater.get_driver().title)
                print("Total Windows: " + str(num_handles))
                updater.get_driver().switch_to_window(all_handles[num_handles - 1])
                # for handle in all_handles:
                #     if handle != current_handle:# and updater.get_driver().title == None:
                #         updater.get_driver().switch_to_window(handle)
                #         break
            except WebDriverException as e:
                updater.update_new_tab(False)
                updater.update_driver(None)
                self.initializeDriver()
                #print("Exception thrown: " + str(e))

        if updater.get_new_tab != False:
            updater.get_driver().get(pageURL)  
            time.sleep(2)
        # else:
        #     print("\nChrome Window was closed. Ending program!")
        #     self.tearDown()  

    def initializeDriver(self):
        print("\nInitializing driver!")
        options = webdriver.ChromeOptions()
        options.add_argument("disable-infobards")
        driver = webdriver.Chrome(chrome_options=options, executable_path=self.DRIVER_PATH)
        driver.maximize_window()
        driver.implicitly_wait(10)
        updater.update_driver(driver)
        updater.update_new_tab(True)

    def login(self):
        pass

    def searchItem(self, item):
        pass

    def tearDown(self):
        updater.get_driver().quit()