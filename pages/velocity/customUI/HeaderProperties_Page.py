import time

from selenium.webdriver.common.by import By


class HeaderPropertiesPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    ROOM_TITLE_TOGGLE = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div[3]/div[2]/div[2]/div/div/div/div[3]/div[2]/div/div/div[1]/div/div/div[1]/div[2]/span/span/div/input"
    HEADER_ICONS_TOGGLE = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div[3]/div[2]/div[2]/div/div/div/div[3]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/span/span/div/input"
    ROOM_ON_EXPAND = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div[3]/div[2]/div[2]/div/div/div/div[3]/div[2]/div/div/div[2]/span/span/button"
    ROOM_ON_OTHER_TOGGLE = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div[3]/div[2]/div[2]/div/div/div/div[3]/div[2]/div/div/div[2]/div/div/div/div[2]/span/span/div/input"
    ROOM_OFF_EXPAND = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div[3]/div[2]/div[2]/div/div/div/div[3]/div[2]/div/div/div[3]/span/span/button"
    ROOM_OFF_OTHER_TOGGLE = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div[3]/div[2]/div[2]/div/div/div/div[3]/div[2]/div/div/div[3]/div/div/div/div[2]/span/span/div/input"
    NAVIGATION_EXPAND = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div[3]/div[2]/div[2]/div/div/div/div[3]/div[2]/div/div/div[4]/span/span/button"
    NAVIGATION_OTHER_TOGGLE = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div[3]/div[2]/div[2]/div/div/div/div[3]/div[2]/div/div/div[4]/div/div/div/div[2]/span/span/div/input"
    HOME_EXPAND = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div[3]/div[2]/div[2]/div/div/div/div[3]/div[2]/div/div/div[6]/span/span/button"
    HOME_OTHER_TOGGLE = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div[3]/div[2]/div[2]/div/div/div/div[3]/div[2]/div/div/div[6]/div/div/div/div[2]/span/span/div/input"
    MACRO_DRAWER_EXPAND = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div[3]/div[2]/div[2]/div/div/div/div[3]/div[2]/div/div/div[7]/span/span/button"
    MACRO_DRAWER_OTHER_TOGGLE = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div[3]/div[2]/div[2]/div/div/div/div[3]/div[2]/div/div/div[7]/div/div/div[1]/div[2]/span/span/div/input"
    ROOM_SUPPORT_HELP_EXPAND = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div[3]/div[2]/div[2]/div/div/div/div[3]/div[2]/div/div/div[9]/span/span/button"
    ROOM_SUPPORT_HELP_OTHER_TOGGLE = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div[3]/div[2]/div[2]/div/div/div/div[3]/div[2]/div/div/div[9]/div/div/div/div[2]/span/span/div/input"

    def getRoomTitleToggle(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ROOM_TITLE_TOGGLE)

    def clickRoomTitleToggle(self):
        self.getRoomTitleToggle().click()

    def getHeaderIconsToggle(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.HEADER_ICONS_TOGGLE)

    def clickHeaderIconsToggle(self):
        self.getHeaderIconsToggle().click()

    def getRoomOnExpand(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ROOM_ON_EXPAND)

    def clickRoomOnExpand(self):
        self.getRoomOnExpand().click()

    def getRoomOnOtherToggle(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ROOM_ON_OTHER_TOGGLE)

    def clickRoomOnOtherToggle(self):
        self.getRoomOnOtherToggle().click()

    def getRoomOffExpand(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ROOM_OFF_EXPAND)

    def clickRoomOffExpand(self):
        self.getRoomOffExpand().click()

    def getRoomOffOtherToggle(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ROOM_OFF_OTHER_TOGGLE)

    def clickRoomOffOtherToggle(self):
        self.getRoomOffOtherToggle().click()

    def getNavigationExpand(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.NAVIGATION_EXPAND)

    def clickNavigationExpand(self):
        self.getNavigationExpand().click()

    def getNavigationOtherToggle(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.NAVIGATION_OTHER_TOGGLE)

    def clickNavigationOtherToggle(self):
        self.getNavigationOtherToggle().click()

    def getHomeExpand(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.HOME_EXPAND)

    def clickHomeExpand(self):
        self.getHomeExpand().click()

    def getHomeOtherToggle(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.HOME_OTHER_TOGGLE)

    def clickHomeOtherToggle(self):
        self.getHomeOtherToggle().click()

    def getMacroDrawerExpand(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.MACRO_DRAWER_EXPAND)

    def clickMacroDrawerExpand(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getMacroDrawerExpand())
        self.driver.implicitly_wait(10)
        self.getMacroDrawerExpand().click()

    def getMacroDrawerOtherToggle(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.MACRO_DRAWER_OTHER_TOGGLE)

    def clickMacroDrawerOtherToggle(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getMacroDrawerOtherToggle())
        self.driver.implicitly_wait(10)
        self.getMacroDrawerOtherToggle().click()

    def getRoomSupportHelpExpand(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ROOM_SUPPORT_HELP_EXPAND)

    def clickRoomSupportHelpExpand(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getRoomSupportHelpExpand())
        self.driver.implicitly_wait(10)
        self.getRoomSupportHelpExpand().click()

    def getRoomSupportHelpOtherToggle(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ROOM_SUPPORT_HELP_OTHER_TOGGLE)

    def clickRoomSupportHelpOtherToggle(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getRoomSupportHelpOtherToggle())
        self.driver.implicitly_wait(10)
        self.getRoomSupportHelpOtherToggle().click()
