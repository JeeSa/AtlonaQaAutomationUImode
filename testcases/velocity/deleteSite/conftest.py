import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from utilities.misc import Miscellaneous


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()

    misc = Miscellaneous()
    # launch the Velocity App
    driver.get(misc.gateway())

    # make this driver and wait available to whichever class requests for it
    request.cls.driver = driver
    request.cls.wait = wait

    yield
    driver.close()