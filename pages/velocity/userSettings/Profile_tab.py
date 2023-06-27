import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ProfileTab:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    EMAIL_FIELD = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div[1]/div/div/div/div[1]/input"
    PROFILE_HELP = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[1]/div/div[1]/button[3]/div/div/span/a"
    FIRST_NAME = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div[1]/div/div/div/div[2]/input"
    SAVE_CHANGES_1 = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div[1]/div/div/div/div[6]/button"
    SAVE_SUCCESS = "/html/body/div[1]/footer/div/div/div[1]/div/div"
    FIRST_NAME_DIV = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div[1]/div/div/div/div[2]/div[1]"

    # Get the location of Home
    def getEmail(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.EMAIL_FIELD)

    # Visibility of added technology
    def visibilityOfProfileTab(self):
        time.sleep(1)
        if self.getEmail().is_displayed():
            return True
        else:
            return False

    # Get Login Button
    def getProfileHelp(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.PROFILE_HELP)

    # Click on the Login button
    def clickProfileHelp(self):
        self.getProfileHelp().click()

    # validate Login help is redirecting to YouTube
    def validateProfileHelp(self):

        # Store the ID of the original window
        main_window = self.driver.current_window_handle

        # Check we don't have other windows open already
        assert len(self.driver.window_handles) == 1

        # Click on the Login help
        self.clickProfileHelp()

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

    def getFirstNameDiv(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getFirstName())
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.FIRST_NAME_DIV)

    def passFirstName(self):
        firstName = self.getFirstNameDiv().text
        return firstName

    # Get Login Button
    def getSaveChanges1(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SAVE_CHANGES_1)

    # Click on the Login button
    def clickSaveChanges1(self):
        self.getSaveChanges1().click()

    # Get the location of Home
    def getSaveSucces(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SAVE_SUCCESS)

    # Visibility of added technology
    def visibilityOfSaveSucces(self):
        time.sleep(1)
        if self.getSaveSucces().is_displayed():
            return True
        else:
            return False
