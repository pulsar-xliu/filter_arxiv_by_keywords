#!/usr/local/bin/python

import datetime
import requests
import os
from bs4 import BeautifulSoup

# Define keywords
keywords = ["pulsar", "neutron star", "black hole", "magnetar", "fast radio burst", "gravitational wave", "radio telescope"]
sub_keywords = ["pulsars", "neutron stars", "black holes", "magnetars", "fast radio bursts", "gravitational waves", "radio telescopes"]
minor_keywords = ["large language model", "machine learning", "deep learning", "X-ray binary", "MeerKAT", "SKA", "LMXB", "NS", "BH", "GW", "FRB"]
all_keywords = keywords + sub_keywords + minor_keywords

# Define website to be read 
link = "https://arxiv.org/list/astro-ph/new"
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

# Write filtered papers into html file
date = datetime.datetime.now().strftime("%Y-%m-%d")
paper_type = link.split('/')[-2]
os.makedirs(f"./{paper_type}", exist_ok=True)
f = open(f"./{paper_type}/astro-ph_new_{date}.html", "w")

# Write a header to render LaTeX equations
f.write("<html><head>\n")
f.write("<script>MathJax = {tex: {inlineMath: [['$', '$'],['$$', '$$']]}}</script>")
f.write('<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>')
f.write(f"<h3>Selected new papers on arXiv Astro-ph, {date}</h3>\n")
f.write(f"<p>Retrived with keywords: <span style='color: Chocolate;'>{', '.join(keywords)}</span></p>\n")
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
f.close()
