import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class AddRoomPopup:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    CANCEL = "/html/body/div[5]/div/div[1]/div/div/div[2]/div[1]/button"
    SITE_DROPDOWN = "/html/body/div[5]/div/div[1]/div/div/div[1]/div[1]/div[1]/div[1]/button"
    SITE_VALUE = "/html/body/div[6]/div/div/div/div/span/div/div"
    BUILDING_DROPDOWN = "/html/body/div[5]/div/div[1]/div/div/div[1]/div[2]/div[1]/div[1]/button"
    BUILDING_VALUE = "//div[contains(text(),'AAA AMS B1')]"
    FLOOR_DROPDOWN = "/html/body/div[5]/div/div[1]/div/div/div[1]/div[3]/div/div[1]/div[1]/button"
    FLOOR_VALUE = "/html/body/div[6]/div/div/div/div/span/div/div"
    ROOM_NAME = "/html/body/div[5]/div/div[1]/div/div/div[1]/div[4]/input"
    ROOM_TYPE_DROPDOWN = "/html/body/div[5]/div/div[1]/div/div/div[1]/div[5]/div[1]/div[1]/button"
    ROOM_TYPE_VALUE = "/html/body/div[6]/div/div/div/div[12]/span/div/div"
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
    def visibilityOfAddRoom(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getCancel())
        time.sleep(1)
        if self.getCancel().is_displayed():
            return True
        else:
            return False

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

    def getBuildingDropdown(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.BUILDING_DROPDOWN)

    # Click on the building image dropdown
    def clickBuildingDropdown(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getBuildingDropdown())
        self.driver.implicitly_wait(10)
        self.getBuildingDropdown().click()

    # Get the location of building image value
    def getBuildingValue(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.BUILDING_VALUE)

    # Click on the building image value
    def clickBuildingValue(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getBuildingValue())
        self.driver.implicitly_wait(10)
        self.getBuildingValue().click()

    def getFloorDropdown(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.FLOOR_DROPDOWN)

    # Click on the building image dropdown
    def clickFloorDropdown(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getFloorDropdown())
        self.driver.implicitly_wait(10)
        self.getFloorDropdown().click()

    # Get the location of building image value
    def getFloorValue(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.FLOOR_VALUE)

    # Click on the building image value
    def clickFloorValue(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getFloorValue())
        self.driver.implicitly_wait(10)
        self.getFloorValue().click()

    def getRoomName(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ROOM_NAME)

    # Provide building Name
    def enterRoomName(self, room_name):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getRoomName())
        self.driver.implicitly_wait(10)
        self.getRoomName().send_keys(room_name)

    # Clear building name Field
    def clearRoomName(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getRoomName())
        self.driver.implicitly_wait(10)
        self.getRoomName().send_keys(Keys.CONTROL + "a")
        self.getRoomName().send_keys(Keys.DELETE)

    def getRoomTypeDropdown(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ROOM_TYPE_DROPDOWN)

    # Click on the building image dropdown
    def clickRoomTypeDropdown(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getRoomTypeDropdown())
        self.driver.implicitly_wait(10)
        self.getRoomTypeDropdown().click()

    # Get the location of building image value
    def getRoomTypeValue(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ROOM_TYPE_VALUE)

    # Click on the building image value
    def clickRoomTypeValue(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getRoomTypeValue())
        self.driver.implicitly_wait(10)
        self.getRoomTypeValue().click()

    def getSubmit(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SUBMIT)

    # Click on cancel
    def clickSubmit(self):
        time.sleep(1)
        self.getSubmit().click()

    def selectDropdown(self):
        self.clickSiteDropdown()
        self.clickSiteValue()
        # Click building image dropdown
        self.clickBuildingDropdown()
        # Click building image value
        self.clickBuildingValue()
        self.clickFloorDropdown()
        self.clickFloorValue()
        self.clickRoomTypeDropdown()
        self.clickRoomTypeValue()

    def createRoom(self, room_name):
        # Enter all values
        self.enterRoomName(room_name)
        # Click building image dropdown
        self.selectDropdown()
        # Click on the submit button
        self.clickSubmit()
        time.sleep(1)

