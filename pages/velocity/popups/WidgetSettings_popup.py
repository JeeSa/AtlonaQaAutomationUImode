import time

from selenium.webdriver.common.by import By


class WidgetSettingPopup:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    CLOSE_BUTTON = "/html/body/div[4]/div/div[1]/div/div/div[2]/div[2]/button"

    # Get the location of Home
    def getClose(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.CLOSE_BUTTON)

    # Click on cancel
    def clickClose(self):
        time.sleep(1)
        self.getClose().click()

    # Visibility of added technology
    def visibilityOfWidgetSettingPopup(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getClose())
        time.sleep(1)
        if self.getClose().is_displayed():
            return True
        else:
            return False