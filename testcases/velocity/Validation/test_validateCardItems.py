import pytest

from pages.velocity.Home_Page import HomePage
from pages.velocity.sites.Buildings_Page import BuildingsPage
from pages.velocity.sites.RoomList_Page import RoomListPage
from pages.velocity.sites.Sites_Page import SitesPage
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestValidateCardItems:
    def test_validateSiteCardItems(self):
        # Case 1: Validate the Site card items are visible properly

        # Login to the velocity app
        ut = Utils(self.driver, self.wait)
        ut.login()

        homePage = HomePage(self.driver, self.wait)

        # Click on the created site
        homePage.clickSite()

        # wait until the sites page is loaded successfully
        self.wait.until(EC.title_contains("Sites"))

        assert "Atlona Velocity | Sites" in self.driver.title

        sites = SitesPage(self.driver, self.wait)

        # Verify if the added technology is visible
        assert sites.visibilityOfViewButton() is True

        # Verify if the added technology is visible
        assert sites.visibilityOfAddBuildingButton() is True

        # Verify if the added technology is visible
        assert sites.visibilityOfDeleteButton() is True

        # Verify if the added technology is visible
        assert sites.visibilityOfExportButton() is True

        # Verify if the added technology is visible
        assert sites.visibilityOfEditButton() is True

    def test_validateBuildingCardItems(self):
        # Case 2: Validate the Building card items are visible properly

        assert "Atlona Velocity | Sites" in self.driver.title

        sites = SitesPage(self.driver, self.wait)

        # Click on the view button
        sites.clickView()

        # wait until the buildings page is loaded successfully
        self.wait.until(EC.title_contains("Buildings"))

        assert "Atlona Velocity | Buildings" in self.driver.title

        buildings = BuildingsPage(self.driver, self.wait)

        # Verify if the added technology is visible
        assert buildings.visibilityOfViewRooms1Button() is True

        # Verify if the added technology is visible
        assert buildings.visibilityOfEditBuilding1Button() is True

        # Verify if the added technology is visible
        assert buildings.visibilityOfCopyBuilding1Button() is True

        # Verify if the added technology is visible
        assert buildings.visibilityOfExportBuilding1Button() is True

        # Verify if the added technology is visible
        assert buildings.visibilityOfDeleteBuilding1Button() is True

    def test_validateRoomCardItems(self):
        # Case 3: Validate the Room card items are visible properly

        assert "Atlona Velocity | Buildings" in self.driver.title

        buildings = BuildingsPage(self.driver, self.wait)

        # Click on the view button
        buildings.clickViewAllRooms1()

        # wait until the room list page is loaded successfully
        self.wait.until(EC.title_contains("Room List"))

        assert "Atlona Velocity | Room List" in self.driver.title

        roomList = RoomListPage(self.driver, self.wait)

        # Verify if the added technology is visible
        assert roomList.visibilityOfControlRoom1Button() is True

        # Verify if the added technology is visible
        assert roomList.visibilityOfEditTechnology1Button() is True

        # Verify if the added technology is visible
        assert roomList.visibilityOfEditRoom1Button() is True

        # Verify if the added technology is visible
        assert roomList.visibilityOfCopyRoom1Button() is True

        # Verify if the added technology is visible
        assert roomList.visibilityOfDeleteRoom1Button() is True

        # Verify if the added technology is visible
        assert roomList.visibilityOfExportRoom1Button() is True









