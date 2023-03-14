from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        # self.should_be_product_page_url()
        self.should_be_add_to_basket_button()

    # def should_be_product_page_url(self):
    #     assert "?promo=newYear" in self.browser.current_url, "Not a product page url"

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "No 'Add to basket' button"

    def click_add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def product_name_should_be_correct(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text in self.browser.find_element(
            *ProductPageLocators.SUCCESS_ALERT).text, "Wrong product name !!!"

    def product_price_should_be_correct(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text in self.browser.find_element(
            *ProductPageLocators.BASKET_ALERT).text, "Wrong price !!!"
