import pytest
from selene.support.shared import browser


'''Tests without parametrization with different fixtures'''


def test_desktop_sign_in(desktop_browser_management):
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-in').click()


def test_mobile_sign_in(mobile_browser_management):
    browser.open('https://github.com/')
    browser.element('.Button--link').click()
    browser.element('[href="/login"]').click()


'''Parametrized tests'''


@pytest.mark.parametrize('window_height,window_width',
                         [pytest.param(1080, 1920, id='Sign in on desktop'),
                          pytest.param(914, 412, id='Sing in on mobile')])
def test_sign_in_on_desktop_and_mobile(window_height, window_width):
    if window_height == 1080:
        browser.config.window_height = 1080
        browser.config.window_width = 1920
        browser.open('https://github.com/')
        browser.element('.HeaderMenu-link--sign-in').click()
    else:
        browser.config.window_height = 914
        browser.config.window_width = 412
        browser.open('https://github.com/')
        browser.element('.Button--link').click()
        browser.element('[href="/login"]').click()


@pytest.mark.parametrize('window_height,window_width',
                         [pytest.param(1080, 1920),
                          pytest.param(914, 412)])
def test_only_desktop_sign_in(window_height, window_width):
    if window_height == 914:
        pytest.skip('Skip mobile tests')
    browser.config.window_height = window_height
    browser.config.window_width = window_width
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-in').click()


@pytest.mark.parametrize('window_height,window_width',
                         [pytest.param(1080, 1920, marks=pytest.mark.skip('Skip desktop tests')),
                          pytest.param(914, 412)])
def test_only_mobile_sign_in(window_height, window_width):
    browser.config.window_height = window_height
    browser.config.window_width = window_width
    browser.open('https://github.com/')
    browser.element('.Button--link').click()
    browser.element('[href="/login"]').click()


'''Parametrization with indirect'''


@pytest.mark.parametrize('browser_window_size', ['1080*1920'], indirect=True)
def test_desktop_sign_in_with_indirect(browser_window_size):
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-in').click()


@pytest.mark.parametrize('browser_window_size', ['914*412'], indirect=True)
def test_mobile_sign_in_with_indirect(browser_window_size):
    browser.open('https://github.com/')
    browser.element('.Button--link').click()
    browser.element('[href="/login"]').click()