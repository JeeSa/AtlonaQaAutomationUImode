import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class StartMeetingPopup:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    MINS_15 = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div/div/span/div/div[1]/div[1]/div/button"
    MINS_30 = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div/div/span/div/div[1]/div[2]/div/button"
    MINS_60 = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div/div/span/div/div[1]/div[3]/div/button"
    START_NEW = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div/div/span/div/div[2]/button"
    CLOSE = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div/div/span/div/div[3]/button"

    # Get Username field
    def get_15mins(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.MINS_15)

    # Click on the Login button
    def click_15mins(self):
        self.get_15mins().click()

    # Get Username field
    def get_30mins(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.MINS_30)

    # Click on the Login button
    def click_30mins(self):
        self.get_30mins().click()

    # Get Username field
    def get_60mins(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.MINS_60)

    # Click on the Login button
    def click_60mins(self):
        self.get_60mins().click()

    # Get Login Button
    def getStart(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.START_NEW)

    # Click on the Login button
    def clickStart(self):
        self.getStart().click()

    # Visibility of delete success
    def visibilityOfStartMeetingPopup(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getStart())
        self.driver.implicitly_wait(10)
        if self.getStart().is_displayed():
            return True
        else:
            return False

    # Get Login Button
    def getClose(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.CLOSE)

    # Click on the Login button
    def clickClose(self):
        self.getClose().click()
