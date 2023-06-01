import time

from selenium.webdriver.common.by import By


class DeviceListSettingsPopup:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    CLOSE = "/html/body/div[5]/div/div[1]/div/div/div[2]/div[2]/button"
    FIRMWARE_VERSION = "showFirmware"
    MODEL = "showModel"
    SAVE = "/html/body/div[5]/div/div[1]/div/div/div[2]/div[3]/button"
    RESET = "/html/body/div[5]/div/div[1]/div/div/div[2]/div[1]/button"


    # Get the location of Home
    def getClose(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.CLOSE)

    # Click on cancel
    def clickClose(self):
        time.sleep(1)
        self.getClose().click()

    # Visibility of added technology
    def visibilityOfDeviceListSettingsPop(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getClose())
        time.sleep(1)
        if self.getClose().is_displayed():
            return True
        else:
            return False

    def getFirmwareVersion(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.NAME, self.FIRMWARE_VERSION)

    # Click on cancel
    def clickFirmwareVersion(self):
        time.sleep(1)
        self.getFirmwareVersion().click()

    def getModel(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.NAME, self.MODEL)

    # Click on cancel
    def clickModel(self):
        time.sleep(1)
        self.getModel().click()

    def getSave(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SAVE)

    # Click on cancel
    def clickSave(self):
        time.sleep(1)
        self.getSave().click()

    def getReset(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.RESET)

    # Click on cancel
    def clickReset(self):
        time.sleep(1)
        self.getReset().click()



