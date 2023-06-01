import time

import pytest

from pages.velocity.sites.Buildings_Page import BuildingsPage
from pages.velocity.Home_Page import HomePage
from pages.velocity.sites.ConfigureEquipment_Page import ConfigureEquipmentPage
from pages.velocity.sites.RoomList_Page import RoomListPage
from pages.velocity.sites.RoomModifyDevices_Page import RoomModifyDevicesPage
from pages.velocity.sites.Sites_Page import SitesPage
from pages.velocity.sites.TechnologyList_Page import TechnologyListPage
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestEditRoomDevice:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.driver, self.wait)
        self.home = HomePage(self.driver, self.wait)
        self.sites = SitesPage(self.driver, self.wait)
        self.buildings = BuildingsPage(self.driver, self.wait)
        self.roomList = RoomListPage(self.driver, self.wait)
        self.modifyDevices = RoomModifyDevicesPage(self.driver, self.wait)
        self.techList = TechnologyListPage(self.driver, self.wait)
        self.confEquip = ConfigureEquipmentPage(self.driver, self.wait)

    def test_editRoomDevice(self):

        # Login to the velocity app
        self.ut.login()
        # Click on the created site
        self.home.clickSite()
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Sites"))
        assert "Atlona Velocity | Sites" in self.driver.title

        # Click on the view button
        self.sites.clickView()
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Buildings"))
        assert "Atlona Velocity | Buildings" in self.driver.title
        # Click on the view button
        self.buildings.clickViewAllRooms1()
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Room List"))
        assert "Atlona Velocity | Room List" in self.driver.title

        # Click on the edit technology button of room 1
        self.roomList.clickEditTechnology1Button()
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Room Modify Devices"))
        assert "Atlona Velocity | Room Modify Devices" in self.driver.title

        # Click on the add technology button
        self.modifyDevices.clickAddTechnologyButton()
        # Search for a product and add that to the device list
        self.techList.addDevice("AT-VTP-800-BL")
        # Click on the close button
        self.techList.clickCloseList()
        time.sleep(2)
        # Verify if the added technology is visible
        assert self.modifyDevices.visibilityOfDevice_1() is True
        # Click on the edit device option
        self.modifyDevices.clickEditDevice()
        time.sleep(1)
        # Verify if the added technology is visible
        assert self.confEquip.visibilityOfConfHeading() is True

        expected_dName = "VTP-800_Black_Left"
        # Edit device alias
        self.confEquip.clearAlias()
        self.confEquip.enterAlias(expected_dName)
        self.confEquip.clickSave()
        time.sleep(1)
        actual_dName = self.modifyDevices.passDeviceName()
        # Check that the edited name is showing after editing
        assert expected_dName == actual_dName



