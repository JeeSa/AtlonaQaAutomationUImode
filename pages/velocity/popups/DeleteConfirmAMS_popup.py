import time

from selenium.webdriver.common.by import By


class DeleteConfirmAMSPopup:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    CLOSE_R = "/html/body/div[8]/div/div[1]/div/div/div[2]/div[1]/button"
    DELETE_R = "/html/body/div[8]/div/div[1]/div/div/div[2]/div[2]/button"
    DELETE_B = "/html/body/div[6]/div/div[1]/div/div/div[2]/div[2]/button"
    CLOSE_B = "/html/body/div[6]/div/div[1]/div/div/div[2]/div[1]/button"


    # Get the location of Home
    def getCloseR(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.CLOSE_R)

    # Click on cancel
    def clickCloseR(self):
        time.sleep(1)
        self.getCloseR().click()

    # Get the location of Submit
    def getDeleteR(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.DELETE_R)

    # Click on cancel
    def clickDeleteR(self):
        time.sleep(1)
        self.getDeleteR().click()

    # Visibility of added technology
    def visibilityOfRoomConfirmPopup(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getDeleteR())
        time.sleep(1)
        if self.getDeleteR().is_displayed():
            return True
        else:
            return False

    def getCloseB(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.CLOSE_B)

    # Click on cancel
    def clickCloseB(self):
        time.sleep(1)
        self.getCloseB().click()

    # Get the location of Submit
    def getDeleteB(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.DELETE_B)

    # Click on cancel
    def clickDeleteB(self):
        time.sleep(1)
        self.getDeleteB().click()

    # Visibility of added technology
    def visibilityOfBuildingConfirmPopup(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getDeleteB())
        time.sleep(1)
        if self.getDeleteB().is_displayed():
            return True
        else:
            return False
