import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class CopyRoomPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    YES_BUTTON = "/html/body/div[5]/div/div[1]/div/div/div[2]/div[2]/button"

    # Get the location of view button 1
    def getYesButton(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.YES_BUTTON)

    # Visibility of view all room 1 button
    def visibilityOfCopyRoom(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getYesButton())
        self.driver.implicitly_wait(10)
        if self.getYesButton().is_displayed():
            return True
        else:
            return False

    # Click on the User Dropdown
    def clickYesButton(self):
        self.getYesButton().click()
