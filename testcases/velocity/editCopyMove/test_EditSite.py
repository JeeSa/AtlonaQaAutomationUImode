import pytest

from pages.velocity.Home_Page import HomePage
from pages.velocity.popups.AddSite_popup import AddSitePopup
from pages.velocity.sites.SiteModify_Page import SiteModifyPage
from pages.velocity.sites.Sites_Page import SitesPage
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestEditSite:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.driver, self.wait)
        self.home = HomePage(self.driver, self.wait)
        self.addSiteForm = AddSitePopup(self.driver, self.wait)
        self.sites = SitesPage(self.driver, self.wait)
        self.siteModify = SiteModifyPage(self.driver, self.wait)

    def test_EditSite(self):

        # Login to the velocity app
        self.ut.login()
        # Click on the add site button
        self.home.clickAddSiteButton()
        # Create New Site
        self.addSiteForm.createSite("Atlona", "Atlona Incorporated", "70 Daggett Drive", "San Jose", "95134")

        # Click on the created site
        self.home.clickSite()
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Sites"))
        assert "Atlona Velocity | Sites" in self.driver.title

        # Click on the add building button
        self.sites.clickEditButton()
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Site Modify"))
        assert "Atlona Velocity | Site Modify" in self.driver.title

        expected_sName = "Atlona Edited"
        # Edit the site name
        self.siteModify.clearSiteName()
        self.siteModify.enterSiteName(expected_sName)
        self.siteModify.clickSaveButton()
        # wait until the sites page is loaded successfully
        self.wait.until(EC.title_contains("Sites"))
        assert "Atlona Velocity | Sites" in self.driver.title
        actual_sName = self.sites.passSiteName()
        # Check that the edited name is showing after editing
        assert expected_sName == actual_sName

