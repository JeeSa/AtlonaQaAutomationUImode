import time
import pytest

from pages.velocity.popups.AddOrImport_popup import AddOrImportPopup
from pages.velocity.sites.AddBuilding_Page import AddBuildingPage
from pages.velocity.sites.Buildings_Page import BuildingsPage
from pages.velocity.Home_Page import HomePage
from pages.velocity.sites.RoomList_Page import RoomListPage
from pages.velocity.sites.Sites_Page import SitesPage
from utilities.utils import Utils
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestAddBuilding:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.driver, self.wait)
        self.home = HomePage(self.driver, self.wait)
        self.sites = SitesPage(self.driver, self.wait)
        self.addBuildingForm = AddBuildingPage(self.driver, self.wait)
        self.buildings = BuildingsPage(self.driver, self.wait)
        self.roomList = RoomListPage(self.driver, self.wait)
        self.addImport = AddOrImportPopup(self.driver, self.wait)

    def test_addBuilding1(self):

        # Login to the velocity app
        self.ut.login()
        # Click on the created site
        self.home.clickSite()
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Sites"))
        assert "Atlona Velocity | Sites" in self.driver.title

        # Click on the add building button
        self.sites.clickAddBuilding()
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Building Add"))
        assert "Atlona Velocity | Building Add" in self.driver.title

        # Create new building
        self.addBuildingForm.createBuilding("EMEA HQ", "Atlona International AG", "Tödistrasse 18, 8002 Zürich, Switzerland")
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Sites"))
        assert "Atlona Velocity | Sites" in self.driver.title
        # Click on the view button
        self.sites.clickView()
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Buildings"))
        assert "Atlona Velocity | Buildings" in self.driver.title

        # Click on the view button
        self.buildings.clickViewAllRooms2()
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Room List"))
        assert "Atlona Velocity | Room List" in self.driver.title

        # Click on the edit technology button
        self.roomList.clickEditTechnology1Button()
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Room Modify Devices"))
        assert "Atlona Velocity | Room Modify Devices" in self.driver.title

    def test_addBuilding2(self):

        self.home.clickVelocityLogo()
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Dashboard"))
        assert "Atlona Velocity | Dashboard" in self.driver.title

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

        # Click on the view button
        self.buildings.clickAddBuildingButton()
        # Click add via form
        self.addImport.clickAddViaForm()
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Building Add"))
        assert "Atlona Velocity | Building Add" in self.driver.title

        # Provide all data to create building
        self.addBuildingForm.createBuilding("EMEA HQ 2", "Atlona International AG 2", "Tödistrasse 18, 8002 Zürich, Switzerland")
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Buildings"))
        assert "Atlona Velocity | Buildings" in self.driver.title

        # Click on the view button
        self.buildings.clickViewAllRooms3()
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Room List"))
        assert "Atlona Velocity | Room List" in self.driver.title
        # Click on the edit technology button
        self.roomList.clickEditTechnology1Button()
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Room Modify Devices"))
        assert "Atlona Velocity | Room Modify Devices" in self.driver.title
