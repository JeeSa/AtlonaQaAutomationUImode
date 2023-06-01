import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class AddNewFloorPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    FLOOR_NAME_FIELD = "qa-6368cbcfee867c8b15731750"
    SUBMIT_BUTTON = "qa-63482e819c7f9125f1d6b1a6"
    FLOOR_COUNT_FIELD = "qa-6368cbf5eec9ea1427e9ae09"
    TOGGLE_BUTTON = "/html/body/div[5]/div/div[1]/div/div/div[1]/div/div[1]/input"

    # Get the location of floor name field
    def getFloorNameField(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.FLOOR_NAME_FIELD)

    # Provide building Name
    def enterFloorName(self, fl_name):
        self.getFloorNameField().send_keys(fl_name)

    # Clear building name Field
    def clearFloorName(self):
        self.getFloorNameField().send_keys(Keys.CONTROL + "a")
        self.getFloorNameField().send_keys(Keys.DELETE)

    # Get the location of view button
    def getSubmitButton(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.SUBMIT_BUTTON)

    # Click on the User Dropdown
    def clickSubmitButton(self):
        self.getSubmitButton().click()

    # Create New floor
    def createOneFloor(self, fl_name):
        # clear floor name
        self.clearFloorName()
        time.sleep(1)

        # Provide floor name
        self.enterFloorName(fl_name)
        time.sleep(1)

        # submit the floor name
        self.clickSubmitButton()

    # Visibility of add site page
    def visibilityOfAddFloorPage(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getSubmitButton())
        self.driver.implicitly_wait(10)
        if self.getSubmitButton().is_displayed():
            return True
        else:
            return False

    # Get the location of floor name field
    def getFloorCountField(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.FLOOR_COUNT_FIELD)

    # Provide building Name
    def enterFloorCount(self, fl_count):
        time.sleep(1)
        self.getFloorCountField().send_keys(fl_count)

    # Clear building name Field
    def clearFloorCount(self):
        self.getFloorCountField().send_keys(Keys.CONTROL + "a")
        self.getFloorCountField().send_keys(Keys.DELETE)

    # Get the location of view button
    def getToggleButton(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.TOGGLE_BUTTON)

    # Click on the User Dropdown
    def clickToggleButton(self):
        if self.visibilityOfFloorName() is True:
            self.getToggleButton().click()

    # Visibility of floor count
    def visibilityOfFloorName(self):
        self.driver.implicitly_wait(10)
        if self.getFloorNameField().is_displayed():
            return True
        else:
            return False
