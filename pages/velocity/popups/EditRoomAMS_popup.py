import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class EditRoomPopup:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    CANCEL = "/html/body/div[7]/div/div[1]/div/div/div[2]/div[4]/button"
    ROOM_NAME = "/html/body/div[7]/div/div[1]/div/div/div[1]/div[4]/input"
    ROOM_TYPE_DROPDOWN = "/html/body/div[7]/div/div[1]/div/div/div[1]/div[5]/div[1]/div[1]/button"
    ROOM_TYPE_VALUE = "/html/body/div[9]/div/div/div/div[12]/span/div/div/div"
    SUBMIT = "/html/body/div[7]/div/div[1]/div/div/div[2]/div[5]/button"
    COPY = "/html/body/div[7]/div/div[1]/div/div/div[2]/div[2]/button"
    DELETE = "/html/body/div[7]/div/div[1]/div/div/div[2]/div[3]/div/button"
    EDIT_ROOM = "/html/body/div[7]/div/div[1]/div/div/div[2]/div[1]/button"

    # Get the location of Home
    def getCancel(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.CANCEL)

    # Click on cancel
    def clickCancel(self):
        time.sleep(1)
        self.getCancel().click()

    # Visibility of added technology
    def visibilityOfEditRoom(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getCancel())
        time.sleep(1)
        if self.getCancel().is_displayed():
            return True
        else:
            return False

    def getRoomName(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ROOM_NAME)

    # Provide building Name
    def enterRoomName(self, building_name):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getRoomName())
        self.driver.implicitly_wait(10)
        self.getRoomName().send_keys(building_name)

    # Clear building name Field
    def clearRoomName(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getRoomName())
        self.driver.implicitly_wait(10)
        self.getRoomName().send_keys(Keys.CONTROL + "a")
        self.getRoomName().send_keys(Keys.DELETE)

    # Get the location of building image dropdown
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
