import time

from selenium.webdriver.common.by import By


class TechnologyListPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    SEARCH_FIELD = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div/div/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/div[1]/div/input"
    CLEAR_SEARCH_BUTTON = "//*[@id=\"modifyDevicesPage\"]/div/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/div[1]/button[2]"
    SEARCH_BUTTON = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div/div/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/div[1]/button[1]"
    ADD_BUTTON = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div/div/div[1]/div/div[2]/div[2]/div[2]/div[3]/div/div[2]/div/span/div/div/div/span/span/div/button[3]"
    CLOSE_LIST_BUTTON = "//*[@id=\"modifyDevicesPage\"]/div/div[1]/div/div[2]/div[2]/div[2]/div[1]/div[1]/span/button"

    # Get the location of view button
    def getSearchField(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SEARCH_FIELD)

    # Provide search keyword
    def enterSearchKeyword(self, search_kw):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getSearchField())
        self.driver.implicitly_wait(10)
        self.getSearchField().send_keys(search_kw)

    # Get the location of clear search button
    def getClearSearchButton(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.CLEAR_SEARCH_BUTTON)

    # Click on the clear search button
    def clickClearSearch(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getClearSearchButton())
        self.driver.implicitly_wait(10)
        self.getClearSearchButton().click()

    # Get the location of search button
    def getSearchButton(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SEARCH_BUTTON)

    # Click on the search button
    def clickSearch(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getSearchButton())
        self.driver.implicitly_wait(10)
        self.getSearchButton().click()

    # Get the location of add button
    def getAddButton(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ADD_BUTTON)

    # Click on the add button
    def clickAdd(self):
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", self.getAddButton())
        self.driver.implicitly_wait(10)
        self.getAddButton().click()

    # Get the location of close button
    def getCloseListButton(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.CLOSE_LIST_BUTTON)

    # Click on the close button
    def clickCloseList(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getCloseListButton())
        self.driver.implicitly_wait(10)
        self.getCloseListButton().click()

    # Add Device
    def addDevice(self, s_kw):
        # Provide search keyword
        self.enterSearchKeyword(s_kw)
        time.sleep(1)
        # Click on the search button
        self.clickSearch()
        # Click on the add button
        self.clickAdd()

