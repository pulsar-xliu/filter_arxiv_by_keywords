
A python script to filter the latest arXiv papers based on keywords and topics. 

## Motivation
Hundereds of papers are published every day on arXiv, making it difficult to keep track of the latest papers on a specific topic. Some tools, e.g. [PulsarAstronomy.net](https://www.pulsarastronomy.net/pulsar/), can filter papers in a specific topic, but users cannot customize by their own preferences. 

This script automates the process of filtering based on keywords and topics. Notable feautures include
- Flexibility. Users can customize filtering keywords and topics.
- Easy viewing. Results are reported in a arXiv-like webpage.

## Usage
After downloading the script,

1. Set your arXiv topic in Line 10 (`link = `).
2. Specify keywords for filtering in Lines 14-16.
3. Run the script in a terminal as below:
```
    python filter_arxiv_by_keywords.py
```
4. Results are saved in `topic/date.html`. View the results with a web browser.

5. Advanced usage. Linux users can automate the filtering with `crontab`. For example, to retrive latest papers at 7am every day, input `crontab -e` on terminal, and add the following line:
```
   00 07 * * * python /path/to/filter_arxiv_by_keywords.py
```

## Example Output
![Effects of the script](https://github.com/pulsar-xliu/filter_arxiv_by_keywords/blob/main/example_output.png)

## Reference
A similar script from [Errea Lab](https://cfm.ehu.es/errealab/blog/python-script-to-filter-the-arxiv-and-get-an-email-daily/) saved filtered results as a text file and alerted users by email.
