import time

import pytest
from pages.velocity.Home_Page import HomePage
from selenium.webdriver.support import expected_conditions as EC

from pages.velocity.menus.UserSettings_Menu import UserSettingMenu
from utilities.utils import Utils


@pytest.mark.usefixtures("setup")
class TestLogout:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.driver, self.wait)
        self.home = HomePage(self.driver, self.wait)
        self.userMenu = UserSettingMenu(self.driver, self.wait)

    def test_logout(self):
        # Login to the app
        self.ut.login()
        # Click on the User Dropdown
        self.home.clickDropdown()
        time.sleep(1)
        # Click on the Logout Button
        self.userMenu.clickLogout()

        # wait until the logout is successful
        self.wait.until(EC.title_contains("Login To The System"))
        assert "Atlona Velocity | Login To The System" in self.driver.title
