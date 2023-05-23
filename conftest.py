import pytest
from typing import Generator
from playwright.sync_api import Playwright, APIRequestContext
from core.utils.config_parser import get_config


@pytest.fixture(scope="session")
def request_context(playwright: Playwright) -> \
        Generator[APIRequestContext, None, None]:
    r_context = playwright.request.new_context(
        base_url=get_config("BaseConfig", "base_url")
    )
    yield r_context
    r_context.dispose()
