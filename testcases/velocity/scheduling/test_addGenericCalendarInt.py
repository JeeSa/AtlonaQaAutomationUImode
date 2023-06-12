import time

import pytest

from pages.velocity.Home_Page import HomePage
from pages.velocity.menus.LeftBarMenu import LeftBarMenu
from pages.velocity.popups.Confirm_popup import ConfirmPopup
from pages.velocity.scheduling.CalendarIntegrationAdd_Page import CalendarIntegrationAddPage
from pages.velocity.scheduling.CalendarIntegrationList_Page import CalendarIntegrationListPage
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestAddGenericCalenderIntegration:
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.driver, self.wait)
        self.home = HomePage(self.driver, self.wait)
        self.leftNav = LeftBarMenu(self.driver, self.wait)
        self.caIntList = CalendarIntegrationListPage(self.driver, self.wait)
        self.caIntAdd = CalendarIntegrationAddPage(self.driver, self.wait)
        self.confirm = ConfirmPopup(self.driver, self.wait)

    def test_addGenericCalenderIntegration(self):
        # Login to the velocity app
        self.ut.login()
        self.home.clickNavBar()
        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        self.leftNav.clickScheduling()
        self.leftNav.clickSch_manage()
        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("Calendar Integration List"))
        assert "Atlona Velocity | Calendar Integration List" in self.driver.title

        self.caIntList.clickAdd()
        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("Calendar Integration Add"))
        assert "Atlona Velocity | Calendar Integration Add" in self.driver.title

        time.sleep(1)
        self.caIntAdd.clickTypeDrop()
        time.sleep(1)
        self.caIntAdd.clickGenericType()
        time.sleep(1)
        self.caIntAdd.enterAlias("Test Integeration 1")
        time.sleep(1)
        self.caIntAdd.clickCreate()
        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("Calendar Integration Modify"))
        assert "Atlona Velocity | Calendar Integration Modify" in self.driver.title

