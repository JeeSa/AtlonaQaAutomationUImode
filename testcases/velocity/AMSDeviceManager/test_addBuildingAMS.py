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
    def test_addBuildingAMS(self):

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
        deviceList.clickAddHamburger()

        addHamburger = DeviceAddHamburger(self.driver, self.wait)
        assert addHamburger.visibilityOfAddHamburgerMenu() is True
        addHamburger.clickAddBuilding()

        addBuildingPop = AddBuildingPopup(self.driver, self.wait)
        assert addBuildingPop.visibilityOfAddBuilding() is True
        addBuildingPop.createBuilding("AAA AMS B1")
        time.sleep(1)

        expected_bName = "AAA AMS B1"
        actual_bName = deviceList.passBuildingName()

        assert expected_bName == actual_bName



