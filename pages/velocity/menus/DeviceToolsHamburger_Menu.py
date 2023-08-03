import time

from selenium.webdriver.common.by import By


class DeviceToolsHamburger:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    SCAN = "/html/body/div[5]/div/div/div/div/div/div[1]/span"
    DEVICE_LIST_SETTINGS = "/html/body/div[5]/div/div/div/div/div/div[2]/span"
    CREDENTIALS_MASS_UPDATE = "credentialsButton"
    FIRMWARE = "/html/body/div[5]/div/div/div/div/div/div[4]/span"
    ALERTS = "alertsButton"
    DELETE_ALL_UNASSIGNED = "/html/body/div[5]/div/div/div/div/div/div[6]/div/span"
    EXPORT_ALL = "/html/body/div[5]/div/div/div/div/div/div[7]/span"

    # Get the location of Home
    def getScan(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SCAN)

    # Click on cancel
    def clickScan(self):
        time.sleep(1)
        self.getScan().click()

    # Get the location of Submit
    def getDeviceListSettings(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.DEVICE_LIST_SETTINGS)

    # Click on cancel
    def clickDeviceListSettings(self):
        time.sleep(1)
        self.getDeviceListSettings().click()

    # Visibility of added technology
    def visibilityOfToolsHamburgerMenu(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getScan())
        time.sleep(1)
        if self.getScan().is_displayed():
            return True
        else:
            return False

    def getCredentialsMassUpdate(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.CREDENTIALS_MASS_UPDATE)

    # Click on cancel
    def clickCredentialsMassUpdate(self):
        time.sleep(1)
        self.getCredentialsMassUpdate().click()

    def getFirmware(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.FIRMWARE)

    # Click on cancel
    def clickFirmware(self):
        time.sleep(1)
        self.getFirmware().click()

    def getAlerts(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.ALERTS)

    # Click on cancel
    def clickAlerts(self):
        time.sleep(1)
        self.getAlerts().click()

    def getDeleteAllUnassigned(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.DELETE_ALL_UNASSIGNED)

    # Click on cancel
    def clickDeleteAllUnassigned(self):
        time.sleep(1)
        self.getDeleteAllUnassigned().click()

    def getExportAll(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.EXPORT_ALL)

    # Visibility of added technology
    def visibilityOfExportAll(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getExportAll())
        time.sleep(1)
        if self.getExportAll().is_displayed():
            return True
        else:
            return False

    # Click on cancel
    def clickExportAll(self):
        time.sleep(1)
        self.getExportAll().click()


