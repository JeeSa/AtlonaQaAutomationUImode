import pytest

from pages.velocity.DeviceList_Page import DeviceListPage
from pages.velocity.Home_Page import HomePage
from pages.velocity.menus.LeftBar_Menu import LeftBarMenu
from pages.velocity.popups.DeleteConfirmAMS_popup import DeleteConfirmAMSPopup
from pages.velocity.popups.EditRoomAMS_popup import EditRoomPopup
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestDeleteRoomAMS:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.driver, self.wait)
        self.home = HomePage(self.driver, self.wait)
        self.leftNav = LeftBarMenu(self.driver, self.wait)
        self.deviceList = DeviceListPage(self.driver, self.wait)
        self.editRoomPopup = EditRoomPopup(self.driver, self.wait)
        self.deleteConfirm = DeleteConfirmAMSPopup(self.driver, self.wait)

    def test_deleteRoomAMS(self):

        # Login to the velocity app
        self.ut.login()
        self.home.clickNavBar()
        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        self.leftNav.clickManagement()
        self.leftNav.clickMng_amsDeviceManager()
        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("Atlona Devices"))
        assert "Atlona Velocity | Atlona Devices" in self.driver.title

        self.deviceList.clickExpandBuilding()
        self.deviceList.hoverRoomDiv()
        self.deviceList.clickRoomSettings()
        assert self.editRoomPopup.visibilityOfEditRoom()
        self.editRoomPopup.clickDelete()
        assert self.deleteConfirm.visibilityOfRoomConfirmPopup()

        self.deleteConfirm.clickDeleteR()
        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("Atlona Devices"))
        assert "Atlona Velocity | Atlona Devices" in self.driver.title
