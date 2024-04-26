#!/usr/bin/env python

import pytest
import re
import unittest
from conftest import url, abs_storage


class TestNav(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def setup(self, context):
        """Use an incognito context for login test."""
        self.context = context
        self.context.storage_state(path=abs_storage)
        self.page = self.context.new_page()

    def teardown(self):
        """Close the page after each test."""
        self.page.close()

    def test_nav(self):
        self.page.goto(url)
        self.page.get_by_role("link", name="Blog").click()
        self.page.locator("#nav").get_by_role("link", name="About").click()
        self.page.get_by_role("link", name="Contact").click()
        self.page.locator("#header header").click()
