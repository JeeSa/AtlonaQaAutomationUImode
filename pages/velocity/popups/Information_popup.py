import time

from selenium.webdriver.common.by import By


class InformationPopup:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    OK = "/html/body/div[5]/div/div[1]/div/div/div[2]/button"
    CONTENT = "/html/body/div[5]/div/div[1]/div/div/div[1]/div/span"

    # Get the location of Home
    def getOk(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.OK)

    # Click on cancel
    def clickOk(self):
        time.sleep(1)
        self.getOk().click()

    # Visibility of added technology
    def visibilityOfInformationPop(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getOk())
        time.sleep(1)
        if self.getOk().is_displayed():
            return True
        else:
            return False

    def getContent(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.CONTENT)

    def passContent(self):
        content = self.getContent().text
        return content
