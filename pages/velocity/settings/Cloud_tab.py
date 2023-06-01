import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class CloudTab:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    APPLY_BUTTON = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/span[1]/div/div[3]/div[2]/div/div[1]/div/div/div/div/div/div[3]/div/button"
    CLOUD_HELP = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/span[1]/div/div[1]/button[3]/div/div/span/a"
    CLOUD_ACCOUNT_HELP = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/span[1]/div/div[3]/div[2]/div/div[2]/div/div/div/div/div[1]/div/div[1]/div/a"

    # Get the location of Home
    def getApplyButton(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.APPLY_BUTTON)

    # Visibility of added technology
    def visibilityOfCloudTab(self):
        time.sleep(1)
        if self.getApplyButton().is_displayed():
            return True
        else:
            return False

    # Get Login Button
    def getCloudHelp(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.CLOUD_HELP)

    # Click on the Login button
    def clickCloudHelp(self):
        self.getCloudHelp().click()

    # validate Login help is redirecting to YouTube
    def validateCloudHelp(self):

        # Store the ID of the original window
        main_window = self.driver.current_window_handle

        # Check we don't have other windows open already
        assert len(self.driver.window_handles) == 1

        # Click on the Login help
        self.clickCloudHelp()

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

    def getCldAccHelp(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.CLOUD_HELP)

    # Click on the Login button
    def clickCldAccHelp(self):
        self.getCloudHelp().click()

    # validate Login help is redirecting to YouTube
    def validateCldAccHelp(self):

        # Store the ID of the original window
        main_window = self.driver.current_window_handle

        # Check we don't have other windows open already
        assert len(self.driver.window_handles) == 1

        # Click on the Login help
        self.clickCldAccHelp()

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
