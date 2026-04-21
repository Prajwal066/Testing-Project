from pages.login_page import LoginPage


def test_complete_checkout_flow(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # Add product to cart
    page.locator("#add-to-cart-sauce-labs-backpack").click()

    # Go to cart
    page.locator(".shopping_cart_link").click()

    # Click checkout
    page.locator("#checkout").click()

    # Fill details
    page.locator("#first-name").fill("Prajwal")
    page.locator("#last-name").fill("Test")
    page.locator("#postal-code").fill("12345")

    # Continue
    page.locator("#continue").click()

    # Finish order
    page.locator("#finish").click()

    # Verify success
    success_message = page.locator(".complete-header")
    assert "Thank you for your order!" in success_message.inner_text()