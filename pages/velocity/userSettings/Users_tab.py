import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class UsersTab:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    SEARCH_FIELD = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div/div/div[1]/table/thead/tr[1]/th[2]/div/span/div/input"
    USERS_HELP = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[1]/div/div[1]/button[2]/div/div/span/a"
    ADD_USER_BUTTON = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[2]/div[1]/button"
    REVOKE_USER_BUTTON = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div/div/div[2]/table/tbody/tr[1]/td[5]/span/div/span[2]/span[2]/div/button"
    SUCCESS_POPUP ="/html/body/div[1]/footer/div/div/div[1]/div/div"
    TABLE_BODY = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div/div/div[2]/table/tbody/tr"

    # Get the location of Home
    def getSearch(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SEARCH_FIELD)

    # Visibility of added technology
    def visibilityOfUsersTab(self):
        time.sleep(1)
        if self.getSearch().is_displayed():
            return True
        else:
            return False

    # Get Login Button
    def getUsersHelp(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.USERS_HELP)

    # Click on the Login button
    def clickUsersHelp(self):
        self.getUsersHelp().click()

    # validate Login help is redirecting to YouTube
    def validateUsersHelp(self):

        # Store the ID of the original window
        main_window = self.driver.current_window_handle

        # Check we don't have other windows open already
        assert len(self.driver.window_handles) == 1

        # Click on the Login help
        self.clickUsersHelp()

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

    # Get Login Button
    def getAddUserButton(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ADD_USER_BUTTON)

    # Click on the Login button
    def clickAddUserButton(self):
        self.getAddUserButton().click()

    # Get Login Button
    def getRevokeUser(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.REVOKE_USER_BUTTON)

    # Click on the Login button
    def clickRevokeUser(self):
        self.getRevokeUser().click()

    # Get the location of Home
    def getSuccessPopup(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SUCCESS_POPUP)

    # Visibility of added technology
    def visibilityOfSuccessPopup(self):
        time.sleep(1)
        if self.getSuccessPopup().is_displayed():
            return True
        else:
            return False

    def getRows(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_elements(By.XPATH, self.TABLE_BODY)

    def totalRowCount(self):
        rows = self.getRows()
        count = len(rows)
        return count
