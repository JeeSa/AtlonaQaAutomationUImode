import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.velocity.security.Registration_Page import RegistrationPage


@pytest.mark.usefixtures("setup")
class TestNegativeCasesRegistration:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.registrationFlow = RegistrationPage(self.driver, self.wait)

    def test_negative_reg_cases_01(self):
        # Case 1: Uncheck the T&C checkbox to verify the invisibility of the Submit button

        # Verify the page after launching the Velocity App
        assert "Atlona" in self.driver.title
        self.driver.implicitly_wait(10)

        # disagree with the Terms and conditions
        self.registrationFlow.disagreeToTnC()
        # Verify if the submit button is invisible
        assert self.wait.until(EC.invisibility_of_element_located((By.ID, "qa-63482e819c7f9125f1d6b1a6")))

    def test_negative_reg_cases_02(self):
        # Case 2: Hit the Submit button when all the fields are blank

        # Verify the page after launching the Velocity App
        assert "Atlona" in self.driver.title
        self.driver.implicitly_wait(10)

        # Agree with the Terms and conditions
        self.registrationFlow.agreeToTnC()
        # Submit the form
        self.registrationFlow.submitForm()
        # Verify remaining on the registration page after unsuccessful registration attempt to the Velocity App
        assert "Atlona" in self.driver.title

    def test_negative_reg_cases_03(self):
        # Case 3: Hit the Submit button When the New admin Password doesn't maintain the password criteria

        # Verify the page after launching the Velocity App
        assert "Atlona" in self.driver.title
        self.driver.implicitly_wait(10)

        # Provide all the required data to register
        self.registrationFlow.registrationMethod("Atlona", "Sharmin", "Jeesa", "sharmin.jeesa@atlona.com", "sharmin.jeesa@atlona.com", "123", "123", "Asia/Dhaka")

        # Verify remaining on the registration page after unsuccessful registration attempt to the Velocity App
        assert "Atlona" in self.driver.title

    def test_negative_reg_cases_04(self):
        # Case 4: Hit the Submit button when the entered passwords are different

        # Verify the page after launching the Velocity App
        assert "Atlona" in self.driver.title
        self.driver.implicitly_wait(10)

        # Clear all the previous data
        self.registrationFlow.clearAllData()

        # Provide all the required data to register
        self.registrationFlow.registrationMethod("Atlona", "Sharmin", "Jeesa", "sharmin.jeesa@atlona.com", "sharmin.jeesa@atlona.com", "12345A.a", "54321", "Asia/Dhaka")

        # Verify remaining on the registration page after unsuccessful registration attempt to the Velocity App
        assert "Atlona" in self.driver.title

    def test_negative_reg_cases_05(self):
        # Case 5: Hit the Submit button when the entered email is invalid

        # Verify the page after launching the Velocity App
        assert "Atlona" in self.driver.title
        self.driver.implicitly_wait(10)

        # Clear all the previous data
        self.registrationFlow.clearAllData()

        # Provide all the required data to register
        self.registrationFlow.registrationMethod("Atlona", "Sharmin", "Jeesa", "sharmin.jeesa*atlona.com", "sharmin.jeesa*atlona.com", "12345A.a", "12345A.a", "Asia/Dhaka")

        # Verify remaining on the registration page after unsuccessful registration attempt to the Velocity App
        assert "Atlona" in self.driver.title

    def test_negative_reg_cases_06(self):
        # Case 6: Hit the Submit button when the entered emails are different

        # Verify the page after launching the Velocity App
        assert "Atlona" in self.driver.title
        self.driver.implicitly_wait(10)

        # Clear all the previous data
        self.registrationFlow.clearAllData()

        # Provide all the required data to register
        self.registrationFlow.registrationMethod("Atlona", "Sharmin", "Jeesa", "sharmin.jeesa@atlona.com", "sharmin.sultana@atlona.com", "12345A.a", "12345A.a", "Asia/Dhaka")

        # Verify remaining on the registration page after unsuccessful registration attempt to the Velocity App
        assert "Atlona" in self.driver.title
