import time

import pytest

from pages.velocity.DeviceList_Page import DeviceListPage
from pages.velocity.Home_Page import HomePage
from pages.velocity.menus.LeftBar_Menu import LeftBarMenu
from pages.velocity.popups.CustomNetworkScan_popup import CustomNetworkPopup
from pages.velocity.popups.ScanNetwork_popup import ScanNetworkPopup
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestSubnetScanAMS:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.driver, self.wait)
        self.home = HomePage(self.driver, self.wait)
        self.leftNav = LeftBarMenu(self.driver, self.wait)
        self.deviceList = DeviceListPage(self.driver, self.wait)
        self.scanPop = ScanNetworkPopup(self.driver, self.wait)
        self.customPop = CustomNetworkPopup(self.driver, self.wait)

    def test_subnetScanAMS(self):
        # Login to the velocity app
        self.ut.login()
        self.home.clickNavBar()
        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        self.leftNav.clickManagement()
        self.leftNav.clickMng_amsDeviceManager()
        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("Atlona Devices"))
        assert "Atlona Velocity | Atlona Devices" in self.driver.title

        self.deviceList.clickScan()
        beforeScanCount = self.deviceList.totalRowCount()
        assert self.scanPop.visibilityOfScanPopup() is True
        self.scanPop.clickDropdown()
        self.scanPop.clickCustom()
        assert self.customPop.visibilityOfCustomNetworkPopup() is True

        self.customPop.clickSubnetScan()
        assert self.customPop.visibilityOfSubnetScanPopup() is True
        self.customPop.clearIpAddress()
        self.customPop.enterIpAddress("10.20.40")
        self.customPop.clickSubnetDropdown()
        self.customPop.clickSubnetValue()
        self.customPop.clickScanNetwork()
        time.sleep(30)
        afterScanCount = self.deviceList.totalRowCount()
        assert beforeScanCount <= afterScanCount
