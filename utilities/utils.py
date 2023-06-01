from pages.velocity.security.Login_Page import LoginPage
from selenium.webdriver.support import expected_conditions as EC


class Utils:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def login(self):
        # wait until Login page loaded successfully
        self.wait.until(EC.title_contains("Login"))
        # Verify the page after launching the Velocity App
        assert "Atlona Velocity | Login To The System" in self.driver.title
        loginFlow = LoginPage(self.driver, self.wait)

        # Provide all the required data and hit the login button
        loginFlow.loginMethod("qa@atlona.com", "Admin123!")

        # wait until the login is successful
        self.wait.until(EC.title_contains("Dashboard"))
        # Verify the page after logging into the Velocity App
        assert "Atlona Velocity | Dashboard" in self.driver.title

