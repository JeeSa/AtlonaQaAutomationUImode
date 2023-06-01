import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class BillOfMaterialsPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    CLOSE_BUTTON = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div[1]/div[2]/div/button"
    ATLONA_DEVICES = "//a[contains(text(),'View')]"

    def getCloseButton(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.CLOSE_BUTTON)

    # Provide Password
    def clickCloseButton(self):
        self.getCloseButton().click()

    def getAtlonaDevices(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_elements(By.XPATH, self.ATLONA_DEVICES)

    # Provide Password
    def clickViewButton(self):
        devices = self.getAtlonaDevices()
        devices[0].click()

