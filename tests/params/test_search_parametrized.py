import pytest

from pages.duckduckgo.search_page import DuckDuckGoSearchPage
from pages.google.search_page import GoogleSearchPage
from tests.conftest import browser


@pytest.mark.duckduckgo
@pytest.mark.google
@pytest.mark.parametrize("page, title, search_phrase", [
    (DuckDuckGoSearchPage, 'DuckDuckGo', 'panda'),
    (GoogleSearchPage, 'Google', 'python'),
])
def test_search(browser, page, title, search_phrase):
    search_page = page(browser)
    search_page.load()
    assert title in search_page.title()

    result_page = search_page.search(search_phrase)

    assert search_phrase == result_page.search_phrase()
    assert search_phrase in result_page.title()
    assert result_page.results_count(search_phrase) > 0
