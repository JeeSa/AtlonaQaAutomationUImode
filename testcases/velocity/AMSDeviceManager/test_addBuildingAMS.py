import time

import pytest

from pages.velocity.DeviceList_Page import DeviceListPage
from pages.velocity.Home_Page import HomePage
from pages.velocity.menus.DeviceAddHamburger_Menu import DeviceAddHamburger
from pages.velocity.menus.LeftBarMenu import LeftBarMenu
from pages.velocity.popups.AddBuilding_popup import AddBuildingPopup
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestAddBuildingAMS:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.driver, self.wait)
        self.home = HomePage(self.driver, self.wait)
        self.leftNav = LeftBarMenu(self.driver, self.wait)
        self.deviceList = DeviceListPage(self.driver, self.wait)
        self.addHamburger = DeviceAddHamburger(self.driver, self.wait)
        self.addBuildingPop = AddBuildingPopup(self.driver, self.wait)

    def test_addBuildingAMS(self):

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

        self.deviceList.clickAddHamburger()
        assert self.addHamburger.visibilityOfAddHamburgerMenu() is True
        self.addHamburger.clickAddBuilding()
        assert self.addBuildingPop.visibilityOfAddBuilding() is True
        self.addBuildingPop.createBuilding("AAA AMS B1")
        time.sleep(1)

        expected_bName = "AAA AMS B1"
        actual_bName = self.deviceList.passBuildingName()
        assert expected_bName == actual_bName

