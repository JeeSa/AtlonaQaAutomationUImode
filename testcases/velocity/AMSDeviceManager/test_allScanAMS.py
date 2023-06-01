import time

import pytest

from pages.velocity.DeviceList_Page import DeviceListPage
from pages.velocity.Home_Page import HomePage
from pages.velocity.menus.DeviceToolsHamburger import DeviceToolsHamburger
from pages.velocity.menus.LeftBarMenu import LeftBarMenu
from pages.velocity.popups.Confirm_popup import ConfirmPopup
from pages.velocity.popups.ScanNetwork_popup import ScanNetworkPopup
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestAllScanAMS:
    def test_allScanAMS(self):

        # Login to the velocity app
        ut = Utils(self.driver, self.wait)
        ut.login()

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
        deviceList.clickScan()

        beforeScanCount = deviceList.totalRowCount()

        scanPop = ScanNetworkPopup(self.driver, self.wait)
        assert scanPop.visibilityOfScanPopup() is True

        scanPop.clickDropdown()
        scanPop.clickAll()
        scanPop.clickScanNetwork()

        """confirmPop = ConfirmPopup(self.driver, self.wait)
        assert confirmPop.visibilityOfConfirmPopup() is True

        confirmPop.clickSubmit()"""
        time.sleep(10)
        afterScanCount = deviceList.totalRowCount()

        assert beforeScanCount != afterScanCount


















