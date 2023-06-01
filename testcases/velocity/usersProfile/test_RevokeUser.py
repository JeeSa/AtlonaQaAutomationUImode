import time

import pytest

from pages.velocity.Home_Page import HomePage
from pages.velocity.menus.UserSettings_Menu import UserSettingMenu
from pages.velocity.popups.Confirm_popup import ConfirmPopup
from pages.velocity.userSettings.Users_tab import UsersTab
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestRevokeUser:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.driver, self.wait)
        self.home = HomePage(self.driver, self.wait)
        self.userMenu = UserSettingMenu(self.driver, self.wait)
        self.users = UsersTab(self.driver, self.wait)
        self.confirm = ConfirmPopup(self.driver, self.wait)

    def test_RevokeUser(self):

        self.ut.login()
        # Click on the User Dropdown
        self.home.clickDropdown()
        time.sleep(1)
        # Click on the Users option
        self.userMenu.clickUsers()
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("User List"))
        assert "Atlona Velocity | User List" in self.driver.title

        beforeCount = self.users.totalRowCount()
        # Click on the User Dropdown
        self.users.clickRevokeUser()
        time.sleep(1)
        # Verify if the confirmation popup is visible
        assert self.confirm.visibilityOfConfirmPopup() is True
        self.confirm.clickSubmit()
        time.sleep(1)
        assert self.users.visibilityOfSuccessPopup() is True
        afterCount = self.users.totalRowCount()
        assert beforeCount > afterCount



