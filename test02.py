import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
import time



class TestCaseClass(unittest.TestCase):



    def get_name_price(self, item_price_name_list):

        item_price_name_list.clear()
        items_name=self.browser.find_elements_by_class_name("grid-product__title-inner")    # находим все названия товаров на странице и записываем их названия в список
        items_price=self.browser.find_elements_by_class_name("grid-product__price-value")   # находим все цены товаров на странице и записываем их цены в список
        for item in items_name:
            item_price_name_list.append([item.text, float(items_price[items_name.index(item)].text[1:])])
        item_price_name_list.sort(key=lambda i: i[1])     



    def setUp(self):

        self.browser = webdriver.Firefox()
        browser = self.browser
        browser.set_window_position(0, 0)
        browser.set_window_size(1280, 1080)


        
    def test_search_item_by_price(self):

        self.browser.get("https://www.ecwid.ru/demo/search")
        time.sleep(5)  # Ждем загрузку страницы

        #print("Заголовок окна: ", self.browser.title, "\n")

        item_price_name_list = []
        self.get_name_price(item_price_name_list)
            
        #print("все элементы: ", item_price_name_list, "\n")

        right_range_element=self.browser.find_element_by_class_name("ec-range__runner--right")                   # находим ползунок максимальной цены
        left_range_element=self.browser.find_element_by_class_name("ec-range__runner--left")                     # находим ползунок минимальной цены
        slider_element_width=self.browser.find_element_by_class_name("ec-range__slider").size['width']           # находим ширину слайдбара
        
        action_chains = ActionChains(self.browser)
        action_chains.drag_and_drop_by_offset(left_range_element, (slider_element_width) // 5, 0).perform()

        time.sleep(1)

        action_chains = ActionChains(self.browser)
        action_chains.drag_and_drop_by_offset(right_range_element, -(slider_element_width) // 5, 0).perform()
        time.sleep(2)

        filter_right_range=self.browser.find_element_by_xpath("//*[@id=\"ecwid-products\"]/div/div/div/div\
        [2]/div/div[2]/div/div[1]/div/div[2]/div[2]/div[1]/div[1]/div/div\
        [3]/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div[1]/div[3]/input").get_attribute('value')

        filter_left_range=self.browser.find_element_by_xpath("//*[@id=\"ecwid-products\"]/div/div/div/div\
        [2]/div/div[2]/div/div[1]/div/div[2]/div[2]/div[1]/div[1]/div/div\
        [3]/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div[1]/div[1]/input").get_attribute('value')

        #print("Цена от", filter_left_range) 
        #print("Цена до", filter_right_range ,"\n")  

        item_price_name_list_ck=[]                                                            # генерируем искусственный список для проверки
        for item in item_price_name_list:
            if (item[1]>float(filter_left_range)) and (item[1]<float(filter_right_range)):
                  item_price_name_list_ck.append(item)

        self.get_name_price(item_price_name_list)
            
        #print("все элементы после фильтра: ", item_price_name_list, "\n")

        if item_price_name_list != []:
            self.assertTrue((item_price_name_list[0][1]>float(filter_left_range)) and 
            (item_price_name_list[-1][1]<float(filter_right_range)))                          # проверка вхождения списка в границы фильтра

        self.assertTrue(item_price_name_list == item_price_name_list_ck)                      # проверка совпадения списка товаров после фильтра и списка для проверки



    def tearDown(self):
        self.browser.close()



if __name__ == "__main__":
    unittest.main()