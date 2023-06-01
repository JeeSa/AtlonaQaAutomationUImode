import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class AddRoomPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    ROOM_NAME_FIELD = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div/div/div/div/div[1]/div/span/span/div/input"
    SAVE_BUTTON = "//*[@id=\"page\"]/span/div/span/span/div[1]/div[2]/div/div/div/div/div/div[3]/button"

    # Get the location of floor name field
    def getRoomNameField(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ROOM_NAME_FIELD)

    # Provide building Name
    def enterRoomName(self, ro_name):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getRoomNameField())
        self.driver.implicitly_wait(10)

        self.getRoomNameField().send_keys(ro_name)

    # Clear building name Field
    def clearRoomName(self):
        self.getRoomNameField().send_keys(Keys.CONTROL + "a")
        self.getRoomNameField().send_keys(Keys.DELETE)

    # Get the location of building image value
    def getSaveButton(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SAVE_BUTTON)

    # Click on the building image value
    def clickSave(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getSaveButton())
        self.driver.implicitly_wait(10)
        self.getSaveButton().click()

    # Create new Room
    def createRoom(self, ro_name):
        # clear floor name
        self.clearRoomName()
        time.sleep(1)

        # Provide floor name
        self.enterRoomName(ro_name)
        time.sleep(1)

        # submit the floor name
        self.clickSave()
