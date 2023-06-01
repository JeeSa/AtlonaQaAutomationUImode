import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class EditFloorPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    FLOOR_NAME = "/html/body/div[5]/div/div[1]/div/div/div[1]/div/input"
    SUBMIT = "/html/body/div[5]/div/div[1]/div/div/div[2]/div[2]/button"

    # Get the location of view button
    def getFloorName(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.FLOOR_NAME)

    # Click on the User Dropdown
    def enterFloorName(self, floor_name):
        self.driver.implicitly_wait(10)
        self.getFloorName().send_keys(floor_name)

    # Clear Site name Field
    def clearFloorName(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getFloorName())
        self.driver.implicitly_wait(10)
        self.getFloorName().send_keys(Keys.CONTROL + "a")
        self.getFloorName().send_keys(Keys.DELETE)

    # Get the location of view button
    def getSubmitButton(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SUBMIT)

    # Visibility of edit floor page
    def visibilityOfEditFloorPage(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getSubmitButton())
        self.driver.implicitly_wait(10)
        if self.getSubmitButton().is_displayed():
            return True
        else:
            return False

    # Click on the User Dropdown
    def clickSubmitButton(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getSubmitButton())
        self.driver.implicitly_wait(10)
        self.getSubmitButton().click()

