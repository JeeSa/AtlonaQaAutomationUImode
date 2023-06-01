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
    def test_ValidateQuestionMarks(self):

        # wait until Login page loaded successfully
        self.wait.until(EC.title_contains("Login"))
        # Verify the page after launching the Velocity App
        assert "Atlona Velocity | Login To The System" in self.driver.title

        login = LoginPage(self.driver, self.wait)
        login.validateLoginHelp()

        # Verify the page after launching the Velocity App
        assert "Atlona Velocity | Login To The System" in self.driver.title

        login.validateSyncHelp()

        # Verify the page after launching the Velocity App
        assert "Atlona Velocity | Login To The System" in self.driver.title

        login.validateForgotPassHelp()

        # Login to the velocity app
        ut = Utils(self.driver, self.wait)
        ut.login()

        homePage = HomePage(self.driver, self.wait)

        homePage.clickNavBar()

        # Verify if the sidebar is visible
        assert homePage.visibilityOfSidebarMenu() is True

        leftNav = LeftBarMenu(self.driver, self.wait)

        leftNav.clickControl()
        leftNav.clickCon_allRooms()

        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("Room List"))

        assert "Atlona Velocity | Room List" in self.driver.title

        roomList = RoomListPage(self.driver, self.wait)

        roomList.validateRoomsHelp()

        assert "Atlona Velocity | Room List" in self.driver.title

        roomList.validateFloor1Help()

        assert "Atlona Velocity | Room List" in self.driver.title

        homePage.clickNavBar()

        # Verify if the sidebar is visible
        assert homePage.visibilityOfSidebarMenu() is True

        leftNav.clickScheduling()
        leftNav.clickSch_manage()

        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("Calendar Integration List"))

        assert "Atlona Velocity | Calendar Integration List" in self.driver.title

        clIntLst = CalendarIntegrationListPage(self.driver, self.wait)
        clIntLst.validateClIntLstHelp()

        assert "Atlona Velocity | Calendar Integration List" in self.driver.title

        homePage.clickNavBar()

        # Verify if the sidebar is visible
        assert homePage.visibilityOfSidebarMenu() is True

        leftNav.clickSettings()
        leftNav.clickSet_gateway()

        gateway = GatewayTab(self.driver, self.wait)

        assert gateway.visibilityOfGatewayTab() is True

        gateway.validateGatewayHelp()

        assert gateway.visibilityOfGatewayTab() is True

        homePage.clickNavBar()

        # Verify if the sidebar is visible
        assert homePage.visibilityOfSidebarMenu() is True

        leftNav.clickSettings()
        leftNav.clickSet_database()

        database = DatabaseTab(self.driver, self.wait)

        assert database.visibilityOfDatabaseTab() is True
        time.sleep(1)
        database.validateDatabaseHelp()

        assert database.visibilityOfDatabaseTab() is True

        homePage.clickNavBar()

        # Verify if the sidebar is visible
        assert homePage.visibilityOfSidebarMenu() is True

        leftNav.clickSettings()
        leftNav.clickSet_licenses()

        licenses = LicensesTab(self.driver, self.wait)

        assert licenses.visibilityOfLicensesTab() is True
        time.sleep(1)
        licenses.validateLicensesHelp()

        assert licenses.visibilityOfLicensesTab() is True

        licenses.validateActSetHelp()

        assert licenses.visibilityOfLicensesTab() is True

        homePage.clickNavBar()

        # Verify if the sidebar is visible
        assert homePage.visibilityOfSidebarMenu() is True

        leftNav.clickSettings()
        leftNav.clickSet_tools()

        tools = ToolsTab(self.driver, self.wait)

        assert tools.visibilityOfToolsTab() is True
        time.sleep(1)
        tools.validateToolsHelp()

        assert tools.visibilityOfToolsTab() is True

        homePage.clickNavBar()

        # Verify if the sidebar is visible
        assert homePage.visibilityOfSidebarMenu() is True

        leftNav.clickSettings()
        leftNav.clickSet_email()

        email = EmailTab(self.driver, self.wait)

        assert email.visibilityOfEmailTab() is True
        time.sleep(1)
        email.validateEmailHelp()

        assert email.visibilityOfEmailTab() is True

        homePage.clickNavBar()

        # Verify if the sidebar is visible
        assert homePage.visibilityOfSidebarMenu() is True

        leftNav.clickSettings()
        leftNav.clickSet_security()

        security = SecurityTab(self.driver, self.wait)

        assert security.visibilityOfSecurityTab() is True
        time.sleep(1)
        security.validateSecurityHelp()

        assert security.visibilityOfSecurityTab() is True

        homePage.clickNavBar()

        # Verify if the sidebar is visible
        assert homePage.visibilityOfSidebarMenu() is True

        leftNav.clickSettings()
        leftNav.clickSet_network()

        network = NetworkTab(self.driver, self.wait)

        assert network.visibilityOfAllNetworksTab() is True
        time.sleep(1)
        network.validateNetworkHelp()

        assert network.visibilityOfAllNetworksTab() is True

        homePage.clickNavBar()

        # Verify if the sidebar is visible
        assert homePage.visibilityOfSidebarMenu() is True

        leftNav.clickCloud()

        cloud = CloudTab(self.driver, self.wait)

        assert cloud.visibilityOfCloudTab() is True
        time.sleep(1)
        cloud.validateCloudHelp()

        assert cloud.visibilityOfCloudTab() is True

        cloud.validateCldAccHelp()
        assert cloud.visibilityOfCloudTab() is True

        home = HomePage(self.driver, self.wait)

        # Click on the User Dropdown
        home.clickDropdown()

        userMenu = UserSettingMenu(self.driver, self.wait)

        # Click on the Logout Button
        userMenu.clickProfile()

        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("User Profile"))

        assert "Atlona Velocity | User Profile" in self.driver.title

        profileTab = ProfileTab(self.driver, self.wait)

        # Click on the Logout Button
        profileTab.validateProfileHelp()

        assert "Atlona Velocity | User Profile" in self.driver.title

        # Click on the User Dropdown
        home.clickDropdown()
        # Click on the Logout Button
        userMenu.clickUsers()

        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("User List"))

        assert "Atlona Velocity | User List" in self.driver.title

        usersTab = UsersTab(self.driver, self.wait)

        # Click on the Logout Button
        usersTab.validateUsersHelp()

        assert "Atlona Velocity | User List" in self.driver.title

        # Click on the Logout Button
        userMenu.clickRolesTab()

        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("Role List"))

        assert "Atlona Velocity | Role List" in self.driver.title

        rolesTab = RolesTab(self.driver, self.wait)

        # Click on the Logout Button
        rolesTab.validateRolesHelp()

        assert "Atlona Velocity | Role List" in self.driver.title

        homePage.clickVelocityLogo()

        # wait until the login is successful
        self.wait.until(EC.title_contains("Dashboard"))
        # Verify the page after logging into the Velocity App
        assert "Atlona Velocity | Dashboard" in self.driver.title

        # Click on the created site
        homePage.clickSite()

        # wait until the sites page is loaded successfully
        self.wait.until(EC.title_contains("Sites"))

        assert "Atlona Velocity | Sites" in self.driver.title

        sites = SitesPage(self.driver, self.wait)
        sites.validateSitesHelp()

        assert "Atlona Velocity | Sites" in self.driver.title

        # Click on the view button
        sites.clickView()

        # wait until the buildings page is loaded successfully
        self.wait.until(EC.title_contains("Buildings"))

        assert "Atlona Velocity | Buildings" in self.driver.title

        buildings = BuildingsPage(self.driver, self.wait)
        buildings.validateBuildingsHelp()

        assert "Atlona Velocity | Buildings" in self.driver.title

        # Click on the view button
        buildings.clickViewAllRooms1()

        # wait until the room list page is loaded successfully
        self.wait.until(EC.title_contains("Room List"))

        assert "Atlona Velocity | Room List" in self.driver.title

        roomList = RoomListPage(self.driver, self.wait)

        roomList.clickEditRoom1Button()

        # wait until the room list page is loaded successfully
        self.wait.until(EC.title_contains("Room Modify"))

        assert "Atlona Velocity | Room Modify" in self.driver.title

        roomModify = RoomModifyPage(self.driver, self.wait)

        roomModify.validateRoomModifyHelp()

        assert "Atlona Velocity | Room Modify" in self.driver.title










