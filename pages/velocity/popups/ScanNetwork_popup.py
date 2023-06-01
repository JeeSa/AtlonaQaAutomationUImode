import time

from selenium.webdriver.common.by import By


class ScanNetworkPopup:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    CLOSE = "/html/body/div[4]/div/div[1]/div/div/div[2]/div[1]/button"
    NETWORK_DROPDOWN = "/html/body/div[4]/div/div[1]/div/div/div[1]/div/div/div[1]/div/div[1]/div[1]/button"
    ALL = "/html/body/div[5]/div/div/div/div[2]/span/div/div/div/span"
    CUSTOM_NETWORK = "/html/body/div[5]/div/div/div/div[3]/span/div/div/div/span"
    ETH0 = "/html/body/div[5]/div/div/div/div[4]/span/div/div/div/span"
    SCAN_NETWORK = "/html/body/div[4]/div/div[1]/div/div/div[2]/div[3]/button"

    # Get the location of Home
    def getClose(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.CLOSE)

    # Click on cancel
    def clickClose(self):
        time.sleep(1)
        self.getClose().click()

    # Visibility of added technology
    def visibilityOfScanPopup(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getClose())
        time.sleep(1)
        if self.getClose().is_displayed():
            return True
        else:
            return False

    def getDropdown(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.NETWORK_DROPDOWN)

    # Click on cancel
    def clickDropdown(self):
        time.sleep(1)
        self.getDropdown().click()

    def getAll(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ALL)

    # Click on cancel
    def clickAll(self):
        time.sleep(1)
        self.getAll().click()

    def getCustom(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.CUSTOM_NETWORK)

    # Click on cancel
    def clickCustom(self):
        time.sleep(1)
        self.getCustom().click()

    def getEth0(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ETH0)

    # Click on cancel
    def clickEth0(self):
        time.sleep(1)
        self.getEth0().click()

    def getScanNetwork(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SCAN_NETWORK)

    # Click on cancel
    def clickScanNetwork(self):
        time.sleep(1)
        self.getScanNetwork().click()


