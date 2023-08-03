import time

import pytest

from pages.velocity.DeviceList_Page import DeviceListPage
from pages.velocity.Home_Page import HomePage
from pages.velocity.menus.DeviceToolsHamburger_Menu import DeviceToolsHamburger
from pages.velocity.menus.LeftBar_Menu import LeftBarMenu
from pages.velocity.popups.ScanNetwork_popup import ScanNetworkPopup
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestPaths2ScanAMS:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.driver, self.wait)
        self.home = HomePage(self.driver, self.wait)
        self.leftNav = LeftBarMenu(self.driver, self.wait)
        self.deviceList = DeviceListPage(self.driver, self.wait)
        self.toolsHamburger = DeviceToolsHamburger(self.driver, self.wait)
        self.scanPop = ScanNetworkPopup(self.driver, self.wait)

    def test_paths2scanAMS_01(self):
        # Case 1: using the Scan button

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
        assert self.scanPop.visibilityOfScanPopup() is True
        self.scanPop.clickClose()

    def test_paths2scanAMS_02(self):
        # Case 2: using the tools menu

        assert "Atlona Velocity | Atlona Devices" in self.driver.title
        self.deviceList.clickToolsHamburger()
        assert self.toolsHamburger.visibilityOfToolsHamburgerMenu() is True
        self.toolsHamburger.clickScan()
        assert self.scanPop.visibilityOfScanPopup() is True
