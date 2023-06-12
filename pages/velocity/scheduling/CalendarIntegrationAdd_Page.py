import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class CalendarIntegrationAddPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    TYPE_DROPDOWN = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div/div/div/span/div/div[2]/div[1]/button"
    GENERIC_TYPE = "/html/body/div[4]/div/div/div/div[4]/span"
    ALIAS_FIELD = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div/div/div/span/span[2]/div/input"
    CREATE_CALENDAR_INTEGRATION = "save"

    # Get Login Button
    def getTypeDrop(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.TYPE_DROPDOWN)

    # Click on the Login button
    def clickTypeDrop(self):
        self.getTypeDrop().click()

    # Get Login Button
    def getGenericType(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.GENERIC_TYPE)

    # Click on the Login button
    def clickGenericType(self):
        self.getGenericType().click()

    # Get Login Button
    def getAlias(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ALIAS_FIELD)

    # Provide Username
    def enterAlias(self, alias):
        self.getAlias().send_keys(alias)

    # Clear Username Field
    def clearAlias(self):
        self.getAlias().send_keys(Keys.CONTROL + "a")
        self.getAlias().send_keys(Keys.DELETE)

    # Get Button
    def getCreate(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.CREATE_CALENDAR_INTEGRATION)

    # Click on the button
    def clickCreate(self):
        self.getCreate().click()

