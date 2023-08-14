import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class BuildingsPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    VIEW_ROOMS1_BUTTON = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div/div/div[1]/div/div/div/div[2]/span/button"
    VIEW_ROOMS2_BUTTON = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div/div/div[2]/div/div/div/div[2]/span/button"
    VIEW_ROOMS3_BUTTON = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div/div/div[3]/div/div/div/div[2]/span/button"

    ADD_BUILDING_BUTTON = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[3]/div[1]/button"
    DELETE_BUILDING1_BUTTON = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div/div/div/div/div/div/div[3]/span[4]/button"
    DELETE_BUILDING2_BUTTON = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div/div/div[2]/div/div/div/div[3]/span[4]/button"
    DELETE_SUCCESS_POPUP = "/html/body/div[1]/footer/div/div/div[1]/div/div"

    EDIT_BUILDING1_BUTTON = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div/div/div/div/div/div/div[3]/span[1]/button"
    COPY_BUILDING1_BUTTON = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div/div/div/div/div/div/div[3]/span[2]/button"
    EXPORT_BUILDING1_BUTTON = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div/div/div/div/div/div/div[3]/span[3]/button"

    BUILDINGS_HELP = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[1]/div[2]/span/div/span[3]/a"
    COPY_SUCCESS_POPUP = "/html/body/div[1]/footer/div/div/div[1]/div/div"

    BUILDING_NAME = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div/div/div/div/div/div/h4"

    # Get the location of view button 1
    def getViewRooms1Button(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.VIEW_ROOMS1_BUTTON)

    # Visibility of view all room 1 button
    def visibilityOfViewRooms1Button(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getViewRooms1Button())
        self.driver.implicitly_wait(10)
        if self.getViewRooms1Button().is_displayed():
            return True
        else:
            return False

    # Click on the User Dropdown
    def clickViewAllRooms1(self):
        self.getViewRooms1Button().click()

    # Get the location of view button 1
    def getViewRooms2Button(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.VIEW_ROOMS2_BUTTON)

    # Visibility of view all room 1 button
    def visibilityOfViewRooms2Button(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getViewRooms2Button())
        self.driver.implicitly_wait(10)
        if self.getViewRooms2Button().is_displayed():
            return True
        else:
            return False

    # Click on the User Dropdown
    def clickViewAllRooms2(self):
        self.getViewRooms2Button().click()

    # Get the location of add button
    def getAddBuildingButton(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ADD_BUILDING_BUTTON)

    # Click on the User Dropdown
    def clickAddBuildingButton(self):
        self.getAddBuildingButton().click()

    # Get the location of add button
    def getDeleteBuilding2(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.DELETE_BUILDING2_BUTTON)

    # Click on the User Dropdown
    def clickDeleteBuilding2(self):
        self.getDeleteBuilding2().click()

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

    # Get the location of view button 1
    def getEditBuilding1Button(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.EDIT_BUILDING1_BUTTON)

    # Visibility of view all room 1 button
    def visibilityOfEditBuilding1Button(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getEditBuilding1Button())
        self.driver.implicitly_wait(10)
        if self.getEditBuilding1Button().is_displayed():
            return True
        else:
            return False

    # Click on the User Dropdown
    def clickEditBuilding1(self):
        self.getEditBuilding1Button().click()

    # Get the location of view button 1
    def getCopyBuilding1Button(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.COPY_BUILDING1_BUTTON)

    # Visibility of view all room 1 button
    def visibilityOfCopyBuilding1Button(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getCopyBuilding1Button())
        self.driver.implicitly_wait(10)
        if self.getCopyBuilding1Button().is_displayed():
            return True
        else:
            return False

    # Click on the User Dropdown
    def clickCopyBuilding1(self):
        self.getCopyBuilding1Button().click()

    # Get the location of view button 1
    def getExportBuilding1Button(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.EXPORT_BUILDING1_BUTTON)

    # Visibility of view all room 1 button
    def visibilityOfExportBuilding1Button(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getExportBuilding1Button())
        self.driver.implicitly_wait(10)
        if self.getExportBuilding1Button().is_displayed():
            return True
        else:
            return False

    # Click on the User Dropdown
    def clickExportBuilding1(self):
        self.getExportBuilding1Button().click()

    # Get the location of view button 1
    def getDeleteBuilding1Button(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.DELETE_BUILDING1_BUTTON)

    # Visibility of view all room 1 button
    def visibilityOfDeleteBuilding1Button(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getDeleteBuilding1Button())
        self.driver.implicitly_wait(10)
        if self.getDeleteBuilding1Button().is_displayed():
            return True
        else:
            return False

    # Click on the User Dropdown
    def clickDeleteBuilding1(self):
        self.getDeleteBuilding1Button().click()

    def getBuildingsHelp(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.BUILDINGS_HELP)

    # Click on the Login button
    def clickBuildingsHelp(self):
        self.getBuildingsHelp().click()

    # validate Login help is redirecting to YouTube
    def validateBuildingsHelp(self):

        # Store the ID of the original window
        main_window = self.driver.current_window_handle

        # Check we don't have other windows open already
        assert len(self.driver.window_handles) == 1

        # Click on the Login help
        self.clickBuildingsHelp()

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

    def getCopySuccess(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.DELETE_SUCCESS_POPUP)

    # Visibility of delete success
    def visibilityOfCopySuccessPopup(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getDeleteSuccess())
        self.driver.implicitly_wait(10)
        if self.getDeleteSuccess().is_displayed():
            return True
        else:
            return False

    # Get the location of view button 1
    def getViewRooms3Button(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.VIEW_ROOMS3_BUTTON)

    # Visibility of view all room 1 button
    def visibilityOfViewRooms3Button(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getViewRooms3Button())
        self.driver.implicitly_wait(10)
        if self.getViewRooms3Button().is_displayed():
            return True
        else:
            return False

    # Click on the User Dropdown
    def clickViewAllRooms3(self):
        self.getViewRooms3Button().click()

    def getBuildingName(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.BUILDING_NAME)

    def passBuildingName(self):
        buildingName = self.getBuildingName().text
        return buildingName

    def navToRoomListOfBuilding1(self):
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Buildings"))
        assert "Atlona Velocity | Buildings" in self.driver.title

        # Click on the view button
        self.clickViewAllRooms1()
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Room List"))
        assert "Atlona Velocity | Room List" in self.driver.title

    def navToRoomListOfBuilding2(self):
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Buildings"))
        assert "Atlona Velocity | Buildings" in self.driver.title

        # Click on the view button
        self.clickViewAllRooms2()
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Room List"))
        assert "Atlona Velocity | Room List" in self.driver.title

    def navToRoomListOfBuilding3(self):
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Buildings"))
        assert "Atlona Velocity | Buildings" in self.driver.title

        # Click on the view button
        self.clickViewAllRooms3()
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Room List"))
        assert "Atlona Velocity | Room List" in self.driver.title

    def navToBuildingModifyPage(self):
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Buildings"))
        assert "Atlona Velocity | Buildings" in self.driver.title

        # Click on the edit button
        self.clickEditBuilding1()
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Building Modify"))
        assert "Atlona Velocity | Building Modify" in self.driver.title

    def copyBuilding(self):
        # Click on the view button
        self.clickCopyBuilding1()
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Buildings"))
        assert "Atlona Velocity | Buildings" in self.driver.title
        # Verify if the copied building is visible
        assert self.visibilityOfViewRooms2Button() is True

