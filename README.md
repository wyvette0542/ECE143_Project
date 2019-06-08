# ECE143_Project
## The Best Programming Language in the US
This is the ECE 143 final project repo for team 8. 

## Data Scraping
Our team manually scraped data from Glassdoor.com and saved each job description into a numpy file. The dataset has 12285 non-repeating job listings. 
 - First, **get_job_ids.py** pulls all the job IDs from Glassdoor and saves the ID numbers as a .txt file. 
 - Then, **save_text.py** loops through all the IDs and saves each corresponding description into a separate numpy array of string. 
 
 ## Data Processing
 - **data_extraction.py** (or **data_extraction_elongated.py** if there were problems with the other file) saves two pandas dataframes(dataframe1 and dataframe2) from the numpy arrays to analyze for any given users purpose.  In addition, txt files corresponding to average salary and amount of languages, locations, or states are generated.  Finally, bar graphs are plotted.  
 - **data_heatmap_python_java.py** , **data_heatmap_avg.py**, and **data_pie_and_line.py** groups data by desirable metrics such as average salary or market representation percentage to create our data visualization. These groupings are then saved as three separate dataframes(dataframe3, dataframe4, and dataframe5).
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

### Line Graph
Our team created one line graph to visualize the difference between a language's market share and popularity.
 - **create_line_market_v_popularity.py**: This file creates a line graph showing the percentage difference between a language's popularity by listing count and the average salary that that language provides. 
