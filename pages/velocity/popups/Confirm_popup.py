import time

from selenium.webdriver.common.by import By


class ConfirmPopup:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    CANCEL_BUTTON = "/html/body/div[5]/div/div[1]/div/div/div[2]/div[1]/button"
    SUBMIT_BUTTON = "qa-63482e819c7f9125f1d6b1a6"

    # Get the location of Home
    def getCancel(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.CANCEL_BUTTON)

    # Click on cancel
    def clickCancel(self):
        time.sleep(1)
        self.getCancel().click()

    # Get the location of Submit
    def getSubmit(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.SUBMIT_BUTTON)

    # Click on cancel
    def clickSubmit(self):
        time.sleep(1)
        self.getSubmit().click()

    # Visibility of added technology
    def visibilityOfConfirmPopup(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getSubmit())
        time.sleep(1)
        if self.getSubmit().is_displayed():
            return True
        else:
            return False
