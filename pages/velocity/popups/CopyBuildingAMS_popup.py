import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class CopyBuildingPopup:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    CLOSE = "/html/body/div[7]/div/div[1]/div/div/div[2]/div[1]/button"
    BUILDING_NAME = "/html/body/div[7]/div/div[1]/div/div/div[1]/div[1]/input"
    SITE_DROPDOWN = "/html/body/div[7]/div/div[1]/div/div/div[1]/div[2]/div[1]/div[1]/button"
    SITE_VALUE = "/html/body/div[8]/div/div/div/div/span/div/div"
    COPY = "/html/body/div[7]/div/div[1]/div/div/div[2]/div[2]/button"

    # Get the location of Home
    def getClose(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.CLOSE)

    # Click on cancel
    def clickClose(self):
        time.sleep(1)
        self.getClose().click()

    # Visibility of added technology
    def visibilityOfCopyBuilding(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getClose())
        time.sleep(1)
        if self.getClose().is_displayed():
            return True
        else:
            return False

    def getBuildingName(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.BUILDING_NAME)

    # Provide building Name
    def enterBuildingName(self, building_name):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getBuildingName())
        self.driver.implicitly_wait(10)
        self.getBuildingName().send_keys(building_name)

    # Clear building name Field
    def clearBuildingName(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getBuildingName())
        self.driver.implicitly_wait(10)
        self.getBuildingName().send_keys(Keys.CONTROL + "a")
        self.getBuildingName().send_keys(Keys.DELETE)

    # Get the location of building image dropdown
    def getSiteDropdown(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SITE_DROPDOWN)

    # Click on the building image dropdown
    def clickSiteDropdown(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getSiteDropdown())
        self.driver.implicitly_wait(10)
        self.getSiteDropdown().click()

    # Get the location of building image value
    def getSiteValue(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SITE_VALUE)

    # Click on the building image value
    def clickSiteValue(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getSiteValue())
        self.driver.implicitly_wait(10)
        self.getSiteValue().click()

    def getCopy(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.COPY)

    # Click on the submit button
    def clickCopy(self):
        self.driver.implicitly_wait(10)
        self.getCopy().click()

