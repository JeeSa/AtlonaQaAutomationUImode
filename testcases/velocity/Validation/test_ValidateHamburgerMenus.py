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
    def test_validateDashboardSettings(self):
        # Case 1: Validate the dashboard widget customization settings

        # Login to the velocity app
        ut = Utils(self.driver, self.wait)
        ut.login()

        homePage = HomePage(self.driver, self.wait)
        # Click on the created site
        homePage.clickWidgetHamburger()

        widget = WidgetSettingPopup(self.driver, self.wait)

        # Verify if the added technology is visible
        assert widget.visibilityOfWidgetSettingPopup() is True
        widget.clickClose()


    def test_validateAddDeviceList(self):
        # Case 2: Validate the Left(add) hamburger menu from the device list page

        homePage = HomePage(self.driver, self.wait)
        homePage.clickNavBar()

        # Verify if the sidebar is visible
        assert homePage.visibilityOfSidebarMenu() is True

        leftNav = LeftBarMenu(self.driver, self.wait)

        leftNav.clickManagement()
        leftNav.clickMng_amsDeviceManager()

        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("Atlona Devices"))

        assert "Atlona Velocity | Atlona Devices" in self.driver.title

        deviceList = DeviceListPage(self.driver, self.wait)
        deviceList.clickAddHamburger()

        addHamburger = DeviceAddHamburger(self.driver, self.wait)
        assert addHamburger.visibilityOfAddHamburgerMenu() is True
        addHamburger.clickAddSite()

        addSitePop = AddSitePopup(self.driver, self.wait)
        assert addSitePop.visibilityOfAddSitePage() is True
        addSitePop.clickCancel()

        deviceList.clickAddHamburger()
        assert addHamburger.visibilityOfAddHamburgerMenu() is True
        addHamburger.clickAddBuilding()

        addBuildingPop = AddBuildingPopup(self.driver, self.wait)
        assert addBuildingPop.visibilityOfAddBuilding() is True
        addBuildingPop.clickCancel()

        deviceList.clickAddHamburger()
        assert addHamburger.visibilityOfAddHamburgerMenu() is True
        addHamburger.clickAddRoom()

        addRoomPop = AddRoomPopup(self.driver, self.wait)
        assert addRoomPop.visibilityOfAddRoom() is True
        addRoomPop.clickCancel()

    def test_validateToolsDeviceList(self):
        # Case 2: Validate the Right(tools) hamburger menu from the device list page

        assert "Atlona Velocity | Atlona Devices" in self.driver.title

        deviceList = DeviceListPage(self.driver, self.wait)
        deviceList.clickToolsHamburger()

        toolsHamburger = DeviceToolsHamburger(self.driver, self.wait)
        assert toolsHamburger.visibilityOfToolsHamburgerMenu() is True
        toolsHamburger.clickScan()

        scanPop = ScanNetworkPopup(self.driver, self.wait)
        assert scanPop.visibilityOfScanPopup() is True
        scanPop.clickClose()

        deviceList.clickToolsHamburger()
        assert toolsHamburger.visibilityOfToolsHamburgerMenu() is True
        toolsHamburger.clickDeviceListSettings()

        deviceListSettingsPop = DeviceListSettingsPopup(self.driver, self.wait)
        assert deviceListSettingsPop.visibilityOfDeviceListSettingsPop() is True
        deviceListSettingsPop.clickClose()

        deviceList.clickToolsHamburger()
        assert toolsHamburger.visibilityOfToolsHamburgerMenu() is True
        toolsHamburger.clickCredentialsMassUpdate()

        credsMassUpdatePop = CredentialsMassUpdatePopup(self.driver, self.wait)
        assert credsMassUpdatePop.visibilityOfCredsMassUpdatePop() is True
        credsMassUpdatePop.clickClose()

        deviceList.clickToolsHamburger()
        assert toolsHamburger.visibilityOfToolsHamburgerMenu() is True
        toolsHamburger.clickFirmware()

        firmwarePop = FirmwarePopup(self.driver, self.wait)
        assert firmwarePop.visibilityOfFirmwarePop() is True
        firmwarePop.clickClose()

        deviceList.clickToolsHamburger()
        assert toolsHamburger.visibilityOfToolsHamburgerMenu() is True
        toolsHamburger.clickAlerts()

        alertsPop = AlertsPopup(self.driver, self.wait)
        assert alertsPop.visibilityOfAlertsPop() is True
        alertsPop.clickCancel()

        deviceList.clickToolsHamburger()
        assert toolsHamburger.visibilityOfToolsHamburgerMenu() is True
        toolsHamburger.clickDeleteAllUnassigned()

        deleteAllUnassignedPop = DeleteAllUnassignedPopup(self.driver, self.wait)
        assert deleteAllUnassignedPop.visibilityOfDeleteAllUnassignedPop() is True
        deleteAllUnassignedPop.clickCancel()

        deviceList.clickToolsHamburger()
        assert toolsHamburger.visibilityOfExportAll() is True

    def test_validateFloorHamburgerMenu(self):
        # Case 2: Validate the Left(add) hamburger menu from the device list page

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
        # Click on the more option button
        roomList.clickMoreButton1()

        flrHamburger = FloorHamburgerMenu(self.driver, self.wait)

        assert flrHamburger.visibilityOfAddRoom() is True
        assert flrHamburger.visibilityOfAddMeetingRoom() is True
        assert flrHamburger.visibilityOfAddMultipleRooms() is True
        assert flrHamburger.visibilityOfImportRoom() is True
        assert flrHamburger.visibilityOfAddNewFloor() is True
        assert flrHamburger.visibilityOfEditFloor() is True
        assert flrHamburger.visibilityOfCopyFloor() is True
        assert flrHamburger.visibilityOfExportFloor() is True
        assert flrHamburger.visibilityOfImportFloor() is True
        assert flrHamburger.visibilityOfDeleteFloor() is True
        assert flrHamburger.visibilityOfReorderRooms() is True
        assert flrHamburger.visibilityOfAllMacros() is True
        assert flrHamburger.visibilityOfAllDevices() is True










