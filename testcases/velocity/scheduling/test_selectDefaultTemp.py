import time

import pytest

from pages.velocity.Home_Page import HomePage
from pages.velocity.menus.LeftBar_Menu import LeftBarMenu
from pages.velocity.scheduling.SchedulingTemplate_Page import SchedulingTemplatePage
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestSelectDefaultTemplate:
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.driver, self.wait)
        self.home = HomePage(self.driver, self.wait)
        self.leftNav = LeftBarMenu(self.driver, self.wait)
        self.schTemp = SchedulingTemplatePage(self.driver, self.wait)

    def test_selectDefaultTemplate(self):
        # Login to the velocity app
        self.ut.login()
        self.home.clickNavBar()
        # Verify if the sidebar is visible
        assert self.home.visibilityOfSidebarMenu() is True
        self.leftNav.clickScheduling()
        self.leftNav.clickSch_schedulingTemplates()
        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("Scheduling Templates"))
        assert "Atlona Velocity | Scheduling Templates" in self.driver.title

        self.schTemp.clickTemp_2()
        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("Scheduling Templates"))
        assert "Atlona Velocity | Scheduling Templates" in self.driver.title
        time.sleep(1)

        self.schTemp.clickTemp_1()
        # wait until the destination page is loaded successfully
        self.wait.until(EC.title_contains("Scheduling Templates"))
        assert "Atlona Velocity | Scheduling Templates" in self.driver.title

