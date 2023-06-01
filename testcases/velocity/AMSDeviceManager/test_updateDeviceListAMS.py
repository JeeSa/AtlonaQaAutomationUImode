import time

import pytest

from pages.velocity.DeviceList_Page import DeviceListPage
from pages.velocity.Home_Page import HomePage
from pages.velocity.menus.DeviceToolsHamburger import DeviceToolsHamburger
from pages.velocity.menus.LeftBarMenu import LeftBarMenu
from pages.velocity.popups.DeviceListSettings_popup import DeviceListSettingsPopup
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestUpdateDeviceListAMS:
    def test_update_deviceListAMS(self):

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

        initialHeaders = deviceList.passTableHeader()

        #print(initialHeaders)

        deviceList.clickToolsHamburger()

        toolsHamburger = DeviceToolsHamburger(self.driver, self.wait)
        assert toolsHamburger.visibilityOfToolsHamburgerMenu() is True

        toolsHamburger.clickDeviceListSettings()

        deviceListSettingsPop = DeviceListSettingsPopup(self.driver, self.wait)
        assert deviceListSettingsPop.visibilityOfDeviceListSettingsPop() is True

        deviceListSettingsPop.clickFirmwareVersion()
        deviceListSettingsPop.clickModel()
        deviceListSettingsPop.clickSave()
        time.sleep(1)

        updatedHeaders = deviceList.passTableHeader()

        #print(updatedHeaders)

        assert initialHeaders != updatedHeaders











