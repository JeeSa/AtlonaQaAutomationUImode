import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class RoleModifyPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    NAME = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div[1]/div/div/div/div/input"
    SAVE_CHANGES = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/span/span/div/div/div/div/div/button"

    # Get Password field
    def getName(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.NAME)

    # Provide Password
    def enterName(self, name):
        self.getName().send_keys(name)

    # Clear Password Field
    def clearName(self):
        self.getName().send_keys(Keys.CONTROL + "a")
        self.getName().send_keys(Keys.DELETE)

    def getSaveChanges(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SAVE_CHANGES)

    # Click on the Logout Button
    def clickSaveChanges(self):
        self.getSaveChanges().click()
