import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class RenameControlPopup:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    CLOSE_BUTTON = "/html/body/div[4]/div/div[1]/div/div/div[2]/div/button"
    PAGE_NAME_FIELD = "/html/body/div[4]/div/div[1]/div/div/div[1]/span/span/div/input"

    # Get the location of add technology button
    def getPageName(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.PAGE_NAME_FIELD)

    # Provide building Name
    def enterPageName(self, page_name):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getPageName())
        self.driver.implicitly_wait(10)
        self.getPageName().send_keys(page_name)

    # Clear building name Field
    def clearPageName(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getPageName())
        self.driver.implicitly_wait(10)
        self.getPageName().send_keys(Keys.CONTROL + "a")
        self.getPageName().send_keys(Keys.DELETE)

    # Get the location of add technology button
    def getCloseButton(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.CLOSE_BUTTON)

    # Visibility of added technology
    def visibilityOfRenameControlPop(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getCloseButton())
        time.sleep(1)
        if self.getCloseButton().is_displayed():
            return True
        else:
            return False

    # Click on the add technology button
    def clickCloseButton(self):
        self.getCloseButton().click()


