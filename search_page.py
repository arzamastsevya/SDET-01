from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from web_page import WebPage


class PageSeacrсhLocators:

    LOCATOR_ITEM_NAME = (By.CLASS_NAME, "grid-product__title")                                           # названия товаров на странице
    LOCATOR_ITEM_PRICE = (By.CLASS_NAME, "grid-product__price")                                          # цены товаров на странице

    LOCATOR_RIGHT_RANGE_RUNNER = (By.CLASS_NAME, "ec-range__runner--right")                              # ползунок максимальной цены
    LOCATOR_LEFT_RANGE_RUNNER = (By.CLASS_NAME, "ec-range__runner--left")                                # ползунок минимальной цены
    LOCATOR_SLIDER = (By.CLASS_NAME, "ec-range__track")                                                  # слайдбар, нам будет нужна его длина

    LOCATOR_FILTER_RIGTH_INPUT = (By.XPATH, "//*[@id=\"ecwid-products\"]/div/div/div/div\
        [2]/div/div[2]/div/div[1]/div/div[2]/div[2]/div[1]/div[1]/div/div\
        [3]/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div[1]/div[3]/input")                            # инпут фильтра максимальной цены

    LOCATOR_FILTER_LEFT_INPUT = (By.XPATH, "//*[@id=\"ecwid-products\"]/div/div/div/div\
        [2]/div/div[2]/div/div[1]/div/div[2]/div[2]/div[1]/div[1]/div/div\
        [3]/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div[1]/div[1]/input")                            # инпут фильтра минимальной цены

    LOCATOR_KEYWORD_INPUT = (By.NAME, "keyword")                                                         # поле ввода для поиска
    LOCATOR_SEARCH_BUTTON = (By.CLASS_NAME, "form-control__ico-btn")                                     # кнопка для активации поиска

    LOCATOR_CLEAR_FILTER = (By.XPATH, "//*[@id=\"ecwid-products\"]/div/div/div/div\
        [2]/div/div[2]/div/div[1]/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div[1]/div/div[2]/a")   # кнопка для сброса фильтра

    LOCATOR_GRID_PRODUCTS = (By.CLASS_NAME, "grid__products")
    LOCATOR_GRID_LOADING = (By.CLASS_NAME, "grid__products--loading")


class SearchPage(WebPage):

    def get_right_range_input(self):
        return self.find_element(PageSeacrсhLocators.LOCATOR_FILTER_RIGTH_INPUT).get_attribute('value')

    def get_left_range_input(self):
        return self.find_element(PageSeacrсhLocators.LOCATOR_FILTER_LEFT_INPUT).get_attribute('value')

    def get_right_range_runner(self):
        return self.find_element(PageSeacrсhLocators.LOCATOR_RIGHT_RANGE_RUNNER)

    def get_left_range_runner(self):
        return self.find_element(PageSeacrсhLocators.LOCATOR_LEFT_RANGE_RUNNER)

    def get_slide_width(self):
        return self.find_element(PageSeacrсhLocators.LOCATOR_SLIDER).size['width']

    def move_right_range_runner(self, percent):
        ActionChains(self.driver).drag_and_drop_by_offset(self.get_right_range_runner(), -(self.get_slide_width()//100)*percent, 0).perform()
        self.find_element_NOT(PageSeacrсhLocators.LOCATOR_GRID_LOADING)
        
    def move_left_range_runner(self, percent):
        ActionChains(self.driver).drag_and_drop_by_offset(self.get_left_range_runner(), (self.get_slide_width()//100)*percent, 0).perform()
        self.find_element_NOT(PageSeacrсhLocators.LOCATOR_GRID_LOADING)

    def input_search_word(self, search_request):
        return self.find_element(PageSeacrсhLocators.LOCATOR_KEYWORD_INPUT).send_keys(search_request)

    def search_button_click(self):
        self.find_element(PageSeacrсhLocators.LOCATOR_SEARCH_BUTTON).click()
        self.find_element_NOT(PageSeacrсhLocators.LOCATOR_GRID_LOADING)

    def clear_filters(self):
        self.find_element(PageSeacrсhLocators.LOCATOR_CLEAR_FILTER).click()
        self.find_element_NOT(PageSeacrсhLocators.LOCATOR_GRID_LOADING)

    def get_names_prices(self):
        item_price_name_list = []
        items_name=self.find_elements(PageSeacrсhLocators.LOCATOR_ITEM_NAME) 
        items_price=self.find_elements(PageSeacrсhLocators.LOCATOR_ITEM_PRICE)
        for item in items_name:
            item_price_name_list.append([item.text, float(items_price[items_name.index(item)].text[1:])])
        item_price_name_list.sort(key=lambda i: i[1])
        return item_price_name_list