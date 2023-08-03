import time

import pytest

from pages.velocity.DeviceList_Page import DeviceListPage
from pages.velocity.Home_Page import HomePage
from pages.velocity.menus.DeviceToolsHamburger_Menu import DeviceToolsHamburger
from pages.velocity.menus.LeftBar_Menu import LeftBarMenu
from pages.velocity.popups.DeviceListSettings_popup import DeviceListSettingsPopup
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestUpdateDeviceListAMS:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.driver, self.wait)
        self.home = HomePage(self.driver, self.wait)
        self.leftNav = LeftBarMenu(self.driver, self.wait)
        self.deviceList = DeviceListPage(self.driver, self.wait)
        self.toolsHamburger = DeviceToolsHamburger(self.driver, self.wait)
        self.deviceListSettingsPop = DeviceListSettingsPopup(self.driver, self.wait)

    def test_update_deviceListAMS(self):

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

        initialHeaders = self.deviceList.passTableHeader()
        self.deviceList.clickToolsHamburger()
        assert self.toolsHamburger.visibilityOfToolsHamburgerMenu() is True
        self.toolsHamburger.clickDeviceListSettings()
        assert self.deviceListSettingsPop.visibilityOfDeviceListSettingsPop() is True

        self.deviceListSettingsPop.clickFirmwareVersion()
        self.deviceListSettingsPop.clickModel()
        self.deviceListSettingsPop.clickSave()
        time.sleep(1)
        updatedHeaders = self.deviceList.passTableHeader()
        assert initialHeaders != updatedHeaders
