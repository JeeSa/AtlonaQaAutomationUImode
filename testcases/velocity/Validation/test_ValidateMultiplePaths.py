import time

import pytest

from pages.velocity.DeviceList_Page import DeviceListPage
from pages.velocity.Home_Page import HomePage
from pages.velocity.RoomProblemReport_Page import RoomProblemReportPage
from pages.velocity.menus.LeftBar_Menu import LeftBarMenu
from pages.velocity.popups.AddOrImport_popup import AddOrImportPopup
from pages.velocity.reportSections.AllDevices_Page import AllDevicesPage
from pages.velocity.sites.Buildings_Page import BuildingsPage
from pages.velocity.sites.RoomList_Page import RoomListPage
from pages.velocity.sites.RoomModifyDevices_Page import RoomModifyDevicesPage
from pages.velocity.sites.Sites_Page import SitesPage
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestValidateMultiplePaths:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.driver, self.wait)
        self.home = HomePage(self.driver, self.wait)
        self.leftNav = LeftBarMenu(self.driver, self.wait)
        self.roomList = RoomListPage(self.driver, self.wait)
        self.sites = SitesPage(self.driver, self.wait)
        self.buildings = BuildingsPage(self.driver, self.wait)
        self.addImport = AddOrImportPopup(self.driver, self.wait)
        self.modifyDevices = RoomModifyDevicesPage(self.driver, self.wait)
        self.roomProblem = RoomProblemReportPage(self.driver, self.wait)
        self.allDevice = AllDevicesPage(self.driver, self.wait)
        self.deviceList = DeviceListPage(self.driver, self.wait)

    def test_validatePaths2Sites(self):

        """Multiple paths to land on the Sites page
            1.Click on the created site from the dashboard
            2.Click "Sites " from the gateway information on the dashboard
            3.Expand all details of the site > Click on any building or room page > Click on the "All sites" from the breadcrumb"""

        # Login to the velocity app
        self.ut.login()
        # Click on the created site
        self.home.clickSite()
        # wait until the sites page is loaded successfully
        self.wait.until(EC.title_contains("Sites"))
        assert "Atlona Velocity | Sites" in self.driver.title

        self.home.clickVelocityLogo()
        # wait until the login is successful
        self.wait.until(EC.title_contains("Dashboard"))
        # Verify the page after logging into the Velocity App
        assert "Atlona Velocity | Dashboard" in self.driver.title
        self.home.clickSites()
        # wait until the sites page is loaded successfully
        self.wait.until(EC.title_contains("Sites"))
        assert "Atlona Velocity | Sites" in self.driver.title

        self.home.clickVelocityLogo()
        # wait until the login is successful
        self.wait.until(EC.title_contains("Dashboard"))
        # Verify the page after logging into the Velocity App
        assert "Atlona Velocity | Dashboard" in self.driver.title
        self.home.clickExpandAll()
        time.sleep(1)
        self.home.clickBuildingName()
        # wait until the room list page is loaded successfully
        self.wait.until(EC.title_contains("Room List"))
        assert "Atlona Velocity | Room List" in self.driver.title

        self.roomList.clickAllAitesBreadcrumb()
        # wait until the sites page is loaded successfully
        self.wait.until(EC.title_contains("Sites"))
        assert "Atlona Velocity | Sites" in self.driver.title

    def test_validatePaths2AddBuilding(self):

        """Multiple paths to land on the Add building page
            1. Click on the created site from the dashboard > Click on the "add building to site" from the sites page
            2. Click on the view button from the sites page > Click on the orange '+' button from the buildings page"""

        self.home.clickVelocityLogo()
        # wait until the login is successful
        self.wait.until(EC.title_contains("Dashboard"))
        # Verify the page after logging into the Velocity App
        assert "Atlona Velocity | Dashboard" in self.driver.title
        self.home.clickSites()
        # wait until the sites page is loaded successfully
        self.wait.until(EC.title_contains("Sites"))
        assert "Atlona Velocity | Sites" in self.driver.title
        # Click on the view button
        self.sites.clickAddBuilding()
        # wait until the buildings page is loaded successfully
        self.wait.until(EC.title_contains("Building Add"))
        assert "Atlona Velocity | Building Add" in self.driver.title

        self.driver.back()
        # wait until the sites page is loaded successfully
        self.wait.until(EC.title_contains("Sites"))
        assert "Atlona Velocity | Sites" in self.driver.title
        self.sites.clickView()
        # wait until the buildings page is loaded successfully
        self.wait.until(EC.title_contains("Buildings"))
        assert "Atlona Velocity | Buildings" in self.driver.title

        # Click on the view button
        self.buildings.clickAddBuildingButton()
        self.addImport.clickAddViaForm()
        # wait until the buildings page is loaded successfully
        self.wait.until(EC.title_contains("Building Add"))
        assert "Atlona Velocity | Building Add" in self.driver.title

    def test_validatePaths2RoomlistOfAnyBuilding(self):

        """Multiple paths to land on the Room list of any particular building
            1. Click on the created site from the dashboard > Click on the view button from the sites page > Click on the "View all rooms" button from the Buildings page
            2. Expand all details of the site > Click on any building 
            3. Expand all details of the site > Click on any room > Click on the building Name from the breadcrumb"""

        self.home.clickVelocityLogo()
        # wait until the login is successful
        self.wait.until(EC.title_contains("Dashboard"))
        # Verify the page after logging into the Velocity App
        assert "Atlona Velocity | Dashboard" in self.driver.title

        self.home.clickSites()
        # wait until the sites page is loaded successfully
        self.wait.until(EC.title_contains("Sites"))
        assert "Atlona Velocity | Sites" in self.driver.title
        self.sites.clickView()
        # wait until the buildings page is loaded successfully
        self.wait.until(EC.title_contains("Buildings"))
        assert "Atlona Velocity | Buildings" in self.driver.title

        # Click on the view button
        self.buildings.clickViewAllRooms1()
        # wait until the room list page is loaded successfully
        self.wait.until(EC.title_contains("Room List"))
        assert "Atlona Velocity | Room List" in self.driver.title

        self.home.clickVelocityLogo()
        # wait until the login is successful
        self.wait.until(EC.title_contains("Dashboard"))
        # Verify the page after logging into the Velocity App
        assert "Atlona Velocity | Dashboard" in self.driver.title
        self.home.clickExpandAll()
        time.sleep(1)
        self.home.clickBuildingName()
        # wait until the room list page is loaded successfully
        self.wait.until(EC.title_contains("Room List"))
        assert "Atlona Velocity | Room List" in self.driver.title

        self.home.clickVelocityLogo()
        # wait until the login is successful
        self.wait.until(EC.title_contains("Dashboard"))
        # Verify the page after logging into the Velocity App
        assert "Atlona Velocity | Dashboard" in self.driver.title
        self.home.clickExpandAll()
        time.sleep(1)
        self.home.clickRoomName()
        # wait until the room list page is loaded successfully
        self.wait.until(EC.title_contains("Room Modify Devices"))
        assert "Atlona Velocity | Room Modify Devices" in self.driver.title

        self.modifyDevices.clickBuildingNameBreadcrumb()
        # wait until the room list page is loaded successfully
        self.wait.until(EC.title_contains("Room List"))
        assert "Atlona Velocity | Room List" in self.driver.title

    def test_validatePaths2RoomlistOfFullSite(self):
        """Multiple paths to land on the Room list of the full site
            1.Click on the Total rooms from the gateway information on the dashboard
            2.Click on the left menu > Control > All rooms
            3.Click on the left menu > Scheduling > All rooms"""

        self.home.clickVelocityLogo()
        # wait until the login is successful
        self.wait.until(EC.title_contains("Dashboard"))
        # Verify the page after logging into the Velocity App
        assert "Atlona Velocity | Dashboard" in self.driver.title

        self.home.clickTotalRooms()
        # wait until the room list page is loaded successfully
        self.wait.until(EC.title_contains("Room List"))
        assert "Atlona Velocity | Room List" in self.driver.title

        self.home.clickVelocityLogo()
        # wait until the login is successful
        self.wait.until(EC.title_contains("Dashboard"))
        # Verify the page after logging into the Velocity App
        assert "Atlona Velocity | Dashboard" in self.driver.title
        self.home.clickNavBar()
        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        self.leftNav.clickControl()
        self.leftNav.clickCon_allRooms()
        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("Room List"))
        assert "Atlona Velocity | Room List" in self.driver.title

        self.home.clickVelocityLogo()
        # wait until the login is successful
        self.wait.until(EC.title_contains("Dashboard"))
        # Verify the page after logging into the Velocity App
        assert "Atlona Velocity | Dashboard" in self.driver.title
        self.home.clickNavBar()
        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        self.leftNav.clickScheduling()
        self.leftNav.clickSch_allRooms()
        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("Room List"))
        assert "Atlona Velocity | Room List" in self.driver.title

    def test_validatePaths2RoomModifyDevice(self):

        """Multiple paths to land on the Room Modify Device page
            1.Click on the created site from the dashboard > Click on the view button from the sites page > Click on the "View all rooms" button from the Buildings page > Click on the "Edit Room Technology" button from the room list page
            2.Expand all details of the site > Click on any room
            3.Click on the left menu > Reports Room Problem > Click on any room > Modify room technology
            4.Click on the left menu > Reports > All devices > Click on any Room
            5.Click on the left menu > Management > Device Manager > Expand building > hover on Room and click on the HDMI icon """

        self.home.clickVelocityLogo()
        # wait until the login is successful
        self.wait.until(EC.title_contains("Dashboard"))
        # Verify the page after logging into the Velocity App
        assert "Atlona Velocity | Dashboard" in self.driver.title

        self.home.clickSites()
        # wait until the sites page is loaded successfully
        self.wait.until(EC.title_contains("Sites"))
        assert "Atlona Velocity | Sites" in self.driver.title

        self.sites.clickView()
        # wait until the buildings page is loaded successfully
        self.wait.until(EC.title_contains("Buildings"))
        assert "Atlona Velocity | Buildings" in self.driver.title

        # Click on the view button
        self.buildings.clickViewAllRooms1()
        # wait until the room list page is loaded successfully
        self.wait.until(EC.title_contains("Room List"))
        assert "Atlona Velocity | Room List" in self.driver.title

        # Click on the edit technology button
        self.roomList.clickEditTechnology1Button()
        # wait until the modify room page is loaded successfully
        self.wait.until(EC.title_contains("Room Modify Devices"))
        assert "Atlona Velocity | Room Modify Devices" in self.driver.title

        self.home.clickVelocityLogo()
        # wait until the login is successful
        self.wait.until(EC.title_contains("Dashboard"))
        # Verify the page after logging into the Velocity App
        assert "Atlona Velocity | Dashboard" in self.driver.title
        self.home.clickExpandAll()
        time.sleep(1)
        self.home.clickRoomName()
        # wait until the room list page is loaded successfully
        self.wait.until(EC.title_contains("Room Modify Devices"))
        assert "Atlona Velocity | Room Modify Devices" in self.driver.title

        self.home.clickVelocityLogo()
        # wait until the login is successful
        self.wait.until(EC.title_contains("Dashboard"))
        # Verify the page after logging into the Velocity App
        assert "Atlona Velocity | Dashboard" in self.driver.title
        self.home.clickNavBar()
        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        self.leftNav.clickReports()
        self.leftNav.clickRep_roomProblems()
        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("Report Room Problem"))
        assert "Atlona Velocity | Report Room Problem" in self.driver.title

        self.roomProblem.clickRoom1()
        assert self.roomProblem.visibilityOfModifyRoomTech1() is True
        self.roomProblem.clickModifyRoomTechnology1()
        # wait until the room list page is loaded successfully
        self.wait.until(EC.title_contains("Room Modify Devices"))
        assert "Atlona Velocity | Room Modify Devices" in self.driver.title

        self.home.clickNavBar()
        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        self.leftNav.clickReports()
        self.leftNav.clickRep_allDevices()
        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("All Devices"))
        assert "Atlona Velocity | All Devices" in self.driver.title

        self.allDevice.clickRoomName()
        # wait until the room list page is loaded successfully
        self.wait.until(EC.title_contains("Room Modify Devices"))
        assert "Atlona Velocity | Room Modify Devices" in self.driver.title
        self.home.clickNavBar()
        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        self.leftNav.clickManagement()
        self.leftNav.clickMng_amsDeviceManager()
        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("Atlona Devices"))
        assert "Atlona Velocity | Atlona Devices" in self.driver.title

        self.deviceList.clickExpandBuilding()
        self.deviceList.hoverRoomDiv()
        self.deviceList.clickHDMI1()
        # wait until the room list page is loaded successfully
        self.wait.until(EC.title_contains("Room Modify Devices"))
        assert "Atlona Velocity | Room Modify Devices" in self.driver.title
