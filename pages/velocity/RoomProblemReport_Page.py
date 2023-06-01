import time

from selenium.webdriver.common.by import By


class RoomProblemReportPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    ROOM1 = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[4]/ul[1]/li/span"
    MODIFY_ROOM_TECHNOLOGY1 = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[4]/ul[2]/li/a"

    # Get the location of add technology button
    def getRoom1(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ROOM1)

    # Click on the add technology button
    def clickRoom1(self):
        self.getRoom1().click()

    # Get the location of add technology button
    def getModifyRoomTechnology1(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.MODIFY_ROOM_TECHNOLOGY1)

    # Visibility of added technology
    def visibilityOfModifyRoomTech1(self):
        # self.driver.implicitly_wait(10)
        time.sleep(2)
        if self.getModifyRoomTechnology1().is_displayed():
            return True
        else:
            return False

    # Click on the add technology button
    def clickModifyRoomTechnology1(self):
        self.getModifyRoomTechnology1().click()

