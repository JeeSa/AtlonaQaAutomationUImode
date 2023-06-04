import pytest

from pages.velocity.DeviceList_Page import DeviceListPage
from pages.velocity.Home_Page import HomePage
from pages.velocity.menus.DeviceAddHamburger_Menu import DeviceAddHamburger
from pages.velocity.menus.DeviceToolsHamburger import DeviceToolsHamburger
from pages.velocity.menus.LeftBarMenu import LeftBarMenu
from pages.velocity.popups.AddBuilding_popup import AddBuildingPopup
from pages.velocity.popups.AddRoom_popup import AddRoomPopup
from pages.velocity.popups.AddSite_popup import AddSitePopup
from pages.velocity.popups.Alerts_popup import AlertsPopup
from pages.velocity.popups.CredentialsMassUpdate_popup import CredentialsMassUpdatePopup
from pages.velocity.popups.DeleteAllUnassigned import DeleteAllUnassignedPopup
from pages.velocity.popups.DeviceListSettings_popup import DeviceListSettingsPopup
from pages.velocity.popups.Firmware_popup import FirmwarePopup
from pages.velocity.popups.ScanNetwork_popup import ScanNetworkPopup
from pages.velocity.popups.WidgetSettings_popup import WidgetSettingPopup
from pages.velocity.sites.FloorHamburger_Menu import FloorHamburgerMenu
from pages.velocity.sites.RoomList_Page import RoomListPage
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestValidateHamburgerMenus:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.driver, self.wait)
        self.home = HomePage(self.driver, self.wait)
        self.widget = WidgetSettingPopup(self.driver, self.wait)
        self.leftNav = LeftBarMenu(self.driver, self.wait)
        self.deviceList = DeviceListPage(self.driver, self.wait)
        self.addHamburger = DeviceAddHamburger(self.driver, self.wait)
        self.addSitePop = AddSitePopup(self.driver, self.wait)
        self.addBuildingPop = AddBuildingPopup(self.driver, self.wait)
        self.addRoomPop = AddRoomPopup(self.driver, self.wait)
        self.toolsHamburger = DeviceToolsHamburger(self.driver, self.wait)
        self.scanPop = ScanNetworkPopup(self.driver, self.wait)
        self.deviceListSettingsPop = DeviceListSettingsPopup(self.driver, self.wait)
        self.credsMassUpdatePop = CredentialsMassUpdatePopup(self.driver, self.wait)
        self.firmwarePop = FirmwarePopup(self.driver, self.wait)
        self.alertsPop = AlertsPopup(self.driver, self.wait)
        self.deleteAllUnassignedPop = DeleteAllUnassignedPopup(self.driver, self.wait)
        self.roomList = RoomListPage(self.driver, self.wait)
        self.flrHamburger = FloorHamburgerMenu(self.driver, self.wait)

    def test_validateDashboardSettings(self):
        # Case 1: Validate the dashboard widget customization settings

        # Login to the velocity app
        self.ut.login()
        # Click on the created site
        self.home.clickWidgetHamburger()
        # Verify if the added technology is visible
        assert self.widget.visibilityOfWidgetSettingPopup() is True
        self.widget.clickClose()

    def test_validateAddDeviceList(self):
        # Case 2: Validate the Left(add) hamburger menu from the device list page

        self.home.clickNavBar()
        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        self.leftNav.clickManagement()
        self.leftNav.clickMng_amsDeviceManager()
        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("Atlona Devices"))
        assert "Atlona Velocity | Atlona Devices" in self.driver.title

        self.deviceList.clickAddHamburger()
        assert self.addHamburger.visibilityOfAddHamburgerMenu() is True
        self.addHamburger.clickAddSite()
        assert self.addSitePop.visibilityOfAddSitePage() is True
        self.addSitePop.clickCancel()

        self.deviceList.clickAddHamburger()
        assert self.addHamburger.visibilityOfAddHamburgerMenu() is True
        self.addHamburger.clickAddBuilding()
        assert self.addBuildingPop.visibilityOfAddBuilding() is True
        self.addBuildingPop.clickCancel()

        self.deviceList.clickAddHamburger()
        assert self.addHamburger.visibilityOfAddHamburgerMenu() is True
        self.addHamburger.clickAddRoom()
        assert self.addRoomPop.visibilityOfAddRoom() is True
        self.addRoomPop.clickCancel()

    def test_validateToolsDeviceList(self):
        # Case 3: Validate the Right(tools) hamburger menu from the device list page

        assert "Atlona Velocity | Atlona Devices" in self.driver.title
        self.deviceList.clickToolsHamburger()
        assert self.toolsHamburger.visibilityOfToolsHamburgerMenu() is True
        self.toolsHamburger.clickScan()
        assert self.scanPop.visibilityOfScanPopup() is True
        self.scanPop.clickClose()

        self.deviceList.clickToolsHamburger()
        assert self.toolsHamburger.visibilityOfToolsHamburgerMenu() is True
        self.toolsHamburger.clickDeviceListSettings()
        assert self.deviceListSettingsPop.visibilityOfDeviceListSettingsPop() is True
        self.deviceListSettingsPop.clickClose()

        self.deviceList.clickToolsHamburger()
        assert self.toolsHamburger.visibilityOfToolsHamburgerMenu() is True
        self.toolsHamburger.clickCredentialsMassUpdate()
        assert self.credsMassUpdatePop.visibilityOfCredsMassUpdatePop() is True
        self.credsMassUpdatePop.clickClose()

        self.deviceList.clickToolsHamburger()
        assert self.toolsHamburger.visibilityOfToolsHamburgerMenu() is True
        self.toolsHamburger.clickFirmware()
        assert self.firmwarePop.visibilityOfFirmwarePop() is True
        self.firmwarePop.clickClose()

        self.deviceList.clickToolsHamburger()
        assert self.toolsHamburger.visibilityOfToolsHamburgerMenu() is True
        self.toolsHamburger.clickAlerts()
        assert self.alertsPop.visibilityOfAlertsPop() is True
        self.alertsPop.clickCancel()

        self.deviceList.clickToolsHamburger()
        assert self.toolsHamburger.visibilityOfToolsHamburgerMenu() is True
        self.toolsHamburger.clickDeleteAllUnassigned()
        assert self.deleteAllUnassignedPop.visibilityOfDeleteAllUnassignedPop() is True
        self.deleteAllUnassignedPop.clickCancel()

        self.deviceList.clickToolsHamburger()
        assert self.toolsHamburger.visibilityOfExportAll() is True

    def test_validateFloorHamburgerMenu(self):
        # Case 4: Validate the floor hamburger menu from the room list page

        self.home.clickNavBar()
        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        self.leftNav.clickControl()
        self.leftNav.clickCon_allRooms()
        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("Room List"))
        assert "Atlona Velocity | Room List" in self.driver.title

        # Click on the more option button
        self.roomList.clickMoreButton1()
        assert self.flrHamburger.visibilityOfAddRoom() is True
        assert self.flrHamburger.visibilityOfAddMeetingRoom() is True
        assert self.flrHamburger.visibilityOfAddMultipleRooms() is True
        assert self.flrHamburger.visibilityOfImportRoom() is True
        assert self.flrHamburger.visibilityOfAddNewFloor() is True
        assert self.flrHamburger.visibilityOfEditFloor() is True
        assert self.flrHamburger.visibilityOfCopyFloor() is True
        assert self.flrHamburger.visibilityOfExportFloor() is True
        assert self.flrHamburger.visibilityOfImportFloor() is True
        assert self.flrHamburger.visibilityOfDeleteFloor() is True
        assert self.flrHamburger.visibilityOfReorderRooms() is True
        assert self.flrHamburger.visibilityOfAllMacros() is True
        assert self.flrHamburger.visibilityOfAllDevices() is True

