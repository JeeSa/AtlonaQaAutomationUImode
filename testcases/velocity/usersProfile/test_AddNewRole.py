import time

import pytest

from pages.velocity.Home_Page import HomePage
from pages.velocity.menus.UserSettings_Menu import UserSettingMenu
from pages.velocity.userSettings.RoleAdd_Page import RoleAddPage
from pages.velocity.userSettings.Roles_tab import RolesTab
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestAddNewRole:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.driver, self.wait)
        self.home = HomePage(self.driver, self.wait)
        self.userMenu = UserSettingMenu(self.driver, self.wait)
        self.roles = RolesTab(self.driver, self.wait)
        self.addRoles = RoleAddPage(self.driver, self.wait)

    def test_AddNewRole_1(self):
        # Add role using the orange plus icon

        self.ut.login()
        # Click on the User Dropdown
        self.home.clickDropdown()
        time.sleep(1)
        # Click on the Logout Button
        self.userMenu.clickUsers()
        # wait until the logout is successful
        self.wait.until(EC.title_contains("User List"))
        assert "Atlona Velocity | User List" in self.driver.title

        # Click on the User Dropdown
        self.roles.clickRolesTab()
        # wait until the logout is successful
        self.wait.until(EC.title_contains("Role List"))
        assert "Atlona Velocity | Role List" in self.driver.title

        before_count = self.roles.roleCount()
        # Click on the Logout Button
        self.roles.clickOrangeAddNewRole()
        # wait until the logout is successful
        self.wait.until(EC.title_contains("Role Add"))
        assert "Atlona Velocity | Role Add" in self.driver.title

        self.addRoles.enterName("Test_Role_001")
        self.addRoles.clickCreateRole()
        # wait until the logout is successful
        self.wait.until(EC.title_contains("Role List"))
        assert "Atlona Velocity | Role List" in self.driver.title
        after_count = self.roles.roleCount()
        assert after_count > before_count

    def test_AddNewRole_2(self):
        # Add role using the grey plus icon

        # wait until the logout is successful
        self.wait.until(EC.title_contains("Role List"))
        assert "Atlona Velocity | Role List" in self.driver.title

        before_count = self.roles.roleCount()
        # Click on the Logout Button
        self.roles.clickGreyAddNewRole()
        # wait until the logout is successful
        self.wait.until(EC.title_contains("Role Add"))
        assert "Atlona Velocity | Role Add" in self.driver.title

        self.addRoles.enterName("Test_Role_002")
        self.addRoles.clickCreateRole()
        # wait until the logout is successful
        self.wait.until(EC.title_contains("Role List"))
        assert "Atlona Velocity | Role List" in self.driver.title
        after_count = self.roles.roleCount()
        assert after_count > before_count




