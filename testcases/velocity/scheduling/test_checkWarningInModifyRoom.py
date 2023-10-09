import time

import pytest

from pages.velocity.Home_Page import HomePage
from pages.velocity.menus.LeftBar_Menu import LeftBarMenu
from pages.velocity.popups.Confirm_popup import ConfirmPopup
from pages.velocity.scheduling.CalendarIntegrationList_Page import CalendarIntegrationListPage
from pages.velocity.scheduling.CalendarIntegrationModify_Page import CalendarIntegrationModifyPage
from pages.velocity.sites.Buildings_Page import BuildingsPage
from pages.velocity.sites.RoomList_Page import RoomListPage
from pages.velocity.sites.RoomModify_Page import RoomModifyPage
from pages.velocity.sites.Sites_Page import SitesPage
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestCheckWarningInModifyRoom:
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.driver, self.wait)
        self.home = HomePage(self.driver, self.wait)
        self.leftNav = LeftBarMenu(self.driver, self.wait)
        self.caIntList = CalendarIntegrationListPage(self.driver, self.wait)
        self.caIntMod = CalendarIntegrationModifyPage(self.driver, self.wait)
        self.confirm = ConfirmPopup(self.driver, self.wait)
        self.sites = SitesPage(self.driver, self.wait)
        self.buildings = BuildingsPage(self.driver, self.wait)
        self.roomList = RoomListPage(self.driver, self.wait)
        self.modifyRoom = RoomModifyPage(self.driver, self.wait)

    def test_checkWarningInModifyRoom(self):
        # Login to the velocity app
        self.ut.login()
        # Open Nav bar
        self.ut.openNavBar()
        # Click Scheduling > Manage
        self.leftNav.clickScheduling()
        self.leftNav.clickSch_manage()
        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("Calendar Integration List"))
        assert "Atlona Velocity | Calendar Integration List" in self.driver.title

        rowCount = self.caIntList.totalRowCount()
        time.sleep(1)
        while rowCount != 10:
            self.caIntList.clickDelete()
            # Verify if the confirmation popup is visible
            assert self.confirm.visibilityOfConfirmPopup() is True
            self.confirm.clickSubmit()
            time.sleep(1)
            rowCount = self.caIntList.totalRowCount()
            time.sleep(1)

        # Navigate to dashboard by clicking on the velocity logo
        self.home.navToDashboard()
        # Navigate to sites page
        self.home.navToSitesPage()
        # Navigate to Buildings Page
        self.sites.navToBuildingsPage()
        # Navigate to Room list page of 1st Building
        self.buildings.navToRoomListOfBuilding1()
        # Navigate to Room Modify Page
        self.roomList.navToRoomModifyPage()

        expected_warning = "Warning: You are missing an association to a calendar resource for this meeting room, please assign via the calendar resources link below"
        time.sleep(1)
        actual_warning = self.modifyRoom.passCalWarning()
        # Check that the expected warning and actual warning is same
        assert expected_warning == actual_warning






