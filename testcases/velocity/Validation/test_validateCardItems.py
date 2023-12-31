import pytest

from pages.velocity.Home_Page import HomePage
from pages.velocity.sites.Buildings_Page import BuildingsPage
from pages.velocity.sites.RoomList_Page import RoomListPage
from pages.velocity.sites.Sites_Page import SitesPage
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestValidateCardItems:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.driver, self.wait)
        self.home = HomePage(self.driver, self.wait)
        self.sites = SitesPage(self.driver, self.wait)
        self.buildings = BuildingsPage(self.driver, self.wait)
        self.roomList = RoomListPage(self.driver, self.wait)

    def test_validateSiteCardItems(self):
        # Case 1: Validate the Site card items are visible properly

        # Login to the velocity app
        self.ut.login()
        # Navigate to sites page
        self.home.navToSitesPage()

        # Verify if the added technology is visible
        assert self.sites.visibilityOfViewButton() is True
        # Verify if the added technology is visible
        assert self.sites.visibilityOfAddBuildingButton() is True
        # Verify if the added technology is visible
        assert self.sites.visibilityOfDeleteButton() is True
        # Verify if the added technology is visible
        assert self.sites.visibilityOfExportButton() is True
        # Verify if the added technology is visible
        assert self.sites.visibilityOfEditButton() is True

    def test_validateBuildingCardItems(self):
        # Case 2: Validate the Building card items are visible properly

        assert "Atlona Velocity | Sites" in self.driver.title
        # Navigate to Buildings Page
        self.sites.navToBuildingsPage()

        # Verify if the added technology is visible
        assert self.buildings.visibilityOfViewRooms1Button() is True
        # Verify if the added technology is visible
        assert self.buildings.visibilityOfEditBuilding1Button() is True
        # Verify if the added technology is visible
        assert self.buildings.visibilityOfCopyBuilding1Button() is True
        # Verify if the added technology is visible
        assert self.buildings.visibilityOfExportBuilding1Button() is True
        # Verify if the added technology is visible
        assert self.buildings.visibilityOfDeleteBuilding1Button() is True

    def test_validateRoomCardItems(self):
        # Case 3: Validate the Room card items are visible properly

        # Navigate to Room list page of 1st Building
        self.buildings.navToRoomListOfBuilding1()

        # Verify if the added technology is visible
        assert self.roomList.visibilityOfControlRoom1Button() is True
        # Verify if the added technology is visible
        assert self.roomList.visibilityOfEditTechnology1Button() is True
        # Verify if the added technology is visible
        assert self.roomList.visibilityOfEditRoom1Button() is True
        # Verify if the added technology is visible
        assert self.roomList.visibilityOfCopyRoom1Button() is True
        # Verify if the added technology is visible
        assert self.roomList.visibilityOfDeleteRoom1Button() is True
        # Verify if the added technology is visible
        assert self.roomList.visibilityOfExportRoom1Button() is True

