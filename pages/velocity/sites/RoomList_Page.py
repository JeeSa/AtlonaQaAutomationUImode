import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class RoomListPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    EDIT_TECHNOLOGY1_BUTTON = "//*[@id=\"page\"]/span/div/span/span/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/div/div[3]/span[1]/button"
    MORE_OPTION_BUTTON1 = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div/div[1]/div[3]/span/div/button"
    ADDED_FLOOR_LOCATION = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div[1]"
    MORE_OPTION_BUTTON2 = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div[1]/div[1]/div[3]/span/div/button"
    DELETE_ROOM2_BUTTON = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div[3]/span[4]/button"
    DELETE_SUCCESS_POPUP = "/html/body/div[1]/footer/div/div/div[1]/div/div"
    EDIT_ROOM1_BUTTON = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/div/div[3]/span[2]/button"
    COPY_ROOM1_BUTTON = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/div/div[3]/span[3]/button"
    DELETE_ROOM1_BUTTON = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/div/div[3]/span[4]/button"
    CONTROL_ROOM1_BUTTON = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/div/div[2]/span/button"
    EXPORT_ROOM1_BUTTON = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/div/div[4]/span/span/a"
    ROOMS_HELP = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[1]/div[2]/span/div/span[3]/a"
    FLOOR1_HELP = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div/div[1]/div[2]/span/span[2]/a"
    COPY_SUCCESS_POPUP = "/html/body/div[1]/footer/div/div/div[1]/div/div"
    MOVE_FLOOR_UP = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div[2]/div[1]/div[3]/span/button[1]"
    MOVE_FLOOR_DOWN = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div[1]/div[1]/div[3]/span/button[2]"
    ALL_SITES_BREADCRUMB = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[1]/div[2]/span/div/span[4]/ol/li[1]/a"
    FLOOR1_NAME = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div/div[1]/div[2]/span/span[1]"
    ROOM1_NAME = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/div/h4"
    VIEW_MEETING_1 = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/div/div[2]/span/button"

    # Get the location of view button
    def getEditTechnology1Button(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.EDIT_TECHNOLOGY1_BUTTON)

    # Visibility of edit technology 1 button
    def visibilityOfEditTechnology1Button(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getEditTechnology1Button())
        self.driver.implicitly_wait(10)
        if self.getEditTechnology1Button().is_displayed():
            return True
        else:
            return False

    # Click on the User Dropdown
    def clickEditTechnology1Button(self):
        self.getEditTechnology1Button().click()

    # Get the location of view button
    def getMoreButton1(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.MORE_OPTION_BUTTON1)

    # Click on the User Dropdown
    def clickMoreButton1(self):
        self.getMoreButton1().click()

    # Get the location of added floor
    def getAddedFloor(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ADDED_FLOOR_LOCATION)

    # Visibility of added floor
    def visibilityOfFloor2(self):
        self.driver.implicitly_wait(10)
        if self.getAddedFloor().is_displayed():
            return True
        else:
            return False

    # Get the location of view button
    def getMoreButton2(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.MORE_OPTION_BUTTON2)

    # Click on the User Dropdown
    def clickMoreButton2(self):
        self.getMoreButton2().click()

    # Get the location of added floor
    def getDeleteBtnRoom2(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.DELETE_ROOM2_BUTTON)

    # Visibility of added room
    def visibilityOfRoom2(self):
        self.driver.implicitly_wait(10)
        if self.getDeleteBtnRoom2().is_displayed():
            return True
        else:
            return False

    # Click on the User Dropdown
    def clickDeleteBtnRoom2(self):
        self.getDeleteBtnRoom2().click()

    # Get the location of added floor
    def getDeleteSuccess(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.DELETE_SUCCESS_POPUP)

    # Visibility of delete success
    def visibilityOfDeleteSuccessPopup(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getDeleteSuccess())
        self.driver.implicitly_wait(10)
        if self.getDeleteSuccess().is_displayed():
            return True
        else:
            return False

    # Get the location of view button
    def getEditRoom1Button(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.EDIT_ROOM1_BUTTON)

    # Visibility of edit technology 1 button
    def visibilityOfEditRoom1Button(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getEditRoom1Button())
        self.driver.implicitly_wait(10)
        if self.getEditRoom1Button().is_displayed():
            return True
        else:
            return False

    # Click on the User Dropdown
    def clickEditRoom1Button(self):
        self.getEditRoom1Button().click()

    # Get the location of view button
    def getCopyRoom1Button(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.COPY_ROOM1_BUTTON)

    # Visibility of edit technology 1 button
    def visibilityOfCopyRoom1Button(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getCopyRoom1Button())
        self.driver.implicitly_wait(10)
        if self.getCopyRoom1Button().is_displayed():
            return True
        else:
            return False

    # Click on the User Dropdown
    def clickCopyRoom1Button(self):
        self.getCopyRoom1Button().click()

    # Get the location of view button
    def getDeleteRoom1Button(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.DELETE_ROOM1_BUTTON)

    # Visibility of edit technology 1 button
    def visibilityOfDeleteRoom1Button(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getDeleteRoom1Button())
        self.driver.implicitly_wait(10)
        if self.getDeleteRoom1Button().is_displayed():
            return True
        else:
            return False

    # Click on the User Dropdown
    def clickDeleteRoom1Button(self):
        self.getDeleteRoom1Button().click()

    # Get the location of view button
    def getControlRoom1Button(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.CONTROL_ROOM1_BUTTON)

    # Visibility of edit technology 1 button
    def visibilityOfControlRoom1Button(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getControlRoom1Button())
        self.driver.implicitly_wait(10)
        if self.getControlRoom1Button().is_displayed():
            return True
        else:
            return False

    # Click on the User Dropdown
    def clickControlRoom1Button(self):
        self.getControlRoom1Button().click()

    # Get the location of view button
    def getExportRoom1Button(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.EXPORT_ROOM1_BUTTON)

    # Visibility of edit technology 1 button
    def visibilityOfExportRoom1Button(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getExportRoom1Button())
        self.driver.implicitly_wait(10)
        if self.getExportRoom1Button().is_displayed():
            return True
        else:
            return False

    # Click on the User Dropdown
    def clickExportRoom1Button(self):
        self.getExportRoom1Button().click()

    # Get Login Button
    def getRoomsHelp(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ROOMS_HELP)

    # Click on the Login button
    def clickRoomsHelp(self):
        self.getRoomsHelp().click()

    # validate Login help is redirecting to YouTube
    def validateRoomsHelp(self):

        # Store the ID of the original window
        main_window = self.driver.current_window_handle

        # Check we don't have other windows open already
        assert len(self.driver.window_handles) == 1

        # Click on the Login help
        self.clickRoomsHelp()

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

    # Get Login Button
    def getFloor1Help(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.FLOOR1_HELP)

    # Click on the Login button
    def clickFloor1Help(self):
        self.getFloor1Help().click()

    # validate Login help is redirecting to YouTube
    def validateFloor1Help(self):

        # Store the ID of the original window
        main_window = self.driver.current_window_handle

        # Check we don't have other windows open already
        assert len(self.driver.window_handles) == 1

        # Click on the Login help
        self.clickRoomsHelp()

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

    # Get the location of added floor
    def getCopySuccess(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.COPY_SUCCESS_POPUP)

    # Visibility of delete success
    def visibilityOfCopySuccessPopup(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getCopySuccess())
        self.driver.implicitly_wait(10)
        if self.getCopySuccess().is_displayed():
            return True
        else:
            return False

    # Get Login Button
    def getMoveUp(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.MOVE_FLOOR_UP)

    # Click on the Login button
    def clickMoveUp(self):
        self.getMoveUp().click()

    # Get Login Button
    def getMoveDown(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.MOVE_FLOOR_DOWN)

    # Click on the Login button
    def clickMoveDown(self):
        self.getMoveDown().click()

    # Get Login Button
    def getAllSitesBreadcrumb(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ALL_SITES_BREADCRUMB)

    # Click on the Login button
    def clickAllAitesBreadcrumb(self):
        self.getAllSitesBreadcrumb().click()

    def getFloorName(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.FLOOR1_NAME)

    def passFloorName(self):
        floorName = self.getFloorName().text
        return floorName

    def getRoomName(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ROOM1_NAME)

    def passRoomName(self):
        roomName = self.getRoomName().text
        return roomName

    # Get the location of view button
    def getViewMeeting1(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.VIEW_MEETING_1)

    # Click on the User Dropdown
    def clickViewMeeting1(self):
        self.getViewMeeting1().click()
