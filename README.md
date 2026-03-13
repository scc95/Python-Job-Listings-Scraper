# Python-Job-Listings-Scraper
My solution for https://roadmap.sh/projects/job-listings-scraper while refreshing python
my goal was to struggle through learning this with no tutorial. I provided the task to gemini and asked for this to give me what I would need to learn with a simple explanation. 

## Features
- Scrapes job titles, companies, locations, and application links.
- Cleans data using `.strip()` 
- Handles missing links to prevent crashing.
- Exports all data to a `jobs.csv` file.

## Tech Stack
- Python
- Requests: To fetch the HTML content.
- BeautifulSoup4 (lxml): To analyze and navigate web data.
- CSV Module: To store the final results.
