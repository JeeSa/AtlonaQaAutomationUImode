import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class RolesTab:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    ROLES_TAB = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[1]/div/div[1]/button[4]"
    ORANGE_ADD_NEW_ROLE = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[2]/div[1]/button"
    ROLES_HELP = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[1]/div/div[1]/button[4]/div/div/span/a"
    GREY_ADD_NEW_ROLE = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div/div/div[1]/table/thead/tr[1]/th[2]/div/span/button"
    COPY_ROLE = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div/div/div[2]/table/tbody/tr[1]/td[6]/span/div/span[2]/span[2]/div/button"
    ROLE_TABLE = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div/div/div[2]/table/tbody/tr"
    ROLE_EDIT = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div/div/div[2]/table/tbody/tr[1]/td[6]/span/div/span[1]/span[2]/div/button"
    DELETE_ROLE = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div/div/div[2]/table/tbody/tr[1]/td[6]/span/div/span[4]/span[2]/div/button"
    ROLE_NAME = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div/div/div[2]/table/tbody/tr[1]/td[1]/span"

    # Get Login Button
    def getRolesTab(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ROLES_TAB)

    # Click on the Login button
    def clickRolesTab(self):
        self.getRolesTab().click()

    def getOrangeAddNewRole(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ORANGE_ADD_NEW_ROLE)

    # Visibility of added technology
    def visibilityOfRolesTab(self):
        time.sleep(1)
        if self.getOrangeAddNewRole().is_displayed():
            return True
        else:
            return False

    def clickOrangeAddNewRole(self):
        self.getOrangeAddNewRole().click()

    # Get Login Button
    def getRolesHelp(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ROLES_HELP)

    # Click on the Login button
    def clickRolesHelp(self):
        self.getRolesHelp().click()

    # validate Login help is redirecting to YouTube
    def validateRolesHelp(self):

        # Store the ID of the original window
        main_window = self.driver.current_window_handle

        # Check we don't have other windows open already
        assert len(self.driver.window_handles) == 1

        # Click on the Login help
        self.clickRolesHelp()

        # Wait for the new window or tab
        self.wait.until(EC.number_of_windows_to_be(2))

        all_windows = self.driver.window_handles
        for new_window in all_windows:
            if new_window != main_window:
                self.driver.switch_to.window(new_window)

                # wait until the destination page is loaded successfully
                self.wait.until(EC.url_contains("youtube.com"))
                time.sleep(1)

                self.driver.close()
                break

        self.driver.switch_to.window(main_window)

        # Check we don't have other windows open anymore
        assert len(self.driver.window_handles) == 1

    def getGreyAddNewRole(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.GREY_ADD_NEW_ROLE)

    def clickGreyAddNewRole(self):
        self.getGreyAddNewRole().click()

    def getCopyRole(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.COPY_ROLE)

    def clickCopyRole(self):
        self.getCopyRole().click()

    def roleCount(self):
        rows = self.driver.find_elements(By.XPATH, self.ROLE_TABLE)
        count = len(rows)
        return count

    def getEditRole(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ROLE_EDIT)

    def clickEditRole(self):
        self.getEditRole().click()

    def getDeleteRole(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.DELETE_ROLE)

    def clickDeleteRole(self):
        self.getDeleteRole().click()

    def getRoleName(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ROLE_NAME)

    def passRoleName(self):
        roleName = self.getRoleName().text
        return roleName
