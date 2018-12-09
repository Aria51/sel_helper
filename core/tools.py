from core import config
from core.elements import SmartElement


def visit(url):
    config.browser.get(url)


def s(locator):
    return SmartElement(locator)


def ss(locator):
    return SmartElementCollection(locator)
