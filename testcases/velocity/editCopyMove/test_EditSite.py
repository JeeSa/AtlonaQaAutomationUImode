import time

import pytest

from pages.velocity.Home_Page import HomePage
from pages.velocity.sites.Sites_Page import SitesPage
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestEditSite:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.driver, self.wait)
        self.home = HomePage(self.driver, self.wait)
        self.sites = SitesPage(self.driver, self.wait)

    def test_EditSite(self):

        # Login to the velocity app
        self.ut.login()
        # Refresh the page
        self.driver.refresh()
        time.sleep(1)
        # Create a new site
        self.ut.addSite("Atlona", "Atlona Incorporated", "70 Daggett Drive", "San Jose", "95134")
        # Navigate to sites page
        self.home.navToSitesPage()
        # Navigate to site modify page
        self.sites.navToSiteModifyPage()
        expected_sName = "Atlona Edited"
        # Edit the site name and verify it
        self.ut.editSiteName(expected_sName)

