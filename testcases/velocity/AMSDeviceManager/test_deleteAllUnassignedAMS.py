import time

import pytest

from pages.velocity.DeviceList_Page import DeviceListPage
from pages.velocity.Home_Page import HomePage
from pages.velocity.menus.DeviceToolsHamburger import DeviceToolsHamburger
from pages.velocity.menus.LeftBarMenu import LeftBarMenu
from pages.velocity.popups.DeleteAllUnassigned import DeleteAllUnassignedPopup
from pages.velocity.popups.DeviceListSettings_popup import DeviceListSettingsPopup
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestDeleteAllUnassignedAMS:
    def test_delete_allUnassignedAMS(self):

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

        beforeDeleteCount = deviceList.totalRowCount()

        deviceList.clickToolsHamburger()

        toolsHamburger = DeviceToolsHamburger(self.driver, self.wait)
        assert toolsHamburger.visibilityOfToolsHamburgerMenu() is True

        toolsHamburger.clickDeleteAllUnassigned()

        deleteAllunassignedPop = DeleteAllUnassignedPopup(self.driver, self.wait)
        assert deleteAllunassignedPop.visibilityOfDeleteAllUnassignedPop() is True

        deleteAllunassignedPop.clickDelete()
        time.sleep(5)

        afterDeleteCount = deviceList.totalRowCount()

        assert beforeDeleteCount != afterDeleteCount











