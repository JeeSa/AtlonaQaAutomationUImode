import time
import pytest
from pages.velocity.customUI.CUI_Page import CUIPage
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
class TestLaunchControl:

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

    def test_launchControl(self):

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
        # Click on the edit technology button
        self.roomList.clickEditTechnology1Button()
        # wait until the  page is loaded successfully
        self.wait.until(EC.title_contains("Room Modify Devices"))
        assert "Atlona Velocity | Room Modify Devices" in self.driver.title

        # Click on the add technology button
        self.modifyDevices.clickCustomUI()
        # wait until the  page is loaded successfully
        self.wait.until(EC.title_contains("Room Modify Screens"))
        assert "Atlona Velocity | Room Modify Screens" in self.driver.title

        # Store the ID of the original window
        main_window = self.driver.current_window_handle
        self.cui.clickLaunchControl()
        time.sleep(2)
        # Wait for the new window or tab
        self.wait.until(EC.number_of_windows_to_be(2))

        all_windows = self.driver.window_handles
        for new_window in all_windows:
            if new_window != main_window:
                self.driver.switch_to.window(new_window)

                self.wait.until(EC.title_contains("Control"))
                assert "Conference Room Control" in self.driver.title
                break
