import time

import pytest

from pages.velocity.Home_Page import HomePage
from pages.velocity.menus.UserSettings_Menu import UserSettingMenu
from pages.velocity.userSettings.UserAdd_Page import UserAddPage
from pages.velocity.userSettings.Users_tab import UsersTab
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestNegativeCasesAddUser:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.driver, self.wait)
        self.home = HomePage(self.driver, self.wait)
        self.userMenu = UserSettingMenu(self.driver, self.wait)
        self.users = UsersTab(self.driver, self.wait)
        self.userAdd = UserAddPage(self.driver, self.wait)

    def test_negativeCases_AddUser_01(self):
        # Case 1: Hit the Create User button when all the required fields are blank

        # Login to the velocity app
        self.ut.login()
        # Click on the User Dropdown
        self.home.clickDropdown()
        time.sleep(1)
        # Click on the user option
        self.userMenu.clickUsers()
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("User List"))
        assert "Atlona Velocity | User List" in self.driver.title

        # Click on the Add User button
        self.users.clickAddUserButton()
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("User Add"))
        assert "Atlona Velocity | User Add" in self.driver.title
        self.userAdd.clickCreateUser()
        assert "Atlona Velocity | User Add" in self.driver.title

    def test_negativeCases_AddUser_02(self):
        # Case 2: Hit the Create User button when the role type is blank

        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("User Add"))
        assert "Atlona Velocity | User Add" in self.driver.title
        self.userAdd.enterAllData("shamin.jeesa@atlona.com", "Sharmin", "Jeesa", "1234")
        self.userAdd.clickCreateUser()
        assert "Atlona Velocity | User Add" in self.driver.title

    def test_negativeCases_AddUser_03(self):
        # Case 3: Hit the Create User button when the email field is blank

        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("User Add"))
        assert "Atlona Velocity | User Add" in self.driver.title
        self.userAdd.clearEmail()
        self.userAdd.selectDropdownValue()
        self.userAdd.clickCreateUser()
        assert "Atlona Velocity | User Add" in self.driver.title

    def test_negativeCases_AddUser_04(self):
        # Case 4: Hit the Create User button when the first name is blank

        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("User Add"))
        assert "Atlona Velocity | User Add" in self.driver.title
        self.userAdd.enterEmail("shamin.jeesa@atlona.com")
        self.userAdd.clearFirstName()
        self.userAdd.clickCreateUser()
        assert "Atlona Velocity | User Add" in self.driver.title

    def test_negativeCases_AddUser_05(self):
        # Case 5: Hit the Create User button when the last name is blank

        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("User Add"))
        assert "Atlona Velocity | User Add" in self.driver.title
        self.userAdd.enterFirstName("Sharmin")
        self.userAdd.clearLastName()
        self.userAdd.clickCreateUser()
        assert "Atlona Velocity | User Add" in self.driver.title

    def test_negativeCases_AddUser_06(self):
        # Case 6: Hit the Create User button when the temporary password is blank

        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("User Add"))
        assert "Atlona Velocity | User Add" in self.driver.title
        self.userAdd.enterLastName("Jeesa")
        self.userAdd.clearTempPass()
        self.userAdd.clickCreateUser()
        assert "Atlona Velocity | User Add" in self.driver.title

