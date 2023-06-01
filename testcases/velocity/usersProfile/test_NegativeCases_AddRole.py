import time

import pytest

from pages.velocity.Home_Page import HomePage
from pages.velocity.menus.UserSettings_Menu import UserSettingMenu
from pages.velocity.userSettings.RoleAdd_Page import RoleAddPage
from pages.velocity.userSettings.Roles_tab import RolesTab
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestNegativeCasesAddRole:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.driver, self.wait)
        self.home = HomePage(self.driver, self.wait)
        self.userMenu = UserSettingMenu(self.driver, self.wait)
        self.roles = RolesTab(self.driver, self.wait)
        self.addRoles = RoleAddPage(self.driver, self.wait)

    def test_NegativeCases_AddRole(self):
        # Add role using the orange plus icon without any role details

        self.ut.login()
        # Click on the User Dropdown
        self.home.clickDropdown()
        time.sleep(1)
        # Click on the Users Button
        self.userMenu.clickUsers()
        # wait until the logout is successful
        self.wait.until(EC.title_contains("User List"))
        assert "Atlona Velocity | User List" in self.driver.title

        # Click on the User Dropdown
        self.roles.clickRolesTab()
        # wait until the logout is successful
        self.wait.until(EC.title_contains("Role List"))
        assert "Atlona Velocity | Role List" in self.driver.title
        self.roles.clickOrangeAddNewRole()
        # wait until the logout is successful
        self.wait.until(EC.title_contains("Role Add"))
        assert "Atlona Velocity | Role Add" in self.driver.title

        self.addRoles.clickCreateRole()
        expected_error = "This field is required"
        actual_error = self.addRoles.getErrorContent()
        assert expected_error == actual_error


