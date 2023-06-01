import pytest
from pages.velocity.security.Registration_Page import RegistrationPage
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestRegistration:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.registrationFlow = RegistrationPage(self.driver, self.wait)

    def test_registration(self):

        # Verify the page after launching the Velocity App
        assert "Atlona" in self.driver.title
        self.driver.implicitly_wait(10)

        # Provide all the required data to register
        self.registrationFlow.registrationMethod("Atlona", "QA", "Automation", "qa@atlona.com", "qa@atlona.com", "Admin123!", "Admin123!", "Asia/Dhaka")

        # wait until the registration is successful
        self.wait.until(EC.title_contains("Dashboard"))
        # Verify the page after successfull registration to the Velocity App
        assert "Atlona Velocity | Dashboard" in self.driver.title
