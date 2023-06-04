import time

import pytest

from pages.velocity.DeviceList_Page import DeviceListPage
from pages.velocity.Home_Page import HomePage
from pages.velocity.menus.DeviceAddHamburger_Menu import DeviceAddHamburger
from pages.velocity.menus.LeftBarMenu import LeftBarMenu
from pages.velocity.popups.AddBuilding_popup import AddBuildingPopup
from pages.velocity.popups.CopyBuildingAMS_popup import CopyBuildingPopup
from pages.velocity.popups.EditBuildingAMS_popup import EditBuildingPopup
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestCopyBuildingAMS:
    def test_copyBuildingAMS(self):

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

        deviceList.hoverBuildingDiv1()
        deviceList.clickSettingsB1()

        editBuildingPopup = EditBuildingPopup(self.driver, self.wait)

        assert editBuildingPopup.visibilityOfEditBuilding()

        editBuildingPopup.clickCopy()

        copyBuildingPopup = CopyBuildingPopup(self.driver, self.wait)

        assert copyBuildingPopup.visibilityOfCopyBuilding()

        expected_bName = "AAA AMS B1 Copy"

        copyBuildingPopup.enterBuildingName(expected_bName)
        copyBuildingPopup.clickSiteDropdown()
        copyBuildingPopup.clickSiteValue()
        copyBuildingPopup.clickCopy()

        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("Atlona Devices"))

        assert "Atlona Velocity | Atlona Devices" in self.driver.title
        time.sleep(1)

        actual_bName = deviceList.passBuildingName2()

        assert expected_bName == actual_bName


