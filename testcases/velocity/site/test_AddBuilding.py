import time
import pytest

from pages.velocity.Home_Page import HomePage
from pages.velocity.sites.Buildings_Page import BuildingsPage
from pages.velocity.sites.RoomList_Page import RoomListPage
from pages.velocity.sites.Sites_Page import SitesPage
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestAddBuilding:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.driver, self.wait)
        self.home = HomePage(self.driver, self.wait)
        self.sites = SitesPage(self.driver, self.wait)
        self.buildings = BuildingsPage(self.driver, self.wait)
        self.roomList = RoomListPage(self.driver, self.wait)

    def test_addBuilding1(self):

        # Login to the velocity app
        self.ut.login()
        # Navigate to sites page
        self.home.navToSitesPage()
        # Navigate to Add building page from the sites page
        self.sites.navToAddBuildingPageFromSitesPage()

        # Create new building
        self.ut.addBuilding("EMEA HQ", "Atlona International AG", "Tödistrasse 18, 8002 Zürich, Switzerland")

        # Navigate to Buildings Page
        self.sites.navToBuildingsPage()
        # Navigate to Room list page of 2nd Building
        self.buildings.navToRoomListOfBuilding1()
        # Navigate to Room Modify Device page of 1st Floor and 1st Room
        self.roomList.navToRModDevOfF1R1()

    def test_addBuilding2(self):

        # Navigate to sites page
        self.home.navToDashboard()
        # Navigate to sites page
        self.home.navToSitesPage()
        # Navigate to Buildings Page
        self.sites.navToBuildingsPage()

        # Provide all data to create building
        self.ut.addBuildingViaForm("EMEA HQ 2", "Atlona International AG 2", "Tödistrasse 18, 8002 Zürich, Switzerland")

        # Navigate to Room list page of 2nd Building
        self.buildings.navToRoomListOfBuilding3()
        # Navigate to Room Modify Device page of 1st Floor and 1st Room
        self.roomList.navToRModDevOfF1R1()
