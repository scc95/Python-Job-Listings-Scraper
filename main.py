import bs4
import requests
#asked gemini for help with CSV 
#prompt: I'm trying to write to a csv in python for a web scraper, I want to learn by doing. Please don't tell me a solution, give me the tools that I'll need and a short, simple explanation
import csv

from bs4 import BeautifulSoup
result = requests.get("https://realpython.github.io/fake-jobs/")
print(result.status_code)
print(result.headers)
print(result.text[:500])    
soup = BeautifulSoup(result.text, "lxml")
links = soup.find_all('div', class_='card-content')
all_jobs = []
for link in links:
    title = link.find('h2', class_='title is-5').text
    company = link.find('h3', class_='subtitle is-6 company').text
    location = link.find('p', class_='location').text
    link = link.find('a', string=lambda text: "apply" in text.lower())
    #this should prevent a crash if there is no href
    if link:
        link_url = link['href']
    else:
        link_url = "No link found"

    #create a dictionary
    #strip() removes spaces/newlines around the words, I found this while searching through google
    job_data = {
        "Title": title.strip(),
        "Company": company.strip(),
        "Location": location.strip(),
        "Link": link_url
    }
    all_jobs.append(job_data)
        
    print(f"Job Title: {title.strip()}, company: {company.strip()}, location: {location.strip()}, application link: {link_url}\n")
    
keys = ["Title", "Company", "Location", "Link"]
with open('jobs.csv', 'w', newline='', encoding='utf-8') as output_file: 
    dict_writer = csv.DictWriter(output_file, fieldnames=keys)
    dict_writer.writeheader()
    dict_writer.writerows(all_jobs)

    

    

    
    

