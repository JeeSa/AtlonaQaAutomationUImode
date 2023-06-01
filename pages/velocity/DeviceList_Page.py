import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


class DeviceListPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # AMS Device management page

    # Locators
    ADD_HAMBURGER_MENU = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div/div[1]/div/div[1]/div[2]/button"
    TOOLS_HAMBURGER_MENU = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[3]/button"
    EXPAND_BUILDING_BUTTON = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div/div[1]/div/div[2]/div[1]/div[2]/div/div/button"
    HDMI_ICON_1 = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/div/button[1]"
    ROOM_SETTINGS = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/div/button[2]"
    ROOM_DIV = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/div"
    SITE_NAME = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/span/strong"
    BUILDING_NAME = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div/div[1]/div/div[2]/div[1]/div[2]/div[1]/div"
    ROOM_NAME = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[1]"
    BUILDING_DIV_1 = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div/div[1]/div/div[2]/div[1]/div[2]/div[1]/div"
    SETTINGS_B1 = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/button[1]"
    BUILDING_DIV_2 = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div/div[1]/div/div[2]/div[1]/div[2]/div[2]/div"
    SITE_DIV = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]"
    SETTINGS_S = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/button[1]"
    SEARCH_FIELD = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/input"
    STRINGED_ROWS = "//u[contains(text(),'Atlona Velocity 10')]"
    TABLE_BODY = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr"
    CLEAR_SEARCH = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div/div[2]/div[1]/div[1]/div[2]/div/button"
    DEVICE_LIST_BUTTON = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div/div[1]/div/div[1]/div[1]/button"
    TABLE_HEADER = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div/div[2]/div[1]/div[2]/div/div[1]/table/thead/tr/th"
    SCAN_BUTTON = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[2]/button"

    # Get the location of Home
    def getAddHamburger(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ADD_HAMBURGER_MENU)

    # Click on cancel
    def clickAddHamburger(self):
        time.sleep(1)
        self.getAddHamburger().click()

    # Get the location of Home
    def getToolsHamburger(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.TOOLS_HAMBURGER_MENU)

    # Click on cancel
    def clickToolsHamburger(self):
        time.sleep(1)
        self.getToolsHamburger().click()

    def getExpandBuilding(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.EXPAND_BUILDING_BUTTON)

    # Click on cancel
    def clickExpandBuilding(self):
        time.sleep(1)
        self.getExpandBuilding().click()

    def getRoomDiv(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ROOM_DIV)

    # Click on cancel
    def hoverRoomDiv(self):
        time.sleep(1)
        action = ActionChains(self.driver)
        roomDiv = self.getRoomDiv()
        action.move_to_element(roomDiv).perform()

    def getHDMI1(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.HDMI_ICON_1)

    # Click on cancel
    def clickHDMI1(self):
        time.sleep(1)
        self.getHDMI1().click()

    def getRoomSettings(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ROOM_SETTINGS)

    # Click on cancel
    def clickRoomSettings(self):
        time.sleep(1)
        self.getRoomSettings().click()

    def getSiteName(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SITE_NAME)

    def passSiteName(self):
        siteName = self.getSiteName().text
        return siteName

    def getBuildingName(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.BUILDING_NAME)

    def passBuildingName(self):
        buildingName = self.getBuildingName().text
        return buildingName

    def getRoomName(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ROOM_NAME)

    def passRoomName(self):
        roomName = self.getRoomName().text
        return roomName

    def getBuildingDiv1(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.BUILDING_DIV_1)

    # Click on cancel
    def hoverBuildingDiv1(self):
        time.sleep(1)
        action = ActionChains(self.driver)
        buildingDiv = self.getBuildingDiv1()
        action.move_to_element(buildingDiv).perform()

    def getSettingsB1(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SETTINGS_B1)

    # Click on cancel
    def clickSettingsB1(self):
        time.sleep(1)
        self.getSettingsB1().click()

    def getBuildingDiv2(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.BUILDING_DIV_2)

    def passBuildingName2(self):
        buildingName = self.getBuildingDiv2().text
        return buildingName

    def getSiteDiv(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SITE_DIV)

    # Click on cancel
    def hoverSiteDiv(self):
        time.sleep(1)
        action = ActionChains(self.driver)
        siteDiv = self.getSiteDiv()
        action.move_to_element(siteDiv).perform()

    def getSettingsS(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SETTINGS_S)

    # Click on cancel
    def clickSettingsS(self):
        time.sleep(1)
        self.getSettingsS().click()

    def getSearchField(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SEARCH_FIELD)

    # Provide Username
    def enterSearchContent(self, content):
        self.getSearchField().send_keys(content)

    # Clear Username Field
    def clearSearchContent(self):
        self.getSearchField().send_keys(Keys.CONTROL + "a")
        self.getSearchField().send_keys(Keys.DELETE)

    def getRows(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_elements(By.XPATH, self.TABLE_BODY)

    def totalRowCount(self):
        rows = self.getRows()
        count = len(rows)
        return count

    def getRowsString(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_elements(By.XPATH, self.STRINGED_ROWS)

    def rowCountWithString(self):
        rows = self.getRowsString()
        count = len(rows)
        return count

    def getClearSearch(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.CLEAR_SEARCH)

    # Provide Password
    def clickClearSearch(self):
        self.getClearSearch().click()

    def getDeviceList(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.DEVICE_LIST_BUTTON)

    # Provide Password
    def clickDeviceList(self):
        self.getDeviceList().click()

    def getTableHeader(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_elements(By.XPATH, self.TABLE_HEADER)

    def passTableHeader(self):
        testList = []
        header = self.getTableHeader()

        for i in header:
            testList.append(i.text)

        return testList

    def getScan(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SCAN_BUTTON)

    # Provide Password
    def clickScan(self):
        self.getScan().click()

    def visibilityOfScanButton(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getScan())
        time.sleep(1)
        if self.getScan().is_displayed():
            return True
        else:
            return False





