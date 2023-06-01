import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ToolsTab:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    FACTORY_RESET_BUTTON = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/span[1]/div/div[3]/div[2]/div/div[1]/div/div/div/span[1]/span/div[2]/button"
    TOOLS_HELP = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/span[1]/div/div[1]/button[5]/div/div/span/a"

    # Get the location of Home
    def getFactoryReset(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.FACTORY_RESET_BUTTON)

    # Visibility of added technology
    def visibilityOfToolsTab(self):
        time.sleep(1)
        if self.getFactoryReset().is_displayed():
            return True
        else:
            return False

    # Get Login Button
    def getToolsHelp(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.TOOLS_HELP)

    # Click on the Login button
    def clickToolsHelp(self):
        self.getToolsHelp().click()

    # validate Login help is redirecting to YouTube
    def validateToolsHelp(self):

        # Store the ID of the original window
        main_window = self.driver.current_window_handle

        # Check we don't have other windows open already
        assert len(self.driver.window_handles) == 1

        # Click on the Login help
        self.clickToolsHelp()

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
