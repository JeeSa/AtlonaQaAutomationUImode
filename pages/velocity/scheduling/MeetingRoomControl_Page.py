import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class MeetingRoomControlPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    START_BUTTON = "save"
    STOP_BUTTON = "save"
    PLUS_ICON = "addmeeting"
    ROOM_ICON = "confrooms"
    CROSS_BUTTON = "NavigationClose"
    BOOK_3 = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div/span/div[1]/div[4]/div[2]/a[3]/div/div[2]/div/span/div/button"
    ROOM2 = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div/div[1]/div[1]/div/div/ul/li[2]"
    ADD_BOOK_3 = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div/div[1]/div[2]/div[2]/a[3]/div/div[2]/div/span/div/button"
    ROOM_STATUS = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div/span/div[1]/div[4]/div[1]/h1"

    # Get Username field
    def getStart(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.START_BUTTON)

    # Click on the Login button
    def clickStart(self):
        self.getStart().click()

    # Get Login Button
    def getStop(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.STOP_BUTTON)

    # Click on the Login button
    def clickStop(self):
        self.getStop().click()

    # Get Login Button
    def getPlus(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.PLUS_ICON)

    # Click on the Login button
    def clickPlus(self):
        self.getPlus().click()

    def getRoomsIcon(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.ROOM_ICON)

    # Click on the Login button
    def clickRoomsIcon(self):
        self.getRoomsIcon().click()

    # Get Login Button
    def getBook3(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.BOOK_3)

    # Click on the Login button
    def clickBook3(self):
        self.getBook3().click()

    # Get Login Button
    def getRoom2(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ROOM2)

    # Click on the Login button
    def clickRoom2(self):
        self.getRoom2().click()

    def getRoomStatus(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ROOM_STATUS)

    def passRoomStatus(self):
        status = self.getRoomStatus().text
        return status

    # Get Login Button
    def getAddBook3(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ADD_BOOK_3)

    # Click on the Login button
    def clickAddBook3(self):
        self.getAddBook3().click()
