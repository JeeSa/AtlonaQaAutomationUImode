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
class TestResetDeviceListAMS:
    def test_reset_deviceListAMS(self):
        # Case 1: using the cross icon

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

        defaultHeaders = ['', 'Status\narrow_drop_down', 'Category\narrow_drop_down', 'Title\narrow_drop_down', 'IP Address\narrow_drop_down', 'MAC Address\narrow_drop_down', 'Version\narrow_drop_down', 'Site\narrow_drop_down', 'Building\narrow_drop_down', 'Room\narrow_drop_down']

        deviceList.clickToolsHamburger()

        toolsHamburger = DeviceToolsHamburger(self.driver, self.wait)
        assert toolsHamburger.visibilityOfToolsHamburgerMenu() is True

        toolsHamburger.clickDeviceListSettings()

        deviceListSettingsPop = DeviceListSettingsPopup(self.driver, self.wait)
        assert deviceListSettingsPop.visibilityOfDeviceListSettingsPop() is True

        deviceListSettingsPop.clickReset()
        deviceListSettingsPop.clickSave()
        time.sleep(1)

        resetedHeaders = deviceList.passTableHeader()

        assert defaultHeaders == resetedHeaders











