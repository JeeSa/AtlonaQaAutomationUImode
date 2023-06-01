from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    USER_DROPDOWN = "userProfileSettingsDropdown"
    ADD_SITE_BUTTON = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div/div/div/div[1]/div[1]/div/div/div/div[2]/div/div/div/button"
    CREATED_SITE = "//*[@id=\"widgetUserList\"]/div/div/div[2]/div/span/div/div/div/span"
    NAVIGATION_HAMBURGER = "navigationHamburgerBar3"
    SIDEBAR_MENU = "Atlona-sidebarMenu"
    VELOCITY_LOGO = "/html/body/div[1]/div[1]/div/nav/div[2]/div/div[1]/span/a"
    WIDGET_HAMBURGER = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/button"
    SITES_GATEWAY_INFORMATION = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div/div/div/div[1]/div[2]/div/div[2]/div/div[7]/span/div/div"
    EXPAND_ALL = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div/div/div/div[1]/div[1]/div/div/div/div[1]/div[3]/div/button[2]"
    BUILDING_NAME = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div/div/div/div[1]/div[1]/div/div/div/div[2]/div/div/div[1]/span/div/div/div/span"
    ROOM_NAME = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div/div/div/div[1]/div[1]/div/div/div/div[2]/div/div/div[1]/div/span/div/div/div/div/span/div/div/div"
    TOTAL_ROOMS = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div/div/div/div[1]/div[2]/div/div[2]/div/div[1]/span/div/div/div/div[1]"

    # Get the location of User Dropdown
    def getUserDropdown(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.USER_DROPDOWN)

    # Click on the User Dropdown
    def clickDropdown(self):
        self.getUserDropdown().click()

    # Get the location of Add site button
    def getAddSiteButton(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ADD_SITE_BUTTON)

    # Click on the User Dropdown
    def clickAddSiteButton(self):
        self.getAddSiteButton().click()

    # Get the location of created site
    def getCreatedSite(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.CREATED_SITE)

    # Click on the created site
    def clickSite(self):
        self.getCreatedSite().click()

    def getNavBar(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.NAVIGATION_HAMBURGER)

    # Click on the User Dropdown
    def clickNavBar(self):
        self.getNavBar().click()

    def getSidebarMenu(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.SIDEBAR_MENU)

    # Visibility of add site page
    def visibilityOfSidebarMenu(self):
        self.driver.implicitly_wait(10)
        if self.getSidebarMenu().is_displayed():
            return True
        else:
            return False

    # Get the location of User Dropdown
    def getVelocityLogo(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.VELOCITY_LOGO)

    # Click on the User Dropdown
    def clickVelocityLogo(self):
        self.getVelocityLogo().click()

    # Get the location of User Dropdown
    def getWidgetHamburger(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.WIDGET_HAMBURGER)

    # Click on the User Dropdown
    def clickWidgetHamburger(self):
        self.getWidgetHamburger().click()

    # Get the location of User Dropdown
    def getSites(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SITES_GATEWAY_INFORMATION)

    # Click on the User Dropdown
    def clickSites(self):
        self.getSites().click()

    # Get the location of User Dropdown
    def getExpandAll(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.EXPAND_ALL)

    # Click on the User Dropdown
    def clickExpandAll(self):
        self.getExpandAll().click()

    # Get the location of User Dropdown
    def getBuildingName(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.BUILDING_NAME)

    # Click on the User Dropdown
    def clickBuildingName(self):
        self.getBuildingName().click()

    # Get the location of User Dropdown
    def getRoomName(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ROOM_NAME)

    # Click on the User Dropdown
    def clickRoomName(self):
        self.getRoomName().click()

    # Get the location of User Dropdown
    def getTotalRooms(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.TOTAL_ROOMS)

    # Click on the User Dropdown
    def clickTotalRooms(self):
        self.getTotalRooms().click()
