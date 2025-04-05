#!/usr/local/bin/python

import os
import datetime
import requests
from termcolor import colored
from bs4 import BeautifulSoup

# Define website to be read 
link = "https://arxiv.org/list/astro-ph/new"

# Define keywords. 
# Use all_keywords for filtering. Report major_keyword only.
major_keyword  = ["pulsar", "neutron star", "black hole", "magnetar", "fast radio burst", "gravitational wave", "radio telescope"]
major_keywords = ["pulsars", "neutron stars", "black holes", "magnetars", "fast radio bursts", "gravitational waves", "radio telescopes"]
minor_keywords = ["large language model", "machine learning", "deep learning", "X-ray binary", "MeerKAT", "SKA", "LMXB", "NS", "BH", "GW", "FRB"]
all_keywords = major_keyword + major_keywords + minor_keywords

def filter_papers(link):
    """Access the website and extract paper information."""
    print(f"\n\tAccessing", colored(f"{link}", 'blue'))
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Extract information 
    titles = soup.find_all('div', {'class' : 'list-title mathjax'})
    abstracts = soup.find_all('p', {'class' : 'mathjax'})
    authors = soup.find_all('div', {'class' : 'list-authors'})
    refs = soup.find_all('a', {'title' : 'Abstract'})

    lines_titles = [title.get_text() for title in titles]
    lines_abstracts = [abstract.get_text() for abstract in abstracts]
    lines_authors = [author.get_text() for author in authors]
    lines_refs = [ref.get_text() for ref in refs]

    print(f"\tPapers extracted.")
    return lines_titles, lines_abstracts, lines_authors, lines_refs

def set_filename(link):
    """Create a filename to save the filtered papers."""
    date = datetime.datetime.now().strftime("%Y-%m-%d-%a")
    date_time = datetime.datetime.now().strftime("%Y-%m-%d-%a_%H:%M:%S")
    paper_type = link.split('/')[-2]
    os.makedirs(f"./{paper_type}", exist_ok=True)
    filename = f"./{paper_type}/astro-ph_new_{date}.html"
    if os.path.exists(filename):
        print(f"\n\tWarning: File exists", colored(f"{filename.split('/')[-1]}", "yellow"))
        temp_filename = f"./{paper_type}/astro-ph_new_{date_time}.html"
    else:
        temp_filename = filename
    return filename, temp_filename, date

def write_html(filename, date, all_keywords, major_keyword, lines_titles, lines_abstracts, lines_authors, lines_refs):
    """Filter the papers by keywords and save as an HTML file."""
    with open(filename, 'w') as f:
        # Write a header to render LaTeX equations
        f.write("<html><head>\n")
        f.write(f"<h3>Selected new papers on arXiv Astro-ph, {date}</h3>\n")
        f.write(f"<p>Retrived with keywords: <span style='color: Chocolate;'>{', '.join(major_keyword)}</span></p>\n")
        f.write("<script>MathJax = {tex: {inlineMath: [['$', '$'],['$$', '$$']]}}</script>")
        f.write('<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>')
        f.write("</head><body>\n")

        match_count = 1
        for i in range(len(lines_abstracts)):
            if any(word in lines_abstracts[i] for word in all_keywords):
                title = lines_titles[i].encode('ascii', 'ignore').decode('ascii')
                author = lines_authors[i].encode('ascii', 'ignore').decode('ascii')
                abstract = lines_abstracts[i].encode('ascii', 'ignore').decode('ascii')
                ref = lines_refs[i].encode('ascii', 'ignore').decode('ascii').replace('arXiv:', 'abs/')

                title_clean = title.split('Title:')[-1].strip()
                html_url = 'https://arxiv.org/' + ref.strip()
                pdf_url = html_url.replace('abs', 'pdf')
                
                # Write the information of the matched papers
                f.write(f"<strong>[{match_count}] arXiv:{ref.split('/')[-1]} [<a href='{html_url}' style='text-decoration: none;'>html</a></strong>, <strong><a href='{pdf_url}' style='text-decoration: none;'>pdf</a>]</strong><br>")
                f.write(f"<strong style='padding-left: 40px; font-size: 1.4em;'>{title_clean}</strong></br>\n")
                f.write(f"<span style='padding-left: 40px; color: blue;'>{author}</span>\n")
                f.write(f"<p style='padding-left: 40px;'>{abstract}</p>\n")
                f.write(f"<br>\n")
                match_count += 1
        f.write(f"<p>Total of {match_count-1}/{len(lines_abstracts)} papers.</p>\n")
        f.write(f"<br><br>\n")
        f.write("</body></html>\n") 
    print(f"\n\tFiltering completed.")

def check_duplications(filename, temp_filename):
    """Check if the filtered papers already exist."""
    if filename == temp_filename:
        print(f"\tNew papers found. Saving as", colored(f"{filename.split('/')[-1]}\n", 'magenta'))
    else:
        with open(filename, 'r') as f1, open(temp_filename, 'r') as f2:
            if f1.read() == f2.read():
                print(colored(f"\tWarning: No new papers found.\n", "yellow"))
                os.remove(temp_filename)
            else:
                print(f"\tNew papers found. Saving as", colored(f"{filename.split('/')[-1]}\n", 'magenta'))

def main():
    paper_info = filter_papers(link)
    filename, temp_filename, date = set_filename(link)
    write_html(temp_filename, date, all_keywords, major_keyword, *paper_info)
    check_duplications(filename, temp_filename)

if __name__ == '__main__':
    main()
