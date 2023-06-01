import time

import pytest

from pages.velocity.Home_Page import HomePage
from pages.velocity.menus.UserSettings_Menu import UserSettingMenu
from pages.velocity.userSettings.ModifyAccount_tab import ModifyAccountTab
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestModifyUserProfile:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.driver, self.wait)
        self.home = HomePage(self.driver, self.wait)
        self.userMenu = UserSettingMenu(self.driver, self.wait)
        self.modifyAcc = ModifyAccountTab(self.driver, self.wait)

    def test_ModifyUserAccount(self):
        # Login to the velocity app
        self.ut.login()
        # Click on the User Dropdown
        self.home.clickDropdown()
        time.sleep(1)
        # Click on the Logout Button
        self.userMenu.clickModifyAccount()
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Modify Account"))
        assert "Atlona Velocity | Modify Account" in self.driver.title

        # Click on the User Dropdown
        self.modifyAcc.clearAccName()
        time.sleep(1)
        self.modifyAcc.enterAccName("Atlona_E")
        time.sleep(1)
        self.modifyAcc.clickSaveChanges()
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Dashboard"))
        assert "Atlona Velocity | Dashboard" in self.driver.title

