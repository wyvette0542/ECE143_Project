import requests    #this is for getting the webpage 
from bs4 import BeautifulSoup    #html parser or whatever
import re

def get_job_ids(): 
    '''
    This is our webscraping file
    We manually pulled the search pages corresponding to search results for the "Software Engineer" position in different cities from glassdoor.com
    Beginning from the first page, we cycle through every listing on every search page for every city to pull current job IDs
    We store these job IDs into a txt file 
    Using this txt file we then make requests to the job listing descriptions that the job IDs point to 
    We scrape these descriptions in order to create our data sets

    '''

    with open('CAGlassdoorURLS.txt') as f:  #This file contains the manually pulled url searches
        url_list = f.readlines()

    headers = requests.utils.default_headers()    #need to provide a user-agent code to access the website
    headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',})

    for current in url_list:    # cycles through the list of urls provided
        
        # Extract job ids for the available 30 pages and append the ids to the file 'id_list.txt'

        for i in range(1, 31):    # There are 30 valid pages
            page = current.format(i)  # current holds the current url page for given search results
            page = page.rstrip()    # strip newline from the url
            page = requests.get(page, headers = headers)  # request the current page
            soup = BeautifulSoup(page.text,'html.parser')   # html parse the current page
            results = soup.find_all('script')   # 'script' tag contains the ID section 
            listings = results[0]   # assign index to variable to perform functions

            idx1 = str(listings).find('jobIds')
            idx2 = str(listings).find('segmentType')
            ans = str(listings)[idx1 : idx2]
            id_list = re.findall(r"\d+", ans)
        
            with open('id_list.txt', 'a+') as f:   # Write all id's into a file
                for job in id_list:
                    f.write(job + '\n')
                
