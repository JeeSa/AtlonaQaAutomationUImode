import pytest
from utilities.utils import Utils


@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_login(self):
        ut = Utils(self.driver, self.wait)
        ut.login()
