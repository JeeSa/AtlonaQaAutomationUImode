import time

import pytest

from pages.velocity.Home_Page import HomePage
from pages.velocity.popups.Confirm_popup import ConfirmPopup
from pages.velocity.sites.Buildings_Page import BuildingsPage
from pages.velocity.menus.FloorHamburger_Menu import FloorHamburgerMenu
from pages.velocity.sites.RoomList_Page import RoomListPage
from pages.velocity.sites.Sites_Page import SitesPage
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestDeleteFloor:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.driver, self.wait)
        self.home = HomePage(self.driver, self.wait)
        self.sites = SitesPage(self.driver, self.wait)
        self.buildings = BuildingsPage(self.driver, self.wait)
        self.roomList = RoomListPage(self.driver, self.wait)
        self.flrHamburger = FloorHamburgerMenu(self.driver, self.wait)
        self.confirm = ConfirmPopup(self.driver, self.wait)

    def test_DeleteFloor(self):

        # Login to the velocity app
        self.ut.login()
        # Navigate to sites page
        self.home.navToSitesPage()
        # Navigate to Buildings Page
        self.sites.navToBuildingsPage()
        # Navigate to Room list page of 1st Building
        self.buildings.navToRoomListOfBuilding1()
        # Copy building
        self.ut.copyFloor()
        # Delete Building
        self.ut.deleteFloor()


