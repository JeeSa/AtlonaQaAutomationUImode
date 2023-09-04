import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class OME_SW32_card:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    SW32_DEVICE = "//h4[contains(text(),'AT-OME-SW32')]"
    EDIT_DEVICE = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div/div/div[2]/div/span/span[1]/div/div/div/div/div[3]/ul/li[1]/button"

    # Get the location of added technology div
    def getSW32Device(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SW32_DEVICE)

    # Visibility of added technology
    def visibilityOfSW32Device(self):
        # self.driver.implicitly_wait(10)
        time.sleep(3)
        if self.getSW32Device().is_displayed():
            return True
        else:
            return False

    # Get Login Button
    def getEdit(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.EDIT_DEVICE)

    # Click on the Login button
    def clickEdit(self):
        self.getEdit().click()
