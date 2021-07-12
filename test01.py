import unittest
from search_page import SearchPage
from config import test_config


class TestCase_01(unittest.TestCase):

    URL = test_config.server_name + "demo/search/"
    browser = test_config.browser


    def setUp(self):

        self.search_page = SearchPage(self.browser, self.URL)


    def test_search_item_by_keywords(self):

        self.search_page.goto_site()
        items = self.search_page.get_names_prices()

        for item in items[:4]:
            self.search_page.input_search_word(item[0])
            self.search_page.search_button_click()
            finded = self.search_page.get_names_prices()          
            self.search_page.clear_filters()
            assert item in finded, f"Search request {item} is not in search results"


    def tearDown(self):

        self.browser.quit()


if __name__ == "__main__":
    unittest.main()