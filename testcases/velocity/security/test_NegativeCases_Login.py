import pytest
from pages.velocity.security.Login_Page import LoginPage
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestNegativeCasesLogin:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.loginFlow = LoginPage(self.driver, self.wait)

    def test_negative_login_cases_01(self):
        # Case 1: Hit the Login button when both username and password fields are blank

        # wait until the page loaded successfully
        self.wait.until(EC.title_contains("Login"))
        # Verify the page title
        assert "Atlona Velocity | Login To The System" in self.driver.title

        # Login to the app
        self.loginFlow.clickLogin()

        # Verify remaining on the login page after unsuccessful logging attempt
        assert "Atlona Velocity | Login To The System" in self.driver.title

    def test_negative_login_cases_02(self):
        # Case 2: Hit the Login button when only username field is blank

        # wait until Login page loaded successfully
        self.wait.until(EC.title_contains("Login"))
        # Verify the page after launching the Velocity App
        assert "Atlona Velocity | Login To The System" in self.driver.title

        # Provide Password
        self.loginFlow.enterPassword("123456A.a")
        # Login to the app
        self.loginFlow.clickLogin()

        # Verify remaining on the login page after unsuccessful logging attempt
        assert "Atlona Velocity | Login To The System" in self.driver.title

    def test_negative_login_cases_03(self):
        # Case 3: Hit the Login button when only password field is blank

        # wait until Login page loaded successfully
        self.wait.until(EC.title_contains("Login"))
        # Verify the page after launching the Velocity App
        assert "Atlona Velocity | Login To The System" in self.driver.title

        # Provide Username
        self.loginFlow.enterUsername("sharmin.jeesa@atlona.com")
        # Clear previous Password
        self.loginFlow.clearPassword()
        # Login to the app
        self.loginFlow.clickLogin()

        # Verify remaining on the login page after unsuccessful logging attempt
        assert "Atlona Velocity | Login To The System" in self.driver.title

    def test_negative_login_cases_04(self):
        # Case 4: Hit the Login button when both username and password are wrong

        # wait until Login page loaded successfully
        self.wait.until(EC.title_contains("Login"))
        # Verify the page after launching the Velocity App
        assert "Atlona Velocity | Login To The System" in self.driver.title

        # Clear previous Username
        self.loginFlow.clearAllData()

        # Provide all the required data and hit the login button
        self.loginFlow.loginMethod("sharmi.jees@atlona.co", "123456")

        # Verify remaining on the login page after unsuccessful logging attempt
        assert "Atlona Velocity | Login To The System" in self.driver.title

    def test_negative_login_cases_05(self):
        # Case 5: Hit the Login button when only the username is wrong

        # wait until Login page loaded successfully
        self.wait.until(EC.title_contains("Login"))
        # Verify the page after launching the Velocity App
        assert "Atlona Velocity | Login To The System" in self.driver.title

        # Clear previous Username
        self.loginFlow.clearAllData()

        # Provide all the required data and hit the login button
        self.loginFlow.loginMethod("sharmi.jees@atlona.co", "123456A.a")

        # Verify remaining on the login page after unsuccessful logging attempt
        assert "Atlona Velocity | Login To The System" in self.driver.title

    def test_negative_login_cases_06(self):
        # Case 6: Hit the Login button when only the password is wrong

        # wait until Login page loaded successfully
        self.wait.until(EC.title_contains("Login"))
        # Verify the page after launching the Velocity App
        assert "Atlona Velocity | Login To The System" in self.driver.title

        # Clear previous Username
        self.loginFlow.clearAllData()

        # Provide all the required data and hit the login button
        self.loginFlow.loginMethod("sharmin.jeesa@atlona.com", "123456")

        # Verify remaining on the login page after unsuccessful logging attempt
        assert "Atlona Velocity | Login To The System" in self.driver.title
