from selenium.webdriver.common.by import By


class UserSettingMenu:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    PROFILE = "userProfileButton"
    USERS = "usersListButton"
    MODIFY_ACCOUNT = "accountListButton"
    LOGOUT = "logoutButton"
    ROLES_TAB = "RoleList"

    # Get the location of logout button
    def getProfile(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.PROFILE)

    # Click on the Logout Button
    def clickProfile(self):
        self.getProfile().click()

    # Get the location of logout button
    def getUsers(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.USERS)

    # Click on the Logout Button
    def clickUsers(self):
        self.getUsers().click()

    # Get the location of logout button
    def getModifyAccount(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.MODIFY_ACCOUNT)

    # Click on the Logout Button
    def clickModifyAccount(self):
        self.getModifyAccount().click()

    # Get the location of logout button
    def getLogout(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.LOGOUT)

    # Click on the Logout Button
    def clickLogout(self):
        self.getLogout().click()

    # Get the location of logout button
    def getRolesTab(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.CLASS_NAME, self.ROLES_TAB)

    # Click on the Logout Button
    def clickRolesTab(self):
        self.getRolesTab().click()
