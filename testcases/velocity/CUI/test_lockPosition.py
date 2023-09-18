import time
import pytest
from selenium.common import NoSuchElementException, StaleElementReferenceException

from pages.velocity.customUI.AddComponents_Page import AddComponentsPage
from pages.velocity.customUI.CUI_Page import CUIPage
from pages.velocity.menus.CUIPage_Menu import CUIPageMenu
from pages.velocity.popups.Confirm_popup import ConfirmPopup
from pages.velocity.sites.Buildings_Page import BuildingsPage
from pages.velocity.Home_Page import HomePage
from pages.velocity.sites.RoomList_Page import RoomListPage
from pages.velocity.sites.RoomModifyDevices_Page import RoomModifyDevicesPage
from pages.velocity.sites.Sites_Page import SitesPage
from utilities.utils import Utils
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestLockPosition:

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
        self.addComp = AddComponentsPage(self.driver, self.wait)

    def test_gridlinesOnOff(self):

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
        time.sleep(1)

        # click on the media expand
        self.addComp.clickMediaExpand()
        time.sleep(1)
        # click on the icon button expand
        self.addComp.clickIconButtonExpand()
        time.sleep(1)
        # click on the popular expand
        self.addComp.clickPopularExpand()
        time.sleep(1)
        # click on the autorenew button
        self.addComp.clickAutoRenewButton()
        time.sleep(1)
        initial_location = self.cui.getRenewButton().location
        # print(initial_location)

        # drag renew button to 120px on x-axis and 150px on y-axis
        self.cui.dragRenewButton(120, 150)
        time.sleep(1)
        before_lock_location = self.cui.getRenewButton().location
        # print(before_lock_location)
        assert before_lock_location != initial_location

        # Click on lock position
        self.cui.clickLockPositionButton()
        time.sleep(1)
        # drag renew button to 120px on x-axis and 150px on y-axis
        self.cui.dragRenewButton(160, 200)
        after_lock_location = self.cui.getRenewButton().location
        # print(after_lock_location)
        assert after_lock_location == before_lock_location

        # Click on lock position
        self.cui.clickLockPositionButton()

