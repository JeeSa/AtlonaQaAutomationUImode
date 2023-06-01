import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class EditSitePopup:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    SITE_NAME_FIELD = "qa-636344ff3e2fc3b02007fc06"
    SUBMIT_BUTTON = "qa-6363446de8beefafd333ce8d"
    CANCEL_BUTTON = "qa-636342b5a217cedbbe5ea1b7"
    DELETE = "/html/body/div[5]/div/div[1]/div/div/div[2]/div[2]/div/button"

    # Get the location of site name
    def getSiteNameField(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.SITE_NAME_FIELD)

    # Provide Site Name
    def enterSiteName(self, site_name):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getSiteNameField())
        self.driver.implicitly_wait(10)
        self.getSiteNameField().send_keys(site_name)

    # Clear Site name Field
    def clearSiteName(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getSiteNameField())
        self.driver.implicitly_wait(10)
        self.getSiteNameField().send_keys(Keys.CONTROL + "a")
        self.getSiteNameField().send_keys(Keys.DELETE)

    # Get the location of submit button
    def getSubmitButton(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.SUBMIT_BUTTON)

    # Click on the submit button
    def clickSubmit(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getSubmitButton())
        self.driver.implicitly_wait(10)
        self.getSubmitButton().click()

    # Get the location of cancel button
    def getCancelButton(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.CANCEL_BUTTON)

    # Click on the submit button
    def clickCancel(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getCancelButton())
        self.driver.implicitly_wait(10)
        self.getCancelButton().click()

    # Visibility of add site page
    def visibilityOfEditSitePage(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getSiteNameField())
        self.driver.implicitly_wait(10)
        if self.getSiteNameField().is_displayed():
            return True
        else:
            return False

    def getDelete(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.DELETE)

    # Click on the submit button
    def clickDelete(self):
        self.driver.implicitly_wait(10)
        self.getDelete().click()

