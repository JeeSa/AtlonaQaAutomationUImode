import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class AllMacrosPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    SEARCH_FIELD = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div[1]/div[1]/div[2]/div/input"
    SEARCH_BUTTON = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div[1]/div[1]/div[2]/button[1]"
    TABLE_BODY = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div[2]/table/tbody/tr"
    STRINGED_ROWS = "//td[contains(text(),'RoomOn')]"
    CLEAR_SEARCH = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div[1]/div[1]/div[2]/button[2]"
    CLOSE_BUTTON = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div[1]/div[2]/div/button"


    # Get Username field
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

    # Get Password field
    def getSearchButton(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SEARCH_BUTTON)

    # Provide Password
    def clickSearchButton(self):
        self.getSearchButton().click()

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

    def getCloseButton(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.CLOSE_BUTTON)

    # Provide Password
    def clickCloseButton(self):
        self.getCloseButton().click()


