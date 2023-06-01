import time

import pytest

from pages.velocity.Home_Page import HomePage
from pages.velocity.menus.LeftBarMenu import LeftBarMenu
from pages.velocity.reportSections.AllDevices_Page import AllDevicesPage
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestEditDevices:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.driver, self.wait)
        self.home = HomePage(self.driver, self.wait)
        self.leftNav = LeftBarMenu(self.driver, self.wait)
        self.allDevice = AllDevicesPage(self.driver, self.wait)

    def test_EditDevices(self):

        # Login to the velocity app
        self.ut.login()
        self.home.clickNavBar()
        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        self.leftNav.clickReports()
        self.leftNav.clickRep_allDevices()
        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("All Devices"))
        assert "Atlona Velocity | All Devices" in self.driver.title

        parameter = "192.110.173.90"
        self.allDevice.clickEditButton()
        self.allDevice.clearIp()
        self.allDevice.enterIp(parameter)
        self.allDevice.clickSave()
        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("All Devices"))
        assert "Atlona Velocity | All Devices" in self.driver.title
        newIP = self.allDevice.passIpAddress()
        assert newIP == parameter

