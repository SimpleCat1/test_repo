class MainLocators:
    dropdown_my_account = "//i[contains(@class,'fa-user')]/ancestor::a/span[@class='caret']"
    dropdown_my_account_register = "//a[contains(@href,'index.php?route=account/register')]"
    dropdown_my_account_login = "//a[contains(@href,'index.php?route=account/login')]"
    dropdown_my_account_logout = "//ul[contains(@class,'dropdown-menu')]//a[contains(@href,'index.php?route=account/logout')]"
    first_product = "//div[contains(@class,'product-thumb')]//img[position()=1]"
    currency_value = "//strong"
    empty_basket = '//div[@id="cart"]/ul/li/p'
    input_search = "//input[contains(@class,'input-lg')]"
    button_search = "//button[contains(@class,'btn-default')]"
    add_item = "//button[contains(@onclick,'cart.add(') and contains(@onclick,'43')]"
    alert = "//div[contains(@class,'alert')]"
    basket = "//span[@id='cart-total']"
