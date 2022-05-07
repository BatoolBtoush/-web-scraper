# **Web Scraper**

## **Feature Tasks**

- Scrape the provided Wikipedia page and record which passages need citations.

- The web scraper should report the number of citations needed via ***get_citations_needed_count()*** function.

- The web scraper should identify those cases and print the relevant passage via ***get_citations_needed_report()*** function


<br>

<br>


## **Implementation Notes**

After importing ***requests*** and ***bs4***

I wrote two functions to perform certain tasks:
1. ***get_citations_needed_count()***

This fucntion takes in the url of the Wikipedia page and returns an integer that indicates the number of paragraphs that need citation

2. ***get_citations_needed_report()***

This function takes in the url of the Wikipedia pagr and returns a string of the parapgraphs that need citation, all formatted where each one has its own line.

