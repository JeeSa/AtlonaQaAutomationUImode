import time

import pytest

from pages.velocity.Home_Page import HomePage
from pages.velocity.menus.UserSettings_Menu import UserSettingMenu
from pages.velocity.userSettings.UserAdd_Page import UserAddPage
from pages.velocity.userSettings.Users_tab import UsersTab
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestAddUser:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.driver, self.wait)
        self.home = HomePage(self.driver, self.wait)
        self.userMenu = UserSettingMenu(self.driver, self.wait)
        self.users = UsersTab(self.driver, self.wait)
        self.userAdd = UserAddPage(self.driver, self.wait)

    def test_AddUser(self):
        # Login to the velocity app
        self.ut.login()
        # Click on the User Dropdown
        self.home.clickDropdown()
        time.sleep(1)
        # Click on the Users Button
        self.userMenu.clickUsers()
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("User List"))
        assert "Atlona Velocity | User List" in self.driver.title

        beforeCount = self.users.totalRowCount()
        # Click on the User Dropdown
        self.users.clickAddUserButton()
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("User Add"))
        assert "Atlona Velocity | User Add" in self.driver.title

        # Create a new user
        self.userAdd.createNewUser("shamin.jeesa@atlona.com", "Sharmin", "Jeesa", "1234")
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("User List"))
        assert "Atlona Velocity | User List" in self.driver.title
        afterCount =self.users.totalRowCount()
        assert beforeCount < afterCount




