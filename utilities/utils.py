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
from pages.velocity.sites.BuildingModify_Page import BuildingModifyPage
from pages.velocity.sites.Buildings_Page import BuildingsPage
from pages.velocity.sites.ConfigureEquipment_Page import ConfigureEquipmentPage
from pages.velocity.sites.CopyRoom_Page import CopyRoomPage
from pages.velocity.sites.EditFloor_Page import EditFloorPage
from pages.velocity.sites.RoomList_Page import RoomListPage
from pages.velocity.sites.RoomModifyDevices_Page import RoomModifyDevicesPage
from pages.velocity.sites.RoomModify_Page import RoomModifyPage
from pages.velocity.sites.SiteModify_Page import SiteModifyPage
from pages.velocity.sites.Sites_Page import SitesPage
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

    def addSite(self, s_nm, ad_1, ad_2, ct_nm, ps_code):
        home = HomePage(self.driver, self.wait)
        addSiteForm = AddSitePopup(self.driver, self.wait)

        # wait until the login is successful
        self.wait.until(EC.title_contains("Dashboard"))
        # Verify the page after logging into the Velocity App
        assert "Atlona Velocity | Dashboard" in self.driver.title

        # Click on the add site button
        home.clickAddSiteButton()
        # Create New Site
        addSiteForm.createSite(s_nm, ad_1, ad_2, ct_nm, ps_code)
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
        buildings = BuildingsPage(self.driver, self.wait)
        addBuildingForm = AddBuildingPage(self.driver, self.wait)
        addImport = AddOrImportPopup(self.driver, self.wait)

        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Buildings"))
        assert "Atlona Velocity | Buildings" in self.driver.title

        # Click on the add building button
        buildings.clickAddBuildingButton()
        # Click add via form
        addImport.clickAddViaForm()

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
        roomList = RoomListPage(self.driver, self.wait)
        flrHamburger = FloorHamburgerMenu(self.driver, self.wait)
        addRoom = AddRoomPage(self.driver, self.wait)

        # Click on the more option button
        roomList.clickMoreButton2()
        time.sleep(2)
        # Click on the add new room option
        flrHamburger.clickAddRoom()
        time.sleep(1)
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Room Modify"))
        assert "Atlona Velocity | Room Modify" in self.driver.title
        addRoom.createRoom(r_name)
        time.sleep(1)
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Room Modify Devices"))
        assert "Atlona Velocity | Room Modify Devices" in self.driver.title

    def addTechnology(self, dev_name):
        modifyDevices = RoomModifyDevicesPage(self.driver, self.wait)
        techList = TechnologyListPage(self.driver, self.wait)

        # wait until the modify room page is loaded successfully
        self.wait.until(EC.title_contains("Room Modify Devices"))
        assert "Atlona Velocity | Room Modify Devices" in self.driver.title

        # Click on the add technology button
        modifyDevices.clickAddTechnologyButton()
        # Search for a product and add that to the device list
        techList.addDevice(dev_name)
        # Click on the close button
        techList.clickCloseList()
        time.sleep(2)
        # Verify if the added technology is visible
        assert modifyDevices.visibilityOfDevice_1() is True

    def editSiteName(self, s_name):
        sites = SitesPage(self.driver, self.wait)
        siteModify = SiteModifyPage(self.driver, self.wait)

        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Site Modify"))
        assert "Atlona Velocity | Site Modify" in self.driver.title

        # Edit the site name
        siteModify.clearSiteName()
        siteModify.enterSiteName(s_name)
        siteModify.clickSaveButton()
        # wait until the sites page is loaded successfully
        self.wait.until(EC.title_contains("Sites"))
        assert "Atlona Velocity | Sites" in self.driver.title
        actual_sName = sites.passSiteName()
        # Check that the edited name is showing after editing
        assert actual_sName == s_name

    def editBuildingName(self, b_name):
        buildings = BuildingsPage(self.driver, self.wait)
        buildingModify = BuildingModifyPage(self.driver, self.wait)

        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Building Modify"))
        assert "Atlona Velocity | Building Modify" in self.driver.title

        # Edit the building name
        buildingModify.clearBuildingName()
        buildingModify.enterBuildingName(b_name)
        buildingModify.clickSaveButton()
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Buildings"))
        assert "Atlona Velocity | Buildings" in self.driver.title
        actual_bName = buildings.passBuildingName()
        # Check that the edited name is showing after editing
        assert actual_bName == b_name

    def editFloorName(self, f_name):
        roomList = RoomListPage(self.driver, self.wait)
        flrHamburger = FloorHamburgerMenu(self.driver, self.wait)
        editFlr = EditFloorPage(self.driver, self.wait)

        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Room List"))
        assert "Atlona Velocity | Room List" in self.driver.title

        # Click on the more option button
        roomList.clickMoreButton1()
        time.sleep(1)
        # Click on the edit floor option
        flrHamburger.clickEditFloor()
        # Verify if the added room is visible
        assert editFlr.visibilityOfEditFloorPage() is True

        editFlr.clearFloorName()
        editFlr.enterFloorName(f_name)
        editFlr.clickSubmitButton()
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Room List"))
        assert "Atlona Velocity | Room List" in self.driver.title
        time.sleep(1)
        actual_fName = roomList.passFloorName()
        # Check that the edited name is showing after editing
        assert actual_fName == f_name

    def editRoomName(self, r_name):
        roomList = RoomListPage(self.driver, self.wait)
        roomModify = RoomModifyPage(self.driver, self.wait)

        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Room Modify"))
        assert "Atlona Velocity | Room Modify" in self.driver.title

        # Edit room name
        roomModify.clearRoomName()
        roomModify.enterRoomName(r_name)
        roomModify.clickSaveChanges()
        # wait until the room list page is loaded successfully
        self.wait.until(EC.title_contains("Room List"))
        assert "Atlona Velocity | Room List" in self.driver.title
        time.sleep(1)
        actual_rName = roomList.passRoomName()
        # Check that the edited name is showing after editing
        assert actual_rName == r_name

    def editDeviceName(self, d_name):
        modifyDevices = RoomModifyDevicesPage(self.driver, self.wait)
        confEquip = ConfigureEquipmentPage(self.driver, self.wait)

        # wait until the modify room page is loaded successfully
        self.wait.until(EC.title_contains("Room Modify Devices"))
        assert "Atlona Velocity | Room Modify Devices" in self.driver.title

        # Click on the edit device option
        modifyDevices.clickEditDevice()
        time.sleep(1)
        # Verify if the added technology is visible
        assert confEquip.visibilityOfConfHeading() is True

        # Edit device alias
        confEquip.clearAlias()
        confEquip.enterAlias(d_name)
        confEquip.clickSave()
        time.sleep(1)
        actual_dName = modifyDevices.passDeviceName()
        # Check that the edited name is showing after editing
        assert actual_dName == d_name

    def copyFloor(self):
        roomList = RoomListPage(self.driver, self.wait)
        flrHamburger = FloorHamburgerMenu(self.driver, self.wait)

        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Room List"))
        assert "Atlona Velocity | Room List" in self.driver.title

        # Click on the more button
        roomList.clickMoreButton1()
        time.sleep(2)
        # Click on the Copy floor option
        flrHamburger.clickCopyFloor()
        time.sleep(2)
        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Room List"))
        assert "Atlona Velocity | Room List" in self.driver.title
        # Verify if the copied floor is visible
        assert roomList.visibilityOfFloor2() is True

    def copyRoom(self):
        roomList = RoomListPage(self.driver, self.wait)
        copyRoom = CopyRoomPage(self.driver, self.wait)

        # wait until the page is loaded successfully
        self.wait.until(EC.title_contains("Room List"))
        assert "Atlona Velocity | Room List" in self.driver.title

        # Click on the Copy button
        roomList.clickCopyRoom1Button()
        time.sleep(2)
        # Verify if the copy room page is visible
        assert copyRoom.visibilityOfCopyRoom() is True
        # Confirm the room copy option
        copyRoom.clickYesButton()
        # wait until the room list page is loaded successfully
        self.wait.until(EC.title_contains("Room List"))
        assert "Atlona Velocity | Room List" in self.driver.title
        # Verify if the copied is visible
        assert roomList.visibilityOfRoom2() is True

    def openNavBar(self):
        home = HomePage(self.driver, self.wait)

        home.clickNavBar()
        # Verify if the sidebar is visible
        assert home.visibilityOfSidebarMenu() is True
