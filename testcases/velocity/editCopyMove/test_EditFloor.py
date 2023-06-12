import time

import pytest

from pages.velocity.Home_Page import HomePage
from pages.velocity.sites.Buildings_Page import BuildingsPage
from pages.velocity.sites.EditFloor_Page import EditFloorPage
from pages.velocity.menus.FloorHamburger_Menu import FloorHamburgerMenu
from pages.velocity.sites.RoomList_Page import RoomListPage
from pages.velocity.sites.Sites_Page import SitesPage
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestEditFloor:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.driver, self.wait)
        self.home = HomePage(self.driver, self.wait)
        self.sites = SitesPage(self.driver, self.wait)
        self.buildings = BuildingsPage(self.driver, self.wait)
        self.roomList = RoomListPage(self.driver, self.wait)
        self.flrHamburger = FloorHamburgerMenu(self.driver, self.wait)
        self.editFlr = EditFloorPage(self.driver, self.wait)

    def test_EditFloor(self):

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
        time.sleep(1)
        # Click on the edit floor option
        self.flrHamburger.clickEditFloor()
        # Verify if the added room is visible
        assert self.editFlr.visibilityOfEditFloorPage() is True

        expected_fName = "Edited Floor Name"
        self.editFlr.clearFloorName()
        self.editFlr.enterFloorName(expected_fName)
        self.editFlr.clickSubmitButton()
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Room List"))
        assert "Atlona Velocity | Room List" in self.driver.title
        time.sleep(1)
        actual_fName = self.roomList.passFloorName()
        # Check that the edited name is showing after editing
        assert expected_fName == actual_fName



