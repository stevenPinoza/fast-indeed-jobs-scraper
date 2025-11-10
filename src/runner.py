thonimport json
from extractors.indeed_parser import IndeedParser
from outputs.exporters import Exporter

def run_scraper():
    # Initialize the parser with some example URLs
    urls = [
        "https://www.indeed.com/jobs?q=software+engineer&l=San+Francisco%2C+CA",
        "https://www.indeed.com/jobs?q=product+manager&l=New+York%2C+NY"
    ]
    
    # Create a parser object
    parser = IndeedParser(urls)
    
    # Extract the job data
    job_data = parser.scrape_jobs()
    
    # Export the data to a JSON file
    exporter = Exporter(job_data)
    exporter.export_to_json('output/jobs_data.json')
    
if __name__ == "__main__":
    run_scraper()