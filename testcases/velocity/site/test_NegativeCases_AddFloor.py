import time

import pytest

from pages.velocity.sites.AddFloor_Page import AddNewFloorPage
from pages.velocity.sites.Buildings_Page import BuildingsPage
from pages.velocity.Home_Page import HomePage
from pages.velocity.menus.FloorHamburger_Menu import FloorHamburgerMenu
from pages.velocity.sites.RoomList_Page import RoomListPage
from pages.velocity.sites.Sites_Page import SitesPage
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestNegativeCasesAddFloor:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.driver, self.wait)
        self.home = HomePage(self.driver, self.wait)
        self.sites = SitesPage(self.driver, self.wait)
        self.buildings = BuildingsPage(self.driver, self.wait)
        self.roomList = RoomListPage(self.driver, self.wait)
        self.flrHamburger = FloorHamburgerMenu(self.driver, self.wait)
        self.addFloor = AddNewFloorPage(self.driver, self.wait)


    def test_negativeCases_addFloor_01(self):
        # Case 1: Hit the Submit button when the floor name field is blank

        # Login to the velocity app
        self.ut.login()
        # Navigate to sites page
        self.home.navToSitesPage()
        # Navigate to Buildings Page
        self.sites.navToBuildingsPage()
        # Navigate to Room list page of 1st Building
        self.buildings.navToRoomListOfBuilding1()

        # Click on the more option button
        self.roomList.clickMoreButton1()
        time.sleep(1)
        # Click on the add new floor option
        self.flrHamburger.clickAddNewFloor()
        # Clear floor name
        self.addFloor.clearFloorName()
        self.addFloor.clickSubmitButton()
        time.sleep(1)
        # Verify if the add floor page is visible
        assert self.addFloor.visibilityOfAddFloorPage() is True

    def test_negativeCases_addFloor_02(self):
        # Case 2: Hit the Submit button when the floor count field is blank

        # Verify if the add floor page is visible
        assert self.addFloor.visibilityOfAddFloorPage() is True
        # Toggle to add multiple floors
        self.addFloor.clickToggleButton()
        # Clear default floor count
        self.addFloor.clearFloorCount()
        # Click on the submit button
        self.addFloor.clickSubmitButton()
        time.sleep(1)
        # Verify if the add floor page is visible
        assert self.addFloor.visibilityOfAddFloorPage() is True

    def test_negativeCases_addFloor_03(self):
        # Case 3: Hit the Submit button when the floor count is less than 1 (any value less than the minimum value from the mentioned range in the error message)

        # Verify if the add floor page is visible
        assert self.addFloor.visibilityOfAddFloorPage() is True
        # Clear default floor count
        self.addFloor.clearFloorCount()
        # Enter any value less than the minimum value from the mentioned range in the error message
        self.addFloor.enterFloorCount(0)
        # Click on the submit button
        self.addFloor.clickSubmitButton()
        time.sleep(1)
        # Verify if the add floor page is visible
        assert self.addFloor.visibilityOfAddFloorPage() is True

    def test_negativeCases_addFloor_04(self):
        # Case 4: Hit the Submit button when the floor count is more than 50 (any value more than the maximum value from the mentioned range in the error message)

        # Verify if the add floor page is visible
        assert self.addFloor.visibilityOfAddFloorPage() is True
        # Clear default floor count
        self.addFloor.clearFloorCount()
        # Enter any value more than the maximum value from the mentioned range in the error message
        self.addFloor.enterFloorCount(51)
        # Click on the submit button
        self.addFloor.clickSubmitButton()
        time.sleep(1)
        # Verify if the add floor page is visible
        assert self.addFloor.visibilityOfAddFloorPage() is True
