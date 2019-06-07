# ECE143_Project
## The Best Programming Language in the US
This is the ECE 143 final project repo for team 8. 

## Data Scraping
Our team mannually scraped data from Glassdoor.com and save each job description into a numpy file. The dataset has 12285 non-reapeating job listings. 
 - First, **get_job_ids.py** pulls all the job ID's from Glassdoor and saves the ID numbers as a .txt file. 
 - Then, **save_text.py** loops through all the ID's and save each corresponding description into a separate numpy array of string. 
 
## Visualizations
### Pie Charts
Our team created three pie charts to analysis each programming language's market representation. 
 - **overall_pie_charts.py**: This file creates two pie charts. One shows the market percentage of each language and the other one shows the amount of listings per language on the market. 
 - **intern_pie_chart.py**: Thie file create one pie chart showing the amount of internship listings per language on the market. 
 
### Heatmaps
Our team created three heatmaps to analysis the average salary in each state. 
 - **avg_heatmap.py**: This file creates a heatmap showing the average Software Engineering job salary in each state. 
 - **java_heatmap.py**: This file creates a heatmap showing the average salary of the jobs which required Java skill. 
 - **python_heatmap.py**: This file creates a heatmap showing the average salary of the jobs which required Python skill. 
