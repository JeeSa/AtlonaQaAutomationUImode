import time

import pytest

from pages.velocity.Home_Page import HomePage
from pages.velocity.popups.Confirm_popup import ConfirmPopup
from pages.velocity.sites.AddRoom_Page import AddRoomPage
from pages.velocity.sites.Buildings_Page import BuildingsPage
from pages.velocity.sites.FloorHamburger_Menu import FloorHamburgerMenu
from pages.velocity.sites.RoomList_Page import RoomListPage
from pages.velocity.sites.RoomModifyDevices_Page import RoomModifyDevicesPage
from pages.velocity.sites.Sites_Page import SitesPage
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestDeleteRoom:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.driver, self.wait)
        self.home = HomePage(self.driver, self.wait)
        self.sites = SitesPage(self.driver, self.wait)
        self.buildings = BuildingsPage(self.driver, self.wait)
        self.roomList = RoomListPage(self.driver, self.wait)
        self.flrHamburger = FloorHamburgerMenu(self.driver, self.wait)
        self.addRoom = AddRoomPage(self.driver, self.wait)
        self.modifyDevices = RoomModifyDevicesPage(self.driver, self.wait)
        self.confirm = ConfirmPopup(self.driver, self.wait)

    def test_deleteRoom(self):

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
        self.flrHamburger.clickAddRoom()
        time.sleep(1)
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Room Modify"))
        assert "Atlona Velocity | Room Modify" in self.driver.title

        # Add a new room
        self.addRoom.createRoom("New Test Room")
        time.sleep(1)
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Room Modify Devices"))
        assert "Atlona Velocity | Room Modify Devices" in self.driver.title

        self.modifyDevices.clickBuildingInBreadcrumb()
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Room List"))
        assert "Atlona Velocity | Room List" in self.driver.title
        # Verify if the added room is visible
        assert self.roomList.visibilityOfRoom2() is True

        # Delete the newly added room
        self.roomList.clickDeleteBtnRoom2()
        # Verify if the confirmation popup is visible
        assert self.confirm.visibilityOfConfirmPopup() is True
        self.confirm.clickSubmit()
        time.sleep(1)
        # Verify if the delete success popup is visible
        assert self.roomList.visibilityOfDeleteSuccessPopup() is True




