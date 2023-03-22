from selenium.webdriver.support import expected_conditions as EC

from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_page_url()
        self.should_be_add_to_basket_button()

    def should_be_product_page_url(self):
        assert "?promo=offer" in self.browser.current_url, "Not a product page url"

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "No 'Add to basket' button"

    def click_add_to_basket(self):
        self.should_be_add_to_basket_button()
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def product_name_should_be_correct(self):
        assert self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME).text + " has been added to your basket." == self.browser.find_element(
            *ProductPageLocators.SUCCESS_ALERT).text, "Wrong product name !!!"

    def product_price_should_be_correct(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text in self.browser.find_element(
            *ProductPageLocators.BASKET_ALERT).text, "Wrong price !!!"

    def added_to_basket_correctly(self):
        self.product_name_should_be_correct()
        self.product_price_should_be_correct()

    def should_not_be_success_message(self):
        assert not self.is_element_present(
            *ProductPageLocators.SUCCESS_ALERT), "Success message present, when it shouldn't"

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def alert_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_ALERT), "Success message did not disappear"
