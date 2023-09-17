import time

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class CUIPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    ADD_PAGE_BUTTON = "//span[contains(text(),'Add')]"
    PAGE_2_NAME = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div/span"
    PAGE_3_NAME ="/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div[2]/div[2]/div[2]/div/div[3]/div/span"
    PAGE_2_OPTIONS = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div/span/span"
    PAGE_3_OPTIONS = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div[2]/div[2]/div[2]/div/div[3]/div/span/span"
    LAUNCH_CONTROL = "//span[contains(text(),'touch_app')]"
    ROOM_TECHNOLOGY = "//span[contains(text(),'settings_input_hdmi')]"
    VARIABLES = "//span[contains(text(),'code')]"
    ROOM_OPTION = "//span[contains(text(),'tune')]"
    EXPAND_CLOSE = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div[1]/div[1]/span"
    HEADER_TAB = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div[3]/div[2]/div[2]/div/div/div/div[1]/button[2]"
    ROOM_TITLE = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div[2]/div[2]/div[1]/div/div/div[2]"
    HEADER_ICONS = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div[2]/div[2]/div[1]/div/div/div[1]/span"
    ROOM_ON = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div[2]/div[2]/div[1]/div/div/div[1]/span/span/div/div[3]"
    ROOM_OFF = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div[2]/div[2]/div[1]/div/div/div[1]/span/span/div/div[4]"
    NAVIGATE = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div[2]/div[2]/div[1]/div/div/div[1]/span/span/div/div[2]"
    HOME = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div[2]/div[2]/div[1]/div/div/div[1]/span/span/div/div[1]"
    MACROS = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div[2]/div[2]/div[1]/div/div/div[1]/span/span/div/div[5]"
    HELP = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div[2]/div[2]/div[1]/div/div/div[1]/span/span/div/div[6]"

    # Get the location of add technology button
    def getAddPageButton(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ADD_PAGE_BUTTON)

    # Click on the add technology button
    def clickAddPageButton(self):
        self.getAddPageButton().click()

    def getPage2Name(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.PAGE_2_NAME)

    def passPage2Name(self):
        page2Name = self.getPage2Name().text
        return page2Name

    def getPage3Name(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.PAGE_3_NAME)

    def passPage3Name(self):
        page3Name = self.getPage3Name().text
        return page3Name

    # Get the location of add technology button
    def getPage2Options(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.PAGE_2_OPTIONS)

    # Click on the add technology button
    def clickPage2Options(self):
        self.getPage2Options().click()

    # Get the location of add technology button
    def getPage3Options(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.PAGE_3_OPTIONS)

    # Click on the add technology button
    def clickPage3Options(self):
        self.getPage3Options().click()

    # Get the location of add technology button
    def getLaunchControl(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.LAUNCH_CONTROL)

    # Click on the add technology button
    def clickLaunchControl(self):
        self.getLaunchControl().click()

    # Get the location of add technology button
    def getRoomTechnology(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ROOM_TECHNOLOGY)

    # Click on the add technology button
    def clickRoomTechnology(self):
        self.getRoomTechnology().click()

    # Get the location of add technology button
    def getVariables(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.VARIABLES)

    # Click on the add technology button
    def clickVariables(self):
        self.getVariables().click()

    # Get the location of add technology button
    def getRoomOption(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ROOM_OPTION)

    # Click on the add technology button
    def clickRoomOption(self):
        self.getRoomOption().click()

    def getExpand(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.EXPAND_CLOSE)

    def clickExpand(self):
        self.getExpand().click()

    def getHeader(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.HEADER_TAB)

    def clickHeader(self):
        self.getHeader().click()

    def getRoomTitle(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ROOM_TITLE)

    # Visibility of added technology
    def visibilityOfRoomtitle(self):
        self.driver.implicitly_wait(10)
        if self.getRoomTitle().is_displayed():
            return True
        else:
            return False

    def getHeaderIcons(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.HEADER_ICONS)

    # Visibility of added technology
    def visibilityOfHeaderIcons(self):
        self.driver.implicitly_wait(10)
        if self.getHeaderIcons().is_displayed():
            return True
        else:
            return False

    def getRoomOn(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ROOM_ON)

    # Visibility of added technology
    def visibilityOfRoomOn(self):
        self.driver.implicitly_wait(10)
        if self.getRoomOn().is_displayed():
            return True
        else:
            return False

    def getRoomOff(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ROOM_OFF)

    # Visibility of added technology
    def visibilityOfRoomOff(self):
        self.driver.implicitly_wait(10)
        if self.getRoomOff().is_displayed():
            return True
        else:
            return False

    def getNavigate(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.NAVIGATE)

    # Visibility of added technology
    def visibilityOfNavigate(self):
        self.driver.implicitly_wait(10)
        if self.getNavigate().is_displayed():
            return True
        else:
            return False

    def getHome(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.HOME)

    # Visibility of added technology
    def visibilityOfHome(self):
        self.driver.implicitly_wait(10)
        if self.getHome().is_displayed():
            return True
        else:
            return False

    def getMacros(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.MACROS)

    # Visibility of added technology
    def visibilityOfMacros(self):
        self.driver.implicitly_wait(10)
        if self.getMacros().is_displayed():
            return True
        else:
            return False

    def getHelp(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.HELP)

    # Visibility of added technology
    def visibilityOfHelp(self):
        self.driver.implicitly_wait(10)
        if self.getHelp().is_displayed():
            return True
        else:
            return False
