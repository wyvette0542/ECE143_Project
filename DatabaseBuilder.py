import numpy as np
import re
import pandas as pd
import matplotlib as plt

""" This file will read all of the job_descriptionX.npy files with the number of languages for each of the job_descriptions"""
try:
    with open('languages.txt', 'r')as f: ## this file contains the coding languages we are going to look for
        read_languages = f.readlines()
except:
    raise AssertionError("file not found")

languages = []
for language in read_languages:
    languages.append(language.lower()[:-1])

print(languages)
### These cities have a space in the middle
citiesWithSpaces = {
"san" : "san_" ,
"los" : "los_" ,
"el" : "el_" ,
"santa" : "santa_" ,
"salt" : "salt_" ,
"redondo" : "redondo_" ,
"rancho" : "rancho_" ,
"redwood" : "redwood_" ,
"culver" : "culver_" ,
"huntington" : "huntington_" ,
"palo" : "palo_" ,
"mountain" : "mountain_" ,
"elk" : "elk_" ,
"aliso" : "aliso_" ,
"new" : "new_" ,
"north" : "north_" ,
"south" : "south_" ,
"east" : "east_" ,
"west" : "west_" ,
"menlo" : "menlo_" ,
"morgan" : "morgan_" ,
"lake" : "lake_" ,
"costa" : "costa_" ,
}

beginning = 0
end = 12282  #### This is the number of files 

## we are going to store the information in a database called data
data = pd.DataFrame(columns = [ "languages_per_entry", "salary", "city", "state"], index = range(beginning, end+1))

for i in range(beginning, end):
    state = ''
    print(i) ## prints location to show progress
    try: ## if a file does not work, we want it to keep going with the rest of the files and report which files it did not work with
        languages_per_entry = {}## resets the entries each round
        file = np.load("job_description" + str(i) + ".npy") # these files are saved as job_description0.npy etc and have arrays with the entries of all of the words in the file
        location_tag = False # this is used to only find the first location instance
        for j in range(0, len(file)):
            if file[j] == 'location' and location_tag == False:
                location_tag = True
                if file[j+1] in citiesWithSpaces:
                    city = citiesWithSpaces[file[j+1]] + file[j+2]
                else:
                    city = file[j+1]
            
            elif file[j] == 'salarylow':
                sal_low = file[j+1]
            
            elif file[j] == 'salaryhigh':
                sal_high = file[j+1]

            elif file[j] == 'logo' :
                state = file[j-1]
                # print(state)

            elif file[j] in languages:
                try:
                    languages_per_entry[file[j]] += 1
                except:
                    languages_per_entry[file[j]] = 1

        salary = (int(sal_low) + int(sal_high))/2
        data.loc[i] = [languages_per_entry, salary, city, state]
        
    except:
        print("failed to work on file" + str(i))

print(data)

# np.save('data.npy', data) ## saves the database as a pickle
data.to_pickle() # save the database as a pickle
