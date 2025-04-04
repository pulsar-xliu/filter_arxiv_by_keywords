
A python script to filter the newest arXiv papers based on keywords and categories. 

## Motivation
Hundereds of papers are published every day on arXiv, making it is to keep track of the latest papers on a specific topic. Some tools, e.g. [PulsarAstronomy.net](https://www.pulsarastronomy.net/pulsar/), can filter papers in a specific category, but users cannot customize by their own preferences. 

This script automates the process of filtering the latest papers based on keywords and categories. Attracting feautures include:
- Flexibility to customize filtering keywords and categories.
- Reporting results as arXiv-like webpage for easy viewing.

## Usage
After downloading the script,

1. Set your arXiv category in Line 10 (`link = `).
2. Specify keywords for filtering in Lines 14-16.
3. Run the script in a terminal as below:
```
    python filter_arxiv_by_keywords.py
```
4. Results are saved in `category/date.html`. View the results with a web browser.

5. Advanced usage. Linux users can automate the filting with `crontab` on a daily basis. For example, to retrive latest papers at 7am every day, input `crontab -e` on terminal, and add the following line:
```
   00 07 * * * python /path/to/filter_arxiv_by_keywords.py
```

## Example Output
![Effects of the script](https://github.com/pulsar-xliu/filter_arxiv_by_keywords/blob/main/example_output.png)

## Acknowledgements
This script is adapted based on the work of [Errea Lab](https://cfm.ehu.es/errealab/blog/python-script-to-filter-the-arxiv-and-get-an-email-daily/), which saved the results as a text file and emailed it to a user.
