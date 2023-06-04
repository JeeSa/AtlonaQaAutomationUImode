import time

import pytest

from pages.velocity.DeviceList_Page import DeviceListPage
from pages.velocity.Home_Page import HomePage
from pages.velocity.menus.LeftBarMenu import LeftBarMenu
from pages.velocity.popups.EditSiteAMS_popup import EditSitePopup
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestEditSiteAMS:
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.driver, self.wait)
        self.home = HomePage(self.driver, self.wait)
        self.leftNav = LeftBarMenu(self.driver, self.wait)
        self.deviceList = DeviceListPage(self.driver, self.wait)
        self.editSitePopup = EditSitePopup(self.driver, self.wait)

    def test_editSiteAMS(self):
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

        self.deviceList.hoverSiteDiv()
        self.deviceList.clickSettingsS()
        assert self.editSitePopup.visibilityOfEditSitePage()

        expected_sName = "Atlona Edited"
        self.editSitePopup.clearSiteName()
        self.editSitePopup.enterSiteName(expected_sName)
        self.editSitePopup.clickSubmit()
        time.sleep(1)
        actual_sName = self.deviceList.passSiteName()
        assert expected_sName == actual_sName


