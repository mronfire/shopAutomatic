# ShopAutomatic

### Description
Are you tired of having to open up your browser and then type your desired shopping webpage? What about having to open different tabs of different sites
to search for the same item again multiple times?
If the answer is YES, then stop doing that and instead opt to use this automated application that does all that for you.

Just select the shopping webpage (or opt to search in all available sites) where you want to look for the item and also provide your username and 
password (optional) and then let the application automate all the steps to find you an available item.

<b>Enjoy!</b>

### Technologies
- PyQT for the GUI
- Python
- Selenium

### Set-Up:
- In order for this to work you will have to download the web driver for the current Chrome version you have installed. At the time of writing this, I have version: <u>85.0.4183.121</u>
If you have a different Chrome version, download required web driver and place it in the drivers folder after you have cloned the project.
- Then, you want to add this drivers location in sites.py:
```
DRIVER_PATH = <pathToProject>/shopAutomatic/drivers/chromedriver.exe
```

### Installation 
#### Option #1:
1. git clone https://github.com/mronfire/shopAutomatic.git
2. cd shopAutomatic\target
3. run executable by typing:
    - shopAutomaticSetup.exe

#### Option #2:
1. Download Zip
2. Open project folder and double-click on the 'target' folder
3. Double-click shopAutomaticSetup.exe to install application in your machine