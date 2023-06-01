import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class CustomNetworkPopup:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    IP_RANGE = "/html/body/div[5]/div/div[1]/div/div/div[1]/div/div[1]/div/div[1]/input"
    SUBNET_SCAN = "/html/body/div[5]/div/div[1]/div/div/div[1]/div/div[1]/div/div[2]/input"
    START_IP = "/html/body/div[5]/div/div[1]/div/div/div[1]/div/div[2]/div[1]/input"
    END_IP = "/html/body/div[5]/div/div[1]/div/div/div[1]/div/div[2]/div[2]/input"
    IP_ADDRESS = "/html/body/div[5]/div/div[1]/div/div/div[1]/div/div[2]/div/input"
    SUBNET_DROPDOWN = "/html/body/div[5]/div/div[1]/div/div/div[1]/div/div[2]/span/span[1]/div/div[2]/div[1]/button"
    SUBNET_VALUE = "/html/body/div[6]/div/div/div/div[2]/span"
    SCAN_NETWORK = "qa-63482e819c7f9125f1d6b1a6"

    # Get the location of Home
    def getIpRange(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.IP_RANGE)

    # Click on cancel
    def clickIpRange(self):
        time.sleep(1)
        self.getIpRange().click()

    # Visibility of added technology

    def getStartIp(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.START_IP)

    # Click on cancel
    def enterStartIp(self, startIp):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getStartIp())
        self.driver.implicitly_wait(10)
        self.getStartIp().send_keys(startIp)

    # Clear city Field
    def clearStartIp(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getStartIp())
        self.driver.implicitly_wait(10)
        self.getStartIp().send_keys(Keys.CONTROL + "a")
        self.getStartIp().send_keys(Keys.DELETE)

    def visibilityOfIpRangePopup(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getStartIp())
        time.sleep(1)
        if self.getStartIp().is_displayed():
            return True
        else:
            return False

    def getEndIp(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.END_IP)

    # Click on cancel
    def enterEndIp(self, endIp):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getEndIp())
        self.driver.implicitly_wait(10)
        self.getEndIp().send_keys(endIp)

    # Clear city Field
    def clearEndIp(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getEndIp())
        self.driver.implicitly_wait(10)
        self.getEndIp().send_keys(Keys.CONTROL + "a")
        self.getEndIp().send_keys(Keys.DELETE)

    def getSubnetScan(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SUBNET_SCAN)

    # Click on cancel
    def clickSubnetScan(self):
        time.sleep(1)
        self.getSubnetScan().click()

    def getIpAddress(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.START_IP)

    # Click on cancel
    def enterIpAddress(self, ipAddress):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getStartIp())
        self.driver.implicitly_wait(10)
        self.getStartIp().send_keys(ipAddress)

    # Clear city Field
    def clearIpAddress(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getIpAddress())
        self.driver.implicitly_wait(10)
        self.getIpAddress().send_keys(Keys.CONTROL + "a")
        self.getIpAddress().send_keys(Keys.DELETE)

    def getSubnetDropDown(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SUBNET_DROPDOWN)

    # Click on cancel
    def clickSubnetDropdown(self):
        time.sleep(1)
        self.getSubnetDropDown().click()

    def visibilityOfSubnetScanPopup(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getSubnetDropDown())
        time.sleep(1)
        if self.getSubnetDropDown().is_displayed():
            return True
        else:
            return False

    def getSubnetValue(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SUBNET_VALUE)

    # Click on cancel
    def clickSubnetValue(self):
        time.sleep(1)
        self.getSubnetValue().click()

    def getScanNetwork(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.SCAN_NETWORK)

    # Click on cancel
    def clickScanNetwork(self):
        time.sleep(1)
        self.getScanNetwork().click()

    def visibilityOfCustomNetworkPopup(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getScanNetwork())
        time.sleep(1)
        if self.getScanNetwork().is_displayed():
            return True
        else:
            return False



