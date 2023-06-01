import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class CalendarIntegrationListPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    CALENDAR_INTEGRATION_LIST_HELP = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[1]/div[2]/span/div/span[3]/a"

    # Get Login Button
    def getClIntLstHelp(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.CALENDAR_INTEGRATION_LIST_HELP)

    # Click on the Login button
    def clickClIntLstHelp(self):
        self.getClIntLstHelp().click()

    # validate Login help is redirecting to YouTube
    def validateClIntLstHelp(self):

        # Store the ID of the original window
        main_window = self.driver.current_window_handle

        # Check we don't have other windows open already
        assert len(self.driver.window_handles) == 1

        # Click on the Login help
        self.clickClIntLstHelp()

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
