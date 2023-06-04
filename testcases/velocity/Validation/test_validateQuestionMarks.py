import time

import pytest

from pages.velocity.CalendarIntegrationList_Page import CalendarIntegrationListPage
from pages.velocity.menus.UserSettings_Menu import UserSettingMenu
from pages.velocity.Home_Page import HomePage
from pages.velocity.menus.LeftBarMenu import LeftBarMenu
from pages.velocity.security.Login_Page import LoginPage
from pages.velocity.settings.Cloud_tab import CloudTab
from pages.velocity.settings.Database_tab import DatabaseTab
from pages.velocity.settings.Email_tab import EmailTab
from pages.velocity.settings.Gateway_tab import GatewayTab
from pages.velocity.settings.Licenses_tab import LicensesTab
from pages.velocity.settings.Network_tab import NetworkTab
from pages.velocity.settings.Security_tab import SecurityTab
from pages.velocity.settings.Tools_tab import ToolsTab
from pages.velocity.sites.Buildings_Page import BuildingsPage
from pages.velocity.sites.RoomList_Page import RoomListPage
from pages.velocity.sites.RoomModify_Page import RoomModifyPage
from pages.velocity.sites.Sites_Page import SitesPage
from pages.velocity.userSettings.Profile_tab import ProfileTab
from pages.velocity.userSettings.Roles_tab import RolesTab
from pages.velocity.userSettings.Users_tab import UsersTab
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestValidateQuestionMarks:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.login = LoginPage(self.driver, self.wait)
        self.ut = Utils(self.driver, self.wait)
        self.home = HomePage(self.driver, self.wait)
        self.leftNav = LeftBarMenu(self.driver, self.wait)
        self.roomList = RoomListPage(self.driver, self.wait)
        self.clIntLst = CalendarIntegrationListPage(self.driver, self.wait)
        self.gateway = GatewayTab(self.driver, self.wait)
        self.database = DatabaseTab(self.driver, self.wait)
        self.licenses = LicensesTab(self.driver, self.wait)
        self.tools = ToolsTab(self.driver, self.wait)
        self.email = EmailTab(self.driver, self.wait)
        self.security = SecurityTab(self.driver, self.wait)
        self.network = NetworkTab(self.driver, self.wait)
        self.cloud = CloudTab(self.driver, self.wait)
        self.userMenu = UserSettingMenu(self.driver, self.wait)
        self.profileTab = ProfileTab(self.driver, self.wait)
        self.usersTab = UsersTab(self.driver, self.wait)
        self.rolesTab = RolesTab(self.driver, self.wait)
        self.sites = SitesPage(self.driver, self.wait)
        self.buildings = BuildingsPage(self.driver, self.wait)
        self.roomModify = RoomModifyPage(self.driver, self.wait)

    def test_ValidateQuestionMarks(self):

        # wait until Login page loaded successfully
        self.wait.until(EC.title_contains("Login"))
        # Verify the page after launching the Velocity App
        assert "Atlona Velocity | Login To The System" in self.driver.title
        time.sleep(1)

        self.login.validateLoginHelp()
        # Verify the page after launching the Velocity App
        assert "Atlona Velocity | Login To The System" in self.driver.title
        self.login.validateSyncHelp()
        # Verify the page after launching the Velocity App
        assert "Atlona Velocity | Login To The System" in self.driver.title
        self.login.validateForgotPassHelp()

        # Login to the velocity app
        self.ut.login()
        self.home.clickNavBar()
        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        self.leftNav.clickControl()
        self.leftNav.clickCon_allRooms()
        time.sleep(1)
        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("Room List"))
        assert "Atlona Velocity | Room List" in self.driver.title
        self.roomList.validateRoomsHelp()
        time.sleep(1)
        assert "Atlona Velocity | Room List" in self.driver.title
        self.roomList.validateFloor1Help()
        assert "Atlona Velocity | Room List" in self.driver.title

        self.home.clickNavBar()
        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        self.leftNav.clickScheduling()
        self.leftNav.clickSch_manage()
        time.sleep(1)
        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("Calendar Integration List"))
        assert "Atlona Velocity | Calendar Integration List" in self.driver.title
        self.clIntLst.validateClIntLstHelp()
        assert "Atlona Velocity | Calendar Integration List" in self.driver.title

        self.home.clickNavBar()
        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        self.leftNav.clickSettings()
        self.leftNav.clickSet_gateway()
        time.sleep(1)
        assert self.gateway.visibilityOfGatewayTab() is True
        self.gateway.validateGatewayHelp()
        assert self.gateway.visibilityOfGatewayTab() is True

        self.home.clickNavBar()
        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        self.leftNav.clickSettings()
        self.leftNav.clickSet_database()
        time.sleep(1)
        assert self.database.visibilityOfDatabaseTab() is True
        time.sleep(1)
        self.database.validateDatabaseHelp()
        assert self.database.visibilityOfDatabaseTab() is True

        self.home.clickNavBar()
        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        self.leftNav.clickSettings()
        self.leftNav.clickSet_licenses()
        time.sleep(1)
        assert self.licenses.visibilityOfLicensesTab() is True
        time.sleep(1)
        self.licenses.validateLicensesHelp()
        assert self.licenses.visibilityOfLicensesTab() is True
        time.sleep(1)
        self.licenses.validateActSetHelp()
        assert self.licenses.visibilityOfLicensesTab() is True

        self.home.clickNavBar()
        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        self.leftNav.clickSettings()
        self.leftNav.clickSet_tools()
        time.sleep(1)
        assert self.tools.visibilityOfToolsTab() is True
        time.sleep(1)
        self.tools.validateToolsHelp()
        assert self.tools.visibilityOfToolsTab() is True

        self.home.clickNavBar()
        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        self.leftNav.clickSettings()
        self.leftNav.clickSet_email()
        time.sleep(1)
        assert self.email.visibilityOfEmailTab() is True
        time.sleep(1)
        self.email.validateEmailHelp()
        assert self.email.visibilityOfEmailTab() is True

        self.home.clickNavBar()
        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        self.leftNav.clickSettings()
        self.leftNav.clickSet_security()
        time.sleep(1)
        assert self.security.visibilityOfSecurityTab() is True
        time.sleep(1)
        self.security.validateSecurityHelp()
        assert self.security.visibilityOfSecurityTab() is True

        self.home.clickNavBar()
        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        self.leftNav.clickSettings()
        self.leftNav.clickSet_network()
        time.sleep(1)
        assert self.network.visibilityOfAllNetworksTab() is True
        time.sleep(1)
        self.network.validateNetworkHelp()
        assert self.network.visibilityOfAllNetworksTab() is True

        self.home.clickNavBar()
        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        self.leftNav.clickCloud()
        assert self.cloud.visibilityOfCloudTab() is True
        time.sleep(1)
        self.cloud.validateCloudHelp()
        assert self.cloud.visibilityOfCloudTab() is True
        time.sleep(1)
        self.cloud.validateCldAccHelp()
        assert self.cloud.visibilityOfCloudTab() is True

        # Click on the User Dropdown
        self.home.clickDropdown()
        time.sleep(1)
        # Click on the Logout Button
        self.userMenu.clickProfile()
        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("User Profile"))
        assert "Atlona Velocity | User Profile" in self.driver.title
        # Click on the Logout Button
        self.profileTab.validateProfileHelp()
        assert "Atlona Velocity | User Profile" in self.driver.title

        # Click on the User Dropdown
        self.home.clickDropdown()
        time.sleep(1)
        # Click on the Logout Button
        self.userMenu.clickUsers()
        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("User List"))
        assert "Atlona Velocity | User List" in self.driver.title
        # Click on the Logout Button
        self.usersTab.validateUsersHelp()
        assert "Atlona Velocity | User List" in self.driver.title

        # Click on the Logout Button
        self.userMenu.clickRolesTab()
        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("Role List"))
        assert "Atlona Velocity | Role List" in self.driver.title
        # Click on the Logout Button
        self.rolesTab.validateRolesHelp()
        assert "Atlona Velocity | Role List" in self.driver.title

        self.home.clickVelocityLogo()
        # wait until the login is successful
        self.wait.until(EC.title_contains("Dashboard"))
        # Verify the page after logging into the Velocity App
        assert "Atlona Velocity | Dashboard" in self.driver.title
        # Click on the created site
        self.home.clickSite()
        # wait until the sites page is loaded successfully
        self.wait.until(EC.title_contains("Sites"))
        assert "Atlona Velocity | Sites" in self.driver.title
        self.sites.validateSitesHelp()
        assert "Atlona Velocity | Sites" in self.driver.title

        # Click on the view button
        self.sites.clickView()
        # wait until the buildings page is loaded successfully
        self.wait.until(EC.title_contains("Buildings"))
        assert "Atlona Velocity | Buildings" in self.driver.title
        self.buildings.validateBuildingsHelp()
        assert "Atlona Velocity | Buildings" in self.driver.title

        # Click on the view button
        self.buildings.clickViewAllRooms1()
        # wait until the room list page is loaded successfully
        self.wait.until(EC.title_contains("Room List"))
        assert "Atlona Velocity | Room List" in self.driver.title
        self.roomList.clickEditRoom1Button()
        # wait until the room list page is loaded successfully
        self.wait.until(EC.title_contains("Room Modify"))
        assert "Atlona Velocity | Room Modify" in self.driver.title
        self.roomModify.validateRoomModifyHelp()
        assert "Atlona Velocity | Room Modify" in self.driver.title


