import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class AddBuildingPopup:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    CANCEL = "/html/body/div[5]/div/div[1]/div/div/div[2]/div[1]/button"
    SITE_DROPDOWN = "/html/body/div[5]/div/div[1]/div/div/div[1]/div[1]/div[1]/div[1]/button"
    SITE_VALUE = "/html/body/div[6]/div/div/div/div/span/div/div"
    BUILDING_NAME = "/html/body/div[5]/div/div[1]/div/div/div[1]/div[2]/input"
    BUILDING_IMAGE_DROPDOWN = "/html/body/div[5]/div/div[1]/div/div/div[1]/div[3]/div[1]/div[1]/button"
    BUILDING_IMAGE_VALUE = "/html/body/div[6]/div/div/div/div[25]/span/div/div/div"
    SUBMIT = "/html/body/div[5]/div/div[1]/div/div/div[2]/div[2]/button"

    # Get the location of Home
    def getCancel(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.CANCEL)

    # Click on cancel
    def clickCancel(self):
        time.sleep(1)
        self.getCancel().click()

    # Visibility of added technology
    def visibilityOfAddBuilding(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getCancel())
        time.sleep(1)
        if self.getCancel().is_displayed():
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

    # Get the location of building image dropdown
    def getBuildingImageDropdown(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.BUILDING_IMAGE_DROPDOWN)

    # Click on the building image dropdown
    def clickBuildingImageDropdown(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getBuildingImageDropdown())
        self.driver.implicitly_wait(10)
        self.getBuildingImageDropdown().click()

    # Get the location of building image value
    def getBuildingImageValue(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.BUILDING_IMAGE_VALUE)

    # Click on the building image value
    def clickBuildingImageValue(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getBuildingImageValue())
        self.driver.implicitly_wait(10)
        self.getBuildingImageValue().click()

    # Get the location of create button
    def getSubmit(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SUBMIT)

    # Click on the submit button
    def clickSubmit(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getSubmit())
        self.driver.implicitly_wait(10)
        self.getSubmit().click()

    def selectDropdown(self):
        self.clickSiteDropdown()
        self.clickSiteValue()
        # Click building image dropdown
        self.clickBuildingImageDropdown()
        # Click building image value
        self.clickBuildingImageValue()

    def createBuilding(self, build_name):
        # Enter all values
        self.enterBuildingName(build_name)
        # Click building image dropdown
        self.selectDropdown()
        # Click on the submit button
        self.clickSubmit()
        time.sleep(1)



