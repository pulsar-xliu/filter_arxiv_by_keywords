
**Filarkey**: **Fil**tering latest **ar**Xiv papers by **key**words and topics

### Features
Everyday 100+ papers are published on arXiv. Picking out the papers of interest is time-consuming.
This script filters the latest papers using keywords and topics. 

Notable feautures include
- **Friendly**: Report results in webpage following arXiv style. Easy to read and navigate.
- **Flexible**: Set filtering keywords and topics based on your interests.
- **Fast**: Filter 100+ papers to a smaller number in a few seconds.

### Usage
After downloading the script,

1. Set your arXiv topic in Line 10 after `link`.
2. Specify keywords for filtering in Lines 14-16.
3. Run the script in a terminal as below:
```
    python filarkey.py
```
4. Results are saved in `topic/date.html`. View the results with a web browser.

5. Advanced usage. Linux users can automate the filtering with `crontab`. For example, to retrive latest papers at 11 am on every workday, input `crontab -e` on terminal, and add the following line:
```
   0 11 * * 1-5 python /path/to/filarkey.py
```

### Sample output
![Effects of the script](https://github.com/pulsar-xliu/filter_arxiv_by_keywords/blob/main/example_output.png)

### Reference
- A similar script from [Errea Lab](https://cfm.ehu.es/errealab/blog/python-script-to-filter-the-arxiv-and-get-an-email-daily/) saves filtered results as a text file and alerts users by email.
- A website on [PulsarAstronomy.net](https://www.pulsarastronomy.net/pulsar/) filters papers related to pulsar astronomy.