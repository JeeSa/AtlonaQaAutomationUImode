import time

import pytest

from pages.velocity.Home_Page import HomePage
from pages.velocity.menus.UserSettings_Menu import UserSettingMenu
from pages.velocity.userSettings.Profile_tab import ProfileTab
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestModifyUserProfile:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.driver, self.wait)
        self.home = HomePage(self.driver, self.wait)
        self.userMenu = UserSettingMenu(self.driver, self.wait)
        self.profile = ProfileTab(self.driver, self.wait)

    def test_ModifyUserProfile(self):

        # Login to the velocity app
        self.ut.login()
        # Click on the User Dropdown
        self.home.clickDropdown()
        time.sleep(1)
        # Click on the Profile option
        self.userMenu.clickProfile()
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("User Profile"))
        assert "Atlona Velocity | User Profile" in self.driver.title

        # Update the User firstname
        expected_ufName = "QA_E"
        self.profile.clearFirstName()
        time.sleep(1)
        self.profile.enterFirstName(expected_ufName)
        time.sleep(1)
        self.profile.clickSaveChanges1()
        assert self.profile.visibilityOfSaveSucces() is True



