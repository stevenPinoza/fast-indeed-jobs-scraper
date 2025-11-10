thonimport requests
from bs4 import BeautifulSoup

class IndeedParser:
    def __init__(self, urls):
        self.urls = urls
    
    def scrape_jobs(self):
        jobs = []
        for url in self.urls:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            job_listings = soup.find_all('div', class_='jobsearch-SerpJobCard')
            for job in job_listings:
                job_title = job.find('h2', class_='title').text.strip()
                company_name = job.find('span', class_='company').text.strip()
                location = job.find('div', class_='location').text.strip()
                posting_date = job.find('span', class_='date').text.strip()
                apply_link = 'https://www.indeed.com' + job.find('a')['href']
                
                jobs.append({
                    'jobTitle': job_title,
                    'companyName': company_name,
                    'location': location,
                    'postingDate': posting_date,
                    'applyLink': apply_link
                })
        return jobs