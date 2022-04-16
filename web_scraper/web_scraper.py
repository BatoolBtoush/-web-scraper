import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/History_of_Mexico"
res = requests.get(URL)
soup = BeautifulSoup(res.content, "html.parser")


def get_citations_needed_count(URL):
    count = []

    for cite in soup.find("div", class_="mw-parser-output").find_all("p"):
        for ref in cite.find_all("a", title="Wikipedia:Citation needed"):
            count.append(ref)
    return len(count)


def get_citations_needed_report(URL):

    for cite in soup.find("div", class_="mw-parser-output").find_all("p"):
        for ref in cite.find_all("a", title="Wikipedia:Citation needed"):
            report = ref.parent.parent.parent.get_text()
            final_report = report.replace("[citation needed]", "")
            split_final_report = final_report.strip(".")
            print("\n", split_final_report, "\n")
            # print(soup.find_all("p")[0].get_text())
            # print(soup.find_all("p")[1].get_text())
            # print(soup.find_all("p")[2].get_text())
            # print(soup.find_all("p")[3].get_text())
            # print(soup.find_all("p")[4].get_text())

    return


print("Number of citations needed in the article is:", get_citations_needed_count(URL))
get_citations_needed_report(URL)
