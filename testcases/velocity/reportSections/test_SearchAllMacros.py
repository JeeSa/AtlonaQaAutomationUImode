import time

import pytest

from pages.velocity.Home_Page import HomePage
from pages.velocity.menus.LeftBarMenu import LeftBarMenu
from pages.velocity.reportSections.AllMacros_Page import AllMacrosPage
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestSearchAllMacros:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.driver, self.wait)
        self.home = HomePage(self.driver, self.wait)
        self.leftNav = LeftBarMenu(self.driver, self.wait)
        self.allMacros = AllMacrosPage(self.driver, self.wait)

    def test_SearchAllMacros(self):

        # Login to the velocity app
        self.ut.login()
        self.home.clickNavBar()
        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        self.leftNav.clickReports()
        self.leftNav.clickRep_allMacros()
        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("All Macros"))
        assert "Atlona Velocity | All Macros" in self.driver.title

        rowCountwithString = self.allMacros.rowCountWithString()
        time.sleep(1)
        self.allMacros.enterSearchContent("RoomOn")
        self.allMacros.clickSearchButton()
        time.sleep(1)
        resultedRowCount = self.allMacros.totalRowCount()
        time.sleep(1)
        assert rowCountwithString == resultedRowCount



