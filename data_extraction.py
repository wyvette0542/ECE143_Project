'''
This file extracts data from generated numpy files and creates two dataframes for further analysis
'''
import numpy as np
import re
import pandas as pd

# Obtain all Languages to be analyzed
with open('languages.txt', 'r')as f:
    read_languages = f.readlines()

languages = []
assert isinstance(read_languages, list)
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
  
# create a new txt file containing the counts of programming languages
f = open('language_counts.txt','w')
i = 0
for val in language_counts:
    line = str(read_languages[i][:-1]) + ': ' + str(val) + '\n'
    f.write(line)
    i = i + 1
f.close()

# Location Analysis
possible_locations = []
for i in range(0, len(locations)):
    if locations[i] not in possible_locations:
        possible_locations.append(locations[i])

location_counts = []
for possible_location in possible_locations:
    amount = locations.count(possible_location)
    location_counts.append(amount)

# create a new txt file containing the counts of locations
f = open('location_counts.txt','w')
i = 0
for val in location_counts:
    line = str(possible_locations[i]) + ': ' + str(val) + '\n'
    f.write(line)
    i = i + 1
f.close()

# State Analysis
possible_states = []
for i in range(0, len(states)):
    if states[i] not in possible_states:
        possible_states.append(states[i])

state_counts = []
for possible_state in possible_states:
    amount = states.count(possible_state)
    state_counts.append(amount)

# create a new txt file containing the counts of states
f = open('state_counts.txt','w')
i = 0
for val in state_counts:
    line = str(possible_states[i]) + ': ' + str(val) + '\n'
    f.write(line)
    i = i + 1
f.close()

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

# Save Data Frames
loc_sal_lang.to_pickle("./dataframe1.pkl")

language_data.to_pickle("./dataframe2.pkl")
