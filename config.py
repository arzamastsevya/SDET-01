from selenium import webdriver

class test_config:

    server_name = "https://www.ecwid.ru/"
    browser = webdriver.Firefox()
    browser.set_window_position(0, 0)
    browser.set_window_size(1280, 1080)