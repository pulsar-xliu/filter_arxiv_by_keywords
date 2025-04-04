
A python script to filter the newest arXiv papers based on keywords and categories. Results are saved as an HTML file for easy viewing and tracking.

## Motivation
Hundereds of papers are published every day on arXiv. It is difficult to keep track of the latest papers on a specific topic. This script aims to automate the process of filtering the latest papers based on keywords and categories.

Some existing tools for filtering arXiv papers, e.g. [Pulsarastronomy.net](https://www.pulsarastronomy.net/pulsar/), but the user cannot customize the filtering criteria. This script provides the flexibility to filter papers based on their own preferences.

## Usage
After downloading the script,

1. Set your arXiv category in Line 10 (`link = `).
2. Specify keywords for filtering in Lines 14-16.
3. Run the script in a terminal as below:
```
    python filter_arxiv_by_keywords.py
```
4. Results are saved in `category/date.html`. View the results with a web browser.

## Example Output
![Effects of the script](https://github.com/pulsar-xliu/filter_arxiv_by_keywords/blob/main/example_output.png)

## Acknowledgements
This script is an adaption based on the work of https://cfm.ehu.es/errealab/blog/python-script-to-filter-the-arxiv-and-get-an-email-daily/, which saved the results as a text file and emailed it to a user.
