from playwright.sync_api import Page,sync_playwright, expect
# Page=class, expect=function used for assertions.
with (sync_playwright() as p):
    browser = p.chromium.launch(headless=False) #opens the browser
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    #page.get_by_role("textbox", name= "Username").fill("standard_user")
    page.get_by_label("Username").fill("standard_user")
    #page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_role("textbox", name= "Password").fill("secret_sauce")
    page.get_by_role("button", name= "Login").click()

    page.wait_for_timeout(3000)
    page.close()