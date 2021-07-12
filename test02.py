import unittest
from search_page import SearchPage
from config import test_config


class TestCase_02(unittest.TestCase):

    URL = test_config.server_name + "demo/search/"
    browser = test_config.browser

 
    def setUp(self):

        self.search_page = SearchPage(self.browser, self.URL)


    def test_search_item_by_price(self):

        self.search_page.goto_site()
        item_price_name_list = self.search_page.get_names_prices()

        self.search_page.move_right_range_runner(20)
        self.search_page.move_left_range_runner(20)

        filter_right_range = self.search_page.get_right_range_input()
        filter_left_range = self.search_page.get_left_range_input()

        item_price_name_list_ck=[]                                                            # генерируем искусственный список для проверки
        for item in item_price_name_list:
            if (item[1]>float(filter_left_range)) and (item[1]<float(filter_right_range)):
                  item_price_name_list_ck.append(item)

        item_price_name_list = self.search_page.get_names_prices()

        if item_price_name_list != []:
            assert ((item_price_name_list[0][1]>float(filter_left_range)) and (item_price_name_list[-1][1]<float(filter_right_range))), "Search result is not in range"
        assert item_price_name_list == item_price_name_list_ck, "Search results is not match the cheklist"


    def tearDown(self):

        self.browser.quit()


if __name__ == "__main__":
    unittest.main()