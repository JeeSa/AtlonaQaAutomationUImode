import time

import pytest

from pages.velocity.Home_Page import HomePage
from pages.velocity.menus.LeftBar_Menu import LeftBarMenu
from pages.velocity.popups.Confirm_popup import ConfirmPopup
from pages.velocity.scheduling.CalendarIntegrationList_Page import CalendarIntegrationListPage
from pages.velocity.scheduling.CalendarIntegrationModify_Page import CalendarIntegrationModifyPage
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestDeleteCalenderIntegration:
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.driver, self.wait)
        self.home = HomePage(self.driver, self.wait)
        self.leftNav = LeftBarMenu(self.driver, self.wait)
        self.caIntList = CalendarIntegrationListPage(self.driver, self.wait)
        self.caIntMod = CalendarIntegrationModifyPage(self.driver, self.wait)
        self.confirm = ConfirmPopup(self.driver, self.wait)

    def test_deleteCalenderIntegration(self):
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

        beforeCount = self.caIntList.totalRowCount()
        time.sleep(1)
    #   print(beforeCount)

        self.caIntList.clickDelete()
        # Verify if the confirmation popup is visible
        assert self.confirm.visibilityOfConfirmPopup() is True
        self.confirm.clickSubmit()
        time.sleep(1)

        afterCount = self.caIntList.totalRowCount()
        time.sleep(1)
        assert beforeCount != afterCount

