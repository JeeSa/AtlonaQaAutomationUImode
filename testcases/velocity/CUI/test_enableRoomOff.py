import time
import pytest
from selenium.common import NoSuchElementException, StaleElementReferenceException

from pages.velocity.customUI.CUI_Page import CUIPage
from pages.velocity.customUI.HeaderProperties_Page import HeaderPropertiesPage
from pages.velocity.menus.CUIPage_Menu import CUIPageMenu
from pages.velocity.popups.Confirm_popup import ConfirmPopup
from pages.velocity.sites.Buildings_Page import BuildingsPage
from pages.velocity.Home_Page import HomePage
from pages.velocity.sites.RoomList_Page import RoomListPage
from pages.velocity.sites.RoomModifyDevices_Page import RoomModifyDevicesPage
from pages.velocity.sites.Sites_Page import SitesPage
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestEnableRoomOff:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.driver, self.wait)
        self.home = HomePage(self.driver, self.wait)
        self.sites = SitesPage(self.driver, self.wait)
        self.buildings = BuildingsPage(self.driver, self.wait)
        self.roomList = RoomListPage(self.driver, self.wait)
        self.modifyDevices = RoomModifyDevicesPage(self.driver, self.wait)
        self.cui = CUIPage(self.driver, self.wait)
        self.cuiPageMenu = CUIPageMenu(self.driver, self.wait)
        self.confirm = ConfirmPopup(self.driver, self.wait)
        self.headerProperties = HeaderPropertiesPage(self.driver, self.wait)

    def test_enableRoomOff(self):

        # Login to the velocity app
        self.ut.login()
        # Navigate to sites page
        self.home.navToSitesPage()
        # Navigate to Buildings Page
        self.sites.navToBuildingsPage()
        # Navigate to Room list page of 1st Building
        self.buildings.navToRoomListOfBuilding1()
        # Navigate to Room modify devices of floor 1 room 1
        self.roomList.navToRModDevOfF1R1()
        # Navigate to Custom UI page
        self.modifyDevices.navToCUIScreen()

        # close the side drawer
        self.cui.clickExpand()
        # Go to the header tab
        self.cui.clickHeader()
        time.sleep(1)
        # Check the room title is visible
        assert self.cui.visibilityOfRoomOff() is True
        # Expand Room on section
        self.headerProperties.clickRoomOffExpand()
        # Uncheck the Room on
        self.headerProperties.clickRoomOffOtherToggle()

        # check the room title is invisible
        try:
            self.cui.visibilityOfRoomOff()
        except StaleElementReferenceException:
            pass
        except NoSuchElementException:
            pass

        time.sleep(1)
        # Check the Room on
        self.headerProperties.clickRoomOffOtherToggle()
        # Check the room title is visible
        assert self.cui.visibilityOfRoomOff() is True



