import time

import pytest

from pages.velocity.Home_Page import HomePage
from pages.velocity.popups.AddSite_popup import AddSitePopup
from utilities.utils import Utils


@pytest.mark.usefixtures("setup")
class TestNegativeCasesAddSite:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.driver, self.wait)
        self.home = HomePage(self.driver, self.wait)
        self.addSiteForm = AddSitePopup(self.driver, self.wait)

    def test_negativeCases_addSite_01(self):
        # Case 1: Hit the Submit button when all the required fields are blank

        # Login to the velocity app
        self.ut.login()
        # Click on the add site button
        self.home.clickAddSiteButton()
        # Click on the submit button
        self.addSiteForm.clickSubmit()
        time.sleep(3)
        # Verify if the add site page is still visible
        assert self.addSiteForm.visibilityOfAddSitePage() is True

    def test_negativeCases_addSite_02(self):
        # Case 2: Hit the Submit button when both state/ province and building image fields are blank

        # enter all values
        self.addSiteForm.enterAllTextValues("Atlona", "Atlona Incorporated", "70 Daggett Drive", "San Jose", "95134")
        time.sleep(1)
        # Click on the submit button
        self.addSiteForm.clickSubmit()
        time.sleep(3)
        # Verify if the site page is still visible
        assert self.addSiteForm.visibilityOfAddSitePage() is True

    def test_negativeCases_addSite_03(self):
        # Case 3: Hit the Submit button when only site name field is blank

        # clear all values
        self.addSiteForm.clearAllText()
        time.sleep(1)
        # enter all values
        self.addSiteForm.enterAllTextValues("Atlona", "Atlona Incorporated", "70 Daggett Drive", "San Jose", "95134")
        time.sleep(1)
        # select all dropdown values
        self.addSiteForm.selectAllDropdownValues()
        time.sleep(1)
        # Clear the site name
        self.addSiteForm.clearSiteName()
        time.sleep(1)
        # Click on the submit button
        self.addSiteForm.clickSubmit()
        time.sleep(1)
        # Verify if the site page is still visible
        assert self.addSiteForm.visibilityOfAddSitePage() is True

    def test_negativeCases_addSite_04(self):
        # Case 4: Hit the Submit button when only address 1 field is blank

        # clear all values
        self.addSiteForm.clearAllText()
        time.sleep(1)
        # enter all values
        self.addSiteForm.enterAllTextValues("Atlona", "Atlona Incorporated", "70 Daggett Drive", "San Jose", "95134")
        time.sleep(1)
        # Clear address
        self.addSiteForm.clearAddress1()
        time.sleep(1)
        # Click on the submit button
        self.addSiteForm.clickSubmit()
        time.sleep(1)
        # Verify if the site page is still visible
        assert self.addSiteForm.visibilityOfAddSitePage() is True

    def test_negativeCases_addSite_05(self):
        # Case 5: Hit the Submit button when only city field is blank

        # clear all values
        self.addSiteForm.clearAllText()
        time.sleep(1)
        # enter all values
        self.addSiteForm.enterAllTextValues("Atlona", "Atlona Incorporated", "70 Daggett Drive", "San Jose", "95134")
        time.sleep(1)
        # Clear City
        self.addSiteForm.clearCity()
        time.sleep(1)
        # Click on the submit button
        self.addSiteForm.clickSubmit()
        time.sleep(1)
        # Verify if the site page is still visible
        assert self.addSiteForm.visibilityOfAddSitePage() is True

    def test_negativeCases_addSite_06(self):
        # Case 6: Hit the Submit button when only postcode field is blank

        # clear all values
        self.addSiteForm.clearAllText()
        time.sleep(1)
        # enter all values
        self.addSiteForm.enterAllTextValues("Atlona", "Atlona Incorporated", "70 Daggett Drive", "San Jose", "95134")
        time.sleep(1)
        # Clear Postcode
        self.addSiteForm.clearPostcode()
        time.sleep(1)
        # Click on the submit button
        self.addSiteForm.clickSubmit()
        time.sleep(1)
        # Verify if the site page is still visible
        assert self.addSiteForm.visibilityOfAddSitePage() is True


