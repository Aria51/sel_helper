from selenium.webdriver.common.keys import Keys
from core.tools import visit
from tests.base_test import *


class TestTodoMVC(BaseTest):

    def test_tasks_life_cycle(self):
        visit()
