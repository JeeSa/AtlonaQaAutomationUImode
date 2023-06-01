import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class SiteModifyPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    SITE_NAME = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div/div/div/div/div[1]/input"
    SAVE_CHANGES = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div/div/div/div/div[11]/button"

    # Get the location of view button
    def getSiteName(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SITE_NAME)

    # Click on the User Dropdown
    def enterSiteName(self, site_name):
        self.driver.implicitly_wait(10)
        self.getSiteName().send_keys(site_name)

    # Clear Site name Field
    def clearSiteName(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getSiteName())
        self.driver.implicitly_wait(10)
        self.getSiteName().send_keys(Keys.CONTROL + "a")
        self.getSiteName().send_keys(Keys.DELETE)

    # Get the location of view button
    def getSaveButton(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SAVE_CHANGES)

    # Click on the User Dropdown
    def clickSaveButton(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getSaveButton())
        self.driver.implicitly_wait(10)
        self.getSaveButton().click()

