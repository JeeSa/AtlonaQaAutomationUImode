import time

from selenium.webdriver.common.by import By


class LeftBarMenu:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    PIN_ICON = "/html/body/div[1]/div[2]/div/div[1]/div/div/div/div/button"
    HOME = "anchor-/#/home"
    CONTROL = "/html/body/div[1]/div[2]/div/div[2]/div/div/ul/li[2]/a"
    CON_ALL_ROOMS = "/html/body/div[1]/div[2]/div/div[2]/div/div/ul/li[2]/ul/li[1]/a"
    CON_DEVICE_DRIVERS = "anchor-/#/equipmentList"
    CON_DEVICE_GROUPS = "anchor-/#/deviceGroupList"
    SCHEDULING = "/html/body/div[1]/div[2]/div/div[2]/div/div/ul/li[3]/a"
    SCH_ALL_ROOMS = "/html/body/div[1]/div[2]/div/div[2]/div/div/ul/li[3]/ul/li[1]/a"
    SCH_SCHEDULING_TEMPLATES = "anchor-/#/schedulingTemplate"
    SCH_MANAGE = "anchor-/#/calendarIntegrationList"
    SCH_ALL_ROOM_SCHEDULE = "anchor-/#/schedulingAllRooms"
    MANAGEMENT = "/html/body/div[1]/div[2]/div/div[2]/div/div/ul/li[4]/a"
    MNG_AMS_DEVICE_MANAGER = "anchor-/#/atlonaDevices"
    MNG_ROOM_SUPPORT_TICKETS = "anchor-/#/ticketList"
    REPORTS = "/html/body/div[1]/div[2]/div/div[2]/div/div/ul/li[5]/a"
    REP_ALL_DEVICES = "anchor-/#/allDevices"
    REP_ALL_MACROS = "anchor-/#/allMacros"
    REP_BILL_OF_MATERIALS = "anchor-/#/billOfMaterials"
    REP_ROOM_PROBLEMS = "anchor-/#/reportRoomProblem"
    SETTINGS = "/html/body/div[1]/div[2]/div/div[2]/div/div/ul/li[6]/a"
    SET_GATEWAY = "/html/body/div[1]/div[2]/div/div[2]/div/div/ul/li[6]/ul/li[1]/a"
    SET_DATABASE = "/html/body/div[1]/div[2]/div/div[2]/div/div/ul/li[6]/ul/li[2]/a"
    SET_LICENSES = "/html/body/div[1]/div[2]/div/div[2]/div/div/ul/li[6]/ul/li[3]/a"
    SET_TOOLS = "/html/body/div[1]/div[2]/div/div[2]/div/div/ul/li[6]/ul/li[4]/a"
    SET_EMAIL = "/html/body/div[1]/div[2]/div/div[2]/div/div/ul/li[6]/ul/li[5]/a"
    SET_SECURITY = "/html/body/div[1]/div[2]/div/div[2]/div/div/ul/li[6]/ul/li[6]/a"
    SET_ROOM_SUPPORT = "/html/body/div[1]/div[2]/div/div[2]/div/div/ul/li[6]/ul/li[7]/a"
    SET_NETWORK = "/html/body/div[1]/div[2]/div/div[2]/div/div/ul/li[6]/ul/li[8]/a"
    CLOUD = "/html/body/div[1]/div[2]/div/div[2]/div/div/ul/li[7]/a"
    HELP = "/html/body/div[1]/div[2]/div/div[2]/div/div/ul/li[8]/a"
    HLP_MANUAL = "/html/body/div[1]/div[2]/div/div[2]/div/div/ul/li[8]/ul/li[1]/a"
    HLP_TRAINING = "/html/body/div[1]/div[2]/div/div[2]/div/div/ul/li[8]/ul/li[2]/a"
    HLP_VIDEOS = "/html/body/div[1]/div[2]/div/div[2]/div/div/ul/li[8]/ul/li[3]/a"
    HLP_SUPPORT = "/html/body/div[1]/div[2]/div/div[2]/div/div/ul/li[8]/ul/li[4]/a"
    HLP_FAQS = "/html/body/div[1]/div[2]/div/div[2]/div/div/ul/li[8]/ul/li[5]/a"
    HLP_ABOUT = "anchor-About"

    # Get the location of Pin icon
    def getPinIcon(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.PIN_ICON)

    # Click on pin icon
    def clickPinIcon(self):
        time.sleep(1)
        self.getPinIcon().click()

    # Get the location of Home
    def getHome(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.HOME)

    # Click on Home
    def clickHome(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getHome())
        time.sleep(1)
        self.getHome().click()

    # Get the location of Control
    def getControl(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.CONTROL)

    # Click on control
    def clickControl(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getControl())
        time.sleep(1)
        self.getControl() .click()

    # Get the location of all rooms from control sub list
    def getCon_allRooms(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.CON_ALL_ROOMS)

    # Click on all rooms from control sub list
    def clickCon_allRooms(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getCon_allRooms())
        time.sleep(1)
        self.getCon_allRooms().click()

    # Get the location of device drivers from control sub list
    def getCon_deviceDrivers(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.CON_DEVICE_DRIVERS)

    # Click on Home
    def clickCon_deviceDrivers(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getCon_deviceDrivers())
        time.sleep(1)
        self.getCon_deviceDrivers().click()

    # Get the location of device groups from control sub list
    def getCon_deviceGroups(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.CON_DEVICE_GROUPS)

    # Click on Home
    def clickCon_deviceGroups(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getCon_deviceGroups())
        time.sleep(1)
        self.getCon_deviceGroups().click()

    # Get the location of scheduling
    def getScheduling(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SCHEDULING)

    # Click on scheduling
    def clickScheduling(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getScheduling())
        time.sleep(1)
        self.getScheduling().click()

    # Get the location of all rooms from scheduling sub list
    def getSch_allRooms(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SCH_ALL_ROOMS)

    # Click on all rooms from scheduling sub list
    def clickSch_allRooms(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getSch_allRooms())
        time.sleep(1)
        self.getSch_allRooms().click()

    # Get the location of scheduling templates from scheduling sub list
    def getSch_schedulingTemplates(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.SCH_SCHEDULING_TEMPLATES)

    # Click on scheduling templates from scheduling sub list
    def clickSch_schedulingTemplates(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getSch_schedulingTemplates())
        time.sleep(1)
        self.getSch_schedulingTemplates().click()

    # Get the location of manage from scheduling sub list
    def getSch_manage(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.SCH_MANAGE)

    # Click on manage from scheduling sub list
    def clickSch_manage(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getSch_manage())
        time.sleep(1)
        self.getSch_manage().click()

    # Get the location of all room schedule from scheduling sub list
    def getSch_allRoomSchedule(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.SCH_ALL_ROOM_SCHEDULE)

    # Click on all room schedule from scheduling sub list
    def clickSch_allRoomSchedule(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getSch_allRoomSchedule())
        time.sleep(1)
        self.getSch_allRoomSchedule().click()

    # Get the location of management
    def getManagement(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.MANAGEMENT)

    # Click on management
    def clickManagement(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getManagement())
        time.sleep(1)
        self.getManagement().click()

    # Get the location of AMS device manager from management sub list
    def getMng_amsDeviceManager(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.MNG_AMS_DEVICE_MANAGER)

    # Click on AMS device manager from management sub list
    def clickMng_amsDeviceManager(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getMng_amsDeviceManager())
        time.sleep(1)
        self.getMng_amsDeviceManager().click()

    # Get the location of Room Support tickets from management sub list
    def getMng_roomSupportTickets(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.MNG_ROOM_SUPPORT_TICKETS)

    # Click on Room Support tickets from management sub list
    def clickMng_roomSupportTickets(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getMng_roomSupportTickets())
        time.sleep(1)
        self.getMng_roomSupportTickets().click()

    # Get the location of reports
    def getReports(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.REPORTS)

    # Click on reports
    def clickReports(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getReports())
        time.sleep(1)
        self.getReports().click()

    # Get the location of all devices from reports sub list
    def getRep_allDevices(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.REP_ALL_DEVICES)

    # Click on all devices from reports sub list
    def clickRep_allDevices(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getRep_allDevices())
        time.sleep(1)
        self.getRep_allDevices().click()

    # Get the location of all macros from reports sub list
    def getRep_allMacros(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.REP_ALL_MACROS)

    # Click on all macros from reports sub list
    def clickRep_allMacros(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getRep_allMacros())
        time.sleep(1)
        self.getRep_allMacros().click()

    # Get the location of bill of materials from reports sub list
    def getRep_billOfMaterials(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.REP_BILL_OF_MATERIALS)

    # Click on bill of materials from reports sub list
    def clickRep_billOfMaterials(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getRep_billOfMaterials())
        time.sleep(1)
        self.getRep_billOfMaterials().click()

    # Get the location of room problems from reports sub list
    def getRep_roomProblems(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.REP_ROOM_PROBLEMS)

    # Click on room problems from reports sub list
    def clickRep_roomProblems(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getRep_roomProblems())
        time.sleep(1)
        self.getRep_roomProblems().click()

    # Get the location of settings
    def getSettings(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SETTINGS)

    # Click on settings
    def clickSettings(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getSettings())
        time.sleep(1)
        self.getSettings().click()

    # Get the location of gateway from settings sub list
    def getSet_gateway(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SET_GATEWAY)

    # Click on gateway from settings sub list
    def clickSet_gateway(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getSet_gateway())
        time.sleep(1)
        self.getSet_gateway().click()

    # Get the location of database from settings sub list
    def getSet_database(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SET_DATABASE)

    # Click on database from settings sub list
    def clickSet_database(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getSet_database())
        time.sleep(1)
        self.getSet_database().click()

    # Get the location of licenses from settings sub list
    def getSet_licenses(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SET_LICENSES)

    # Click on licenses from settings sub list
    def clickSet_licenses(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getSet_licenses())
        time.sleep(1)
        self.getSet_licenses().click()

    # Get the location of tools from settings sub list
    def getSet_tools(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SET_TOOLS)

    # Click on tools from settings sub list
    def clickSet_tools(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getSet_tools())
        time.sleep(1)
        self.getSet_tools().click()

    # Get the location of email from settings sub list
    def getSet_email(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SET_EMAIL)

    # Click on email from settings sub list
    def clickSet_email(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getSet_email())
        time.sleep(1)
        self.getSet_email().click()

    # Get the location of security from settings sub list
    def getSet_security(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SET_SECURITY)

    # Click on security from settings sub list
    def clickSet_security(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getSet_security())
        time.sleep(1)
        self.getSet_security().click()

    # Get the location of room support from settings sub list
    def getSet_roomSupport(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SET_ROOM_SUPPORT)

    # Click on room support from settings sub list
    def clickSet_roomSupport(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getSet_roomSupport())
        time.sleep(1)
        self.getSet_roomSupport().click()

    # Get the location of network from settings sub list
    def getSet_network(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.SET_NETWORK)

    # Click on network from settings sub list
    def clickSet_network(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getSet_network())
        time.sleep(1)
        self.getSet_network().click()

    # Get the location of cloud
    def getCloud(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.CLOUD)

    # Click on Cloud
    def clickCloud(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getCloud())
        time.sleep(1)
        self.getCloud().click()

    # Get the location of help
    def getHelp(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.HELP)

    # Click on help
    def clickHelp(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getHelp())
        time.sleep(1)
        self.getHelp().click()

    # Get the location of manual from help sub list
    def getHlp_manual(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.HLP_MANUAL)

    # Click on manual from help sub list
    def clickHlp_manual(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getHlp_manual())
        time.sleep(1)
        self.getHlp_manual().click()

    # Get the location of training from help sub list
    def getHlp_training(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.HLP_TRAINING)

    # Click on training from help sub list
    def clickHlp_training(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getHlp_training())
        time.sleep(1)
        self.getHlp_training().click()

    # Get the location of videos from help sub list
    def getHlp_videos(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.HLP_VIDEOS)

    # Click on videos from help sub list
    def clickHlp_videos(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getHlp_videos())
        time.sleep(1)
        self.getHlp_videos().click()

    # Get the location of support from help sub list
    def getHlp_support(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.HLP_SUPPORT)

    # Click on support from help sub list
    def clickHlp_support(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getHlp_support())
        time.sleep(1)
        self.getHlp_support().click()

    # Get the location of faqs from help sub list
    def getHlp_faqs(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.HLP_FAQS)

    # Click on faqs from help sub list
    def clickHlp_faqs(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getHlp_faqs())
        time.sleep(1)
        self.getHlp_faqs().click()

    # Get the location of about from help sub list
    def getHlp_about(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.HLP_ABOUT)

    # Click on Home
    def clickHlp_about(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getHlp_about())
        time.sleep(1)
        self.getHlp_about().click()
