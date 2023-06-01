import time

from selenium.webdriver.common.by import By


class AlertsPopup:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    CANCEL = "/html/body/div[5]/div/div[1]/div/div/div[2]/div[1]/button"

    # Get the location of Home
    def getCancel(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.CANCEL)

    # Click on cancel
    def clickCancel(self):
        time.sleep(1)
        self.getCancel().click()

    # Visibility of added technology
    def visibilityOfAlertsPop(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getCancel())
        time.sleep(1)
        if self.getCancel().is_displayed():
            return True
        else:
            return False

