import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class EditBuildingPopup:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    CANCEL = "/html/body/div[5]/div/div[1]/div/div/div[2]/div[3]/button"
    BUILDING_NAME = "/html/body/div[5]/div/div[1]/div/div/div[1]/div[2]/input"
    BUILDING_IMAGE_DROPDOWN = "/html/body/div[5]/div/div[1]/div/div/div[1]/div[3]/div[1]/div[1]/button"
    BUILDING_IMAGE_VALUE = "/html/body/div[7]/div/div/div/div[25]/span/div/div/div"
    SUBMIT = "/html/body/div[5]/div/div[1]/div/div/div[2]/div[4]/button"
    COPY = "/html/body/div[5]/div/div[1]/div/div/div[2]/div[1]/button"
    DELETE = "/html/body/div[5]/div/div[1]/div/div/div[2]/div[2]/div/button"

    # Get the location of Home
    def getCancel(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.CANCEL)

    # Click on cancel
    def clickCancel(self):
        time.sleep(1)
        self.getCancel().click()

    # Visibility of added technology
    def visibilityOfEditBuilding(self):
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

    def getCopy(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.COPY)

    # Click on the submit button
    def clickCopy(self):
        self.driver.implicitly_wait(10)
        self.getCopy().click()

    def getDelete(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.DELETE)

    # Click on the submit button
    def clickDelete(self):
        self.driver.implicitly_wait(10)
        self.getDelete().click()
