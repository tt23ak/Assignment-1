# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 23:47:23 2023

@author: User
"""

import pandas as pd
import matplotlib.pyplot as plt



#For LINE PLOT



# Step:1 Read the data from the CSV file
data = pd.read_csv("C:/Users/User/Downloads/full_data_clean.csv")

# Step:2 Convert the 'date' column to datetime type
data['date'] = pd.to_datetime(data['date'])

# Step:3 Take out the year From the "date" column, and round it to the closest whole number
data['year'] = data['date'].dt.year.round().astype(int)

# Group the data by 'year' and 'transport_type', calculate the mean, and reset the index
yearly_means = data.groupby(['year', 'transport_type'])['value'].mean().reset_index()

# Create a line plot for each transport type's annual average
plt.figure(figsize=(12, 6))

transport_types = yearly_means['transport_type'].unique()

for transport_type in transport_types:
    yearly_data = yearly_means[yearly_means['transport_type'] == transport_type]
    plt.plot(yearly_data['year'], yearly_data['value'], label=transport_type,  linestyle='-')
plt.title(' UK Annual Average Transportation Use')
plt.xlabel('Year')
plt.ylabel('Average Value')

# Format x-axis labels as integers 
plt.xticks(yearly_means['year'].unique(), rotation=45)

plt.legend(title='Transport Type', loc='upper left', bbox_to_anchor=(1, 1))


plt.show()




#FOR SCATTER PLOT




data['date'] = pd.to_datetime(data['date'])

# Step 3: Extract the year from the 'date' column and round it to the closest whole number
data['year'] = data['date'].dt.year.round().astype(int)

# Step 4: Group the data by 'year' and 'transport_type', calculate the mean, and reset the index
yearly_means = data.groupby(['year', 'transport_type'])['value'].mean().reset_index()

# Step 5: Create a scatter plot for each transport type
plt.figure(figsize=(10, 6))

transport_types = yearly_means['transport_type'].unique()
for transport_type in transport_types:
    data_subset = yearly_means[yearly_means['transport_type'] == transport_type]
    plt.scatter(data_subset['year'], data_subset['value'], label=transport_type, alpha=0.5)

plt.title('Scatter Plot of UK Transportation Data (Yearly Means)')
plt.xlabel('Year')
plt.ylabel('Average Value')
plt.legend(title='Transport Type', loc='upper left', bbox_to_anchor=(1, 1))



# Step 6: Customize the x-axis ticks to remove the decimal part
plt.xticks([int(year) for year in plt.xticks()[0]])

plt.show()



# FOR BAR CHART


#Step:2 Convert the 'date' column to datetime type
data['date'] = pd.to_datetime(data['date'])

#Step:3 Extract the year from the 'date' column and round it to the closest whole number
data['year'] = data['date'].dt.year.round().astype(int)

#Step:4 Group the data by 'year' and 'transport_type', calculate the mean, and reset the index
yearly_means = data.groupby(['year', 'transport_type'])['value'].mean().reset_index()

# Pivot the data to create a bar chart
pivoted_data = yearly_means.pivot(index='year', columns='transport_type', values='value')

# Create a bar chart
plt.figure(figsize=(12, 6))
pivoted_data.plot(kind='bar', width=0.8)

plt.title('UK Annual Average Transportation Use')
plt.xlabel('Year')
plt.ylabel('Average Value')
plt.xticks(rotation=45)
plt.legend(title='Transport Type', loc='upper left', bbox_to_anchor=(1, 1))

plt.show()


