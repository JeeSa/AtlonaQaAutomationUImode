import time

import pytest

from pages.velocity.Home_Page import HomePage
from pages.velocity.menus.UserSettings_Menu import UserSettingMenu
from pages.velocity.userSettings.Roles_tab import RolesTab
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestCopyRole:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.driver, self.wait)
        self.home = HomePage(self.driver, self.wait)
        self.userMenu = UserSettingMenu(self.driver, self.wait)
        self.roles = RolesTab(self.driver, self.wait)


    def test_CopyRole(self):

        self.ut.login()
        # Click on the User Dropdown
        self.home.clickDropdown()
        time.sleep(1)
        # Click on the users option
        self.userMenu.clickUsers()
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("User List"))
        assert "Atlona Velocity | User List" in self.driver.title

        # Click on the User Roles tab
        self.roles.clickRolesTab()
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Role List"))
        assert "Atlona Velocity | Role List" in self.driver.title

        before_count = self.roles.roleCount()
        # Click on the copy role Button
        self.roles.clickCopyRole()
        time.sleep(1)
        self.wait.until(EC.title_contains("Role List"))
        assert "Atlona Velocity | Role List" in self.driver.title
        after_count = self.roles.roleCount()
        assert after_count > before_count

