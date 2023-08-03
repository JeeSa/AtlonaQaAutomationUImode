import time

from selenium.webdriver.common.by import By


class CUIPageMenu:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    SET_AS_HOMEPAGE = "//div[contains(text(),'Set as Home Page')]"
    RENAME = "//div[contains(text(),'Rename')]"
    DELETE = "//div[contains(text(),'Delete')]"

    # Get the location of add technology button
    def getSetAsHomepage(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SET_AS_HOMEPAGE)

    # Visibility of added technology
    def visibilityOfPageMenu(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getSetAsHomepage())
        time.sleep(1)
        if self.getSetAsHomepage().is_displayed():
            return True
        else:
            return False


    # Click on the add technology button
    def clickSetAsHomepage(self):
        self.getSetAsHomepage().click()

    # Get the location of add technology button
    def getRename(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.RENAME)

    # Click on the add technology button
    def clickRename(self):
        self.getRename().click()

    # Get the location of add technology button
    def getDelete(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.DELETE)

    # Click on the add technology button
    def clickDelete(self):
        self.getDelete().click()
