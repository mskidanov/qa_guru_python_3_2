import pytest
from selene.support.shared import browser

google_url = 'https://google.com/ncr'

@pytest.fixture()
def browser_open():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open(google_url)
