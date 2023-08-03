import time

import pytest

from pages.velocity.Home_Page import HomePage
from pages.velocity.menus.LeftBar_Menu import LeftBarMenu
from pages.velocity.reportSections.AllDevices_Page import AllDevicesPage
from pages.velocity.reportSections.AllMacros_Page import AllMacrosPage
from pages.velocity.reportSections.BillOfMaterials import BillOfMaterialsPage
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestClearSearch:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.driver, self.wait)
        self.home = HomePage(self.driver, self.wait)
        self.leftNav = LeftBarMenu(self.driver, self.wait)
        self.allDevice = AllDevicesPage(self.driver, self.wait)
        self.allMacros = AllMacrosPage(self.driver, self.wait)
        self.billOfMaterials = BillOfMaterialsPage(self.driver, self.wait)

    def test_CloseReports_AllDevices(self):

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

        self.allDevice.clickCloseButton()
        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("Room List"))
        assert "Atlona Velocity | Room List" in self.driver.title

    def test_CloseReports_AllMacros(self):

        self.home.clickNavBar()
        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        self.leftNav.clickReports()
        self.leftNav.clickRep_allMacros()
        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("All Macros"))
        assert "Atlona Velocity | All Macros" in self.driver.title

        self.allMacros.clickCloseButton()
        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("Room List"))
        assert "Atlona Velocity | Room List" in self.driver.title

    def test_CloseReports_BillOfMaterials(self):

        self.home.clickNavBar()
        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        self.leftNav.clickReports()
        self.leftNav.clickRep_billOfMaterials()
        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("Bill Of Materials"))
        assert "Atlona Velocity | Bill Of Materials" in self.driver.title

        self.billOfMaterials.clickCloseButton()
        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("Room List"))
        assert "Atlona Velocity | Room List" in self.driver.title

