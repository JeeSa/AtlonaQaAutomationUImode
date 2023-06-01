import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ModifyAccountTab:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    ACCOUNT_NAME_FIELD = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div[1]/div/div/div/div/div[1]/input"
    SAVE_CHANGES = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div[1]/div/div/div/div/div[11]/button"
    # Get the location of Home
    def getAccName(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ACCOUNT_NAME_FIELD)

    # Provide Password
    def enterAccName(self, acc_name):
        self.getAccName().send_keys(acc_name)

    # Clear Password Field
    def clearAccName(self):
        self.getAccName().send_keys(Keys.CONTROL + "a")
        self.getAccName().send_keys(Keys.DELETE)

    def getSaveChanges(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SAVE_CHANGES)

    # Click on the Login button
    def clickSaveChanges(self):
        self.getSaveChanges().click()
