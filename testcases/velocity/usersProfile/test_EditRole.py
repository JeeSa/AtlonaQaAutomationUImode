import time

import pytest

from pages.velocity.Home_Page import HomePage
from pages.velocity.menus.UserSettings_Menu import UserSettingMenu
from pages.velocity.userSettings.RoleModify_Page import RoleModifyPage
from pages.velocity.userSettings.Roles_tab import RolesTab
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestEditRole:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.driver, self.wait)
        self.home = HomePage(self.driver, self.wait)
        self.userMenu = UserSettingMenu(self.driver, self.wait)
        self.roles = RolesTab(self.driver, self.wait)
        self.modifyRoles = RoleModifyPage(self.driver, self.wait)

    def test_EditRole(self):

        self.ut.login()
        # Click on the User Dropdown
        self.home.clickDropdown()
        time.sleep(1)
        # Click on the Logout Button
        self.userMenu.clickUsers()
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("User List"))
        assert "Atlona Velocity | User List" in self.driver.title

        # Click on the User Dropdown
        self.roles.clickRolesTab()
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Role List"))
        assert "Atlona Velocity | Role List" in self.driver.title
        # Click on the Logout Button
        self.roles.clickEditRole()
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Role Modify"))
        assert "Atlona Velocity | Role Modify" in self.driver.title

        nameParameter = "Edited Role Name"
        self.modifyRoles.clearName()
        self.modifyRoles.enterName(nameParameter)
        self.modifyRoles.clickSaveChanges()
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Role List"))
        assert "Atlona Velocity | Role List" in self.driver.title
        newName = self.roles.passRoleName()
        assert newName == nameParameter
