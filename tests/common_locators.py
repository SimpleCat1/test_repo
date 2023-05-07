class CommonLocators:
    dropdown_my_account = "//i[contains(@class,'fa-user')]/ancestor::a/span[@class='caret']"

    # product catalog
    breadcrumb = "//ul[@class='breadcrumb']/li"

    # add item from shop
    add_item = "//button[contains(@onclick,'cart.add(') and contains(@onclick,'43')]"

    allert = "//div[contains(@class,'alert')]"
    basket = "//span[@id='cart-total']"
