from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class RegistrationPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    COMPANY_NAME_FIELD = "CompanyName"
    ADMIN_FIRSTNAME_FIELD = "First"
    ADMIN_LASTNAME_FIELD = "Last"
    ADMIN_EMAIL_FIELD = "Email"
    CONFIRM_EMAIL_FIELD = "EmailConfirm"
    ADMIN_PASSWORD_FIELD = "Password"
    CONFIRM_PASSWORD_FIELD = "ConfirmPassword"
    TIMEZONE_FIELD = "qa-63470f5f66e6ef45bac408ef"
    CONSENT_CHECKBOX = "qa-634730ddc6f67de914b805cc"
    SUBMIT_BUTTON = "qa-63482e819c7f9125f1d6b1a6"

    # Get the location of company name
    def getCompanyName(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.NAME, self.COMPANY_NAME_FIELD)

    # Provide Company Name
    def enterCompanyName(self, comp_name):
        self.getCompanyName().send_keys(comp_name)

    # Clear Company name Field
    def clearCompanyName(self):
            self.getCompanyName().send_keys(Keys.CONTROL + "a")
            self.getCompanyName().send_keys(Keys.DELETE)

    # Get Admin First Name
    def getAdminFirstName(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.NAME, self.ADMIN_FIRSTNAME_FIELD)

    # Provide Admin First Name
    def enterAdminFirstName(self, ad_fname):
        self.getAdminFirstName().send_keys(ad_fname)

    # Clear Admin first name Field
    def clearAdminFirstName(self):
        self.getAdminFirstName().send_keys(Keys.CONTROL + "a")
        self.getAdminFirstName().send_keys(Keys.DELETE)

    # Get admin Last Name
    def getAdminLastName(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.NAME, self.ADMIN_LASTNAME_FIELD)

    # Provide Admin Last Name
    def enterAdminLastName(self, ad_lname):
        self.getAdminLastName().send_keys(ad_lname)

    # Clear Admin last name Field
    def clearAdminLastName(self):
        self.getAdminLastName().send_keys(Keys.CONTROL + "a")
        self.getAdminLastName().send_keys(Keys.DELETE)

    # Get admin Email address
    def getAdminEmail(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.NAME, self.ADMIN_EMAIL_FIELD)

    # Provide Admin email address
    def enterAdminEmail(self, ad_email):
        self.getAdminEmail().send_keys(ad_email)

    # Clear Admin Email Field
    def clearAdminEmail(self):
        self.getAdminEmail().send_keys(Keys.CONTROL + "a")
        self.getAdminEmail().send_keys(Keys.DELETE)

    # Get confirm admin location
    def getConfirmEmail(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.NAME, self.CONFIRM_EMAIL_FIELD)

    # Confirm Admin email
    def enterConfirmEmail(self, conf_ad_email):
        self.getConfirmEmail().send_keys(conf_ad_email)

    # Clear confirm email Field
    def clearConfirmEmail(self):
        self.getConfirmEmail().send_keys(Keys.CONTROL + "a")
        self.getConfirmEmail().send_keys(Keys.DELETE)

    # Get Password Location
    def getAdminPassword(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.NAME, self.ADMIN_PASSWORD_FIELD)

    # Provide Admin password
    def enterAdminPassword(self, ad_pass):
        self.getAdminPassword().send_keys(ad_pass)

    # Clear confirm email Field
    def clearAdminPassword(self):
        self.getAdminPassword().send_keys(Keys.CONTROL + "a")
        self.getAdminPassword().send_keys(Keys.DELETE)

    # Get Confirm password location
    def getConfirmPassword(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.NAME, self.CONFIRM_PASSWORD_FIELD)

    # Confirm New Admin password
    def enterConfirmPassword(self, conf_ad_pass):
        self.getConfirmPassword().send_keys(conf_ad_pass)

    # Clear confirm email Field
    def clearConfirmPassword(self):
        self.getConfirmPassword().send_keys(Keys.CONTROL + "a")
        self.getConfirmPassword().send_keys(Keys.DELETE)

    # Get Timezone location
    def getTimezone(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.TIMEZONE_FIELD)

    # Select Time zone
    def selectTimeZone(self, select_timezone):
        TimeZone = self.getTimezone()
        TimeZoneDropDown = Select(TimeZone)
        TimeZoneDropDown.select_by_value(select_timezone)

    # Deselect Time zone
    def deselectTimeZone(self, deselect_timezone):
        TimeZone = self.getTimezone()
        TimeZoneDropDown = Select(TimeZone)
        TimeZoneDropDown.deselect_by_value(deselect_timezone)

    # Get Timezone location
    def getConsentBox(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.CONSENT_CHECKBOX)

    # Agree with the Terms and conditions
    def agreeToTnC(self):
        # condition to check if the checkbox is selected or not
        CheckboxStatus = self.getConsentBox().is_selected()
        if CheckboxStatus == False:
            self.getConsentBox().click()

    # disAgree with the Terms and conditions
    def disagreeToTnC(self):
        # condition to check if the checkbox is selected or not
        CheckboxStatus = self.getConsentBox().is_selected()
        if CheckboxStatus == True:
            self.getConsentBox().click()

    # Get submit button
    def getSubmitButton(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.SUBMIT_BUTTON)

    # Submit the form
    def submitForm(self):
        self.getSubmitButton().click()

    def registrationMethod(self, cName, afName, alName, aEmail, confEmail, aPassword, confPassword, sTimeZone):
        # Provide Company Name
        self.enterCompanyName(cName)
        # Provide Admin First Name
        self.enterAdminFirstName(afName)
        # Provide Admin Last Name
        self.enterAdminLastName(alName)
        # Provide Admin email address
        self.enterAdminEmail(aEmail)
        # Confirm Admin email
        self.enterConfirmEmail(confEmail)
        # Provide Admin password
        self.enterAdminPassword(aPassword)
        # Confirm New Admin password
        self.enterConfirmPassword(confPassword)
        # Select Time zone
        self.selectTimeZone(sTimeZone)
        # Agree with the Terms and conditions
        self.agreeToTnC()
        # Submit the form
        self.submitForm()

    def clearAllData(self):
        # Clear all the previous data
        self.clearCompanyName()
        self.clearAdminFirstName()
        self.clearAdminLastName()
        self.clearAdminEmail()
        self.clearConfirmEmail()
        self.clearAdminPassword()
        self.clearConfirmPassword()

