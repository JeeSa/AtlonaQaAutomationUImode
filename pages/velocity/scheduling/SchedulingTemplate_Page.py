import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class SchedulingTemplatePage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    TEMPLATE_1 = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div/div[2]/button"
    TEMPLATE_2 = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[2]/div/div[2]/button[1]"
    EDIT_TEMP2 = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[2]/div/div[2]/button[2]"

    # Get Login Button
    def getTemp_1(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.TEMPLATE_1)

    # Click on the Login button
    def clickTemp_1(self):
        self.getTemp_1().click()

    # Get Login Button
    def getTemp_2(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.TEMPLATE_2)

    # Click on the Login button
    def clickTemp_2(self):
        self.getTemp_2().click()

    def getEditTemp_2(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.EDIT_TEMP2)

    # Click on the Login button
    def clickEditTemp_2(self):
        self.getEditTemp_2().click()
