import time

import pytest

from pages.velocity.DeviceList_Page import DeviceListPage
from pages.velocity.Home_Page import HomePage
from pages.velocity.menus.DeviceAddHamburger_Menu import DeviceAddHamburger
from pages.velocity.menus.LeftBarMenu import LeftBarMenu
from pages.velocity.popups.AddSite_popup import AddSitePopup
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestAddSiteEmptyGateway:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.driver, self.wait)
        self.home = HomePage(self.driver, self.wait)
        self.leftNav = LeftBarMenu(self.driver, self.wait)
        self.deviceList = DeviceListPage(self.driver, self.wait)
        self.addHamburger = DeviceAddHamburger(self.driver, self.wait)
        self.addSitePop = AddSitePopup(self.driver, self.wait)

    def test_addSite_emptyGateway(self):

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
        self.addHamburger.clickAddSite()
        assert self.addSitePop.visibilityOfAddSitePage() is True
        self.addSitePop.createSiteAMS("Atlona", "Atlona Incorporated", "70 Daggett Drive", "San Jose", "95134")
        time.sleep(1)

        expected_sName = "Atlona"
        actual_sName = self.deviceList.passSiteName()
        assert expected_sName == actual_sName
