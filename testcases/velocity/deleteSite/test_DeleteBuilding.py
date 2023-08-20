import time

import pytest

from pages.velocity.Home_Page import HomePage
from pages.velocity.popups.Confirm_popup import ConfirmPopup
from pages.velocity.sites.Buildings_Page import BuildingsPage
from pages.velocity.sites.Sites_Page import SitesPage
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestDeleteBuilding:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.driver, self.wait)
        self.home = HomePage(self.driver, self.wait)
        self.sites = SitesPage(self.driver, self.wait)
        self.buildings = BuildingsPage(self.driver, self.wait)
        self.confirm = ConfirmPopup(self.driver, self.wait)

    def test_addDeleteBuilding(self):

        # Login to the velocity app
        self.ut.login()
        # Navigate to sites page
        self.home.navToSitesPage()
        # Navigate to buildings page
        self.sites.navToBuildingsPage()
        # Click on the building delete button
        self.ut.deleteBuilding()

