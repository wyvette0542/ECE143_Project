# ECE143_Project
## The Best Programming Language in the US
This is the ECE 143 final project repo for team 8. 

## Data Scraping
Our team mannually scraped data from Glassdoor.com and save each job description into a numpy file. The dataset has 12285 non-reapeating job listings. 
 - First, **get_job_ids.py** pulls all the job ID's from Glassdoor and saves the ID numbers as a .txt file. 
 - Then, **save_text.py** loops through all the ID's and save each corresponding description into a separate numpy array of string. 
 - Next, **data_extraction.py** (or **data_extraction_elongated.py** if there were problems with the other file) saves two pandas dataframes from the numpy arrays to analyze for any given users purpose.  In addition, txt files corresponding to average salary and amount of languages, locations, or states are generated.  Finally, bar graphs are plotted.  

## Dataframes
In processing our data, we made 5 separate dataframes. Each used in different files for different .py files to generate our visualization.
 - **dataframe1.pkl**: Provides an overall dataframe of our data. Everything is grouped by job ID.
 - **dataframe2.pkl**: Expands our data so that we have a data entry for each language per job ID.
 - **dataframe3.pkl**: Dataframe that groups by a state's min and max paying languages per state. Used to create overall heatmap.
 - **dataframe4.pkl**: Dataframe for our pie charts. The data is divided by Market% per language and popularity by listing count.
 - **dataframe5.pkl**: Dataframe that is grouped by Python and Java data entries to create our java and python heatmaps.
 
## Visualizations
### Pie Charts
Our team created three pie charts to analysis each programming language's market representation. 
 - **create_piecharts_overall.py**: This file creates two pie charts. One shows the market percentage of each language and the other one shows the amount of listings per language on the market. 
 - **intern_pie_chart.py**: Thie file create one pie chart showing the amount of internship listings per language on the market. 
 
### Heatmaps
Our team created three heatmaps to analysis the average salary in each state. 
 - **create_heatmap_overall.py**: This file creates a heatmap showing the highest, lowest, and mean Software Engineering job salary.
 - **create_heatmap_java.py**: This file creates a heatmap showing the average salary of the jobs which required Java skill. 
 - **create_heatmap_python.py**: This file creates a heatmap showing the average salary of the jobs which required Python skill. 
