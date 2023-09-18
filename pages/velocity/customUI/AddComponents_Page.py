import time

from selenium.webdriver.common.by import By


class AddComponentsPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    MEDIA_EXPAND = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div[1]/div[2]/div[2]/div/div/div/div[2]/span/div/div/button"
    ICON_BUTTONS_EXPAND = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div/div[1]/span/div/div/button"
    POPULAR_EXPAND = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/span/div/div/button"
    AUTO_RENEW_BUTTON = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/div/button[1]"

    def getMediaExpand(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.MEDIA_EXPAND)

    def clickMediaExpand(self):
        self.getMediaExpand().click()

    def getIconButtonExpand(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ICON_BUTTONS_EXPAND)

    def clickIconButtonExpand(self):
        self.getIconButtonExpand().click()

    def getPopularExpand(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.POPULAR_EXPAND)

    def clickPopularExpand(self):
        self.getPopularExpand().click()

    def getAutoRenewButton(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.AUTO_RENEW_BUTTON)

    def clickAutoRenewButton(self):
        self.getAutoRenewButton().click()

