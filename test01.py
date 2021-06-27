import unittest
from selenium import webdriver
import time



class TestCaseClass(unittest.TestCase):



    def get_items_names(self, items_name_list):

        items_name_list.clear()
        items=self.browser.find_elements_by_class_name("grid-product__title-inner")   # находим все товары на странице и записываем их названия в список
        for item in items:
            items_name_list.append(item.text)   



    def setUp(self):

        self.browser = webdriver.Firefox()
        browser = self.browser
        browser.set_window_position(0, 0)
        browser.set_window_size(1280, 720)



    def test_search_item_by_keywords(self):

        self.browser.get("https://www.ecwid.ru/demo/search")
        time.sleep(5)  # Ждем загрузку страницы

        #print("Заголовок окна: ", self.browser.title, "\n")
       
        items_name_list = []  # список товаров на первой странице
        self.get_items_names(items_name_list)       

        #print("все элементы: ", items_name_list, "\n")

        search_input_element=self.browser.find_element_by_name("keyword")                        # находим поле ввода для поиска
        search_button_element=self.browser.find_element_by_class_name("form-control__ico-btn")   # находим кнопку для поиска

        finded_items_name_list = []  # список найденных названий товаров

        for item in items_name_list[:4]:                   # прогоняем поиск для каждого элемента списка

            search_input_element.clear()                   # очищаем поле ввода
            time.sleep(1) 
            search_input_element.send_keys(item)           # записываем в поле ввода строку поиска
            time.sleep(1)
            search_button_element.click()                  # жмем кнопку поиска
            time.sleep(1)
            self.get_items_names(finded_items_name_list) 

            #print("Запрос: ", item) 
            #print("Нашлось: ", finded_items_name_list, "\n")
            #print(self.browser.current_url, "\n")
            
            # проверяем что название товара из строки поиска входит в список найденных товаров                                                               
            self.assertIn(item, "".join(finded_items_name_list))  

            finded_items_name_list.clear()                 # очищаем список найденных товаров
            self.browser.back()
            time.sleep(1)



    def tearDown(self):
        self.browser.close()



if __name__ == "__main__":
    unittest.main()