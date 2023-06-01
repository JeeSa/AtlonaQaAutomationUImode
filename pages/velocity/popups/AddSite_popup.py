import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class AddSitePopup:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    SITE_NAME_FIELD = "qa-636344ff3e2fc3b02007fc06"
    COUNTRY_DROPDOWN = "//*[@id=\"qa-6363453a612d1c03793c03ff\"]/div[1]/button"
    COUNTRY_VALUE = "/html/body/div[5]/div/div/div/div[231]/span/div/div/div"
    COUNTRY_VALUE_AMS = "/html/body/div[6]/div/div/div/div[231]/span/div/div/div"
    ADDRESS1_FIELD = "qa-63634565488b56ea6837817f"
    ADDRESS2_FIELD = "qa-63634583c557624f05c82575"
    CITY_FIELD = "qa-636345b49bc675eb4effc257"
    POSTCODE_FIELD = "qa-636345d43e31f0c05b5ae9c4"
    STATE_DROPDOWN = "/html/body/div[4]/div/div[1]/div/div/div[1]/div/div[7]/div[2]/div[1]/button"
    STATE_DROPDOWN_AMS = "/html/body/div[5]/div/div[1]/div/div/div[1]/div/div[7]/div[2]/div[1]/button"
    STATE_VALUE = "/html/body/div[5]/div/div/div/div[5]/span/div/div/div"
    STATE_VALUE_AMS = "/html/body/div[6]/div/div/div/div[5]/span/div/div/div"
    BUILDING_IMAGE_DROPDOWN = "/html/body/div[4]/div/div[1]/div/div/div[1]/div/div[8]/div[1]/div[1]/button"
    BUILDING_IMAGE_DROPDOWN_AMS = "/html/body/div[5]/div/div[1]/div/div/div[1]/div/div[8]/div[1]/div[1]/button"
    BUILDING_IMAGE_VALUE = "/html/body/div[5]/div/div/div/div[25]/span/div/div/div"
    BUILDING_IMAGE_VALUE_AMS = "/html/body/div[6]/div/div/div/div[25]/span/div/div/div"
    SUBMIT_BUTTON = "qa-6363446de8beefafd333ce8d"
    IMPORT_BUTTON = "qa-6363441df4de68850bb52cbd"
    CANCEL_BUTTON = "qa-636342b5a217cedbbe5ea1b7"

    # Get the location of site name
    def getSiteNameField(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.SITE_NAME_FIELD)

    # Provide Site Name
    def enterSiteName(self, site_name):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getSiteNameField())
        self.driver.implicitly_wait(10)
        self.getSiteNameField().send_keys(site_name)

    # Clear Site name Field
    def clearSiteName(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getSiteNameField())
        self.driver.implicitly_wait(10)
        self.getSiteNameField().send_keys(Keys.CONTROL + "a")
        self.getSiteNameField().send_keys(Keys.DELETE)

    # Get the location of country dropdown
    def getCountryDropdown(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.COUNTRY_DROPDOWN)

    # Click on the country dropdown
    def clickCountryDropdown(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getCountryDropdown())
        self.driver.implicitly_wait(10)
        self.getCountryDropdown().click()

    # Get the location of country value
    def getCountryValue(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.COUNTRY_VALUE)

    # Click on the country value
    def clickCountryValue(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getCountryValue())
        self.driver.implicitly_wait(10)
        self.getCountryValue().click()

    def getCountryValueAMS(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.COUNTRY_VALUE_AMS)

    # Click on the country value
    def clickCountryValueAMS(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getCountryValueAMS())
        self.driver.implicitly_wait(10)
        self.getCountryValueAMS().click()

    # Get the location of address 1
    def getAddress1Field(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.ADDRESS1_FIELD)

    # Provide address 1
    def enterAddress1(self, ad1):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getAddress1Field())
        self.driver.implicitly_wait(10)
        self.getAddress1Field().send_keys(ad1)

    # Clear address 1 Field
    def clearAddress1(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getAddress1Field())
        self.driver.implicitly_wait(10)
        self.getAddress1Field().send_keys(Keys.CONTROL + "a")
        self.getAddress1Field().send_keys(Keys.DELETE)

    # Get the location of address 2
    def getAddress2Field(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.ADDRESS2_FIELD)

    # Provide address 1
    def enterAddress2(self, ad2):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getAddress2Field())
        self.driver.implicitly_wait(10)
        self.getAddress2Field().send_keys(ad2)

    # Clear address 2 Field
    def clearAddress2(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getAddress2Field())
        self.driver.implicitly_wait(10)
        self.getAddress2Field().send_keys(Keys.CONTROL + "a")
        self.getAddress2Field().send_keys(Keys.DELETE)

    # Get the location of City
    def getCityField(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.CITY_FIELD)

    # Provide city
    def enterCity(self, city):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getCityField())
        self.driver.implicitly_wait(10)
        self.getCityField().send_keys(city)

    # Clear city Field
    def clearCity(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getCityField())
        self.driver.implicitly_wait(10)
        self.getCityField().send_keys(Keys.CONTROL + "a")
        self.getCityField().send_keys(Keys.DELETE)

    # Get the location of Postcode
    def getPostcodeField(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.POSTCODE_FIELD)

    # Provide postcode
    def enterPostcode(self, p_code):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getPostcodeField())
        self.driver.implicitly_wait(10)
        self.getPostcodeField().send_keys(p_code)

    # Clear city Field
    def clearPostcode(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getPostcodeField())
        self.driver.implicitly_wait(10)

        self.getPostcodeField().send_keys(Keys.CONTROL + "a")
        self.getPostcodeField().send_keys(Keys.DELETE)

    # Get the location of state/ province dropdown
    def getStateDropdown(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.STATE_DROPDOWN)

    # Click on the state/ province dropdown
    def clickStateDropdown(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getStateDropdown())
        self.driver.implicitly_wait(10)
        self.getStateDropdown().click()

    def getStateDropdownAMS(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.STATE_DROPDOWN_AMS)

    # Click on the state/ province dropdown
    def clickStateDropdownAMS(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getStateDropdownAMS())
        self.driver.implicitly_wait(10)
        self.getStateDropdownAMS().click()

    # Get the location of state/ province value
    def getStateValue(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.STATE_VALUE)

    # Click on the state/ province value
    def clickStateValue(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getStateValue())
        self.driver.implicitly_wait(10)
        self.getStateValue().click()

    def getStateValueAMS(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.STATE_VALUE_AMS)

    # Click on the state/ province value
    def clickStateValueAMS(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getStateValueAMS())
        self.driver.implicitly_wait(10)
        self.getStateValueAMS().click()

    # Get the location of building image dropdown
    def getBuildingImageDropdown(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.BUILDING_IMAGE_DROPDOWN)

    # Click on the building image dropdown
    def clickBuildingImageDropdown(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getBuildingImageDropdown())
        self.driver.implicitly_wait(10)
        self.getBuildingImageDropdown().click()

    def getBuildingImageDropdownAMS(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.BUILDING_IMAGE_DROPDOWN_AMS)

    # Click on the building image dropdown
    def clickBuildingImageDropdownAMS(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getBuildingImageDropdownAMS())
        self.driver.implicitly_wait(10)
        self.getBuildingImageDropdownAMS().click()

    # Get the location of building image value
    def getBuildingImageValue(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.BUILDING_IMAGE_VALUE)

    # Click on the building image value
    def clickBuildingImageValue(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getBuildingImageValue())
        self.driver.implicitly_wait(10)
        self.getBuildingImageValue().click()

    def getBuildingImageValueAMS(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.BUILDING_IMAGE_VALUE_AMS)

    # Click on the building image value
    def clickBuildingImageValueAMS(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getBuildingImageValueAMS())
        self.driver.implicitly_wait(10)
        self.getBuildingImageValueAMS().click()

    # Get the location of submit button
    def getSubmitButton(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.SUBMIT_BUTTON)

    # Click on the submit button
    def clickSubmit(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getSubmitButton())
        self.driver.implicitly_wait(10)
        self.getSubmitButton().click()

    # Get the location of import button
    def getImportButton(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.IMPORT_BUTTON)

    # Click on the submit button
    def clickImport(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getImportButton())
        self.driver.implicitly_wait(10)
        self.getImportButton().click()

    # Get the location of cancel button
    def getCancelButton(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.CANCEL_BUTTON)

    # Click on the submit button
    def clickCancel(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getCancelButton())
        self.driver.implicitly_wait(10)
        self.getCancelButton().click()

    # enter all value
    def enterAllTextValues(self, s_nm, ad_1, ad_2, ct_nm, ps_code):
        # Provide Site name
        self.enterSiteName(s_nm)
        time.sleep(1)
        # Provide Address 1
        self.enterAddress1(ad_1)
        time.sleep(1)
        # Provide Address 2
        self.enterAddress2(ad_2)
        time.sleep(1)
        # Provide City
        self.enterCity(ct_nm)
        time.sleep(1)
        # Provide Postcode
        self.enterPostcode(ps_code)
        time.sleep(1)

    # select all dropdown value
    def selectAllDropdownValues(self):
        # Click country dropdown
        self.clickCountryDropdown()
        time.sleep(1)
        # Click country value
        self.clickCountryValue()
        time.sleep(1)
        # Click state/ province dropdown button
        self.clickStateDropdown()
        time.sleep(1)
        # Click state/ province value
        self.clickStateValue()
        time.sleep(1)
        # Click building image dropdown
        self.clickBuildingImageDropdown()
        time.sleep(1)
        # Click building image value
        self.clickBuildingImageValue()
        time.sleep(1)

    def selectAllDropdownValuesAMS(self):
        # Click country dropdown
        self.clickCountryDropdown()
        time.sleep(1)
        # Click country value
        self.clickCountryValueAMS()
        time.sleep(1)
        # Click state/ province dropdown button
        self.clickStateDropdownAMS()
        time.sleep(1)
        # Click state/ province value
        self.clickStateValueAMS()
        time.sleep(1)
        # Click building image dropdown
        self.clickBuildingImageDropdownAMS()
        time.sleep(1)
        # Click building image value
        self.clickBuildingImageValueAMS()
        time.sleep(1)

    # Create new site
    def createSite(self, s_nm, ad_1, ad_2, ct_nm, ps_code):
        # enter values
        self.enterAllTextValues(s_nm, ad_1, ad_2, ct_nm, ps_code)
        # select all dropdown values
        self.selectAllDropdownValues()
        # Click on the submit button
        self.clickSubmit()
        time.sleep(1)

    def createSiteAMS(self, s_nm, ad_1, ad_2, ct_nm, ps_code):
        # enter values
        self.enterAllTextValues(s_nm, ad_1, ad_2, ct_nm, ps_code)
        # select all dropdown values
        self.selectAllDropdownValuesAMS()
        # Click on the submit button
        self.clickSubmit()
        time.sleep(1)


    # Visibility of add site page
    def visibilityOfAddSitePage(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getSiteNameField())
        self.driver.implicitly_wait(10)
        if self.getSiteNameField().is_displayed():
            return True
        else:
            return False


    # Clear all text fields
    def clearAllText(self):
        # clear Site name
        self.clearSiteName()
        time.sleep(1)
        # clear address 1
        self.clearAddress1()
        time.sleep(1)
        # clear address 2
        self.clearAddress2()
        time.sleep(1)
        # clear city
        self.clearCity()
        time.sleep(1)
        # clear Postcode
        self.clearPostcode()
        time.sleep(1)

