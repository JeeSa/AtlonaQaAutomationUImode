import time

import pytest

from pages.velocity.popups.About_popup import AboutPopup
from pages.velocity.Home_Page import HomePage
from pages.velocity.menus.LeftBar_Menu import LeftBarMenu
from pages.velocity.settings.Cloud_tab import CloudTab
from pages.velocity.settings.Database_tab import DatabaseTab
from pages.velocity.settings.Email_tab import EmailTab
from pages.velocity.settings.Gateway_tab import GatewayTab
from pages.velocity.settings.Licenses_tab import LicensesTab
from pages.velocity.settings.Network_tab import NetworkTab
from pages.velocity.settings.RoomSupport_tab import RoomSupportTab
from pages.velocity.settings.Security_tab import SecurityTab
from pages.velocity.settings.Tools_tab import ToolsTab
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestLeftNavigationMenu:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.driver, self.wait)
        self.home = HomePage(self.driver, self.wait)
        self.leftNav = LeftBarMenu(self.driver, self.wait)
        self.gateway = GatewayTab(self.driver, self.wait)
        self.database = DatabaseTab(self.driver, self.wait)
        self.licenses = LicensesTab(self.driver, self.wait)
        self.tools = ToolsTab(self.driver, self.wait)
        self.email = EmailTab(self.driver, self.wait)
        self.security = SecurityTab(self.driver, self.wait)
        self.roomSupport = RoomSupportTab(self.driver, self.wait)
        self.network = NetworkTab(self.driver, self.wait)
        self.cloud = CloudTab(self.driver, self.wait)
        self.about = AboutPopup(self.driver, self.wait)

    def test_LeftNavigationMenu(self):

        # Login to the velocity app
        self.ut.login()
        self.home.clickNavBar()
        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        self.leftNav.clickControl()
        self.leftNav.clickCon_allRooms()
        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("Room List"))
        assert "Atlona Velocity | Room List" in self.driver.title

        self.home.clickNavBar()
        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        self.leftNav.clickControl()
        self.leftNav.clickCon_deviceDrivers()
        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("Equipment List"))
        assert "Atlona Velocity | Equipment List" in self.driver.title

        self.home.clickNavBar()
        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        self.leftNav.clickControl()
        self.leftNav.clickCon_deviceGroups()
        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("Device Group List"))
        assert "Atlona Velocity | Device Group List" in self.driver.title

        self.home.clickNavBar()
        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        self.leftNav.clickScheduling()
        self.leftNav.clickSch_allRooms()
        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("Room List"))
        assert "Atlona Velocity | Room List" in self.driver.title

        self.home.clickNavBar()
        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        self.leftNav.clickScheduling()
        self.leftNav.clickSch_schedulingTemplates()
        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("Scheduling Templates"))
        assert "Atlona Velocity | Scheduling Templates" in self.driver.title

        self.home.clickNavBar()
        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        self.leftNav.clickScheduling()
        self.leftNav.clickSch_manage()
        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("Calendar Integration List"))
        assert "Atlona Velocity | Calendar Integration List" in self.driver.title

        self.home.clickNavBar()
        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        self.leftNav.clickScheduling()
        self.leftNav.clickSch_allRoomSchedule()
        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("Meeting Schedule for all Rooms"))
        assert "Atlona Velocity | Meeting Schedule for all Rooms" in self.driver.title

        self.home.clickNavBar()
        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        self.leftNav.clickManagement()
        self.leftNav.clickMng_amsDeviceManager()
        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("Atlona Devices"))
        assert "Atlona Velocity | Atlona Devices" in self.driver.title

        self.home.clickNavBar()
        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        self.leftNav.clickManagement()
        self.leftNav.clickMng_roomSupportTickets()
        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("Help Tickets"))
        assert "Atlona Velocity | Help Tickets" in self.driver.title

        self.home.clickNavBar()
        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        self.leftNav.clickReports()
        self.leftNav.clickRep_allDevices()
        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("All Devices"))
        assert "Atlona Velocity | All Devices" in self.driver.title

        self.home.clickNavBar()
        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        self.leftNav.clickReports()
        self.leftNav.clickRep_allMacros()
        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("All Macros"))
        assert "Atlona Velocity | All Macros" in self.driver.title

        self.home.clickNavBar()
        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        self.leftNav.clickReports()
        self.leftNav.clickRep_billOfMaterials()
        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("Bill Of Materials"))
        assert "Atlona Velocity | Bill Of Materials" in self.driver.title

        self.home.clickNavBar()
        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        self.leftNav.clickReports()
        self.leftNav.clickRep_roomProblems()
        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("Report Room Problem"))
        assert "Atlona Velocity | Report Room Problem" in self.driver.title

        self.home.clickNavBar()
        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        self.leftNav.clickSettings()
        self.leftNav.clickSet_gateway()
        assert self.gateway.visibilityOfGatewayTab() is True

        self.home.clickNavBar()
        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        self.leftNav.clickSettings()
        self.leftNav.clickSet_database()
        assert self.database.visibilityOfDatabaseTab() is True

        self.home.clickNavBar()
        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        self.leftNav.clickSettings()
        self.leftNav.clickSet_licenses()
        assert self.licenses.visibilityOfLicensesTab() is True

        self.home.clickNavBar()
        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        self.leftNav.clickSettings()
        self.leftNav.clickSet_tools()
        assert self.tools.visibilityOfToolsTab() is True

        self.home.clickNavBar()
        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        self.leftNav.clickSettings()
        self.leftNav.clickSet_email()
        assert self.email.visibilityOfEmailTab() is True

        self.home.clickNavBar()
        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        self.leftNav.clickSettings()
        self.leftNav.clickSet_security()
        assert self.security.visibilityOfSecurityTab() is True

        self.home.clickNavBar()
        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        self.leftNav.clickSettings()
        self.leftNav.clickSet_roomSupport()
        assert self.roomSupport.visibilityOfRoomSupportTab() is True

        self.home.clickNavBar()
        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        self.leftNav.clickSettings()
        self.leftNav.clickSet_network()
        assert self.network.visibilityOfAllNetworksTab() is True

        self.home.clickNavBar()
        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        self.leftNav.clickCloud()
        assert self.cloud.visibilityOfCloudTab() is True

        self.home.clickNavBar()
        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        self.leftNav.clickPinIcon()
        self.leftNav.clickHome()
        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("Dashboard"))
        assert "Atlona Velocity | Dashboard" in self.driver.title

        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        # Store the ID of the original window
        main_window = self.driver.current_window_handle
        # Check we don't have other windows open already
        assert len(self.driver.window_handles) == 1
        self.leftNav.clickHelp()
        self.leftNav.clickHlp_manual()
        # Wait for the new window or tab
        self.wait.until(EC.number_of_windows_to_be(2))

        all_windows = self.driver.window_handles
        for new_window in all_windows:
            if new_window != main_window:
                self.driver.switch_to.window(new_window)
                # wait until the destination page is loaded successfully
                self.wait.until(EC.url_contains("pdf/manuals/Velocity.pdf"))
                assert "https://atlona.com/pdf/manuals/Velocity.pdf" in self.driver.current_url
                time.sleep(1)
                self.driver.close()
                break

        self.driver.switch_to.window(main_window)
        # Check we don't have other windows open anymore
        assert len(self.driver.window_handles) == 1

        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        self.leftNav.clickHlp_training()
        # Wait for the new window or tab
        self.wait.until(EC.number_of_windows_to_be(2))

        all_windows = self.driver.window_handles
        for new_window in all_windows:
            if new_window != main_window:
                self.driver.switch_to.window(new_window)
                # wait until the destination page is loaded successfully
                self.wait.until(EC.url_contains("training"))
                assert "https://atlona.com/training/" in self.driver.current_url
                time.sleep(1)
                self.driver.close()
                break

        self.driver.switch_to.window(main_window)
        # Check we don't have other windows open anymore
        assert len(self.driver.window_handles) == 1

        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        self.leftNav.clickHlp_videos()
        # Wait for the new window or tab
        self.wait.until(EC.number_of_windows_to_be(2))

        all_windows = self.driver.window_handles
        for new_window in all_windows:
            if new_window != main_window:
                self.driver.switch_to.window(new_window)
                # wait until the destination page is loaded successfully
                self.wait.until(EC.url_contains("youtube.com/playlist"))
                assert "https://www.youtube.com/playlist?list=PLM8SV1hQYIl5C_0zfhHaNdVbY-PCRC20L" in self.driver.current_url
                time.sleep(1)
                self.driver.close()
                break

        self.driver.switch_to.window(main_window)
        # Check we don't have other windows open anymore
        assert len(self.driver.window_handles) == 1

        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        self.leftNav.clickHlp_support()
        # Wait for the new window or tab
        self.wait.until(EC.number_of_windows_to_be(2))

        all_windows = self.driver.window_handles
        for new_window in all_windows:
            if new_window != main_window:
                self.driver.switch_to.window(new_window)
                # wait until the destination page is loaded successfully
                self.wait.until(EC.url_contains("livechat"))
                assert "https://v2.zopim.com/widget/livechat.html?key=46DeMcdBPEED6rFHi3GtSPq5knQWNdif" in self.driver.current_url
                time.sleep(1)
                self.driver.close()
                break

        self.driver.switch_to.window(main_window)

        # Check we don't have other windows open anymore
        assert len(self.driver.window_handles) == 1
        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        self.leftNav.clickHlp_faqs()
        # Wait for the new window or tab
        self.wait.until(EC.number_of_windows_to_be(2))

        all_windows = self.driver.window_handles
        for new_window in all_windows:
            if new_window != main_window:
                self.driver.switch_to.window(new_window)

                # wait until the destination page is loaded successfully
                self.wait.until(EC.url_contains("support.atlona"))
                assert "https://support.atlona.com/hc/en-us/" in self.driver.current_url
                time.sleep(1)

                self.driver.close()
                break

        self.driver.switch_to.window(main_window)
        # Check we don't have other windows open anymore
        assert len(self.driver.window_handles) == 1

        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        self.leftNav.clickHlp_about()
        assert self.about.visibilityOfAboutPopup() is True
        self.about.clickCancel()
        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True







