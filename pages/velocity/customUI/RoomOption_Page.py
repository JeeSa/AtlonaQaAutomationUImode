import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class RoomOptionPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    CLOSE_BUTTON = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[1]/button/div/img"
    ROOM_NAME_HEADING = "//h2[contains(text(),'Room Name')]"

    # Get the location of add technology button
    def getRoomNameH(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ROOM_NAME_HEADING)

    # Visibility of added technology
    def visibilityOfRoomNameH(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getRoomNameH())
        time.sleep(1)
        if self.getRoomNameH().is_displayed():
            return True
        else:
            return False

    # Get the location of add technology button
    def getCloseButton(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.CLOSE_BUTTON)

    # Click on the add technology button
    def clickCloseButton(self):
        self.getCloseButton().click()


