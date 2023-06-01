import time

import pytest

from pages.velocity.DeviceList_Page import DeviceListPage
from pages.velocity.Home_Page import HomePage
from pages.velocity.menus.LeftBarMenu import LeftBarMenu
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestSearchDeviceAMS:
    def test_Search_DeviceAMS(self):
        # Case 1: Validate the dashboard widget customization settings

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

        stringedRowCount = deviceList.rowCountWithString()

        deviceList.enterSearchContent("AT-VTP-1000VL")
        time.sleep(1)

        resultedRowCount = deviceList.totalRowCount()

        assert stringedRowCount == resultedRowCount



