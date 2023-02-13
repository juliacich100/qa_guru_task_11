import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function')
def desktop_browser_management():
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    yield
    browser.quit()


@pytest.fixture(scope='function')
def mobile_browser_management():
    browser.config.window_height = 914
    browser.config.window_width = 412
    yield
    browser.quit()


@pytest.fixture(params=['1080*1920', '914*412'], scope='session')
def browser_window_size(request):
    if request.param == '1080*1920':
        browser.config.window_height = 1080
        browser.config.window_width = 1920
    else:
        browser.config.window_height = 914
        browser.config.window_width = 412
    yield
    browser.quit()