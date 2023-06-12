import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class SchedulingTemplateModifyPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    RESET = "reset"
    SAVE = "save"
    SET_DEFAULT = "setDefault"

    # Get Login Button
    def getReset(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.RESET)

    # Click on the Login button
    def clickReset(self):
        self.getReset().click()

    # Get Login Button
    def getSave(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.SAVE)

    # Click on the Login button
    def clickSave(self):
        self.getSave().click()

    def getSetDefault(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.SET_DEFAULT)

    # Click on the Login button
    def clickSetDefault(self):
        self.getSetDefault().click()
