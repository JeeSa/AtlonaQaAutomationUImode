import time
from selenium.webdriver.common.by import By


class FloorHamburgerMenu:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    ADD_ROOM = "/html/body/div[5]/div/div/div/div/div/div[1]/span"
    ADD_MEETING_ROOM = "/html/body/div[5]/div/div/div/div/div/div[2]/span"
    ADD_MULTIPLE_ROOMS = "/html/body/div[5]/div/div/div/div/div/div[3]/span"
    IMPORT_ROOM = "/html/body/div[5]/div/div/div/div/div/div[4]/span"
    ADD_NEW_FLOOR = "/html/body/div[5]/div/div/div/div/div/div[5]/span"
    EDIT_FLOOR = "/html/body/div[5]/div/div/div/div/div/div[6]/span"
    COPY_FLOOR = "/html/body/div[5]/div/div/div/div/div/div[7]/span"
    EXPORT_FLOOR = "/html/body/div[5]/div/div/div/div/div/div[8]/span"
    IMPORT_FLOOR = "/html/body/div[5]/div/div/div/div/div/div[9]/span"
    DELETE_FLOOR = "/html/body/div[5]/div/div/div/div/div/div[10]/span"
    REORDER_ROOMS = "/html/body/div[5]/div/div/div/div/div/div[11]/span"
    ALL_MACROS = "/html/body/div[5]/div/div/div/div/div/div[12]/span"
    ALL_DEVICES = "/html/body/div[5]/div/div/div/div/div/div[13]/span"

    # Get the location of view button
    def getAddRoom(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ADD_ROOM)

    # Visibility of added technology
    def visibilityOfAddRoom(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getAddRoom())
        time.sleep(1)
        if self.getAddRoom().is_displayed():
            return True
        else:
            return False

    # Click on the User Dropdown
    def clickAddRoom(self):
        self.getAddRoom().click()

    # Get the location of view button
    def getAddMeetingRoom(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ADD_MEETING_ROOM)

    # Visibility of added technology
    def visibilityOfAddMeetingRoom(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getAddMeetingRoom())
        time.sleep(1)
        if self.getAddMeetingRoom().is_displayed():
            return True
        else:
            return False

    # Click on the User Dropdown
    def clickAddMeetingRoom(self):
        self.getAddMeetingRoom().click()

    # Get the location of view button
    def getAddMultipleRooms(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ADD_MULTIPLE_ROOMS)

    # Visibility of added technology
    def visibilityOfAddMultipleRooms(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getAddMultipleRooms())
        time.sleep(1)
        if self.getAddMultipleRooms().is_displayed():
            return True
        else:
            return False

    # Click on the User Dropdown
    def clickAddMultipleRooms(self):
        self.getAddMultipleRooms().click()

    # Get the location of view button
    def getImportRoom(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.IMPORT_ROOM)

    # Visibility of added technology
    def visibilityOfImportRoom(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getImportRoom())
        time.sleep(1)
        if self.getImportRoom().is_displayed():
            return True
        else:
            return False

    # Click on the User Dropdown
    def clickImportRoom(self):
        self.getImportRoom().click()

    # Get the location of view button
    def getAddNewFloor(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ADD_NEW_FLOOR)

    # Visibility of added technology
    def visibilityOfAddNewFloor(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getAddNewFloor())
        time.sleep(1)
        if self.getAddNewFloor().is_displayed():
            return True
        else:
            return False

    # Click on the User Dropdown
    def clickAddNewFloor(self):
        time.sleep(1)
        self.getAddNewFloor().click()

    # Get the location of view button
    def getEditFloor(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.EDIT_FLOOR)

    # Visibility of added technology
    def visibilityOfEditFloor(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getEditFloor())
        time.sleep(1)
        if self.getEditFloor().is_displayed():
            return True
        else:
            return False

    # Click on the User Dropdown
    def clickEditFloor(self):
        self.getEditFloor().click()

    # Get the location of view button
    def getCopyFloor(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.COPY_FLOOR)

    # Visibility of added technology
    def visibilityOfCopyFloor(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getCopyFloor())
        time.sleep(1)
        if self.getCopyFloor().is_displayed():
            return True
        else:
            return False

    # Click on the User Dropdown
    def clickCopyFloor(self):
        self.getCopyFloor().click()

    # Get the location of view button
    def getExportFloor(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.EXPORT_FLOOR)

    # Visibility of added technology
    def visibilityOfExportFloor(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getExportFloor())
        time.sleep(1)
        if self.getExportFloor().is_displayed():
            return True
        else:
            return False

    # Click on the User Dropdown
    def clickExportFloor(self):
        self.getExportFloor().click()

    # Get the location of view button
    def getImportFloor(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.IMPORT_FLOOR)

    # Visibility of added technology
    def visibilityOfImportFloor(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getImportFloor())
        time.sleep(1)
        if self.getImportFloor().is_displayed():
            return True
        else:
            return False

    # Click on the User Dropdown
    def clickImportFloor(self):
        self.getImportFloor().click()

    # Get the location of delete floor button
    def getDeleteFloor(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.DELETE_FLOOR)

    # Visibility of added technology
    def visibilityOfDeleteFloor(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getDeleteFloor())
        time.sleep(1)
        if self.getDeleteFloor().is_displayed():
            return True
        else:
            return False

    # Click on the delete floor button
    def clickDeleteFloor(self):
        self.getDeleteFloor().click()

    # Get the location of view button
    def getReorderRooms(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.REORDER_ROOMS)

    # Visibility of added technology
    def visibilityOfReorderRooms(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getReorderRooms())
        time.sleep(1)
        if self.getReorderRooms().is_displayed():
            return True
        else:
            return False

    # Click on the User Dropdown
    def clickReorderRooms(self):
        self.getReorderRooms().click()

    # Get the location of view button
    def getAllMacros(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ALL_MACROS)

    # Visibility of added technology
    def visibilityOfAllMacros(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getAllMacros())
        time.sleep(1)
        if self.getAllMacros().is_displayed():
            return True
        else:
            return False

    # Click on the User Dropdown
    def clickAllMacros(self):
        self.getAllMacros().click()

    # Get the location of view button
    def getAllDevices(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ALL_DEVICES)

    # Visibility of added technology
    def visibilityOfAllDevices(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getAllDevices())
        time.sleep(1)
        if self.getAllDevices().is_displayed():
            return True
        else:
            return False

    # Click on the User Dropdown
    def clickAllDevices(self):
        self.getAllDevices().click()
