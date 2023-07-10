import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class BookingConfirmPopup:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    OK_BUTTON = "/html/body/div[4]/div/div[1]/div/div/div[2]/div/button"

    # Get Username field
    def getOk(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.OK_BUTTON)

    # Click on the Login button
    def clickOk(self):
        self.getOk().click()

    # Visibility of added technology
    def visibilityOfOkPop(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getOk())
        time.sleep(1)
        if self.getOk().is_displayed():
            return True
        else:
            return False
