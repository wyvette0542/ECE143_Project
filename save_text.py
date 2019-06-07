import requests    #this is for getting the webpage 
from bs4 import BeautifulSoup    #html parser or whatever
import re
import string
import numpy as np

def save_text():
    '''
    This is our job description scraping file
    The functio goes through every id in 'id_list.txt' and save the text description as a numpy array of strings
    '''

    headers = requests.utils.default_headers()    #need to provide a user-agent code to access the website
    headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',})

    with open('id_list.txt', 'r')as f:
        job_list = f.readlines()

    job_list = list(set(job_list))

    # Map the languages with punctuations to letters only
    punctuatedLanguages = {"asp.net" : "aspdotnet",
        "f#" : "fsharp",
        "objective-c" : "objectivec",
        "objective-c++" : "objectivecplusplus",
        "c#": "csharp",
        "c++": "cplusplus",
        }

    start = 0
    end = 12285
    # for i in range(end, start, -1): ## this one runs backward
    for i in range(start, end):  #this one runs forward
        job_id = job_list[i].replace('\n', '')
        jobPage0 = 'https://www.glassdoor.com/Job/json/details.htm?jobListingId=' + job_id
        jobPage0 = requests.get(jobPage0,headers = headers)
        jobsoup  = BeautifulSoup(jobPage0.text,'html.parser')
        jobsoup = str(jobsoup).lower()
        for element in punctuatedLanguages:
            jobsoup = jobsoup.replace(element, punctuatedLanguages[element])
        jobsoup = re.sub('[%s]'%string.punctuation, " ", jobsoup)
        jobsoup = jobsoup.split()
        np.save('job_description' + str(i) + '.npy', jobsoup)   # Save each job description as a numpy file
        print(i)