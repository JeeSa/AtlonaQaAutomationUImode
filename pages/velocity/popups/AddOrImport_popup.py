import time

from selenium.webdriver.common.by import By


class AddOrImportPopup:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    ADD_VIA_FORM = "/html/body/div[5]/div/div[1]/div/div/div/div/div/div/div[1]/div"
    IMPORT_AND_UPLOAD = "/html/body/div[5]/div/div[1]/div/div/div/div/div/div/div[2]/div"

    # Get the location of Home
    def getAddViaForm(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.ADD_VIA_FORM)

    # Click on cancel
    def clickAddViaForm(self):
        time.sleep(1)
        self.getAddViaForm().click()

    # Get the location of Submit
    def getImportAndUpload(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.IMPORT_AND_UPLOAD)

    # Click on cancel
    def clickImportAndUpload(self):
        time.sleep(1)
        self.getImportAndUpload().click()

    # Visibility of added technology
    def visibilityOfAddPopup(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.getAddViaForm())
        time.sleep(1)
        if self.getAddViaForm().is_displayed():
            return True
        else:
            return False
