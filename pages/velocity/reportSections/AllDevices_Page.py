import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class AllDevicesPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    SEARCH_FIELD = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div[1]/div[1]/div[2]/div/input"
    SEARCH_BUTTON = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div[1]/div[1]/div[2]/button[1]"
    SEARCH_CONTENT = "Atlona"
    TABLE_BODY = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div[2]/table/tbody/tr"
    STRINGED_ROWS = "//td[contains(text(),'Atlona')]"
    CLEAR_SEARCH = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div[1]/div[1]/div[2]/button[2]"
    CLOSE_BUTTON = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div[1]/div[2]/div/button"
    EDIT_BUTTON = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div[2]/table/tbody/tr[1]/td[9]"
    IP_INPUT = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div[2]/table/tbody/tr[1]/td[2]/input"
    SAVE_BUTTON = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div[2]/table/tbody/tr[1]/td[10]/span/div/button"
    IP_ADDRESS = "//td[contains(text(),'192.110.173.90')]"
    ROOM_NAME = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div[2]/table/tbody/tr[1]/td[8]/span/a"

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

    def getEditButton(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.EDIT_BUTTON)

    # Provide Password
    def clickEditButton(self):
        self.getEditButton().click()

    def getIpInput(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.IP_INPUT)

    # Provide Username
    def enterIp(self, content):
        self.getIpInput().send_keys(content)

    # Clear Username Field
    def clearIp(self):
        self.getIpInput().send_keys(Keys.CONTROL + "a")
        self.getIpInput().send_keys(Keys.DELETE)

    def getSave(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SAVE_BUTTON)

    # Provide Password
    def clickSave(self):
        self.getSave().click()

    def getIpAddress(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.IP_ADDRESS)

    def passIpAddress(self):
        ipAdd = self.getIpAddress().text
        return ipAdd

    def getRoomName(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ROOM_NAME)

    # Provide Password
    def clickRoomName(self):
        self.getRoomName().click()

