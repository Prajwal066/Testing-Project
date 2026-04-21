from pages.login_page import LoginPage


def test_add_to_cart(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # Add product to cart
    page.locator("#add-to-cart-sauce-labs-backpack").click()

    # Check cart count
    cart_badge = page.locator(".shopping_cart_badge")
    assert cart_badge.inner_text() == "1"