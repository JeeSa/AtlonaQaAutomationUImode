import pytest

from pages.velocity.Home_Page import HomePage
from pages.velocity.sites.BuildingModify_Page import BuildingModifyPage
from pages.velocity.sites.Buildings_Page import BuildingsPage
from pages.velocity.sites.Sites_Page import SitesPage
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestEditBuilding:
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.driver, self.wait)
        self.home = HomePage(self.driver, self.wait)
        self.sites = SitesPage(self.driver, self.wait)
        self.buildings = BuildingsPage(self.driver, self.wait)
        self.buildingModify = BuildingModifyPage(self.driver, self.wait)

    def test_EditBuilding(self):

        # Login to the velocity app
        self.ut.login()
        # Click on the created site
        self.home.clickSite()
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Sites"))
        assert "Atlona Velocity | Sites" in self.driver.title

        # Click on the view button
        self.sites.clickView()
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Buildings"))
        assert "Atlona Velocity | Buildings" in self.driver.title
        # Click on the edit button
        self.buildings.clickEditBuilding1()
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Building Modify"))
        assert "Atlona Velocity | Building Modify" in self.driver.title

        expected_bName = "Edited Building Name"
        # Edit the building name
        self.buildingModify.clearBuildingName()
        self.buildingModify.enterBuildingName(expected_bName)
        self.buildingModify.clickSaveButton()
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Buildings"))
        assert "Atlona Velocity | Buildings" in self.driver.title
        actual_bName = self.buildings.passBuildingName()
        # Check that the edited name is showing after editing
        assert expected_bName == actual_bName



