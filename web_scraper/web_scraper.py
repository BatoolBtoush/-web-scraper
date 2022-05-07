from fileinput import filename
from hashlib import new
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
    report_list = []

    for cite in soup.find("div", class_="mw-parser-output").find_all("p"):
        for ref in cite.find_all("a", title="Wikipedia:Citation needed"):
            report = ref.parent.parent.parent.get_text()
            report_list.append(report)

    if report_list[1] == report_list[2]:
        save_one = report_list[1]
        report_list.pop(1)
        report_list.pop(1)
        report_list.append(save_one)
        report_list.insert(1, save_one)
        report_list.pop(4)

    splited = save_one.split("[citation needed]")
    splited.pop(2)

    new_list = splited + report_list
    new_list.pop(3)
    save_first_part = new_list[0]
    save_second_part = new_list[1]
    new_list.pop(0)
    new_list.pop(0)
    new_list.insert(1, save_first_part)
    new_list.insert(2, save_second_part)

    fix_new_list_zero = new_list[0].replace(".[citation needed][6]", "")
    fix_new_list_two = new_list[2].strip()
    fix_new_list_three = new_list[3].replace("[citation needed]", "")

    new_list.pop(0)
    new_list.pop(2)

    new_list.insert(0, fix_new_list_zero)
    new_list.insert(2, fix_new_list_two)
    new_list.insert(3, fix_new_list_three)

    new_list.pop(4)

    return "\n \n".join(new_list)


print("Number of citations needed in the article is:", get_citations_needed_count(URL))
print("===" * 40)
print(get_citations_needed_report(URL))
