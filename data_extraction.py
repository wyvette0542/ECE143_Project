import numpy as np
import re
import pandas as pd
import matplotlib.pyplot as plt 

# Obtain all Languages to be analyzed
with open('languages.txt', 'r')as f:
    read_languages = f.readlines()

languages = []
for language in read_languages:
    languages.append(language.lower()[:-1])

# Lists for Data Processing
found_languages = []
all_languages = []
locations = []
salaries = []
states = []

# DataFrame for States vs Salary, Location vs Salary
loc_sal_lang = pd.DataFrame(columns=['Location','Salary', 'Languages', 'States'])

# Pull location/state, salary, and languages to learn from each numpy file
for i in range(0, 12285):
    file = np.load("job_description" + str(i) + ".npy")
    location_tag = False
    logo_tag = False
    for j in range(0, len(file)):
        if file[j] == 'location' and location_tag == False:
            location_tag = True
            if file[j+1] == 'san':
                locations.append('san_' + file[j+2])
            elif file[j+1] == 'los':
                locations.append('los_' + file[j+2])
            elif file[j+1] == 'el':
                locations.append('el_' + file[j+2])
            elif file[j+1] == 'santa':
                locations.append('santa_' + file[j+2])
            elif file[j+1] == 'salt':
                locations.append('salt_' + file[j+2])
            elif file[j+1] == 'redondo':
                locations.append('redondo_' + file[j+2])
            elif file[j+1] == 'rancho':
                locations.append('rancho_' + file[j+2])
            elif file[j+1] == 'redwood':
                locations.append('redwood_' + file[j+2])
            elif file[j+1] == 'culver':
                locations.append('culver_' + file[j+2])
            elif file[j+1] == 'huntington':
                locations.append('huntington_' + file[j+2])
            elif file[j+1] == 'palo':
                locations.append('palo_' + file[j+2])
            elif file[j+1] == 'mountain':
                locations.append('mountain_' + file[j+2])
            elif file[j+1] == 'elk':
                locations.append('elk_' + file[j+2])
            elif file[j+1] == 'aliso':
                locations.append('aliso_' + file[j+2])
            elif file[j+1] == 'new':
                locations.append('new_' + file[j+2])
            elif file[j+1] == 'north':
                locations.append('north_' + file[j+2])
            elif file[j+1] == 'south':
                locations.append('south_' + file[j+2])
            elif file[j+1] == 'east':
                locations.append('east_' + file[j+2])
            elif file[j+1] == 'west':
                locations.append('west_' + file[j+2])
            elif file[j+1] == 'menlo':
                locations.append('menlo_' + file[j+2])
            elif file[j+1] == 'morgan':
                locations.append('morgan_' + file[j+2])
            elif file[j+1] == 'lake':
                locations.append('lake_' + file[j+2])
            elif file[j+1] == 'costa':
                locations.append('costa_' + file[j+2])
            else:
                locations.append(file[j+1])
        
        elif file[j] == 'salarylow':
            sal_low = file[j+1]
        
        elif file[j] == 'salaryhigh':
            sal_high = file[j+1]
            
        elif file[j] == 'logo' and logo_tag == False:
            if len(file[j-1]) == 2:
                logo_tag = True
                states.append(file[j-1])
    
    if logo_tag == False:
        locations.pop()
        continue
        
    salary = (int(sal_low) + int(sal_high))/2
    salaries.append(salary)
    languages_per_entry = []
    for language in languages:
        if language in file:
            found_languages.append(language)
            languages_per_entry.append(language)
    all_languages.append(languages_per_entry)

# Obtaining total language counts
language_counts = []
for language in languages:
    amount = found_languages.count(language)
    language_counts.append(amount)

# Bar Chart parameters
left = range(1,51)
height = language_counts
tick_label = languages
  
# plotting a bar chart for languages vs number of jobs with programming language as a requirement
plt.bar(left, height, tick_label = tick_label,
        width = 0.5, color = ['red', 'green']) 
plt.xticks(left, tick_label, rotation='vertical')
plt.tick_params(axis='x', which='major', labelsize=7)

# naming the x-axis 
plt.xlabel('Programming Languages')
# naming the y-axis 
plt.ylabel('Number of jobs') 
# plot title 
plt.title('Programming Languages vs Number of Jobs with Programming Language as a Requirement') 
  
# function to show the plot 
plt.show() 

# Location Analysis
possible_locations = []
for i in range(0, len(locations)):
    if locations[i] not in possible_locations:
        possible_locations.append(locations[i])

location_counts = []
for possible_location in possible_locations:
    amount = locations.count(possible_location)
    location_counts.append(amount)

# State Analysis
possible_states = []
for i in range(0, len(states)):
    if states[i] not in possible_states:
        possible_states.append(states[i])

state_counts = []
for possible_state in possible_states:
    amount = states.count(possible_state)
    state_counts.append(amount)

# Store data into First Dataframe
loc_sal_lang['Location'] = locations
loc_sal_lang['Salary'] = salaries
loc_sal_lang['Languages'] = all_languages
loc_sal_lang['States'] = states

# Second Dataframe with Individual Language Analysis
language_data = pd.DataFrame(columns=['Language','Salary', 'Location', 'States'])
languages_in_data = []
salaries_per_language = []
locations_per_language = []
states_per_language = []

# Obtain data for Second Dataframe
for row in loc_sal_lang.itertuples():
    for a_language in row.Languages:
        languages_in_data.append(a_language)
        salaries_per_language.append(row.Salary)
        locations_per_language.append(row.Location)
        states_per_language.append(row.States)

# Store data into Second Dataframe
language_data['Language'] = languages_in_data
language_data['Salary'] = salaries_per_language
language_data['Location'] = locations_per_language
language_data['States'] = states_per_language

# Location vs Salary
grp = loc_sal_lang.groupby('Location')

f = open('location_salary.txt','w')
for key, item in grp:
    line = 'Location: ' + str(key) + '; Average Salary: ' + str(item['Salary'].mean()) + '\n'
    f.write(line)

f.close()

# Language vs Salary, Language vs Location
grp2 = language_data.groupby('Language')
f = open('language_salary.txt','w')
g = open('language_location_counts.txt', 'w')
all_languages = []
avg_salaries_languages = []
for key, item in grp2:
    line = 'Language: ' + str(key) + '; Average Salary: ' + str(item['Salary'].mean()) + '\n'
    if (str(key) == 'arduino') or (str(key) == 'c') or (str(key) == 'cplusplus') or (str(key) == 'c3') or (str(key) == 'erlang'):
        all_languages.append(str(key))
        avg_salaries_languages.append(item['Salary'].mean())
    
    elif (str(key) == 'python') or (str(key) == 'java') or (str(key) == 'javascript') or (str(key) == 'qml') or (str(key) == 'sql'):
        all_languages.append(str(key))
        avg_salaries_languages.append(item['Salary'].mean())
        
    elif (str(key) == 'css') or (str(key) == 'r') or (str(key) == 'csharp') or (str(key) == 'matlab') or (str(key) == 'go'):
        all_languages.append(str(key))
        avg_salaries_languages.append(item['Salary'].mean())
        
    f.write(line)
    
    values = item['Location'].value_counts()
    vals = str(values.astype(str))
    top_loc = vals.splitlines()[0]
    if key == 'rust':
        top_loc = vals.splitlines()[1]
    top_loc = top_loc.split()
    top_loc = top_loc[0]
    line2 = 'Language: ' + str(key) + '; Locations: ' + top_loc + '\n'
    g.write(line2)
f.close()
g.close()

# Save Data Frames
loc_sal_lang.to_pickle("./dataframe1.pkl")

language_data.to_pickle("./dataframe2.pkl")

# Group by States
grp3 = language_data.groupby('States')

f = open('states_salary.txt','w')
all_states = []
avg_salaries_state = []
for key, item in grp3:
    line = 'State: ' + str(key) + '; Average Salary: ' + str(item['Salary'].mean()) + '\n'
    f.write(line)
    all_states.append(str(key).upper())
    avg_salaries_state.append(item['Salary'].mean())
f.close()

# Salary vs State
state_salary_dict = dict(zip(all_states, avg_salaries_state))
sorted_salaries = (sorted(state_salary_dict.values(), reverse = True))
sorted_states = []
for i in range(len(sorted_salaries)):
    for key in state_salary_dict:
        if (sorted_salaries[i] == state_salary_dict[key]):
            sorted_states.append(key)

# Graph Parameters
left = range(1,21)
height = sorted_salaries
tick_label = sorted_states
  
# plotting a bar chart for Average Salaries for Each State
plt.bar(left, height, tick_label = tick_label,
        width = 0.5, color = ['red']) 
plt.xticks(left, tick_label, rotation=60)
plt.tick_params(axis='x', which='major', labelsize=9)

# naming the x-axis 
plt.xlabel('States')
# naming the y-axis 
plt.ylabel('Avg Salary of Job') 
# plot title 
plt.title('Average Salaries of Jobs for Each State') 
  
# function to show the plot 
plt.show() 

# Salary vs Language
language_salary_dict = dict(zip(all_languages, avg_salaries_languages))
sorted_salaries_lang = (sorted(language_salary_dict.values(), reverse = True))
sorted_langs = []
for i in range(len(sorted_salaries_lang)):
    for key in language_salary_dict:
        if (sorted_salaries_lang[i] == language_salary_dict[key]):
            sorted_langs.append(key)

# Graph Parameters
left = range(1,16)
height = sorted_salaries_lang
tick_label = sorted_langs
  
# plotting a bar chart for Avarage Salaries of Jobs for Each Language
plt.bar(left, height, tick_label = tick_label,
        width = 0.5, color = ['red']) 
plt.xticks(left, tick_label, rotation=60)
plt.tick_params(axis='x', which='major', labelsize=9)

# naming the x-axis 
plt.xlabel('Language')
# naming the y-axis 
plt.ylabel('Avg Salary of Job') 
# plot title 
plt.title('Average Salaries of Jobs for Each Language') 
  
# function to show the plot 
plt.show() 