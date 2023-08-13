import time

from pages.velocity.Home_Page import HomePage
from pages.velocity.menus.FloorHamburger_Menu import FloorHamburgerMenu
from pages.velocity.popups.AddOrImport_popup import AddOrImportPopup
from pages.velocity.popups.AddSite_popup import AddSitePopup
from pages.velocity.security.Login_Page import LoginPage
from selenium.webdriver.support import expected_conditions as EC

from pages.velocity.sites.AddBuilding_Page import AddBuildingPage
from pages.velocity.sites.AddFloor_Page import AddNewFloorPage
from pages.velocity.sites.AddRoom_Page import AddRoomPage
from pages.velocity.sites.Buildings_Page import BuildingsPage
from pages.velocity.sites.RoomList_Page import RoomListPage
from pages.velocity.sites.RoomModifyDevices_Page import RoomModifyDevicesPage
from pages.velocity.sites.TechnologyList_Page import TechnologyListPage


class Utils:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def login(self):
        loginFlow = LoginPage(self.driver, self.wait)

        # wait until Login page loaded successfully
        self.wait.until(EC.title_contains("Login"))
        # Verify the page after launching the Velocity App
        assert "Atlona Velocity | Login To The System" in self.driver.title

        # Provide all the required data and hit the login button
        loginFlow.loginMethod("qa@atlona.com", "Admin123!")

        # wait until the login is successful
        self.wait.until(EC.title_contains("Dashboard"))
        # Verify the page after logging into the Velocity App
        assert "Atlona Velocity | Dashboard" in self.driver.title

    def addSite(self):
        home = HomePage(self.driver, self.wait)
        addSiteForm = AddSitePopup(self.driver, self.wait)

        # wait until the login is successful
        self.wait.until(EC.title_contains("Dashboard"))
        # Verify the page after logging into the Velocity App
        assert "Atlona Velocity | Dashboard" in self.driver.title

        # Click on the add site button
        home.clickAddSiteButton()
        # Create New Site
        addSiteForm.createSite("Atlona", "Atlona Incorporated", "70 Daggett Drive", "San Jose", "95134")
        # Check the created site is visible or not
        assert home.visibilityOfCreatedSite() is True

    def addBuilding(self, b_name, ad_1, ad_2):
        addBuildingForm = AddBuildingPage(self.driver, self.wait)

        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Building Add"))
        assert "Atlona Velocity | Building Add" in self.driver.title

        # Create new building
        addBuildingForm.createBuilding(b_name, ad_1, ad_2)
        self.wait.until(EC.title_contains("Sites"))
        assert "Atlona Velocity | Sites" in self.driver.title

    def addBuildingViaForm(self, b_name, ad_1, ad_2):
        self.buildings = BuildingsPage(self.driver, self.wait)
        addBuildingForm = AddBuildingPage(self.driver, self.wait)
        self.addImport = AddOrImportPopup(self.driver, self.wait)

        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Buildings"))
        assert "Atlona Velocity | Buildings" in self.driver.title

        # Click on the add building button
        self.buildings.clickAddBuildingButton()
        # Click add via form
        self.addImport.clickAddViaForm()

        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Building Add"))
        assert "Atlona Velocity | Building Add" in self.driver.title

        # Create new building
        addBuildingForm.createBuilding(b_name, ad_1, ad_2)
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Buildings"))
        assert "Atlona Velocity | Buildings" in self.driver.title

    def addFloor(self, f_name):
        roomList = RoomListPage(self.driver, self.wait)
        flrHamburger = FloorHamburgerMenu(self.driver, self.wait)
        addFloor = AddNewFloorPage(self.driver, self.wait)

        # wait until the room list page is loaded successfully
        self.wait.until(EC.title_contains("Room List"))
        assert "Atlona Velocity | Room List" in self.driver.title

        # Click on the more option button
        roomList.clickMoreButton1()
        # Click on the add new floor option
        flrHamburger.clickAddNewFloor()
        addFloor.createOneFloor(f_name)
        time.sleep(1)
        # Verify if the added room is visible
        assert roomList.visibilityOfFloor2() is True

    def addRoom(self, r_name):
        self.roomList = RoomListPage(self.driver, self.wait)
        self.flrHamburger = FloorHamburgerMenu(self.driver, self.wait)
        self.addRoom = AddRoomPage(self.driver, self.wait)

        # Click on the more option button
        self.roomList.clickMoreButton2()
        time.sleep(2)
        # Click on the add new room option
        self.flrHamburger.clickAddRoom()
        time.sleep(1)
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Room Modify"))
        assert "Atlona Velocity | Room Modify" in self.driver.title
        self.addRoom.createRoom(r_name)
        time.sleep(1)
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Room Modify Devices"))
        assert "Atlona Velocity | Room Modify Devices" in self.driver.title

    def addTechnology(self, dev_name):
        self.modifyDevices = RoomModifyDevicesPage(self.driver, self.wait)
        self.techList = TechnologyListPage(self.driver, self.wait)

        # wait until the modify room page is loaded successfully
        self.wait.until(EC.title_contains("Room Modify Devices"))
        assert "Atlona Velocity | Room Modify Devices" in self.driver.title

        # Click on the add technology button
        self.modifyDevices.clickAddTechnologyButton()
        # Search for a product and add that to the device list
        self.techList.addDevice(dev_name)
        # Click on the close button
        self.techList.clickCloseList()
        time.sleep(2)
        # Verify if the added technology is visible
        assert self.modifyDevices.visibilityOfDevice_1() is True
