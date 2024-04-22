#!/usr/bin/env python3

import pytest
from decouple import config
from pathlib import Path
from playwright.sync_api import BrowserType
from typing import Dict

# env vars
url = config("URL", default="localhost:8080")
browser_type = config("BROWSER_TYPE", default="chromium")
cwd = Path(__file__).parent
repo_dir = Path(__file__).resolve().parent.parent

# storage state
abs_storage = repo_dir / "tests" / ".auth" / "state.json"
if not abs_storage.exists():
    abs_storage.write_text("{}")
rel_storage = str(abs_storage.relative_to(cwd))

# browser arguments
launch_args = {"locale": "en-US",
               "headless": False,
               "slow_mo": 0,
               "viewport": {"width": 1280, "height": 1329},
               "devtools": False
}


@pytest.fixture(scope="session")
def context(browser_type: BrowserType, browser_type_launch_args: Dict, browser_context_args: Dict):
    """Launch a browser context for the entire session."""
    # all launch arguments are passed to the persisent browser context as-is
    context = browser_type.launch_persistent_context(
        rel_storage, **{**browser_type_launch_args, **browser_context_args, **launch_args}
    )
    yield context
    context.close()


@pytest.fixture(scope="function")
def incognito_context(browser_type: BrowserType, browser_type_launch_args: Dict, browser_context_args: Dict):
    """
    Launch a new browser context for each test.

    This fixture is used for tests that require a clean slate, such as login tests.

    Note: unlike `launch_persistent_context`, not all `launch_args` are available to both browser type and context.
    """
    # access launch arguments for browser type
    launch_args_for_type = {
        "headless": launch_args["headless"],
        "slow_mo": launch_args["slow_mo"],
        "devtools": launch_args["devtools"],
    }
    # access launch arguments for browser context
    launch_args_for_context = {"locale": launch_args["locale"], "viewport": launch_args["viewport"]}
    # launch browser and context with args, but without storage state
    with browser_type.launch(**{**browser_type_launch_args, **launch_args_for_type}) as browser:
        with browser.new_context(**{**browser_context_args, **launch_args_for_context}) as context:
            yield context
