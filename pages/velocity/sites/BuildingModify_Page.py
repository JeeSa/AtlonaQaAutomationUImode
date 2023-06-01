import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class BuildingModifyPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    BUILDING_NAME = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div/div/div/div/div[1]/input"
    SAVE_CHANGES = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div/div/div/div/div[5]/button"

    # Get the location of view button
    def getBuildingName(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.BUILDING_NAME)

    # Click on the User Dropdown
    def enterBuildingName(self, building_name):
        self.driver.implicitly_wait(10)
        self.getBuildingName().send_keys(building_name)

    # Clear Site name Field
    def clearBuildingName(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getBuildingName())
        self.driver.implicitly_wait(10)
        self.getBuildingName().send_keys(Keys.CONTROL + "a")
        self.getBuildingName().send_keys(Keys.DELETE)

    # Get the location of view button
    def getSaveButton(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SAVE_CHANGES)

    # Click on the User Dropdown
    def clickSaveButton(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getSaveButton())
        self.driver.implicitly_wait(10)
        self.getSaveButton().click()

