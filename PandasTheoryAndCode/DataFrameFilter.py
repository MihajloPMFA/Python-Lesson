import pandas as pd

data = pd.read_csv("dataset.csv")

# Here you will learn how to filter down this DataFrame in order to get the exact data you need to plot the chart.

# Follow through the next steps:
#       1) Create a list that contains the 4 platforms we need the data for:
platforms = ['PS4', 'XOne', 'PC', 'WiiU']
#       2) Using the list, filter out the unneccesary platforms using the next command:
filtered_data = data[data['platform'].isin(platforms)]
# For further understanding let's explain and revise what certain parts of this line do:
#       2.1) data - the DataFrame that contains all the platform data
#       2.2) By adding [] brackets next to it like this:
data[''''''] #we can access a specific column within the DataFrame
#in our case we want to access the 'platform' column

# Check the file "filtered_data1.txt" under 1. for an example of how the data['platform'] column would look when printed out
# Because we want to filter our DataFrame by the platforms that are in the list we created before, we can use the .isin(platforms) function
# This will essentially check wether the platforms in the DataFrame match up with any platform in the list, and only keep those rows that have one of the platforms in the DataFrame.

# Now we have this kind of structure:

data['platform'].isin(platforms)
# If you would print this out you would get a DataFrame with 1 column that has True/False values in it that correspond with wether a platform that was in that row appeared in the list we created.
# See file "filtered_data1.txt" under 2. for a example

# Lastly putting the previous line in the [] brackets of our 'data' DataFrame like this: 
data[data['platform'].isin(platforms)]
# Will make it so the DataFrame only has the information about the platforms we need.
# Because this will also return a DataFrame we need to give it a variable to return the value to

filtered_data = data[data['platform'].isin(platforms)]

# Which will give the following result - see file "filtered_data2.py"

#After completely going through this file, return to the "Pandas.txt" file.