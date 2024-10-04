import pytest
from pages.duckduckgo.search_page import DuckDuckGoSearchPage
from pages.google.search_page import GoogleSearchPage


@pytest.mark.parametrize(
    "page, title, search_phrase", [
        pytest.param(DuckDuckGoSearchPage, 'DuckDuckGo', 'panda', marks=pytest.mark.duckduckgo),
        pytest.param(GoogleSearchPage, 'Google', 'python', marks=pytest.mark.google)
    ])
def test_search(browser, page, title, search_phrase):
    search_page = page(browser)
    search_page.load()
    assert title in search_page.title(), f"Expected title '{title}' not found!"
    result_page = search_page.search(search_phrase)
    assert search_phrase == result_page.search_phrase(), f"Search phrase '{search_phrase}' mismatch!"
    assert search_phrase in result_page.title(), f"Search phrase '{search_phrase}' not in page title!"
    assert result_page.results_count(search_phrase) > 0, "No results found for search phrase!"
