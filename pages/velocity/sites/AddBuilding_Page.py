import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class AddBuildingPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    BUILDING_NAME_FIELD = "qa-6368c3e5f3a6970d53855c57"
    ADDRESS1_FIELD = "qa-6368c41e2116568e46663475"
    ADDRESS2_FIELD = "qa-6368c43fe6807e7fdd684e31"
    BUILDING_IMAGE_DROPDOWN = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div/div/div/div[4]/div[2]/div[2]/div[1]/button"
    BUILDING_IMAGE_VALUE = "/html/body/div[4]/div/div/div/div[25]/span"
    CREATE_BUTTON = "save"

    # Get the location of building name
    def getBuildingNameField(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.BUILDING_NAME_FIELD)

    # Provide building Name
    def enterBuildingName(self, building_name):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getBuildingNameField())
        self.driver.implicitly_wait(10)
        self.getBuildingNameField().send_keys(building_name)

    # Clear building name Field
    def clearBuildingName(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getBuildingNameField())
        self.driver.implicitly_wait(10)
        self.getBuildingNameField().send_keys(Keys.CONTROL + "a")
        self.getBuildingNameField().send_keys(Keys.DELETE)

    # Get the location of address 1
    def getAddress1Field(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.ADDRESS1_FIELD)

    # Provide address 1
    def enterAddress1(self, ad1):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getAddress1Field())
        self.driver.implicitly_wait(10)
        self.getAddress1Field().send_keys(ad1)

    # Clear address 1 Field
    def clearAddress1(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getAddress1Field())
        self.driver.implicitly_wait(10)
        self.getAddress1Field().send_keys(Keys.CONTROL + "a")
        self.getAddress1Field().send_keys(Keys.DELETE)

    # Get the location of address 2
    def getAddress2Field(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.ADDRESS2_FIELD)

    # Provide address 1
    def enterAddress2(self, ad2):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getAddress2Field())
        self.driver.implicitly_wait(10)

        self.getAddress2Field().send_keys(ad2)

    # Clear address 2 Field
    def clearAddress2(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getAddress2Field())
        self.driver.implicitly_wait(10)
        self.getAddress2Field().send_keys(Keys.CONTROL + "a")
        self.getAddress2Field().send_keys(Keys.DELETE)

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
    def getCreateButton(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.CREATE_BUTTON)

    # Click on the submit button
    def clickCreateBuilding(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getCreateButton())
        self.driver.implicitly_wait(10)
        self.getCreateButton().click()

    def enterAllValues(self, build_name, ad_1, ad_2):
        # Provide Site name
        self.enterBuildingName(build_name)
        time.sleep(1)
        # Provide Address 1
        self.enterAddress1(ad_1)
        time.sleep(1)
        # Provide Address 2
        self.enterAddress2(ad_2)
        time.sleep(1)

    def clearAllText(self):
        # Clear building name
        self.clearBuildingName()
        time.sleep(1)
        # Clear Address 1
        self.clearAddress1()
        time.sleep(1)
        # Clear Address 2
        self.clearAddress2()
        time.sleep(1)

    def selectDropdown(self):
        # Click building image dropdown
        self.clickBuildingImageDropdown()
        # Click building image value
        self.clickBuildingImageValue()

    def createBuilding(self, build_name, ad_1, ad_2):
        # Enter all values
        self.enterAllValues(build_name, ad_1, ad_2)
        # Click building image dropdown
        self.selectDropdown()
        # Click on the submit button
        self.clickCreateBuilding()
        time.sleep(1)

