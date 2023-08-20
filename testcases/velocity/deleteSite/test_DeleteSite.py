import time

import pytest

from pages.velocity.Home_Page import HomePage
from pages.velocity.popups.Confirm_popup import ConfirmPopup
from pages.velocity.sites.Sites_Page import SitesPage
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestDeleteSite:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.driver, self.wait)
        self.home = HomePage(self.driver, self.wait)
        self.sites = SitesPage(self.driver, self.wait)
        self.confirm = ConfirmPopup(self.driver, self.wait)

    def test_deleteSite(self):

        # Login to the velocity app
        self.ut.login()
        # Navigate to sites page
        self.home.navToSitesPage()
        # Delete site
        self.ut.deleteSite()
