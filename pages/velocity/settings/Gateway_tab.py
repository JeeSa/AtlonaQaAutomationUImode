import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class GatewayTab:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    CHECK_FOR_UPDATE_BUTTON = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/span[1]/div/div[3]/div/div[1]/div[1]/div/div/div/div/div/span/div/button"
    GATEWAY_HELP = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div/span[1]/div/div[1]/button[1]/div/div/span/a"

    # Get the location of Home
    def getCheckForUpdate(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.CHECK_FOR_UPDATE_BUTTON)

    # Visibility of added technology
    def visibilityOfGatewayTab(self):
        time.sleep(1)
        if self.getCheckForUpdate().is_displayed():
            return True
        else:
            return False

    # Get Login Button
    def getGatewayHelp(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.GATEWAY_HELP)

    # Click on the Login button
    def clickGatewayHelp(self):
        self.getGatewayHelp().click()

    # validate Login help is redirecting to YouTube
    def validateGatewayHelp(self):

        # Store the ID of the original window
        main_window = self.driver.current_window_handle

        # Check we don't have other windows open already
        assert len(self.driver.window_handles) == 1

        # Click on the Login help
        self.clickGatewayHelp()

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
