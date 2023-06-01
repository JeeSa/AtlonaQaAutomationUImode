import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class UserAddPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    EMAIL = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div/div/div/div[1]/input"
    FIRST_NAME = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div/div/div/div[2]/input"
    LAST_NAME = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div/div/div/div[3]/input"
    TEMPORARY_PASSWORD = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div/div/div/div[4]/input"
    ROLE_DROPDOWN = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div/div/div/div[5]/div[2]/div[1]/button"
    ROLE_LIST = "/html/body/div[4]/div/div/div"
    ACCOUNT_ADMINISTRATOR_ROLE ="/html/body/div[4]/div/div/div/div[1]/span/div/div"
    CREATE_USER = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div/div/div/div[7]/button"

    # Get Password field
    def getEmail(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.EMAIL)

    # Provide Password
    def enterEmail(self, email):
        self.getEmail().send_keys(email)

    # Clear Password Field
    def clearEmail(self):
        self.getEmail().send_keys(Keys.CONTROL + "a")
        self.getEmail().send_keys(Keys.DELETE)

    # Get Password field
    def getFirstName(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.FIRST_NAME)

    # Provide Password
    def enterFirstName(self, f_name):
        self.getFirstName().send_keys(f_name)

    # Clear Password Field
    def clearFirstName(self):
        self.getFirstName().send_keys(Keys.CONTROL + "a")
        self.getFirstName().send_keys(Keys.DELETE)

    # Get Password field
    def getLastName(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.LAST_NAME)

    # Provide Password
    def enterLastName(self, l_name):
        self.getLastName().send_keys(l_name)

    # Clear Password Field
    def clearLastName(self):
        self.getLastName().send_keys(Keys.CONTROL + "a")
        self.getLastName().send_keys(Keys.DELETE)

    # Get Password field
    def getTempPass(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.TEMPORARY_PASSWORD)

    # Provide Password
    def enterTempPass(self, temp_pass):
        self.getTempPass().send_keys(temp_pass)

    # Clear Password Field
    def clearTempPass(self):
        self.getTempPass().send_keys(Keys.CONTROL + "a")
        self.getTempPass().send_keys(Keys.DELETE)

    def getRoleDropdown(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ROLE_DROPDOWN)

    # Click on the Logout Button
    def clickRoleDropdown(self):
        self.getRoleDropdown().click()

    def getRoleList(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ROLE_LIST)

    # Visibility of added technology
    def visibilityOfRoleList(self):
        time.sleep(1)
        if self.getRoleList().is_displayed():
            return True
        else:
            return False

    def getAccAdmin(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ACCOUNT_ADMINISTRATOR_ROLE)

    # Click on the Logout Button
    def clickAccAdmin(self):
        self.getAccAdmin().click()

    def getCreateUser(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.CREATE_USER)

    # Click on the Logout Button
    def clickCreateUser(self):
        self.getCreateUser().click()

    def enterAllData(self, email, fname, lname, tpass):
        self.enterEmail(email)
        self.enterFirstName(fname)
        self.enterLastName(lname)
        self.clearTempPass()
        time.sleep(1)
        self.enterTempPass(tpass)

    def selectDropdownValue(self):
        self.clickRoleDropdown()
        assert self.visibilityOfRoleList() is True
        self.clickAccAdmin()

    def createNewUser(self, email, fname, lname, tpass):
        self.enterAllData(email, fname, lname, tpass)
        self.selectDropdownValue()
        self.clickCreateUser()

