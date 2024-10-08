import pytest

from pages.duckduckgo.search_page import DuckDuckGoSearchPage
from pages.google.search_page import GoogleSearchPage
from tests.conftest import browser

@pytest.mark.duckduckgo
def test_basic_duckduckgo_search(browser):
    search_page = DuckDuckGoSearchPage(browser)

    search_page.load()

    assert 'DuckDuckGo' in search_page.title()

    search_phrase = 'panda'
    result_page = search_page.search(search_phrase)

    assert search_phrase == result_page.search_phrase()
    assert search_phrase in result_page.title()
    assert result_page.results_count(search_phrase) > 0


@pytest.mark.google
def test_load_google_search(browser):
    search_page = GoogleSearchPage(browser)
    search_page.load()

    assert 'Google' in search_page.title()

    search_phrase = 'panda'
    result_page = search_page.search(search_phrase)

    assert search_phrase == result_page.search_phrase()
    assert search_phrase in result_page.title()
    assert result_page.results_count(search_phrase) > 0
