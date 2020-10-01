from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import yaml
import time
from util import updater

class Sites():
    # Enter the path to chromedriver location
    DRIVER_PATH  = 'C:/Users/marod/myprojects/shopAutomatic/drivers/chromedriver.exe'
    #new_tab = False

    def __init__(self, pageURL, page):#, newTab, driver):
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
            print("\nInitializing driver!")
            options = webdriver.ChromeOptions()
            options.add_argument("disable-infobards")
            driver = webdriver.Chrome(chrome_options=options, executable_path=self.DRIVER_PATH)
            driver.maximize_window()
            driver.implicitly_wait(10)
            updater.update_driver(driver)
            updater.update_new_tab(True)

        else:
            #FIXME: Need to create tabs for each site
            current_handle = updater.get_driver().current_window_handle
            updater.get_driver().find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
            #self.driver.execute_script("window.open('about:blank', 'tab');")
            time.sleep(3)
            all_handles = updater.get_driver().window_handles
            print("\nPage Title before switching: " + updater.get_driver().title)
            print("\nTotal Windows: " + str(len(all_handles)))
            for handle in all_handles:
                if handle != current_handle:
                    updater.get_driver().switch_to_window(handle)
                    print("\nPage title after switching: " + updater.get_driver().title)
                    break
            time.sleep(2)

        updater.get_driver().get(pageURL)    

    def login(self):
        pass

    def searchItem(self, item):
        pass

    def closeDriver(self):
        updater.get_driver().close()