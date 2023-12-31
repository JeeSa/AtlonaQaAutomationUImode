import time

import pytest

from pages.velocity.sites.Buildings_Page import BuildingsPage
from pages.velocity.Home_Page import HomePage
from pages.velocity.menus.FloorHamburger_Menu import FloorHamburgerMenu
from pages.velocity.sites.RoomList_Page import RoomListPage
from pages.velocity.sites.RoomModifyDevices_Page import RoomModifyDevicesPage
from pages.velocity.sites.RoomModify_Page import RoomModifyPage
from pages.velocity.sites.Sites_Page import SitesPage
from pages.velocity.sites.TechnologyList_Page import TechnologyListPage
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestAddMeetingRoomWithCaInt:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.driver, self.wait)
        self.home = HomePage(self.driver, self.wait)
        self.sites = SitesPage(self.driver, self.wait)
        self.buildings = BuildingsPage(self.driver, self.wait)
        self.roomList = RoomListPage(self.driver, self.wait)
        self.flrHamburger = FloorHamburgerMenu(self.driver, self.wait)
        self.modRoom = RoomModifyPage(self.driver, self.wait)
        self.modifyDevices = RoomModifyDevicesPage(self.driver, self.wait)
        self.techList = TechnologyListPage(self.driver, self.wait)

    def test_addMeetingRoomWithCaInt(self):

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

        # Click on the more option button
        self.roomList.clickMoreButton1()
        time.sleep(2)
        # Click on the add new room option
        self.flrHamburger.clickAddMeetingRoom()
        time.sleep(1)
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Room Modify"))
        assert "Atlona Velocity | Room Modify" in self.driver.title
        self.modRoom.createMeetingRoom("New Test Meeting Room")
        time.sleep(1)
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Room List"))
        assert "Atlona Velocity | Room List" in self.driver.title

        # Click on the edit technology button
        self.roomList.clickEditTechnology1Button()
        # wait until the  page is loaded successfully
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
        assert self.modifyDevices.visibilityOfVTPDevice() is True


