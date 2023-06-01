import time

import pytest

from pages.velocity.Home_Page import HomePage
from pages.velocity.menus.LeftBarMenu import LeftBarMenu
from pages.velocity.reportSections.AllDevices_Page import AllDevicesPage
from pages.velocity.reportSections.BillOfMaterials import BillOfMaterialsPage
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestViewDevices:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.driver, self.wait)
        self.home = HomePage(self.driver, self.wait)
        self.leftNav = LeftBarMenu(self.driver, self.wait)
        self.allDevice = AllDevicesPage(self.driver, self.wait)
        self.billOfMaterials = BillOfMaterialsPage(self.driver, self.wait)

    def test_ViewDevices(self):

        # Login to the velocity app
        self.ut.login()
        self.home.clickNavBar()
        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        self.leftNav.clickReports()
        self.leftNav.clickRep_billOfMaterials()
        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("Bill Of Materials"))
        assert "Atlona Velocity | Bill Of Materials" in self.driver.title

        # Store the ID of the original window
        main_window = self.driver.current_window_handle
        # Check we don't have other windows open already
        assert len(self.driver.window_handles) == 1
        # Click on the Login help
        self.billOfMaterials.clickViewButton()
        # Wait for the new window or tab
        self.wait.until(EC.number_of_windows_to_be(2))

        all_windows = self.driver.window_handles
        for new_window in all_windows:
            if new_window != main_window:
                self.driver.switch_to.window(new_window)
                # wait until the destination page is loaded successfully
                self.wait.until(EC.url_contains("https://atlona.com/product"))
                time.sleep(1)
                self.driver.close()
                break

        self.driver.switch_to.window(main_window)
        # Check we don't have other windows open anymore
        assert len(self.driver.window_handles) == 1



