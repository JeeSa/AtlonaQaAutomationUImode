import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class RoomModifyPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    ROOM_MODIFY_HELP = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[1]/div[2]/span/div/span[3]/a"
    NAME = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div/div/div/div/div[1]/div/span/span/div/input"
    SAVE_CHANGES = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div/div/div/div/div[3]/button"
    SAVE_FOR_MEETING_ROOM = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div/div/div/div/div[4]/button/div/div"
    EDIT_SUCCESS_POPUP = "/html/body/div[1]/footer/div/div/div[1]/div/div"

    # Get Login Button
    def getRoomModifyHelp(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ROOM_MODIFY_HELP)

    # Click on the Login button
    def clickRoomModifyHelp(self):
        self.getRoomModifyHelp().click()

    # validate Login help is redirecting to YouTube
    def validateRoomModifyHelp(self):

        # Store the ID of the original window
        main_window = self.driver.current_window_handle

        # Check we don't have other windows open already
        assert len(self.driver.window_handles) == 1

        # Click on the Login help
        self.clickRoomModifyHelp()

        # Wait for the new window or tab
        self.wait.until(EC.number_of_windows_to_be(2))

        all_windows = self.driver.window_handles
        for new_window in all_windows:
            if new_window != main_window:
                self.driver.switch_to.window(new_window)

                # wait until the destination page is loaded successfully
                self.wait.until(EC.url_contains("youtube.com"))
                time.sleep(1)

                self.driver.close()
                break

        self.driver.switch_to.window(main_window)

        # Check we don't have other windows open anymore
        assert len(self.driver.window_handles) == 1

    # Get the location of view button
    def getRoomName(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.NAME)

    # Click on the User Dropdown
    def enterRoomName(self, ro_name):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getRoomName())
        self.driver.implicitly_wait(10)
        self.getRoomName().send_keys(ro_name)

    # Clear Site name Field
    def clearRoomName(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getRoomName())
        self.driver.implicitly_wait(10)
        self.getRoomName().send_keys(Keys.CONTROL + "a")
        self.getRoomName().send_keys(Keys.DELETE)

    # Get the location of view button
    def getSaveChanges(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SAVE_CHANGES)

    # Click on the User Dropdown
    def clickSaveChanges(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getSaveChanges())
        self.driver.implicitly_wait(10)
        self.getSaveChanges().click()

    # Get the location of view button
    def getSaveMeeting(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SAVE_FOR_MEETING_ROOM)

    # Click on the User Dropdown
    def clickSaveMeeting(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getSaveMeeting())
        self.driver.implicitly_wait(10)
        self.getSaveMeeting().click()

    # Get the location of added floor
    def getEditSuccess(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.EDIT_SUCCESS_POPUP)

    # Create new Room
    def createMeetingRoom(self, ro_name):
        # clear floor name
        self.clearRoomName()
        time.sleep(1)

        # Provide floor name
        self.enterRoomName(ro_name)
        time.sleep(1)

        # submit the floor name
        self.clickSaveMeeting()


    # Visibility of delete success
    def visibilityOfEditSuccessPopup(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getEditSuccess())
        self.driver.implicitly_wait(10)
        if self.getEditSuccess().is_displayed():
            return True
        else:
            return False
