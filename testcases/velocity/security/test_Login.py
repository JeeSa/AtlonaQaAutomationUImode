import pytest
from utilities.utils import Utils


@pytest.mark.usefixtures("setup")
class TestLogin:
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utils(self.driver, self.wait)

    def test_login(self):
        self.ut.login()
