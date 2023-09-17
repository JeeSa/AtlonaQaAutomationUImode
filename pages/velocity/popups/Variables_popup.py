import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class VariablesPopup:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    CLOSE_BUTTON = "/html/body/div[6]/div/div[1]/div/div/div/div[1]/div/button"
    POPUP_NAME = "//h1[contains(text(),'Variables')]"

    # Get the location of add technology button
    def getPopupName(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.POPUP_NAME)

    # Visibility of added technology
    def visibilityOfVariablesPop(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getPopupName())
        time.sleep(1)
        if self.getPopupName().is_displayed():
            return True
        else:
            return False

    # Get the location of add technology button
    def getCloseButton(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.CLOSE_BUTTON)

    # Click on the add technology button
    def clickCloseButton(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getCloseButton())
        time.sleep(1)
        self.getCloseButton().click()


