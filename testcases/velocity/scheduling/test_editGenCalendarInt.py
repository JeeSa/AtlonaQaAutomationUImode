import time

import pytest

from pages.velocity.Home_Page import HomePage
from pages.velocity.menus.LeftBar_Menu import LeftBarMenu
from pages.velocity.scheduling.CalendarIntegrationList_Page import CalendarIntegrationListPage
from pages.velocity.scheduling.CalendarIntegrationModify_Page import CalendarIntegrationModifyPage
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestEditGenericCalenderIntegration:
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.driver, self.wait)
        self.home = HomePage(self.driver, self.wait)
        self.leftNav = LeftBarMenu(self.driver, self.wait)
        self.caIntList = CalendarIntegrationListPage(self.driver, self.wait)
        self.caIntMod = CalendarIntegrationModifyPage(self.driver, self.wait)

    def test_editGenericCalenderIntegration(self):
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

        self.caIntList.clickEdit()
        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("Calendar Integration Modify"))
        assert "Atlona Velocity | Calendar Integration Modify" in self.driver.title

        expected_caIntName = "Test Integration 1 Edited"
        time.sleep(1)
        self.caIntMod.clearAlias()
        time.sleep(1)
        self.caIntMod.enterAlias(expected_caIntName)
        time.sleep(1)
        self.caIntMod.clickSave()
        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("Calendar Integration List"))
        assert "Atlona Velocity | Calendar Integration List" in self.driver.title
        actual_caIntName = self.caIntList.passCaIntName()
        # Check that the edited name is showing after editing
        assert expected_caIntName == actual_caIntName


