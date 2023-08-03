import time

import pytest

from pages.velocity.DeviceList_Page import DeviceListPage
from pages.velocity.Home_Page import HomePage
from pages.velocity.menus.LeftBar_Menu import LeftBarMenu
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestClearSearchAMS:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.driver, self.wait)
        self.home = HomePage(self.driver, self.wait)
        self.leftNav = LeftBarMenu(self.driver, self.wait)
        self.deviceList = DeviceListPage(self.driver, self.wait)

    def test_ClearSearchAMS_01(self):
        # Case 1: using the cross icon

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

        totalRowCount = self.deviceList.totalRowCount()
        self.deviceList.enterSearchContent("AT-VTP-1000VL")
        time.sleep(1)
        self.deviceList.clickClearSearch()
        time.sleep(1)
        afterClearRowCount = self.deviceList.totalRowCount()
        assert totalRowCount == afterClearRowCount

    def test_ClearSearchAMS_02(self):
        # Case 1: using the device list button

        assert "Atlona Velocity | Atlona Devices" in self.driver.title
        totalRowCount = self.deviceList.totalRowCount()
        self.deviceList.enterSearchContent("AT-VTP-1000VL")
        time.sleep(1)
        self.deviceList.clickDeviceList()
        time.sleep(1)
        afterClearRowCount = self.deviceList.totalRowCount()
        assert totalRowCount == afterClearRowCount
