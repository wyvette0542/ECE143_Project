
# coding: utf-8

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt 


# In[ ]:


loc_sal_lang = pd.read_pickle('dataframe1.pkl')
assert(isinstance(loc_sal_lang,pd.DataFrame))
language_data = pd.read_pickle('dataframe2.pkl')
assert(isinstance(language_data,pd.DataFrame))


# In[ ]:


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

