# ECE143_Project
This is the ECE 143 final project repo for team 8. 

## Data Scraping
Our team mannually scraped data from Glassdoor.com and save each job description into a numpy file. 
First, function get_job_ids() pulls all the job ID's from Glassdoor and saves the ID numbers as a .txt file. 
Then, function save_text() loops through all the ID's and save each corresponding description into a separate numpy array of string. 
