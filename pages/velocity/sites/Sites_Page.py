import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class SitesPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    VIEW_BUTTON = "//*[@id=\"page\"]/span/div/span/span/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/span/button"
    ADD_BUILDING_BUTTON = "//*[@id=\"page\"]/span/div/span/span/div[1]/div[2]/div/div/div/div/div/div/div/div[3]/span[3]/button"
    DELETE_BUTTON = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div/div/div/div/div/div/div[3]/span[4]/button"
    EXPORT_BUTTON = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div/div/div/div/div/div/div[3]/span[2]/button"
    EDIT_BUTTON = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div/div/div/div/div/div/div[3]/span[1]/button"
    SITES_HELP = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[1]/div[2]/span/div/span[3]/a"
    SITE_NAME = "/html/body/div[1]/div[3]/main/div[1]/div/span/div/span/span/div[1]/div[2]/div/div/div/div/div/div/div/h4"

    # Get the location of view button
    def getViewButton(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.VIEW_BUTTON)

    # Visibility of View button
    def visibilityOfViewButton(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getViewButton())
        self.driver.implicitly_wait(10)
        if self.getViewButton().is_displayed():
            return True
        else:
            return False

    # Click on the User Dropdown
    def clickView(self):
        self.getViewButton().click()

    # Get the location of view button
    def getAddBuildingButton(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ADD_BUILDING_BUTTON)

    # Visibility of Add building button
    def visibilityOfAddBuildingButton(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getAddBuildingButton())
        self.driver.implicitly_wait(10)
        if self.getAddBuildingButton().is_displayed():
            return True
        else:
            return False

    # Click on the User Dropdown
    def clickAddBuilding(self):
        self.getAddBuildingButton().click()

    # Get the location of view button
    def getDeleteButton(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.DELETE_BUTTON)

    # Visibility of Add building button
    def visibilityOfDeleteButton(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getDeleteButton())
        self.driver.implicitly_wait(10)
        if self.getDeleteButton().is_displayed():
            return True
        else:
            return False

    # Click on the User Dropdown
    def clickDeleteButton(self):
        self.getDeleteButton().click()

    # Get the location of view button
    def getExportButton(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.EXPORT_BUTTON)

    # Visibility of Add building button
    def visibilityOfExportButton(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getExportButton())
        self.driver.implicitly_wait(10)
        if self.getExportButton().is_displayed():
            return True
        else:
            return False

    # Click on the User Dropdown
    def clickExportButton(self):
        self.getExportButton().click()

    # Get the location of view button
    def getEditButton(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.EDIT_BUTTON)

    # Visibility of Add building button
    def visibilityOfEditButton(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getEditButton())
        self.driver.implicitly_wait(10)
        if self.getEditButton().is_displayed():
            return True
        else:
            return False

    # Click on the User Dropdown
    def clickEditButton(self):
        self.getEditButton().click()

    def getSitesHelp(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SITES_HELP)

    # Click on the Login button
    def clickSitesHelp(self):
        self.getSitesHelp().click()

    # validate Login help is redirecting to YouTube
    def validateSitesHelp(self):

        # Store the ID of the original window
        main_window = self.driver.current_window_handle

        # Check we don't have other windows open already
        assert len(self.driver.window_handles) == 1

        # Click on the Login help
        self.clickSitesHelp()

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

    def getSiteName(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SITE_NAME)

    def passSiteName(self):
        siteName = self.getSiteName().text
        return siteName

    def navToBuildingsPage(self):
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Sites"))
        assert "Atlona Velocity | Sites" in self.driver.title

        # Click on the view button
        self.clickView()
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Buildings"))
        assert "Atlona Velocity | Buildings" in self.driver.title

    def navToAddBuildingPageFromSitesPage(self):
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Sites"))
        assert "Atlona Velocity | Sites" in self.driver.title

        # Click on the add building button
        self.clickAddBuilding()
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Building Add"))
        assert "Atlona Velocity | Building Add" in self.driver.title

    def navToSiteModifyPage(self):
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Sites"))
        assert "Atlona Velocity | Sites" in self.driver.title

        # Click on the add building button
        self.clickEditButton()
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Site Modify"))
        assert "Atlona Velocity | Site Modify" in self.driver.title

