import time

import pytest

from pages.velocity.DeviceList_Page import DeviceListPage
from pages.velocity.Home_Page import HomePage
from pages.velocity.menus.LeftBar_Menu import LeftBarMenu
from pages.velocity.popups.CopyBuildingAMS_popup import CopyBuildingPopup
from pages.velocity.popups.EditBuildingAMS_popup import EditBuildingPopup
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestCopyBuildingAMS:
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.driver, self.wait)
        self.home = HomePage(self.driver, self.wait)
        self.leftNav = LeftBarMenu(self.driver, self.wait)
        self.deviceList = DeviceListPage(self.driver, self.wait)
        self.editBuildingPopup = EditBuildingPopup(self.driver, self.wait)
        self.copyBuildingPopup = CopyBuildingPopup(self.driver, self.wait)

    def test_copyBuildingAMS(self):

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

        self.deviceList.hoverBuildingDiv1()
        self.deviceList.clickSettingsB1()
        assert self.editBuildingPopup.visibilityOfEditBuilding()
        self.editBuildingPopup.clickCopy()
        time.sleep(1)
        assert self.copyBuildingPopup.visibilityOfCopyBuilding()

        expected_bName = "AAA AMS B1 Copy"
        self.copyBuildingPopup.enterBuildingName(expected_bName)
        self.copyBuildingPopup.clickSiteDropdown()
        self.copyBuildingPopup.clickSiteValue()
        self.copyBuildingPopup.clickCopy()
        time.sleep(1)
        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("Atlona Devices"))
        assert "Atlona Velocity | Atlona Devices" in self.driver.title
        time.sleep(1)
        actual_bName = self.deviceList.passBuildingName2()
        assert expected_bName == actual_bName

