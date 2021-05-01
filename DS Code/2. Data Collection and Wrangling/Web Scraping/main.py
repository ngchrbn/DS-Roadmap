import re
import requests
from bs4 import BeautifulSoup

URL = 'https://eg.indeed.com/%D9%88%D8%B8%D8%A7%D8%A6%D9%81?q=Python&l=Cairo'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='resultsCol')

pattern = "python"

job_elements = results.find_all('div', class_='jobsearch-SerpJobCard')

for job_elem in job_elements:
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='sjcl')
    summary_elem = job_elem.find('div', class_='summary')
    if None in (title_elem, company_elem, summary_elem):
        continue
    match_res = re.findall(pattern, title_elem.text.strip(), re.IGNORECASE)
    if not match_res:
        continue
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(summary_elem.text.strip())
    print("============================================", end='\n'*4)