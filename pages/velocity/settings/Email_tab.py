import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class EmailTab:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    SAVE_SETTINGS_BUTTON = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/span[1]/div/div[3]/div[2]/div/div[1]/div/div/div/div[8]/button"
    EMAIL_HELP = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/span[1]/div/div[1]/button[6]/div/div/span/a"

    # Get the location of Home
    def getSaveSettings(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SAVE_SETTINGS_BUTTON)

    # Visibility of added technology
    def visibilityOfEmailTab(self):
        time.sleep(1)
        if self.getSaveSettings().is_displayed():
            return True
        else:
            return False

    # Get Login Button
    def getEmailHelp(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.EMAIL_HELP)

    # Click on the Login button
    def clickEmailHelp(self):
        self.getEmailHelp().click()

    # validate Login help is redirecting to YouTube
    def validateEmailHelp(self):

        # Store the ID of the original window
        main_window = self.driver.current_window_handle

        # Check we don't have other windows open already
        assert len(self.driver.window_handles) == 1

        # Click on the Login help
        self.clickEmailHelp()

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
