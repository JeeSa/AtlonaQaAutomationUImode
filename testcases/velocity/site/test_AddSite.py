import time
import pytest

from pages.velocity.Home_Page import HomePage
from pages.velocity.sites.Buildings_Page import BuildingsPage
from pages.velocity.sites.RoomList_Page import RoomListPage
from pages.velocity.sites.Sites_Page import SitesPage
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestAddSite:
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.driver, self.wait)
        self.home = HomePage(self.driver, self.wait)
        self.sites = SitesPage(self.driver, self.wait)
        self.buildings = BuildingsPage(self.driver, self.wait)
        self.roomList = RoomListPage(self.driver, self.wait)


    def test_addSite(self):

        # Login to the velocity app
        self.ut.login()
        # Refresh the page
        self.driver.refresh()
        time.sleep(1)
        # Create a new site
        self.ut.addSite("Atlona", "Atlona Incorporated", "70 Daggett Drive", "San Jose", "95134")

        # Navigate to sites page
        self.home.navToSitesPage()
        # Navigate to Buildings Page
        self.sites.navToBuildingsPage()
        # Navigate to Room list page of 1st Building
        self.buildings.navToRoomListOfBuilding1()
        # Navigate to Room Modify Device page of 1st Floor and 1st Room
        self.roomList.navToRModDevOfF1R1()
