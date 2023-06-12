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
    ADD = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[2]/div[1]/button"
    EDIT = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div/div/div[2]/table/tbody/tr/td[5]/span/div/span[1]/span[2]/div/button"
    DELETE = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div/div/div[2]/table/tbody/tr/td[5]/span/div/span[2]/span[2]/div/button"
    CALENDAR_INTEGRATION_1_NAME = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div/div/div[2]/table/tbody/tr/td[2]/span"
    TABLE_BODY = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div/div/div[2]/table/tbody/tr"
    STRINGED_ROWS = "//td[contains(text(),'Test')]"
    SEARCH_FIELD = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div[1]/div/div/div[1]/table/thead/tr[1]/th[3]/div/span/div/input"

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

    # Get Button
    def getAdd(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ADD)

    # Click on the button
    def clickAdd(self):
        self.getAdd().click()

    # Get Button
    def getEdit(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.EDIT)

    # Click on the button
    def clickEdit(self):
        self.getEdit().click()

    # Get Button
    def getDelete(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.DELETE)

    # Click on the button
    def clickDelete(self):
        self.getDelete().click()

    def getCaIntName(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.CALENDAR_INTEGRATION_1_NAME)

    def passCaIntName(self):
        caIntName = self.getCaIntName().text
        return caIntName

    def getRows(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_elements(By.XPATH, self.TABLE_BODY)

    def totalRowCount(self):
        rows = self.getRows()
        count = len(rows)
        return count

    def getRowsString(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_elements(By.XPATH, self.STRINGED_ROWS)

    def rowCountWithString(self):
        rows = self.getRowsString()
        count = len(rows)
        return count

    def getSearchField(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SEARCH_FIELD)

    # Provide Username
    def enterSearchContent(self, content):
        self.getSearchField().send_keys(content)

    # Clear Username Field
    def clearSearchContent(self):
        self.getSearchField().send_keys(Keys.CONTROL + "a")
        self.getSearchField().send_keys(Keys.DELETE)
