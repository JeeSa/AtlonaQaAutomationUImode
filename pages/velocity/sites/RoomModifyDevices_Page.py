import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class RoomModifyDevicesPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    ADD_TECHNOLOGY_BUTTON = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div/div/div[1]/div/div[1]/div[3]/span/button[3]"
    VTP_DEVICE = "//h4[contains(text(),'Atlona Velocity 8\" Touch Panel - Black 1')]"
    BUILDING_BREADCRUMB = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div/div/div[1]/div/div[1]/div[2]/span/div/span[2]/ol/li[3]/a"
    EDIT_ROOM_DEVICES = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div/div/div[2]/div/span/span[1]/div/div/div[1]/div/span/table/tr/td/ul/li[1]/button"
    COPY_ROOM_DEVICE = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div/div/div[2]/div/span/span[1]/div/div/div[1]/div/span/table/tr/td/ul/li[3]/button"
    DELETE_ROOM_DEVICE = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div/div/div[2]/div/span/span[1]/div[1]/div/div[1]/div/span/table/tr/td/ul/li[4]/button"
    DEVICE_2 = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div/div/div[2]/div/span/span[1]/div[2]/div"
    BUILDING_NAME_BREADCRUMB = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div/div/div[1]/div/div[1]/div[2]/span/div/span[2]/ol/li[3]/a"
    DEVICE1_NAME = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div/div/div[2]/div/span/span[1]/div/div/div[1]/div/h4"
    CUSTOM_UI_DESIGNER = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div/div/div[2]/div/span/span[1]/div/div/div[1]/div/span/table/tr/td/ul/li[2]/button"
    IP = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div/div/div[2]/div/span/span[1]/div/div/div[1]/div/a"

    # Get the location of add technology button
    def getAddTechnologyButton(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ADD_TECHNOLOGY_BUTTON)

    # Click on the add technology button
    def clickAddTechnologyButton(self):
        self.getAddTechnologyButton().click()

    # Get the location of added technology div
    def getVTPDevice(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.VTP_DEVICE)

    # Visibility of added technology
    def visibilityOfVTPDevice(self):
        # self.driver.implicitly_wait(10)
        time.sleep(3)
        if self.getVTPDevice().is_displayed():
            return True
        else:
            return False

    # Get the location of add technology button
    def getBuildingInBreadcrumb(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.BUILDING_BREADCRUMB)

    # Click on the add technology button
    def clickBuildingInBreadcrumb(self):
        self.getBuildingInBreadcrumb().click()

    # Get the location of add technology button
    def getEditDevice(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.EDIT_ROOM_DEVICES)

    # Click on the add technology button
    def clickEditDevice(self):
        self.getEditDevice().click()

    # Get the location of add technology button
    def getCopyDevice(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.COPY_ROOM_DEVICE)

    # Click on the add technology button
    def clickCopyDevice(self):
        self.getCopyDevice().click()

    # Get the location of add technology button
    def getDeleteDevice(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.DELETE_ROOM_DEVICE)

    # Click on the add technology button
    def clickDeleteDevice(self):
        self.getDeleteDevice().click()

    # Get the location of added technology div
    def getDevice_2(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.DEVICE_2)

    # Visibility of added technology
    def visibilityOfDevice_2(self):
        # self.driver.implicitly_wait(10)
        time.sleep(3)
        if self.getDevice_2().is_displayed():
            return True
        else:
            return False

    # Get Login Button
    def getBuildingNameBreadcrumb(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.BUILDING_NAME_BREADCRUMB)

    # Click on the Login button
    def clickBuildingNameBreadcrumb(self):
        self.getBuildingNameBreadcrumb().click()

    def getDeviceName(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.DEVICE1_NAME)

    def passDeviceName(self):
        deviceName = self.getDeviceName().text
        return deviceName

    # Get Login Button
    def getCustomUI(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.CUSTOM_UI_DESIGNER)

    # Click on the Login button
    def clickCustomUI(self):
        self.getCustomUI().click()

    def copyRoomDevice(self):
        # wait until the modify room page is loaded successfully
        self.wait.until(EC.title_contains("Room Modify Devices"))
        assert "Atlona Velocity | Room Modify Devices" in self.driver.title

        # Click on the Copy device option
        self.clickCopyDevice()
        time.sleep(1)
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Room Modify Devices"))
        assert "Atlona Velocity | Room Modify Devices" in self.driver.title
        # Verify if the copied device is visible
        assert self.visibilityOfDevice_2() is True

    def getIp(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.IP)

    def passIp(self):
        ip = self.getIp().text
        return ip

    def navToCUIScreen(self):
        self.wait.until(EC.title_contains("Room Modify Devices"))
        assert "Atlona Velocity | Room Modify Devices" in self.driver.title

        # Click on the add technology button
        self.clickCustomUI()
        # wait until the  page is loaded successfully
        self.wait.until(EC.title_contains("Room Modify Screens"))
        assert "Atlona Velocity | Room Modify Screens" in self.driver.title

