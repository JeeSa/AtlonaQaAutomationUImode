import time

from selenium.webdriver.common.by import By


class RoomSupportTab:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    EMAIL_FIELD = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/span[1]/div/div[3]/div[2]/div/div/div/div/div/span[2]/div[1]/div[2]/span/span/div/input"

    # Get the location of Home
    def getEmailField(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.EMAIL_FIELD)

    # Visibility of added technology
    def visibilityOfRoomSupportTab(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getEmailField())
        time.sleep(1)
        if self.getEmailField().is_displayed():
            return True
        else:
            return False
