
import pytest

from pages.velocity.DeviceList_Page import DeviceListPage
from pages.velocity.Home_Page import HomePage
from pages.velocity.menus.LeftBarMenu import LeftBarMenu
from pages.velocity.popups.DeleteConfirmAMS_popup import DeleteConfirmAMSPopup
from pages.velocity.popups.EditBuildingAMS_popup import EditBuildingPopup
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestDeleteBuildingAMS:
    def test_deleteBuildingAMS(self):

        # Login to the velocity app
        ut = Utils(self.driver, self.wait)
        ut.login()

        homePage = HomePage(self.driver, self.wait)
        homePage.clickNavBar()

        # Verify if the sidebar is visible
        assert homePage.visibilityOfSidebarMenu() is True

        leftNav = LeftBarMenu(self.driver, self.wait)

        leftNav.clickManagement()
        leftNav.clickMng_amsDeviceManager()

        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("Atlona Devices"))

        assert "Atlona Velocity | Atlona Devices" in self.driver.title

        deviceList = DeviceListPage(self.driver, self.wait)

        deviceList.hoverBuildingDiv1()
        deviceList.clickSettingsB1()

        editBuildingPopup = EditBuildingPopup(self.driver, self.wait)

        assert editBuildingPopup.visibilityOfEditBuilding()

        editBuildingPopup.clickDelete()

        deleteConfirm = DeleteConfirmAMSPopup(self.driver, self.wait)

        assert deleteConfirm.visibilityOfBuildingConfirmPopup()

        deleteConfirm.clickDeleteB()

        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("Atlona Devices"))

        assert "Atlona Velocity | Atlona Devices" in self.driver.title
