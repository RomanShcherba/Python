from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.products_page import ProductsPage
from utils.test_data import TestData



def test_add_to_cart(driver):
        main_page = MainPage(driver)
        main_page.enter_search_text(TestData.search_input)
        main_page.click_search_button()
        products_page = ProductsPage(driver)
        products_page.click_to_product()
        product_page = ProductPage(driver)
        product_page.buy_button()
        product_page.open_cart_button()
        product_page.get_pop_up_cart()
        actual_message = products_page.get_pop_up_cart()
        expected_message = TestData.product_name
        assert actual_message == expected_message