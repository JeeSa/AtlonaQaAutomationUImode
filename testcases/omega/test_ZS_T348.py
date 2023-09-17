import pytest

from pages.products_card.OME_SW21_TX_WPC_card import OME_SW21_TX_WPC_card
from pages.velocity.Home_Page import HomePage
from pages.velocity.sites.Buildings_Page import BuildingsPage
from pages.velocity.sites.RoomList_Page import RoomListPage
from pages.velocity.sites.RoomModifyDevices_Page import RoomModifyDevicesPage
from pages.velocity.sites.Sites_Page import SitesPage
from utilities.utils import Utils


@pytest.mark.usefixtures("setup")
class TestZS_T348:
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.driver, self.wait)
        self.home = HomePage(self.driver, self.wait)
        self.sites = SitesPage(self.driver, self.wait)
        self.buildings = BuildingsPage(self.driver, self.wait)
        self.roomList = RoomListPage(self.driver, self.wait)
        self.modifyDevices = RoomModifyDevicesPage(self.driver, self.wait)
        self.sw21txwpc = OME_SW21_TX_WPC_card(self.driver, self.wait)

    def test_zs_t348(self):
        # Login to the velocity app
        self.ut.login()
        # Navigate to sites page
        self.home.navToSitesPage()
        # Navigate to Buildings Page
        self.sites.navToBuildingsPage()
        # Navigate to Room list page of 1st Building
        self.buildings.navToRoomListOfBuilding1()
        # create a new room
        self.ut.addRoom("New Room for Omega")
        # Add technologies to the room
        self.ut.addTechnology("AT-OME-SW21-TX-WPC")
        # Verify if the added technology is visible
        assert self.sw21txwpc.visibilityOfSW21TXWPCDevice() is True
        self.sw21txwpc.clickEdit()
        self.ut.assignIPtoDevice("10.20.40.78")


