import time

import pytest

from pages.velocity.sites.AddBuilding_Page import AddBuildingPage
from pages.velocity.Home_Page import HomePage
from pages.velocity.sites.Sites_Page import SitesPage
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestNegativeCasesAddBuilding:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.driver, self.wait)
        self.home = HomePage(self.driver, self.wait)
        self.sites = SitesPage(self.driver, self.wait)
        self.addBuildingForm = AddBuildingPage(self.driver, self.wait)

    def test_negativeCases_addBuilding_01(self):
        # Case 1: Hit the Submit button when all the required fields are blank

        # Login to the velocity app

        self.ut.login()
        # Click on the created site
        self.home.clickSite()
        # wait until the sites page is loaded successfully
        self.wait.until(EC.title_contains("Sites"))
        assert "Atlona Velocity | Sites" in self.driver.title

        # Click on the add building button
        self.sites.clickAddBuilding()
        # wait until the sites page is loaded successfully
        self.wait.until(EC.title_contains("Building Add"))
        assert "Atlona Velocity | Building Add" in self.driver.title
        # Click on create building
        self.addBuildingForm.clickCreateBuilding()
        assert "Atlona Velocity | Building Add" in self.driver.title

    def test_negativeCases_addBuilding_02(self):
        # Case 2: Hit the Submit button when only building image field is blank

        # Provide all data except the dropdown values
        self.addBuildingForm.enterAllValues("EMEA HQ", "Atlona International AG", "Tödistrasse 18, 8002 Zürich, Switzerland")
        # Click on create building
        self.addBuildingForm.clickCreateBuilding()
        assert "Atlona Velocity | Building Add" in self.driver.title

    def test_negativeCases_addBuilding_03(self):
        # Case 3: Hit the Submit button when only building name field is blank

        # Provide all data except the dropdown values
        self.addBuildingForm.enterAllValues("EMEA HQ", "Atlona International AG", "Tödistrasse 18, 8002 Zürich, Switzerland")
        # Select all the dropdown values
        self.addBuildingForm.selectDropdown()
        time.sleep(1)
        # Clear the building name
        self.addBuildingForm.clearBuildingName()
        # Click on create building
        self.addBuildingForm.clickCreateBuilding()
        assert "Atlona Velocity | Building Add" in self.driver.title
