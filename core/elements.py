from core import config

class WaitingFinder(object):

    def finder(self):
        pass

    def __getattr__(self, item):
        return getattr(self.finder(), item)

class SmartElement(WaitingFinder):

    def __init__(self, locator):
        self.locator = locator

    def finder(self):
        return config.browser.find_element_by_css_selector(self.locator)



class SmartElementCollection(WaitingFinder):

    def __init__(self, locator):
        self.locator = locator

    def finder(self):
        return config.browser.find_elements_by_css_selector(self.locator)


