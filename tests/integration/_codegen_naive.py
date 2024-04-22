#!/usr/bin/env python

from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://localhost:8080/")
    page.get_by_role("link", name="Blog").click()
    page.get_by_role("link", name="About").click()
    page.get_by_role("link", name="Contact").click()
    page.get_by_role("link", name="Dummy logotype").click()
    breakpoint()
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
