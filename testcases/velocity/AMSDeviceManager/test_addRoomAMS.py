import time

import pytest

from pages.velocity.DeviceList_Page import DeviceListPage
from pages.velocity.Home_Page import HomePage
from pages.velocity.menus.DeviceAddHamburger_Menu import DeviceAddHamburger
from pages.velocity.menus.LeftBar_Menu import LeftBarMenu
from pages.velocity.popups.AddRoom_popup import AddRoomPopup
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestAddRoomAMS:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.driver, self.wait)
        self.home = HomePage(self.driver, self.wait)
        self.leftNav = LeftBarMenu(self.driver, self.wait)
        self.deviceList = DeviceListPage(self.driver, self.wait)
        self.addHamburger = DeviceAddHamburger(self.driver, self.wait)
        self.addRoomPop = AddRoomPopup(self.driver, self.wait)

    def test_addRoomAMS(self):

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
        self.addHamburger.clickAddRoom()
        assert self.addRoomPop.visibilityOfAddRoom() is True
        self.addRoomPop.createRoom("AAA AMS R1")
        time.sleep(1)
        self.deviceList.clickExpandBuilding()

        expected_rName = "AAA AMS R1"
        actual_rName = self.deviceList.passRoomName()
        assert expected_rName == actual_rName

