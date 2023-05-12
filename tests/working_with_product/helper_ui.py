import allure

from tests.common_helper_ui import CommonHelperUi


class HelperUi(CommonHelperUi):

    @allure.step('We remove the product from the basket')
    def remove_item_from_shopping_cart(self, browser, request):
        self._log_create(request)
        self.element_invisibility(browser, request, '//div[@id="cart"]/ul/li/p')
        self.click(
            browser,
            request,
            '//button[contains(@class,"btn-inverse")]',
            'element_visibility',
        )
        self.click(browser, request, '//button[contains(@class,"btn-danger")]', 'element_visibility')
