import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class ConfigureEquipmentPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    CONF_HEADING = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div/div/div[2]/div/span/span[1]/div/span/div[2]/div[2]/div/div[1]/h1"
    ALIAS = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div/div/div[2]/div/span/span[1]/div/span/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/div/div[1]/input"
    SAVE = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div/div/div[2]/div/span/span[1]/div/span/div[2]/div[2]/div/div[1]/div[2]/button"
    IP_ADDRESS = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div/div/div[2]/div/span/span[1]/div/span/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/input"
    CLOSE = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div/div/div[2]/div/span/span[1]/div/span/div[2]/div[2]/div/div[1]/div[1]/button"

    # Get the location of add technology button
    def getConfHeading(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.CONF_HEADING)

    # Visibility of delete success
    def visibilityOfConfHeading(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getConfHeading())
        self.driver.implicitly_wait(10)
        if self.getConfHeading().is_displayed():
            return True
        else:
            return False

    # Get the location of added technology div
    def getAlias(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ALIAS)

    # Click on the User Dropdown
    def enterAlias(self, alias):
        self.driver.implicitly_wait(10)
        self.getAlias().send_keys(alias)

    # Clear Site name Field
    def clearAlias(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getAlias())
        self.driver.implicitly_wait(10)
        self.getAlias().send_keys(Keys.CONTROL + "a")
        self.getAlias().send_keys(Keys.DELETE)

    # Get the location of added technology div
    def getIP(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.IP_ADDRESS)

    # Click on the User Dropdown
    def enterIP(self, ip):
        self.driver.implicitly_wait(10)
        self.getIP().send_keys(ip)

    # Clear Site name Field
    def clearIP(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getIP())
        self.driver.implicitly_wait(10)
        self.getIP().send_keys(Keys.CONTROL + "a")
        self.getIP().send_keys(Keys.DELETE)

    # Get the location of view button
    def getSave(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SAVE)

    # Click on the User Dropdown
    def clickSave(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getSave())
        self.driver.implicitly_wait(10)
        self.getSave().click()

    # Get the location of view button
    def getClose(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.CLOSE)

    # Click on the User Dropdown
    def clickClose(self):
        self.driver.implicitly_wait(10)
        self.getClose().click()
