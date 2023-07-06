import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ScheduleMeetingPopup:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    SUBJECT_FIELD = "/html/body/div[4]/div/div[1]/div/div/div[1]/div/input"
    SAVE_BUTTON = "/html/body/div[4]/div/div[1]/div/div/div[2]/div[1]/button"
    CANCEL_BUTTON = "/html/body/div[4]/div/div[1]/div/div/div[2]/div[2]/button"

    # Get Username field
    def getSubject(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SUBJECT_FIELD)

    # Provide Username
    def enterSubject(self, sbj):
        self.getSubject().send_keys(sbj)

    # Clear Username Field
    def clearSubject(self):
        self.getSubject().send_keys(Keys.CONTROL + "a")
        self.getSubject().send_keys(Keys.DELETE)

    # Get Login Button
    def getSave(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SAVE_BUTTON)

    # Click on the Login button
    def clickSave(self):
        self.getSave().click()

    # Visibility of delete success
    def visibilityOfSchMeetingPopup(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getSave())
        self.driver.implicitly_wait(10)
        if self.getSave().is_displayed():
            return True
        else:
            return False

    # Get Login Button
    def getCancel(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.CANCEL_BUTTON)

    # Click on the Login button
    def clickCancel(self):
        self.getCancel().click()
