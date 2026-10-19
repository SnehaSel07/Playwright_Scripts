from textwrap import fill

from playwright.sync_api import sync_playwright, expect
#from pytest_playwright.pytest_playwright import browser

# Page=class, expect=function used for assertions.
def test_xpath_example(page):
     page.goto("https://www.saucedemo.com/")
     # Absolute xpath
     page.locator("//html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input").fill("error_user")

     # Relative Xpath
     page.locator("//*[@id='password']").fill("secret_sauce")
     page.locator("//*[@id='login-button']").click()

# launching the browser
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    test_xpath_example(page)
    page.wait_for_timeout(3000)

    browser.close()





