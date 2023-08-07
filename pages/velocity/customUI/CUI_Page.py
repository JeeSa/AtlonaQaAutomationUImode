import time

from selenium.webdriver.common.by import By


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
