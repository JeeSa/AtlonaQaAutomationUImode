import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    USERNAME_FIELD = "username"
    PASSWORD_FIELD = "password"
    LOGIN_BUTTON = "loginbutton"
    LOGIN_HELP = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div[2]/div/h1/a"
    SYNC_HELP = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div[2]/div/div/span[1]/span/a"
    FORGOT_PASSWORD_HELP = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/div[2]/div/div/span[2]/span/span/a[2]"

    # Get Username field
    def getUsername(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.USERNAME_FIELD)

    # Provide Username
    def enterUsername(self, user_name):
        self.getUsername().send_keys(user_name)

    # Clear Username Field
    def clearUsername(self):
        self.getUsername().send_keys(Keys.CONTROL + "a")
        self.getUsername().send_keys(Keys.DELETE)

    # Get Password field
    def getPassword(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.PASSWORD_FIELD)

    # Provide Password
    def enterPassword(self, pass_word):
        self.getPassword().send_keys(pass_word)

    # Clear Password Field
    def clearPassword(self):
        self.getPassword().send_keys(Keys.CONTROL + "a")
        self.getPassword().send_keys(Keys.DELETE)

    # Get Login Button
    def getLogin(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.LOGIN_BUTTON)

    # Click on the Login button
    def clickLogin(self):
        self.getLogin().click()

    # Get Login Button
    def getLoginHelp(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.LOGIN_HELP)

    # Click on the Login button
    def clickLoginHelp(self):
        self.getLoginHelp().click()

    # validate Login help is redirecting to YouTube
    def validateLoginHelp(self):

        # Store the ID of the original window
        main_window = self.driver.current_window_handle

        # Check we don't have other windows open already
        assert len(self.driver.window_handles) == 1

        # Click on the Login help
        self.clickLoginHelp()

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
    def getSyncHelp(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SYNC_HELP)

    # Click on the Login button
    def clickSyncHelp(self):
        self.getSyncHelp().click()

    # validate Login help is redirecting to YouTube
    def validateSyncHelp(self):

        # Store the ID of the original window
        main_window = self.driver.current_window_handle

        # Check we don't have other windows open already
        assert len(self.driver.window_handles) == 1

        # Click on the Login help
        self.clickSyncHelp()

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
    def getForogtPassHelp(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.FORGOT_PASSWORD_HELP)

    # Click on the Login button
    def clickForgotPassHelp(self):
        self.getForogtPassHelp().click()

    # validate Login help is redirecting to YouTube
    def validateForgotPassHelp(self):

        # Store the ID of the original window
        main_window = self.driver.current_window_handle

        # Check we don't have other windows open already
        assert len(self.driver.window_handles) == 1

        # Click on the Login help
        self.clickForgotPassHelp()

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

    def clearAllData(self):
        # Clear all the previous data
        self.clearUsername()
        self.clearPassword()

    def loginMethod(self, uName, password):
        # Provide Username
        self.enterUsername(uName)
        # Provide Password
        self.enterPassword(password)
        # Login to the app
        self.clickLogin()
