import time

from selenium.webdriver.common.by import By


class DeviceAddHamburger:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    ADD_SITE = "/html/body/div[5]/div/div/div/div/div/div[1]/span"
    ADD_BUILDING = "addBuildingToSiteButton"
    ADD_ROOM = "addRoomToSiteButton"

    # Get the location of Home
    def getAddSite(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ADD_SITE)

    # Click on cancel
    def clickAddSite(self):
        time.sleep(1)
        self.getAddSite().click()

    # Get the location of Submit
    def getAddBuilding(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.ADD_BUILDING)

    # Click on cancel
    def clickAddBuilding(self):
        time.sleep(1)
        self.getAddBuilding().click()

    # Visibility of added technology
    def visibilityOfAddHamburgerMenu(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getAddSite())
        time.sleep(1)
        if self.getAddSite().is_displayed():
            return True
        else:
            return False

    def getAddRoom(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.ADD_ROOM)

    # Click on cancel
    def clickAddRoom(self):
        time.sleep(1)
        self.getAddRoom().click()
