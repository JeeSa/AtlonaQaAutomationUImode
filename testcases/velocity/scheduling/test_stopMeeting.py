import time

import pytest

from pages.velocity.popups.StartMeeting_popup import StartMeetingPopup
from pages.velocity.scheduling.MeetingRoomControl_Page import MeetingRoomControlPage
from pages.velocity.sites.Buildings_Page import BuildingsPage
from pages.velocity.Home_Page import HomePage
from pages.velocity.menus.FloorHamburger_Menu import FloorHamburgerMenu
from pages.velocity.sites.RoomList_Page import RoomListPage
from pages.velocity.sites.RoomModifyDevices_Page import RoomModifyDevicesPage
from pages.velocity.sites.RoomModify_Page import RoomModifyPage
from pages.velocity.sites.Sites_Page import SitesPage
from pages.velocity.sites.TechnologyList_Page import TechnologyListPage
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestStopMeeting:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.driver, self.wait)
        self.home = HomePage(self.driver, self.wait)
        self.sites = SitesPage(self.driver, self.wait)
        self.buildings = BuildingsPage(self.driver, self.wait)
        self.roomList = RoomListPage(self.driver, self.wait)
        self.flrHamburger = FloorHamburgerMenu(self.driver, self.wait)
        self.modRoom = RoomModifyPage(self.driver, self.wait)
        self.modifyDevices = RoomModifyDevicesPage(self.driver, self.wait)
        self.techList = TechnologyListPage(self.driver, self.wait)
        self.mRoomControl = MeetingRoomControlPage(self.driver, self.wait)
        self.startMeetingPop = StartMeetingPopup(self.driver, self.wait)

    def test_stopMeeting(self):

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

        # Store the ID of the original window
        main_window = self.driver.current_window_handle
        # Check we don't have other windows open already
        assert len(self.driver.window_handles) == 1

        # Click on the more option button
        self.roomList.clickViewMeeting1()
        time.sleep(2)
        # Wait for the new window or tab
        self.wait.until(EC.number_of_windows_to_be(2))

        all_windows = self.driver.window_handles
        for new_window in all_windows:
            if new_window != main_window:
                self.driver.switch_to.window(new_window)

                self.wait.until(EC.title_contains("Control"))
                assert "New Test Meeting Room Control" in self.driver.title
                time.sleep(1)

                beforeStatus = self.mRoomControl.passRoomStatus()
                self.mRoomControl.clickStop()
                time.sleep(1)

                afterStatus = self.mRoomControl.passRoomStatus()
                assert beforeStatus != afterStatus

                self.driver.close()
                break

        self.driver.switch_to.window(main_window)
        # Check we don't have other windows open anymore
        assert len(self.driver.window_handles) == 1
        assert "Atlona Velocity | Room List" in self.driver.title


