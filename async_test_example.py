import asyncio
from playwright.async_api import async_playwright

async def async_def():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        await page.goto("https://www.saucedemo.com/")
        await page.locator("#user-name").fill("standard_user")
        await page.wait_for_timeout(3000)
        await browser.close()

asyncio.run(async_def())