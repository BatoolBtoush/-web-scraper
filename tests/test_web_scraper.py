from web_scraper.web_scraper import (
    get_citations_needed_count,
    get_citations_needed_report,
)


def test_get_citations_needed_count():
    URL = "https://en.wikipedia.org/wiki/History_of_Mexico"
    actual = get_citations_needed_count(URL)
    expected = 5
    assert actual == expected


def test_get_citations_needed_report():
    URL = "https://en.wikipedia.org/wiki/History_of_Mexico"
    actual = get_citations_needed_report(URL)
    expected = None
    assert actual == expected
